import pytest
import boto3

# AWS credentials
#'your_access_key'
ACCESS_KEY = "AKIAYKBTCUBFXMGGBDR8"
#'your_secret_key'
SECRET_KEY = "S7mCI0NHyixi+vi3u8aEBb9KLSvtQr0Z64QYef8q"
#'your_region'
REGION = 'ap-southeasteast-1'

@pytest.fixture(scope='module')
def ec2_client():
    ec2 = boto3.client('ec2', region_name=REGION, aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    return ec2

def test_create_ec2_instance(ec2_client):
    instance = ec2_client.run_instances(
        ImageId='ami-1234567890abcdef0',
        InstanceType='t2.micro',
        KeyName='my-key-pair',
        MinCount=1,
        MaxCount=1
    )
    instance_id = instance['Instances'][0]['InstanceId']
    assert instance_id is not None
