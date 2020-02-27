# Sequence Type: A list <class 'list'> is a collection which is ordered and changeable. Allows duplicate members.
var_a = [1, 2, 'hello', 'two']
print('\nvar_a variable =', (var_a))
#
var_b = [1, 2,
'hello',
'two']
print('var_a variable =', (var_a))
#
type(var_a) # type() - data type checking
print('\nvar_a variable data type is:', type(var_a), '\n')
#
var_a[3] # access to a list elements from the end
print(var_a[3])
print(var_a[-3])
#
var_a[1:3] # access to a list range
print(var_a[1:3])
print(var_a[2:])
print(var_a[:])
#
id(var_a) # id() - memory id check
print('\na memory cell id for var_a variable is:', id(var_a))
#
var_c = [2, 'hi']
print('\nvar_a =', var_a)
print('var_c =', var_c)
print('if we change var_a: "var_a = var_a + var_c"')
var_a = var_a + var_c
print('\nvar_a variable =', (var_a), '\na memory cell id for var_a variable is:', id(var_a))
var_a[2] = "bye"
print('\nchanging 3rd element of var_a - "var_a[2] = "bye""')
print('\nvar_a variable =', (var_a), '\na memory cell id for var_a variable is:', id(var_a))
var_e = var_a
print('\nif we create a new variable "var_e = var_a" the id of both will be same:', '\nvar_a id =', id(var_a), '\nvar_e id =', id(var_e))
#
print('\n', '*'*50, '\n')
#
var_d = [['a', 'b', 'c'], [1, 2, 3]]
print('\nvar_d =', (var_d))
print('access to var_d list element - "var_d[X][X]"')
print(var_d[0]) # access to a list element
print(var_d[1])
print(var_d[0][2])