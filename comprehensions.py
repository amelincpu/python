# Comprehensions.
#
print('\n', '*'*50, '\n')
#
v_ip = '10.0.0.1'
#
# Creating a list from a strin by a loop:
v_ip_octets = []
for v_octet in v_ip.split('.'):
    v_ip_octets.append(int(v_octet))
print(v_ip_octets, '\n')
#
# The same operaton by comprehension:
v_ip_octets1 = [int(v_octet1) for v_octet1 in v_ip.split('.')]
print(v_ip_octets1)
#
print('\n', '*'*50, '\n')
#
# 'if' usinf in list comprehension:
v_from_device = ['vlan', 10, 'vlan', 20, 'vlan', 30]
v_vlan_list = [v_item for v_item in v_from_device if type(v_item) == int]
for v_item1 in v_vlan_list:
    print(v_item1)
#
print('\n', '*'*50, '\n')
#
# Creating a set by comprehension:
v_from_device1 = ['vlan', 10, 'vlan', 20, 'vlan', 30,  'vlan', 10]
v_vlan_set = {v_item2 for v_item2 in v_from_device1 if type(v_item2) == int}
print(v_vlan_set)
#
print('\n', '*'*50, '\n')
#
# Creating a dictionary by comprehension:
v_list = list(range(7))
print(v_list)
v_dictionary = {v_key: v_key for v_key in v_list}
print(v_dictionary)
#
print('\n', '*'*50, '\n')