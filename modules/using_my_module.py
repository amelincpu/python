import sys

# sys.path.insert(1, 'C:/Users/Alex/Dropbox/Phyton/modules/')

# print(sys.path)

import my_module_check_ip

print(my_module_check_ip.__doc__)

print(my_module_check_ip.f_check_ip.__doc__)

v_ip_input = input('Enter an ip address: ') 

if my_module_check_ip.f_check_ip(v_ip_input):
    print('The ip is valid')
else:
    print('The ip is not valid')