"""Jinga2 testing."""


from stars_print import print_stars
from jinja2 import Template
import yaml
import os
import sys

print_stars()

with open(os.path.join(sys.path[0], 'vlan_config.txt')) as template_file:
    template1 = Template(template_file.read())

with open(os.path.join(sys.path[0], 'vlans_on_ports.yaml')) as port_vlan_file:
    ports_vlans = yaml.safe_load(port_vlan_file)

with open(os.path.join(sys.path[0], 'switch_config.txt'), 'w') as switch_config_file:
    for port in ports_vlans:
        print(template1.render(port))
        switch_config_file.write(template1.render(port))

print_stars()
