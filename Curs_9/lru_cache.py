from functools import lru_cache

@lru_cache(maxsize=3)
def sum(a,b):
    return a + b

def sum_and_report(a,b):
    print(sum(a, b))
    print(sum.cache_info())
# print(sum(1,2))
# print(sum.cache_info())

# print(sum(1,2))
# print(sum.cache_info())

sum_and_report(1,2)
sum_and_report(1,2)
sum_and_report(1,2)
sum_and_report(2,3)
sum_and_report(3,4)
sum_and_report(3,4)

sum_and_report(5,5) # eject 1, 2
sum_and_report(5,5)

sum_and_report(3,4)

#sum_and_report(1,2)
sum_and_report(2,3)



