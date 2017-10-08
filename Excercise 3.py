import math

def add(a, b):
    try:
        return math.sqrt(a+b)
    except TypeError:
        return None

print(add(2,2))
print(add("2","2"))
print(add(2,"3"))
