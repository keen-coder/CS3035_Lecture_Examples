import timeit

start = timeit.default_timer()
print('Monty Python ' * 10000000)
end = timeit.default_timer()
print(end - start) # Time in seconds, e.g. 5.38091952400282
