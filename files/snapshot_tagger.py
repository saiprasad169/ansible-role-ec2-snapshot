import boto3,json,csv
insta=boto3.client('ec2').describe_instances()
instlist=[]
ec2 = boto3.resource('ec2')

for i in insta['Reservations']:
		 instlist.append(i['Instances'][0])

volumes=[]
voltags=[]
for m in instlist:
    for l in m['BlockDeviceMappings']:
            volumes.append({l['Ebs']['VolumeId']: m['Tags']})

client = boto3.client('ec2')
snap_vols={}
snaps=client.describe_snapshots(OwnerIds=['188033381281'])['Snapshots']
for i in snaps:
    snap_vols.setdefault(i['VolumeId'],[]).append(i['SnapshotId'])

for key,value in snap_vols.items():
    for k2 in volumes:
        if key in k2:
            for z in value:
                voltags.append({z: k2[key]})

for tt in voltags:
    for k,v in tt.items():
        ec2.Snapshot(k).create_tags(Tags=v)
