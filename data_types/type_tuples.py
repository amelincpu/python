import sys # 'sys' module importing
# Sequence Type: A tuple <class 'tuple'> is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#
print('\n', '*'*50, '\n')
#
var_a = ('red', 'black', 'white', 21, 24)
print('var_a variable =', (var_a))
#
type(var_a) # type() - data type checking
print('var_a variable data type is:', type(var_a))
#
print('\n', '*'*50, '\n')
#
# a list to a tuple converting - tuple(list_variable)
var_b = ['apple', 'banana', 23, 35]
var_c = tuple(var_b)
print('var_b=', (var_b))
print('var_c=', (var_c))
print('\nvar_b variable data type is:', type(var_b))
print('var_c variable data type is:', type(var_c))
# check a varibale size in memory - sys.getsizeof(var)
print ('\nvar_b size is', sys.getsizeof(var_b), 'bytes')
print ('var_c size is', sys.getsizeof(var_c), 'bytes')
#
print('\n', '*'*50, '\n')
#
print('var_a variable =', (var_a))
print('var_c variable =', (var_c))
var_d = var_a + var_c
print('\nvar_d = var_a + var_c =', var_d)
print('var_d length =', len(var_d)) # len() - check lenght
#
print('\n', '*'*50, '\n')
#
# a tuple to a list converting - list(tuple_variable)
var_e = list(var_d)
print('var_e = list(var_d) =', var_e)
print('var_e variable data type is:', type(var_e))
#
print('\n', '*'*50, '\n')