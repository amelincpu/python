'''
IPaddress module
'''

import ipaddress

print('\n', '*'*50, '\n')

v_ip1 = ipaddress.ip_address('8.8.8.8')
print(v_ip1)
print('is the ip {} ='.format(v_ip1), v_ip1.is_multicast)

print('\n', '*'*50, '\n')

v_network1 = ipaddress.ip_network('10.0.0.0/28')
print(v_network1)
print(v_network1.broadcast_address)
print(v_network1.prefixlen)
print(v_network1.num_addresses)
for v_ip in v_network1:
    print (v_ip)
print(list(v_network1))

print('\n', '*'*50, '\n')

v_new_network = ipaddress.ip_network(v_network1).subnets(new_prefix=30)
print(list(v_new_network))

print('\n', '*'*50, '\n')

v_ip2 = ipaddress.ip_interface('8.8.8.8')
print(v_ip1)
print(v_ip2.network)

print('\n', '*'*50, '\n')