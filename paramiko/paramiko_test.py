"""Testing paramiko."""


import paramiko
import time
import os
import sys


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.1.1.2',
                   username='alex',
                   password='alex',
                   look_for_keys=False,
                   allow_agent=False)

ssh_session = ssh_client.invoke_shell()
ssh_session.send('en\n')
ssh_session.send('alex\n')
ssh_session.send('terminal length 0\n')
ssh_session.send('sh run\n')
time.sleep(2)
ssh_output = ssh_session.recv(100000)
print(ssh_output)

with open(os.path.join(sys.path[0], 'ssh_output.txt'), 'wb') as txt_file:
    txt_file.write(ssh_output)
