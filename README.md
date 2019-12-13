# vanhacktest


Deploying
1 Need to have aws credentials 
2 Run `ansible-playbook -i AWS_Ansible/inventory/hosts AWS_Ansible/playbooks/ansible-create-aws-environment.yml -e 'ansible_python_interpreter=/usr/bin/python3'`
3 Run `ansible-playbook -i AWS_Ansible/inventory/hosts AWS_Ansible/playbooks/launch-flask-python.yml -e 'ansible_python_interpreter=/usr/bin/python3'`



pip install flask

sudo apt install python
sudo apt install python-pip
pip install boto boto3 ansible

TODO: 
- Change the KeyPair