#!/usr/bin/env bash

aws_account_id=$(curl -s http://169.254.169.254/latest/meta-data/iam/info | jq --raw-output '.InstanceProfileArn' | cut -d ':' -f 5)
printf $aws_account_id
