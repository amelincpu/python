# Sorted function.

print('\n', '*'*50, '\n')

print(sorted((5, 6, 2, 9, 11)))

print(sorted('kajifeufksqo'))

v_list = [
    [23, 'Fa0/1', 'f123.d144.43dc'],
    [3, 'Fa0/5', 'fe23.de44.43dc'],
    [23, 'Fa0/13', 'a123.dee4.43dc']
    ]
print(sorted(v_list))

# import a feature to point to an item in a list, to call by index
from operator import itemgetter
print(sorted(v_list, key=itemgetter(1)))

print('\n', '*'*50, '\n')

# 'key=int' helps 'sorted' to work with integer
v_vlans = ['23', '2', '12', '1', '10', '100']
print(sorted(v_vlans))
print(sorted(v_vlans, key=int))

print('\n', '*'*50, '\n')