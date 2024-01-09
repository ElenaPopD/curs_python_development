a = [1,2,3]
b = [4,5]

for nr_a, nr_b in zip(a,b):
    print(nr_a, nr_b)

from itertools import zip_longest

for nr_a, nr_b in zip_longest(a,b, fillvalue=1000):
    print(nr_a, nr_b)