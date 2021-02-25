"""Testing Netmiko."""


import netmiko
import os
import sys


def print_stars():
    """Print 100 stars in the same line to make better output visibility."""
    print('\n', '*'*100, '\n', end='')


print_stars()

ssh_device = {'device_type': 'cisco_ios',
              'ip': '10.1.1.2',
              'username': 'alex',
              'password': 'alex1',
              'secret': 'alex'}

try:
    ssh_session = netmiko.ConnectHandler(**ssh_device)
    ssh_session.enable()

    print(ssh_session.send_command('sh clock'))

    print_stars()

    if 'Loopback0' in ssh_session.send_command('show run | incl interface'):
        print('Loopback0 is already configured')
    else:
        ssh_session.send_config_set(['interface lo 0',
                                    'ip add 1.1.1.1 255.255.255.255'])
        print('Loopback0 has been configured')

    print_stars()

    print(ssh_session.send_command('sh ip int br'))
    ssh_session.send_command('wr mem')

    print_stars()

    with open(os.path.join(sys.path[0], 'startup.cfg'), 'w') as txt_file:
        txt_file.write(ssh_session.send_command('show start'))

    ssh_session.disconnect()

except netmiko.NetMikoAuthenticationException:
    print('Wrong password for SSH')
