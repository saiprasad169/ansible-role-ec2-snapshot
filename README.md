Role Name
=========

Ansible EC2 Snapshot Role, by default this will configure daily snapshots with a 14 day retention policy

Requirements
------------

* RHEL/Centos7 (Any OS utilizing Yum package manager)
* AWS CLI
Role Variables
--------------

*  ebs_snapshot_retention_days:

Dependencies
------------

OULibraries.ec2-init

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: OULibraries.ec2-snapshot, ebs_snapshot_retention_days: 14 }

License
-------

[MIT](https://github.com/OULibraries/ansible-role-elk/blob/master/LICENSE)

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
