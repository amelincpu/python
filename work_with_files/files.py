#
# 
print('\n', '*'*50, '\n')
#
# print file content
with open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile1.txt') as var_a:
    print(var_a.read())
#
print('\n', '*'*50, '\n')
#
# open a file and print all lines from it, then close it
var_a = open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile1.txt')
print(var_a.readlines())
var_a.close()
#
print('\n', '*'*50, '\n')
#
# open a file and print the first line only from it, then close it
var_a = open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile1.txt')
print(var_a.readline())
var_a.close()
#
# create/reset a file and write lines in it, then close it
var_b = open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile2.txt', 'w')
var_b.write('new line1\n')
var_b.write('new line2\n')
var_b.close()
#
print('\n', '*'*50, '\n')
#
# copy one file to another
var_a = open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile1.txt')
var_c = open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile3.txt', 'w')
for var_d in var_a:
    var_c.write(var_d)
var_a.close()
var_c.close()
var_c = open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile1.txt')
print(var_c.readlines())
var_c.close()
#
print('\n', '*'*50, '\n')
#
# write to a file from a list
var_e = [
    'command1',
    'command2',
    'command3']
var_f = open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile4.txt', 'w')
for var_g in var_e:
    var_f.write(var_g+'\n')
var_f.close()
with open('C:/Users/Alex/Dropbox/Phyton/work_with_files/textfile4.txt') as var_h:
    print(var_h.read())
#
print('\n', '*'*50, '\n')
#
# check is a file closed
print(var_f.closed)
#
print('\n', '*'*50, '\n')