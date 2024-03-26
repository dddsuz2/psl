def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


print(any([1, 0]))
print(any([0]))
print(any([0, 0]))
print(any([1, 1]))
print(any([0, "a"]))
