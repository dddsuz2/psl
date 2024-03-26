print(abs(0.3))
print(abs(2))
print(abs(1.1))

print(abs(-1))
print(abs(-0.2))

class my_abs:
    def __init__(self, value):
        self.value = value
    def __abs__(self):
        return self.value
    
class not_abs:
    def __init__(self, value):
        self.value = value

a = my_abs(-2)
print(abs(a)) # -2

b = my_abs(-2)
print(abs(b)) # -2
