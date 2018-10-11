import boto3
import sys

class initiate():

def awstask(self, client, boto3):
	self.client = boto3.client('ec2', aws_access_key_id='key', aws_secret_access_key='key', region_name='desired_region')

class volumes():

def client(self,volumes, tags):
	self.volumes = map('DeviceName', 'EbsVolumes')
		device_name = '$PATH'
		ebs = ['DeleteOnTermination', 'VolumeSize', 'VolumeType']
			while ebs():
				return f'Delete On Termination is {DeleteOnTermination}'
				return f'Volume Size is {VolumeSize}'
				return f'Volume Type is{VolumeType}'
	self.tags = self.volumes('key', 'value')

class paramaters():

def instances(self, imageid, instancetype, keyname, maxcount, mincount, monitoring, sgids, subnetids):
	self.imageid = imageid,
    	self.instancetype = instancetype,
    	self.keyname = keynanme,
    	for i in instances:
		if maxcount > 1:
			return f'There is only {maxcount} instance/s'
		elif mincount < 1:
			return f'There is only {mincount} instance/s'
		else:
			return "There are no instances"

	self.monitoring = True
	self.sgids = sgids
        self.subnetids = subnetids,

class tags():

def tags(self, r, key, values, client)
	self.r = describe tags('key', 'values')
	ebstags = {key:str('name'), value:str('value')}
	with open('tagged_volumes.txt', 'r') as fp:
		for line in fp:
		line = line.rstrip()
		tagged_volumes = tagged_volumes + 1
		volumes.remove(line)

	with open('untagged_volumes.txt', 'w') as fp:
		for volume_id in volumes:
		fp.write(volume_id + '')

untagged_volumes = all_volumes - tagged_volumes
print "untagged_volumes:" + str(untagged_volumes)
print "total volumes:" + str(all_volumes)
