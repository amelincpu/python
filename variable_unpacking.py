# Variable unpacking.
#
print('\n', '*'*50, '\n')
#
# Unpack a string to variables:
v_from_device = 'dmz Gi0/1 aaaa.bbbb.cccc 10.0.0.2 255.255.255.0'
print('v_from_device = ', v_from_device, '\n', 'v_from_device variable data type is:', type(v_from_device))
v_int_description, v_port_number, v_mac, v_ip, v_mask = v_from_device.split()
print('\n', v_int_description,'\n', v_port_number, '\n', v_ip, '\n', v_mac,'\n', v_mask)
#
print('\n', '*'*50, '\n')
#
# A string to a list unpacking. And then to variables with selection from the list:
v_from_device_to_list = v_from_device.split()
print(v_from_device_to_list)
_, v_port_number1, _, v_ip1, v_mask1 = v_from_device_to_list # _ just a name of a variable which in use of everybody
print('\n', v_port_number1, '\n', v_ip1, '\n', v_mask1)
#
v_int_description2, v_port_number2, *v_rest_data = v_from_device_to_list # * takes all other data
print('\n', v_int_description2, '\n', v_port_number2, '\n', v_rest_data)
#
print('\n', '*'*50, '\n')
#
# Unpacking a dictionary to a list of tuples, then to a list with options:
v_dictionary = {
    'type': 'car',
    'color': 'blue',
    'number': 23}
print(v_dictionary, '\n')
v_list = list(v_dictionary.items())
print(v_list, '\n')
v_list2 = []
for v_tup in v_list:
    v_key, v_value = v_tup
    print(v_key, v_value)
    v_list2.append(v_key)
    v_list2.append(v_value)
print('\n', v_list2, '\n')
# Keys and values can be checked from a loop:
for v_key, v_value in v_list:
    print(v_key, v_value)
#
print('\n', '*'*50, '\n')
#
#print all values from the new list:
for v_value1 in v_list2:
    print(v_value1)
#
print('\n', '*'*50, '\n')