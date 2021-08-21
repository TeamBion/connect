#!/usr/bin/env python3
from simple_term_menu import TerminalMenu
import boto3
import sys
import os
import subprocess


def parseTag(tags, specifiedTag="Name"):
	parsedTagValue = ""
	for tag in tags:
		if tag["Key"] == specifiedTag:
			parsedTagValue = tag["Value"]
		else:
			pass
	return parsedTagValue

def getRunningInstance(ec2Client):

	gatheredInstances = []
	instances = ec2Client.instances.filter(Filters=[{
		'Name': 'instance-state-name',
		'Values': ['running']}])

	for instance in instances:
		instance_label = ""
		instanceTag = parseTag(instance.tags)
		instance_label = "{} , {}".format(instanceTag, instance.id)

		gatheredInstances.append(instance_label)

	return gatheredInstances


def startSession(instanceKey, region):
	instanceId = instanceKey.split(" , ")[1]
	print(instanceId)
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

def connector(ec2Client, region):
	instances = getRunningInstance(ec2Client)

	if instances == None or instances == '':
		print("Error: There is no running in specific conditions")
		sys.exit(1)

	else:

		terminal_menu = TerminalMenu(instances)
		menu_entry_index = terminal_menu.show()
		startSession(instances[menu_entry_index], region)


if __name__ == "__main__":
	try:
		region = sys.argv[1]

	except Exception as exp:
		print("Index error on usage behzo <REGION-NAME>, eu-west-1 using as default")
		region = "eu-west-1"

	ec2Client = boto3.resource("ec2", region_name=region)

	connector(ec2Client, region)
