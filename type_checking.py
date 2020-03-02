# Type checking
#
print('\n', '*'*50, '\n')
#
# check with boolean 'True' or 'False'
var_a = 'Hello World!'
print('var_a =', var_a)
#
var_b = (type(var_a) == str)
print('var_b =', var_b)
print('var_b type is:', type(var_b))
#
if var_b == True:
    print('var_a is a string')
else:
    print('var_a is not a string')
#
print('\n', '*'*50, '\n')