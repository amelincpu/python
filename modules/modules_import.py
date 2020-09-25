# Modules import.

print('\n', '*'*50, '\n')

# import 'sys' module, access to the module functions via 'sys.*'
import sys

print(sys.version)

print('\n', '*'*50, '\n')

# import only 'version' function from 'sys' module, access to the function via 'version'

from sys import version

print(version)

print('\n', '*'*50, '\n')