#
#
print('\n', '*'*50, '\n')
#
# 
v_result = []
with open('C:/Users/Alex/Dropbox/Phyton/working_with_dictionaries/config.txt') as v_original_file:
    for v_line in v_original_file:
        if 'interface' in v_line:
            v_interface = v_line.split()[1]
        if 'address' in v_line:
            v_ip = v_line.split()[2]
            v_result.append([v_interface, ' - ', v_ip])
with open('C:/Users/Alex/Dropbox/Phyton/working_with_dictionaries/result.txt', 'w') as var_cfgfile:
    for var_line in v_result:
        for var_line1 in var_line:
            var_cfgfile.write(var_line1)
        var_cfgfile.write('\n')
var_cfgfile.closed
#
#
with open('C:/Users/Alex/Dropbox/Phyton/working_with_dictionaries/result.txt') as var_a:
    for var_b in var_a:
        print(var_b.rstrip())
#
print('\n', '*'*50, '\n')