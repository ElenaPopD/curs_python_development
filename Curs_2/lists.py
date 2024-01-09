['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# Append
a = [1,2,3]
a.append(1)
print(a)

# Copy
b = a.copy()
print(b)
print(a is b)

# Count
print(a.count(1))

# Extend
a.extend(b)
print(a)
# Append list
a.append([1,2,3])
print(a)

# Index
print(a.index(3))
# print(a.index(None)) # eroare

# Pop - ultimul element din lista este scos si returnat
print(a.pop())
print(a)
print(a.pop())
print(a)

# Insert
a.insert(4, 5)
print(a)

a.insert(int(len(a)/2), 100)
print(a)

# Remove
a.remove(3)
a.remove(a[3])
print(a)
del a[3]
len(a)
print(a)
# reverse
a.reverse()
print(a)

# sort
a.sort()
print(a)
# Clear
a.clear()
print(a)