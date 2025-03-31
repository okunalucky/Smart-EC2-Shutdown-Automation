import boto3 # type: ignore

### minimum instance type
mini_instancetype = "t2.medium"

### list of all instance_types
instance_order = [
    "t2.nano", "t3.nano",
    "t2.micro", "t3.micro",
    "t2.small", "t3.small",
    "t2.medium", "t3.medium",
    "t2.large", "t3.large",
    "t2.xlarge", "t3.xlarge",
    "t2.2xlarge", "t3.2xlarge"
]

 Ec2 InstanceIds = [] # type: ignore

### describe instance
def get_all_instances():# type: ignore
    client = boto3.client('ec2')
    response = client.describe_instances()
    for i in response["Reservations"]:
     for j in i["instances"]:
        instance_id = j[instance_id]
        instance_type = j[instance_type]
        ##check if the instance type is greater than minimum
        if instance_order.index(instance_type) >= instance_order.index(mini_instancetype):
            Ec2 InstanceIds.append(instance id) # type: ignore
    return Ec2 InstanceIds # type: ignore

### terminate instance
def terminate_instance(instance_ids):
    client = boto3.client('ec2')
    response = client.terminate_instances(InstanceIds = instance_ids)
    return response

##lambda header
def lambda_handler(event, context):
    client = boto3.client('ec2')
    instance_to_terminate = get_all_instances()
    terminate_instance(instance_to_terminate)