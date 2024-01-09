b = {1,2,3}
print(type(b))
c = {1:1}
print(type(c))
b.add(3)
print(b)
b.add(4)
print(b)
b.add(4)
print(b)
a = {2,3,5}
print(a - b)
print(b - a)
c = [1,1,1,1,1]
d = set(c)
print(c, d)
print(a.union(b))
print(a.intersection(b))