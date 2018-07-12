#!/usr/bin/env bash

account_id=$(/opt/oulib/aws/bin/ec2_get_account_id.sh)
region=$(/opt/oulib/aws/bin/ec2_get_region.sh)
instance_id=$(curl -s http://169.254.169.254/latest/meta-data/instance-id/)
printf arn:aws:ec2:${region}:${account_id}:instance/${instance_id}
