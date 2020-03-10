# Python supports the usual logical conditions from mathematics:
# 
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
#
print('\n', '*'*50, '\n')
#
# if-else
var_a = 2
print('variable var_a =', var_a)
if var_a > 3:
    print('var_a > 3')
else:
    print('var_a < 3')
#
print('\n', '*'*50, '\n')
#
# if-elif-else vs if-if-else
var_a = 5
print('variable var_a =', var_a)
if var_a > 3:
    print('var_a > 3')
elif var_a == 5:
    print('var_a = 5')
else:
    print('var_a < 3')
#
print('\n', '*'*50, '\n')
#
var_a = 5
print('variable var_a =', var_a)
if var_a > 3:
    print('var_a > 3')
    if var_a == 5:
         print('var_a = 5')
else:
    print('var_a < 3')
#
print('\n', '*'*50, '\n')