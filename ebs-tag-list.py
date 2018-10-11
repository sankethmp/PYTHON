import boto3
import sys

# Requires AMI_ID, Key_Pair, Security-Group, Subnet
client = boto3.client('ec2', aws_access_key_id='key', aws_secret_access_key='key', region_name='us-east-1')

response = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 80,
                'VolumeType': 'gp2',
            },
        },
    ],
    ImageId='ami-id',
    InstanceType='t2.micro',
    KeyName='MyEC2Key',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
    SecurityGroupIds=[
        'sg-id',
    ],
    SubnetId='subnet-id',
    UserData='userdata.txt'
)

elb = boto3.client('elb', aws_access_key_id='key', aws_secret_access_key='key', region_name='us-east-1')

# Requires ELB Name & Instance ID
response = elb.create_load_balancer(
    LoadBalancerName='Mynewelbmiq',
    Listeners=[
        {
            'Protocol': 'HTTP',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'HTTP',
            'InstancePort': 80,
        },
    ],

    Subnets=[
        'subnet-id',
    ],
    SecurityGroups=[
        'sg-id',
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Elbmiq'
        }
    ]
)
response = client.create_load_balancer_listeners(
    LoadBalancerName='Mynewelbmiq',
    Listeners=[
        {
            'Protocol': 'HTTP',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'HTTP',
            'InstancePort': 80,
        },
    ]
)
