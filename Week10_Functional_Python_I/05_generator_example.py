def numbers():
    for i in range(1024):
        print(f" = {i}")
        yield i  # generators use a yield statement and not a return

x = numbers()

print(next(x))
print(next(x))

