a = [print(x) for x in range(10)]
print(type(a))

b = (print(x) for x in range(10))
print(type(b))

next(b)
next(b)
for _ in b:
    pass
