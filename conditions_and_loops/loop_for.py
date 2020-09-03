# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#
print('\n', '*'*50, '\n')
#
var_a = [] # an empty list
for x in [0, 1, 2, 3]:
    var_a.append('hello') # fill the empty list from 0 to 3
print('var_a=', var_a)
#
print('\n', '*'*50, '\n')
#
#
# en example of 'for' using
var_b = '192.168.23.45'
print('var_b=', var_b)
print('var_b type is', type(var_b))
var_b1 = var_b.split('.')
print('\nvar_b1=', var_b1)
print('var_b1 type is', type(var_b1))
var_b2 = []
print('\nvar_b2=', var_b2)
print('var_b2 type is', type(var_b2), '\n')
for var_x in var_b1: # executes the body for all elements in the list
    var_b2.append('{:08b}'.format(int(var_x)))
    print('add', '{:03}'.format(int(var_x)), '| var_b2 =', var_b2)
print('\nvar_b2=', var_b2)
print('var_b2 type is', type(var_b2)) 
#
print('\n', '*'*50, '\n')
#
#
# 'range' using in 'for'
for var_y in range(6):
    print('interface Gi0/{}'.format(var_y))
#
print('\n', '*'*50, '\n')
#
#
# a double loop example
#
#var_c = ['0/1', '0/2', '0/3'] it is equal:
var_c =[]
for var_y1 in range(3):
    var_c.append('0/{}'.format(var_y1))
#
var_d = ['no shutdown', 'switchport mode access', 'switchport access vlan 5']
print('var_c=', var_c)
print('var_d=', var_d)
for var_x1 in var_c:
    print('\ninterface Gi{}'.format(var_x1))
    for var_x2 in var_d:
        print(var_x2)
#
print('\n', '*'*50, '\n')