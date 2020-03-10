# Username and Password input
#
print('\n', '*'*100, '\n')
#
var_username = input('Username: ')
var_password = input('Password: ')
#
if len(var_password) < 8:
    print('Password is too short')
elif var_username.lower() in var_password.lower():
    print('Password contains Username')
else:
    print('\nPassword for user "{}" set'.format(var_username))