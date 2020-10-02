'''
Pprint module
'''

import pprint

print('\n', '*'*50, '\n')

v_sh_ip_int = [('GigabitEthernet0/3.301', '10.0.4.129'),
('GigabitEthernet0/3.450', '10.0.4.193'),
('GigabitEthernet0/3.451', '10.0.5.1'),
('GigabitEthernet0/3.601', '172.16.0.1'),
('GigabitEthernet0/3.650', '172.16.2.1')]

pprint.pprint(v_sh_ip_int, width=20, depth=1)

print('\n', '*'*50, '\n')