#!/usr/bin/env python3
from simple_term_menu import TerminalMenu
import boto3
import sys
import os
import subprocess

def getRunningInstance(ec2Client):

	gatheredInstances = []
	instances = ec2Client.instances.filter(Filters=[{
		'Name': 'instance-state-name',
		'Values': ['running']}])

	for instance in instances:
		for tag in instance.tags:
			if 'Name'in tag['Key']:
				name = tag['Value']
				tmp_instace = ""
				tmp_instace = "{} , {}".format(name, instance.id)
				gatheredInstances.append(tmp_instace)

	return gatheredInstances


def startSession(instanceKey):
	instanceId = instanceKey.split(" , ")[1]

	if instanceId.startswith("i-"):
		cmd = ['aws', 'ssm', 'start-session', '--target', instanceId]
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

def connector(ec2Client):
	instances = getRunningInstance(ec2Client)

	if instances == None or instances == '':
		print("Error: There is no running in specific conditions")
		sys.exit(1)

	else:

		terminal_menu = TerminalMenu(instances)
		menu_entry_index = terminal_menu.show()
		startSession(instances[menu_entry_index])


if __name__ == "__main__":
	try:
		region = sys.argv[1]

	except Exception as exp:
		print("Index error on usage behzo <REGION-NAME>, eu-west-1 using as default")
		region = "eu-west-1"

	ec2Client = boto3.resource("ec2", region_name=region)

	connector(ec2Client)