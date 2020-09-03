# Using 'for' and 'if' together.
#
print('\n', '*'*50, '\n')
#
var_a = {
    '0/0': 10,
    '0/1': 20,
    '0/2': 30
}
#
var_b = [
    'no shutdown',
    'switchport mode access',
    'switchport access vlan']
#
print(var_a)
print(var_b)
#
for var_c in var_a:
    print('\ninterface Gi{}'.format(var_c))
    for var_d in var_b:
        if 'vlan' in var_d:
            print(var_d, var_a[var_c])
        else:
            print(var_d)
#
print('\n', '*'*50, '\n')