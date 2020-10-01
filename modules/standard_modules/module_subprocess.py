'''
Subprocess module
'''

import subprocess

# run 'ping' in windowas cmd, put the output in the variable 
v_ping_output = subprocess.run('ping 8.8.8.8', stdout=subprocess.PIPE)

# decode in 'utf-8' and print 'stdout' output
print(v_ping_output.stdout.decode('utf-8'))