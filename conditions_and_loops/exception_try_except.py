#
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
    print(var_a['size'])
except KeyError:
    print('the key does not exist')
#
print('\n', '*'*50, '\n')