# Mapping Type: A dictionary <class 'dict'> is a collection, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
var_a = {
    'type': 'car',
    'color': 'blue',
    'number': 23
}
#
print('\n', '*'*100, '\n')
#
print('\nvar_a variable =', (var_a))

type(var_a) # type() - data type checking
print('\nvar_a variable data type is:', type(var_a))

# call a key value from a dictionary - dictionary['key name']
print('\n"color" key from var_a =', var_a['color'])
#
print('\n', '*'*100, '\n')
#
# change a key value in a dictionary - dictionary['key name'] = black
var_a['color'] = 'black'
print("\nchange 'color' key in var_a - 'var_a['color'] = 'black''", "\nvar_a variable =", (var_a))
#
print('\n', '*'*100, '\n')
#
print('\nvar_a variable =', (var_a))
id(var_a) # id() - memory id check
print('\na memory cell id for var_a variable is:', id(var_a), '\nif we delete "number" key from var_a dictionary: "del var_a["number"]"')
del var_a['number']
print('\nvar_a variable =', (var_a))
print('\na memory cell id for var_a variable is:', id(var_a))
#
print('\n', '*'*100, '\n')
#
# adding one dictionary to another - dictionary1.update(dictionary2)
var_b = {
    'shape' : 'triangle',
    'day' : 'Monday'
}
print('var_a variable =', (var_a))
print('var_b variable =', (var_b),'\n' ,'\nnew var_a value is: var_a = var_a + var_b')
var_a.update(var_b)
print('\nnew var_a variable =', (var_a), '\na memory cell id for var_a variable is:', id(var_a))
#
print('\n', '*'*100, '\n')
#
var_c = {
    'option1' : {
    'type': 'car',
    'color': 'blue',
    'number': 23
    },
    'option2' : {
    'type': 'boat',
    'color': 'green',
    'number': 55
    },
    'option3' : {
    'type': 'airplane',
    'color': 'red',
    'number': 82
    }
}
print('\nvar_c variable =', (var_c))
#
print('\n', '*'*100, '\n')
#
# dictionary methods
print('var_a variable =', (var_a))
print('var_a keys:', var_a.keys())
print('var_a values:', var_a.values())
print('var_a items:', var_a.items()) # 'dict_items, dict_values, dict_keys' - view objects