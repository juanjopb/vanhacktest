# Vanhack Test


This is a short example to attend the Vanhacktest requirements.

The code contains Ansible playbooks that will deploy in AWS the Infrastructure needed in order to Run 
- EC2 Instance (s)
- RDS instance 
- ELB classic

After the infrastructure is deployed, the Web application written in Python will be copied to previous EC2 Instances.

  
There are two options to execute.
-  [Pre-Loaded Environment](#Pre-Loaded-Environment)
-  [Load environment from scratch](#Load-environment-from-scratch)

  

## Pre-Loaded Environment:

URL: http://vanhack-load-balancer-1758030516.us-east-1.elb.amazonaws.com

Repository https://github.com/juanjopb/vanhacktest branch `preloaded`

  

If you want to get into the EC2 instances (us-east-1 - N. Virginia) using ssh:

- You will need the PEM file that was sent by email or the PEM file that vanhack informed by the email.
- ssh -i "aws-private.pem" ubuntu@ec2-54-197-40-42.compute-1.amazonaws.com
- ssh -i "aws-private.pem" ubuntu@ec2-54-163-31-98.compute-1.amazonaws.com

  
  

## Load From Scratch: 

>  **Note:** The code was tested deploying from Ubuntu 19.04 machine, but should works using different distributions or SO.
>  You could deploy this code using the AWS credentials sent or using different AWS account. but It necessary to have configured.


### Requirements:
There are some requirements in order to run the code 
- Python, Git, Ansible, Awscli installed.
```sh

$ sudo apt-get install python3.7 python-pip git awscli
$ pip install boto boto3 ansible

```
- AWS credentials were sent by email, you will need to configure.

  

### Before to deploy

Some configurations could be customized, the settings are located on `AWS_Ansible/playbooks/group_vars/all`
To change names, regions to deploy, or amount of instance, please take a look at the mentioned file.
>  **Note:** Using the Credentials sent and cloning the [repository](https://github.com/juanjopb/vanhacktest) in the **master** branch will deploy a New version in the Region (us-west-1 N.California) If is going to be deployed in another region, need to be changed the **(base_image) ami** and **aws_region**
>  If you want to deploy more than one instance, please modify '*ec2_count_instances=desired number*'


### Deploying

1. Configure the aws credentials, `cd ~/.aws

```sh
$ cd ~/.aws
$ vim credentials
$ [default]
$ aws_access_key_id = Access_Key_Sent_by_email
$ aws_secret_access_key = Secret_Access_Key_Sent_by_email

```

2. Clone the repo https://github.com/juanjopb/vanhacktest

3. Located on the top of the cloned repo run the following command

```sh

$ vanhacktest > ansible-playbook -i AWS_Ansible/playbooks/inventory/hosts AWS_Ansible/playbooks/All-tasks.yml -e 'ansible_python_interpreter=/usr/bin/python3'

```
4. The deploy will start to show the progress 

>  **Note:** The first time deploying the RDS instance could take almost 30 minutes to be ready. To avoid the time there is a RDS Instance preloaded.
>  **Note:** A private key will be saved on ***`AWS_Ansible/aws-private.pem`,*** please be careful and dont lose it..

5. Take note about the URL Endpoint Generated at the end of the Ansible Script.
 ![Should show somenthing similar](s3://juanjosepb/vanhacktest/ansible-final-information.png)
 
  
Name: Juan José Perez
Email: juanjopb@hotmail.com

  
  
  
  