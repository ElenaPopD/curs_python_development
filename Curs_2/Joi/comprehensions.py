a = [1,2,3,4,5,6,7,8,9,10]
a = [42, 69, 102, 55, 90, 37, 91, 94]

b = []
for element in a:
    if element % 2 == 0:
        b.append(element)
print(b)

c = [element for element in a if element % 2 == 0]

print(c)

d = filter(lambda x : x % 2 ==0, a)
print(list(d))

e = [element ** 2 for element in a if element %2 == 0]
print(e)
