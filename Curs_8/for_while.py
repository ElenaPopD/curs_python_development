a = [1,2,3]

for element in a:
    print(element)

# iterator_a = iter(a)
# print(next(iterator_a))
# print(next(iterator_a))
# print(next(iterator_a))
# print(next(iterator_a))
# For with while
iterator_a = iter(a)
while True:
    try:
        print(next(iterator_a))
    except StopIteration:
        break

