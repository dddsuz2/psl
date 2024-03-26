print(bool(0))
print(bool(1))

class my_bool:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return bool(self.value)
    
t = my_bool(0)
print(bool(t))
