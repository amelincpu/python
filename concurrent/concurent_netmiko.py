"""Testing Netmiko."""


import netmiko
import os
import sys
import yaml
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO)

def print_stars():
    """Print 100 stars in the same line to make better output visibility."""
    print('\n', '*'*100, '\n', end='')


def send_ssh_show(ssh_device, ios_show):
    """Open ssh and run show command."""
    logging.info(f'Connecting to {ssh_device["ip"]}')
    with netmiko.ConnectHandler(**ssh_device) as ssh_session:
        ssh_session.enable()
        return ssh_session.send_command(ios_show)


print_stars()

with open(os.path.join(sys.path[0], 'device_list.yaml')) as device_list_file:
    device_list = yaml.safe_load(device_list_file)

with ThreadPoolExecutor(max_workers=3) as ssh_executor:
    executor_result = ssh_executor.map(send_ssh_show, device_list, ['sh clock']*3)
    for ssh_out in executor_result:
        print(ssh_out)

print_stars()
