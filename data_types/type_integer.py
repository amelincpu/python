# Integer <class 'int'> is a numeric type. Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
var_a = 1
print('\nvar_a variable =', (var_a))

type(var_a) # type() - data type checking
print('var_a variable data type is:', type(var_a))

id(var_a) # id() - memory id check
print('\na memory cell id for var_a variable is:', id(var_a), '\nif we change var_a: "var_a = var_a + 1"')
var_a = var_a + 1
print('var_a variable =', (var_a), '\na memory cell id for var_a variable is:', id(var_a))