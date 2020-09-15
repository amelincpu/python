# A configuration parsing and creating of a dictionary or writing to a file.
#
print('\n', '*'*50, '\n')
#
# Creating a dictionary from a config file:
v_result1 = {}
with open('C:/Users/Alex/Dropbox/Phyton/working_with_dictionaries/config.txt') as v_original_file1:
    for v_line2 in v_original_file1:
        if 'interface' in v_line2:
            v_interface1 = v_line2.split()[1]
        if 'address' in v_line2:
            v_ip2 = v_line2.split()[2]
            v_result1[v_interface1] = v_ip2

print(v_result1)
#
print('\n', '*'*50, '\n')
#
# Open a file and grab data from it to a list:
v_result = [] # an empty list creation
with open('C:/Users/Alex/Dropbox/Phyton/working_with_dictionaries/config.txt') as v_original_file:
    for v_line in v_original_file:
        if 'interface' in v_line:
            v_interface = v_line.split()[1]
        if 'address' in v_line:
            v_ip = v_line.split()[2]
            v_result.append([v_interface, ' - ', v_ip])
#
# Write the data to a file:
with open('C:/Users/Alex/Dropbox/Phyton/working_with_dictionaries/result.txt', 'w') as var_cfgfile:
    for var_line in v_result:
        for var_line1 in var_line:
            var_cfgfile.write(var_line1)
        var_cfgfile.write('\n')
var_cfgfile.closed
#
# Print the result file:
with open('C:/Users/Alex/Dropbox/Phyton/working_with_dictionaries/result.txt') as var_a:
    for var_b in var_a:
        print(var_b.rstrip())
#
print('\n', '*'*50, '\n')