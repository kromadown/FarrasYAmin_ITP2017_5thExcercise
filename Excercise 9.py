def my_gen(n):
	i = int(input())
	while i > n:
		yield i
		i -= 1

g = my_gen(-1)
print(type(g))

for x in g:
	print(x)
