# Could be multiple 'except'. Also could be 'else' in the end. 'finally' is always performed.
#
print('\n', '*'*50, '\n')
#
var_a = {
    'type': 'car',
    'color': 'blue',
    'number': 23
}
#
try:
    print(var_a['color'])
except KeyError: # could be 'except (KeyError, KeyError1):'
    print('the key does not exist')
#
print('\n', '*'*50, '\n')
#
try:
    print(var_a['size'])
except KeyError:
    print('the key does not exist')
#
print('\n', '*'*50, '\n')