'''
Not default module Tabulate
'''

import tabulate

print('\n', '*'*50, '\n')

v_sh_ip_int = [('GigabitEthernet0/3.301', '10.0.4.129'),
('GigabitEthernet0/3.450', '10.0.4.193'),
('GigabitEthernet0/3.451', '10.0.5.1'),
('GigabitEthernet0/3.601', '172.16.0.1'),
('GigabitEthernet0/3.650', '172.16.2.1')]

print(type(v_sh_ip_int))

print(tabulate.tabulate(v_sh_ip_int))

print('\n', '*'*50, '\n')

print(tabulate.tabulate(v_sh_ip_int, headers=['Interface', 'IP'], tablefmt='pipe'))

print('\n', '*'*50, '\n')

print(tabulate.tabulate(v_sh_ip_int, headers=['Interface', 'IP'], tablefmt='html'))

print('\n', '*'*50, '\n')