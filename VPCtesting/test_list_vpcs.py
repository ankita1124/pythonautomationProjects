import boto3

# Replace with your AWS access key ID and secret access key
ACCESS_KEY_ID = 'AKIAYKBTCUBFXMGGBDR7'
#'your_secret_access_key'
SECRET_ACCESS_KEY = "S7mCI0NHyixi+vi3u8aEBb9KLSvtQr0Z64QYef8W"
#'your_region_name'
REGION_NAME = 'ap-northeast-1'

def test_list_vpcs():
    # Create a Boto3 client for EC2
    ec2 = boto3.client('ec2',
                       aws_access_key_id=ACCESS_KEY_ID,
                       aws_secret_access_key=SECRET_ACCESS_KEY,
                       region_name=REGION_NAME)

    # Call the describe_vpcs() method to get a list of all VPCs
    response = ec2.describe_vpcs()

    # Extract the VPC IDs from the response
    vpc_ids = [vpc['VpcId'] for vpc in response['Vpcs']]

    # Assert that the VPC IDs list is not empty
    assert len(vpc_ids) > 0

    # Print the VPC IDs
    print(vpc_ids)
