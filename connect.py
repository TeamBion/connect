#!/usr/bin/env python3
from simple_term_menu import TerminalMenu
import boto3
import sys
import os
import subprocess
import optparse

def parseTag(tags, specifiedTag="Name"):
	parsedTagValue = ""
	for tag in tags:
		if tag["Key"] == specifiedTag:
			parsedTagValue = tag["Value"]
		else:
			pass
	return parsedTagValue

def getRunningInstance(ec2Client, tag, tagValue):

	gatheredInstances = []


	if tag == "" or tagValue == "":
		filters = [{ 'Name': 'instance-state-name', 'Values': ['running']}]

	else:
		filters = [{ 'Name': 'instance-state-name', 'Values': ['running']}, { "Name": "tag:{}".format(tag), "Values": ["{}".format(tagValue)]}]

	instances = ec2Client.instances.filter(Filters=filters)

	for instance in instances:

		instance_label = ""
		instanceTag = parseTag(instance.tags, tag)
		instance_label = "{} , {}".format(instanceTag, instance.id)

		gatheredInstances.append(instance_label)

	return gatheredInstances


def startSession(instanceKey, region):
	instanceId = instanceKey.split(" , ")[1]

	if instanceId.startswith("i-"):
		cmd = ['aws', 'ssm', 'start-session', '--target', instanceId, '--region', region]
		env = os.environ.copy()
		p = subprocess.Popen(cmd, env=env)

		while True:
			try:
				p.wait()
				break
			except KeyboardInterrupt as e:
				pass
	else:
		print("Invalid instance id {}".format(instanceId))

def connector(ec2Client, region, tag, tagValue):
	instances = getRunningInstance(ec2Client, tag, tagValue)

	if instances == None or instances == '':
		print("Error: There is no running in specific conditions")
		sys.exit(1)

	else:

		terminal_menu = TerminalMenu(instances)
		menu_entry_index = terminal_menu.show()
		startSession(instances[menu_entry_index], region)


if __name__ == "__main__":
	try:
		parser = optparse.OptionParser()

		parser.add_option('-r', '--region',
			action="store", dest="region",
			help="Region name of the aws account", default="eu-west-1")

		parser.add_option('-t', '--tag',
			action="store", dest="tag",
			help="Tag of the EC2 instance", default="Name")

		parser.add_option('-v', '--value',
			action="store", dest="value",
			help="Value of the EC2 instance tag", default="")
			

		(options, args) = parser.parse_args()
		data = vars(options)
		region = data["region"]
		tag = data["tag"]
		tagValue = data["value"]
		
	except Exception as exp:
		print("Index error on usage behzo <REGION-NAME>, eu-west-1 using as default")
		region = "eu-west-1"

	ec2Client = boto3.resource("ec2", region_name=region)

	connector(ec2Client, region, tag, tagValue)
