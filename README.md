# Vanhack Test

This is a Short example to attend the Vanhacktest requirements.

The example Ansible playbooks that deploy all the Infrastructure needed in order to Run an EC2 Instance, RDS instance with a ELB classic, and the instances running a webserver in Python.

There are two options to execute.
- [Pre-Loaded Environment](#preloaded) (us-east-1 - N. Virginia)
- [Load an environment from scratch](#scratch)

### Pre-Loaded Environment:
URL: http://vanhack-load-balancer-1758030516.us-east-1.elb.amazonaws.com
Repository https://github.com/juanjopb/vanhacktest branch `preloaded`

If you want to get int the EC2 instances:
- Connect using ssh you will need the PEM file that was sent by email or the PEM file that vanhack informed by the email.
- ssh -i "aws-private-vanhack.pem" ubuntu@ec2-54-172-18-197.compute-1.amazonaws.com


### Load From Scratch
Requirements:
This Option was tested deploying from Ubuntu 19.04. should works using different versions.

- Python, Git, Ansible, Awscli installed
 ```sh
$ sudo apt-get install python3.7 python-pip git awscli
$ pip install boto boto3 ansible
```
- AWS credentials were sent by email, you will need to configure.

Before to deploy
Some configurations could be changed, there are located on `AWS_Ansible/playbooks/group_vars/all`
If you want to deploy more than one instance, please modify 'ec2_count_instances=desired number'

Deploying
1. Configure the aws credentials, `cd ~/.aws
 ```sh
$ vi credentials
$ [default]
$ aws_access_key_id = Access Key Sent
$ aws_secret_access_key = Secret Access Key Sent
``` 
2. Clone the repo https://github.com/juanjopb/vanhacktest
3. located on the top of the cloned repo run the following command 
```sh
$ ansible-playbook -i AWS_Ansible/playbooks/inventory/hosts AWS_Ansible/playbooks/All-tasks.yml -e 'ansible_python_interpreter=/usr/bin/python3'
```

> **Note:** the firs time it's a little delayed due to the RDS creation and preparation.

NOTE: the firs time it's a little delayed due to the RDS creation and preparation
4. A private key will be saved on `AWS_Ansible/aws-private.pem`, please be careful and dont lose it.
5. Take note about the URL Endpoint Generated at the end of the Ansible Script.



juanjopb@hotmail.com





sudo apt install python3.7 python3-pip
pip install boto boto3 ansible

TODO: 
- Change the KeyPair