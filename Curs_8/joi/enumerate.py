from itertools import count
a = "Ana are mere"
for index, val in enumerate(a):
    print(f"{index} {val}")


def my_enumerate(iterable):
    # index = range(len(iterable))
    # for (idx, val) in zip(index, iterable):
    #     yield idx, val
    # nr_crt = 0
    # for val in iterable:
    #     yield nr_crt, val
    #     nr_crt += 1
    for idx, val in zip(count(0), iterable):
        yield idx, val


for index, val in my_enumerate(a):
    print(f"{index} {val}")