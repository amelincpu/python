import re

old_mac = '''
0d01.345a.ee45f
0001.345a.EE45f
0221.345a.E845f
a221.345a.e845f
'''

print(old_mac)

print(re.sub(r'(\w+)\.(\w+)\.(\w+)', r'\1:\2:\3', old_mac))