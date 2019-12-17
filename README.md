# vanhacktest

This is a Short example to attend the Vanhacktest requirements.

There are two options to execute.

- Pre-Loaded Environment.
- Load an environment from scratch.

### Pre-Loaded Environment:
URL: 

If you wanto to see the EC2 instances:
- To connect by ssh you will need the PEM file that was sent by email or the PEM file that vanhack informed by the email.
- You need to Know the [IPaddresses]


### Load From Scratch
Requirements:
This Option was tested deploying from an Ubuntu 19.04. should works using different versions.
- Python installed
- Git Installed
- Ansible Installed
- pip3 install boto boto3 ansible
- some AWS credentials were sent by email, you will need to configure.

Deploying
1. Configure the aws credentials 
2. Clone the repo 
3. located on the top of the cloned repo run `ansible-playbook -i AWS_Ansible/inventory/hosts AWS_Ansible/playbooks/ansible-create-aws-environment.yml -e 'ansible_python_interpreter=/usr/bin/python3'`
4. During the running, the system will ask you to add in finger
4. Take note about the URL Generated at the end
4. Run `ansible-playbook -i AWS_Ansible/inventory/hosts AWS_Ansible/playbooks/launch-flask-python.yml -e 'ansible_python_interpreter=/usr/bin/python3'`



sudo apt install python
sudo apt install python-pip
pip install boto boto3 ansible

TODO: 
- Change the KeyPair
