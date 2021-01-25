"""Enumerate function."""


print('\n', '*'*50, '\n')

# 'enumerate' returns index-item pairs
v_list = [
    ['vlan 23', 'Fa0/01', 'f123.d144.43dc'],
    ['vlan 3', 'Fa0/05', 'fe23.de44.43dc'],
    ['vlan 23', 'Fa0/13', 'a123.dee4.43dc']
    ]

for v_index, v_item in enumerate(v_list, 1):
    print(v_index, v_item)

print('\n', '*'*50, '\n')
