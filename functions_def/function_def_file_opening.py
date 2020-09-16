# creation and call a function
#
import os # the module to check a file is exist
#
print('\n', '*'*50, '\n')
#
# a function creation
def f_open_file(v_filename): # v_filename calls 'a parameter'
    # The function checks a file is exist and then opens it.
    if os.path.exists(v_filename): # checks a file is exist
        with open(v_filename) as v_file:
            return v_file.read()
    else:
        return print('the file is not exist')
#
# requests a filename for printing
v_filename_input = input('Specify a filename to print it: ')
#
print(f_open_file('C:/Users/Alex/Dropbox/Phyton/functions_def/{}'.format(v_filename_input))) # v_filename_input calls 'an argument'
#
print('\n', '*'*50, '\n')