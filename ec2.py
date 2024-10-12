import boto3

AWS_REGION = "us-east-1"
EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION) 

instances = EC2_RESOURCE.instances.all()
for instance in instances:
    print(f'ID: {instance.id}, State: {instance.state["Name"]}, Type: {instance.instance_type}')
    INSTANCE_ID = instance.id 
instance =  EC2_RESOURCE.Instance(INSTANCE_ID)

public_ip = instance.public_ip_address
    
def create_ec2():
    KEY_PAIR_NAME = 'myKey'
    AMI_ID = 'ami-01195fa866471e53d' # Amazon Linux 2
    SUBNET_ID = 'subnet-0947774229d538006'
    SECURITY_GROUP_ID = 'sg-03288733c92d82848'
    USER_DATA = '''#!/bin/bash
    echo hello worldd
    yum update
    '''

    instances = EC2_RESOURCE.create_instances(
        MinCount = 1,
        MaxCount = 1,
        UserData=USER_DATA,
        ImageId=AMI_ID,
        InstanceType='a1.medium',
        KeyName=KEY_PAIR_NAME,
        SecurityGroupIds = [SECURITY_GROUP_ID],
        SubnetId=SUBNET_ID
    )
  
   
        
def start_instance():
    response = instance.start()
    print(response)

   
def stop_instance():
     response = instance.stop()
     print(response)
    
    
def get_public_ip():
       return public_ip
    
 


