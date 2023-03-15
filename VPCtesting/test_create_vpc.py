import boto3
import pytest

@pytest.fixture(scope="session")
def vpc():
    #ec2 = boto3.client('ec2', aws_access_key_id="AKIAYKBTCUBFXMGGBDR",
    #                  aws_secret_access_key="S7mCI0NHyixi+vi3u8aEBb9KLSvtQr0Z64QYef8e", region_name='ap-southeast-1')

    ec2=boto3.resource('ec2',aws_access_key_id="AKIAYKBTCUBFXMGGBDR",aws_secret_access_key="S7mCI0NHyixi+vi3u8aEBb9KLSvtQr0Z64QYef8", region_name='ap-southeast-1')
    vpc=ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc.create_tags(Tags=[{"key": "Name", "Value":"Test VPC"}])
    yield vpc
    vpc.delete()

def test_vpc_created(vpc):
    assert vpc.state == 'available'
    assert vpc.cidr_block == '10.0.0.0/16'

