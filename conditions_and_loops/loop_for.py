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
# 'range' using in 'for'
for var_x in range(5):
    print('interface Gi0/{}'.format(var_x))
#
print('\n', '*'*50, '\n')