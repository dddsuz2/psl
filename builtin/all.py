def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print(all([0, 0, 1]))
print(all([0, 0, 0]))
print(all([1, 1, 1]))
print(all(["a"]))
