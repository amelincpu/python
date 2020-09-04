#
#
print('\n', '*'*50, '\n')
#
# print file context with no spaces between lines and only lines starts with 'command2'
with open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile4.txt') as var_a:
    for var_b in var_a:
        if var_b.startswith('command2'):
            print(var_b.rstrip())
#
print('\n', '*'*50, '\n')
#
# write from a list to a file
var_commands = [
    'int fa 0/1',
    'no shut',
    'switchport mode access',
    'switchport access vlan 10'
]
with open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile5.txt', 'w') as var_cfgfile:
    for var_line in var_commands:
        var_cfgfile.write(var_line+'\n')
print('the file is closed - ', var_cfgfile.closed, '\n')
with open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile5.txt') as var_a:
    for var_b in var_a:
        print(var_b.rstrip())
#
print('\n', '*'*50, '\n')
#
# load from a file to a list
var_buffer = []
with open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile5.txt') as var_scriptfile:
    for var_line in var_scriptfile:
        var_buffer.append(var_line.rstrip())
print(var_buffer, '\n')
for var_line1 in var_buffer:
    if var_line1.startswith('switchport'):
        print(var_line1)
#
print('\n', '*'*50, '\n')
#
# copy from file to file
print('copy from file to file:\n')
with open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile5.txt') as var_src_file, open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile6.txt', 'w') as var_dst_file:
    for var_line3 in var_src_file:
        var_dst_file.write(var_line3)
        print(var_line3.rstrip())
print('\n new file Python information: ', var_dst_file)
#
print('\n', '*'*50, '\n')