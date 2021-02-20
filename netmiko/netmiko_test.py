"""Testing Netmiko."""


import netmiko


def print_stars():
    """Print 100 stars in the same line to make better output visibility."""
    print('\n', '*'*100, '\n', end='')


print_stars()

ssh_device = {'device_type': 'cisco_ios',
              'ip': '10.1.1.2',
              'username': 'alex',
              'password': 'alex',
              'secret': 'alex'}

ssh_session = netmiko.ConnectHandler(**ssh_device)
ssh_session.enable()
print(ssh_session.send_command('sh clock'))

print_stars()

ssh_session.send_config_set(['interface lo 0',
                             'ip add 1.1.1.1 255.255.255.255'])
print(ssh_session.send_command('sh ip int br'))

print_stars()
