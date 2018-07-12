#!/usr/bin/env bash

ec2_az=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
ec2_region=$(echo "${ec2_az::-1}")
printf $ec2_region
