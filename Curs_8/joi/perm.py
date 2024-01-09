from itertools import permutations, combinations
a = [1,2,3]
for permutare in permutations(a):
    print(permutare)

for comb in combinations(a, 2):
    print(comb)