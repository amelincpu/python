# Sorted function.

print('\n', '*'*50, '\n')

print(sorted((5, 6, 2, 9, 11)))

print(sorted('kajifeufksqo'))

v_list = [
    [23, 'Fa0/01', 'f123.d144.43dc'],
    [3, 'Fa0/05', 'fe23.de44.43dc'],
    [23, 'Fa0/13', 'a123.dee4.43dc']
    ]
print(sorted(v_list))

# import a feature to point to an item in a list, to call by index
from operator import itemgetter
print(sorted(v_list, key=itemgetter(1)))

print('\n', '*'*50, '\n')