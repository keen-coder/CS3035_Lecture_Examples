

def min_or_max(list1, f):
    return f(list1)


L = [2, 10, 3, 5, 6, 7, 1, 8, 9, 4]

print(min_or_max(L, max))
print(min_or_max(L, min))