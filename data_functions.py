# Python Functions
#
print('\n', '*'*50, '\n')
#
# input - Read a string from standard input
var_a = input('enter value of var_a:')
print('value of var_a is:', var_a)
print('var_a variable data type is:', type(var_a))
#
print('\n', '*'*50, '\n')
#
# int - Convert a number or string to an integer, or return 0 if no arguments are given.
var_b = '100'
print('var_b=', int(var_b))
print('var_b=', int(var_b, 2)) # from bin to dec
#
print('\n', '*'*50, '\n')
#
# bin - Return the binary representation of an integer.
print('bin(255)', bin(255))
#
print('\n', '*'*50, '\n')
#
# hex - Return the hexadecimal representation of an integer.
print('hex(255)', hex(255))
#
print('\n', '*'*50, '\n')
#
# Types conversion - list(), tuple(), set()
var_c = 'Hello World!'
print('value of var_c is:', var_c)
print('var_c variable data type is:', type(var_c))
#
print('\nlist(var_c):', list(var_c), '\ntype(list(var_c)):', type(list(var_c)))
#
print('\ntuple(var_c):', tuple(var_c), '\ntype(tuple(var_c)):', type(tuple(var_c)))
#
print('\nset(var_c):', set(var_c), '\ntype(set(var_c)):', type(set(var_c)))
#
print('\n', '*'*50, '\n')
#
# a list to variables unpack
var_d = ['1.1.1.0', '/24', '255.255.255.0']
print('subnet:', var_d[0])
print('cidr:', var_d[1])
print('mask', var_d[2])
#
var_e1, var_e2, var_e3 = var_d
print('\nsubnet:', var_e1)
print('cidr:', var_e2)
print('mask', var_e3)
#
print('\n', '*'*50, '\n')