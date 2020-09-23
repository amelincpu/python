# Print function.

# import the time module
import time

print('\n', '*'*50, '\n')

# parameter 'sep' specifies hot to separate print data
print(1,2,3, sep='|')

# parameter 'end' specifies hot to end the print ('\n' is defaul)
print(1,2,3, end='|')

print('\n', '*'*50, '\n')

# parameter 'flush' tells print to print without end of the string waiting
for v_percentage in range(10, 101, 10):
    print(v_percentage, end='% ', flush=True)
    time.sleep(0.5)

print('\n', '*'*50, '\n')