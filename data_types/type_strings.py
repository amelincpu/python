# integer is a text type
var_a = 'Hello World!'
print('\nvar_a variable =', (var_a))

var_b = '''\nHello World!
Hello World!
Hello World!
Hello World!
'''
print('\nvar_b variable =', (var_b))

type(var_a) # type() - data type checking
print('var_a variable data type is:', type(var_a))

id(var_a) # id() - memory id check
print('\na memory cell id for var_a variable is:', id(var_a), '\na memory cell id for var_b variable is:', id(var_b), '\n', '\nif we do var_a = var_a + var_b')
var_a = var_a + var_b
print('var_a variable =', (var_a), '\na memory cell id for var_a variable is:', id(var_a))

var_a = 'Hello World!' # returning original value of var_a
print('\nvar_a variable =', (var_a))
var_a[0] # access to a string elements from 0 until X
print('\naccess to a string elements:')
print(var_a[0])
print(var_a[7])

var_a[-3] # access to a string elements from the end
print(var_a[-2])
print(var_a[-4])

var_a[-3] # access to a string range
print(var_a[2:5])
print(var_a[5:])
print(var_a[5:-1])
print(var_a[0:9:2]) # 3rd means only every second element from the range
print(var_a[::-1]) # flip the string

# string methods
print('\nstring methods:')
var_a_up = var_a.upper() # make all symbols upper case
print(var_a_up)
var_a_low = var_a.lower() # make all symbols lower case
print(var_a_low)