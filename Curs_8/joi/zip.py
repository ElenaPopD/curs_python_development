a = range(1,11)
b = range(11,21)
# print(list(a))
# print(list(b))

for (nr_a, nr_b) in zip(a,b):
    print(f"({nr_a}, {nr_b})")

    