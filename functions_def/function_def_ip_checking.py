# The script checks an ip is correct.

# import the module to work with ip addresses
import ipaddress

print('\n', '*'*50, '\n')

def check_ip(v_ip):
    # the function checks an ip is correct
    try:
        ipaddress.ip_interface(v_ip)
        return True
    except ValueError:
        return False

# requests to enter an ip
v_ip_input = input('Enter an ip address: ') 

# call the function to check the input
v_check_ip_result = check_ip(v_ip_input)

# print the result of checking
if v_check_ip_result:
    print('The ip address is valid')
else:
    print('The ip address is not valid')

print('\n', '*'*50, '\n')