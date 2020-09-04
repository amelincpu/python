#
#
print('\n', '*'*50, '\n')
#
var_a = 3
while var_a < 30:
    print(var_a)
    var_a = var_a + 1
    if var_a == 16:
        print('var_a = 16')
        break # stops the loop when 'var_a'=16 
#
print('\n', '*'*50, '\n')
#
var_a = 3
while var_a < 30:
    print(var_a)
    var_a = var_a + 1
#    continue # ignores any code after the line and jumps back to the main loop ('while' string)
    if var_a == 16:
        print('var_a = 16')
        break # stops the loop when 'var_a'=16 
#
print('\n', '*'*50, '\n')