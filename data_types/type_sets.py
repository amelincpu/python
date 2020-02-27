# Set Type: A set <class 'set'> is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
#
print('\n', '*'*50, '\n')
#
var_a = {'red', 'black', 'white', 21, 24}
print('var_a variable =', (var_a))
#
type(var_a) # type() - data type checking
print('var_a variable data type is:', type(var_a))
#
print('\n', '*'*50, '\n')
#
# a list to a tuple converting - tuple(list_variable)
var_b = [1, 2, 'hello', 'two', 1, 2, 2, 1, 'two']
var_c = set(var_b) # only unique values come into the set
print('var_b=', var_b)
print('var_c = set(var_b)')
print('var_c=', var_c)
print('var_c variable data type is:', type(var_c))
#
print('\n', '*'*50, '\n')
#
# 'add' - a method to add a new element
# 'discard' - a method to delete a element
var_c.add(4)
print('var_c.add(4)')
print('var_c=', var_c)
#
var_c.discard('two')
print("var_c.discard('two')")
print('var_c=', var_c)
#
print('\n', '*'*50, '\n')