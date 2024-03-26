print(bin(23))
print(bin(-10))


class my_bin:
    def __init__(self, value):
        self.value = value

    def __index__(self):
        return int(self.value)
    
t = my_bin("19")
print(bin(t))
