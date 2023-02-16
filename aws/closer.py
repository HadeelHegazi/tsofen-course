import boto3
import os
import json

def get_all_region():
    ec2 = boto3.client('ec2')
    regions = ec2.describe_regions().get('Regions',[] )
    return regions

def get_all_instances_iterator(region_name):

    ec2_resource = boto3.resource('ec2',region_name)
    instances_iterator = ec2_resource.instances.all()
    return instances_iterator

def demo_ec2_instances():
    regions = get_all_region()
    for region in regions:
        region_name = region['RegionName']
        ec2_client = boto3.client('ec2',region_name)
        instances_iterator = get_all_instances_iterator(region_name)
        ids = [inst.id for inst in instances_iterator]
        if ids != [] :
            response = ec2_client.terminate_instances(InstanceIds=ids)

def get_all_nat_getaways(region_name):
    ec2 = boto3.client('ec2',region_name)
    nat_getways = ec2.describe_nat_gateways().get('NatGateways')
    return nat_getways


def demo_ec2_delete_nat_gateway():
    regions = get_all_region()
    for region in regions:
        region_name = region['RegionName']
        ec2_client = boto3.client('ec2',region_name)
        nat_getaways = get_all_nat_getaways(region_name)
        ids = [nat.get('NatGatewayId') for nat in nat_getaways]
        if ids != [] :
            for Natid in ids:
                response = ec2_client.delete_nat_gateway(NatGatewayId=Natid)
				
def get_all_elastic_ip(region_name):
    ec2 = boto3.client('ec2',region_name)
    elastic_ips = ec2.describe_nat_gateways().get('NatGateways')
    addresses = [natgateway.get('NatGatewayAddresses') for natgateway in elastic_ips]
    return addresses

def demo_ec2_delete_elastic_ip():
    regions = get_all_region()
    for region in regions:
        region_name = region['RegionName']
        ec2_client = boto3.client('ec2',region_name)
        elastic_ips = get_all_elastic_ip(region_name)
        ids = [natAddress[0].get('AllocationId') for natAddress in elastic_ips]
        if ids != [] :
            for Natid in ids:
                response = ec2_client.release_address(AllocationId=Natid)

demo_ec2_instances()
demo_ec2_delete_nat_gateway()
demo_ec2_delete_elastic_ip()
