# Modules import.

print('\n', '*'*50, '\n')

# import 'sys' module, access to the module functions via 'sys.*'
import sys
print(sys.version)

print('\n', '*'*50, '\n')

# import only 'version' function from 'sys' module, access to the function via 'version'
from sys import version
print(version)

# import a few functions
from sys import version, argv

# assinge an alias for a module
import sys as module_system
print(module_system.version)

print('\n', '*'*50, '\n')