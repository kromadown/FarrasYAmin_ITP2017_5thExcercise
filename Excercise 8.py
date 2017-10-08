import math

n = int(input())
a = lambda x: print(x**2)
a(n)

cod = int(input())
mw = int(input())
s = lambda x, y: print (math.sqrt(x**2 + y**2))
s(cod, mw)

gg = [1,2,3,4,5]
h = lambda x: print(float(sum(x)) / max(len(x), 1))
h(gg)

text = input()
ex = lambda x: print("".join(set(x)))
ex(text)
