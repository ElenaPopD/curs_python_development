from collections import defaultdict


# a = {}
# a[0] # KeyError


c = defaultdict(lambda: 1)
print(c[0])