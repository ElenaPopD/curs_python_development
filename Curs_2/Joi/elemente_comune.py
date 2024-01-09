a = [1, 2 ,3]
b = [2, 3 ,5]

c = []

for i in a:
    if i in b:
        c.append(i)
print(c)

d = [i for i in a if i in b]
print(d)

