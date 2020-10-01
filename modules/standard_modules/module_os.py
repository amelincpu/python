'''
OS module
'''

import os

# 'listdir' built-in function from 'os' module reads a folder content
v_dir_folder = os.listdir('c:/')
for v_item in v_dir_folder:
    print(v_item)