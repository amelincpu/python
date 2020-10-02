v_list = ['a', 'b', 'c', 'd', 'e']
print(v_list)

print(iter(v_list))

v_list_iter = iter(v_list)

print(next(v_list_iter))
print(next(v_list_iter))
print(next(v_list_iter))
print(next(v_list_iter))
print(next(v_list_iter))

print(sorted.__doc__) # Return a new list containing all items from the iterable in ascending order.