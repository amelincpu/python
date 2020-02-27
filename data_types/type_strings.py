# Text Type: A string <class 'str'> is a text type.
var_a = 'Hello World!'
print('\nvar_a variable =', (var_a))
#
var_b = '''\nHello World!
Hello World!
Hello World!
Hello World!
'''
print('\nvar_b variable =', (var_b))
#
type(var_a) # type() - data type checking
print('var_a variable data type is:', type(var_a))
#
id(var_a) # id() - memory id check
print('\na memory cell id for var_a variable is:', id(var_a), '\na memory cell id for var_b variable is:', id(var_b), '\n', '\nif we do var_a = var_a + var_b')
var_a = var_a + var_b
print('var_a variable =', (var_a), '\na memory cell id for var_a variable is:', id(var_a))
#
var_a = 'Hello World!' # returning original value of var_a
print('\nvar_a variable =', (var_a))
var_a[0] # access to a string elements from 0 until X
print('\naccess to a string elements:')
print(var_a[0])
print(var_a[7])
#
var_a[-3] # access to a string elements from the end
print(var_a[-2])
print(var_a[-4])
#
var_a[-3] # access to a string range
print(var_a[2:5])
print(var_a[5:])
print(var_a[5:-1])
print(var_a[0:9:2]) # 3rd means only every second element from the range
print(var_a[::-1]) # flip the string
#
# string methods
print('\nstring methods:')
var_a_up = var_a.upper() # make all symbols upper case
print(var_a_up)
var_a_low = var_a.lower() # make all symbols lower case
print(var_a_low)
#
# str method
print('\n"str" method using:', str.lower(var_a))
#
# format method
var_c = 'interface {}'
var_d = 'Fa0/1'
var_e = var_c.format(var_d)
print('\n"format" method using:', var_e)
var_f = '{} {} {}'
var_g = var_f.format('Switch', 14, (var_d))
print('\n"format" method using:', var_g)
#
# output editing 
var_f = '{:20} {:<20} {:20}' # ':' - width; '<' - alignment
var_g = var_f.format('Switch', 14, (var_d))
print('\n"format" method using:', var_g)
var_g = var_f.format('Switch', 21, (var_d))
print('"format" method using:', var_g)
#
# format converting
print('\n4 is', '{:b}'.format(4), 'in binary') # ':b' - to binary
print(' 4 is', '{:08b}'.format(4), 'in binary') # '08' - fill 0 till 8 symbols
#
# call {} by names
var_f = '''
IP address: {var_f1}
Mask:       {var_f2}
'''
print('\n',var_f.format(var_f1='1.1.1.1', var_f2='255.255.255.0'))