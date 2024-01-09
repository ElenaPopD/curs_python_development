#
# fib(n) = fib(n-1) + fib(n-2) if n > 1 else n
# fib(0) = 0 
# fib(1) = 1
# fib(2) = fib(1) + fib(0) = 0 + 1 = 1
# fib(3) = fib(2) + fib(1) = 1 + 1 = 2
from functools import cache

@cache
def fib(n):
    if n in (0,1):
        return n
    return fib(n-1) + fib(n-2)
    #return fib(n-1) + fib(n-2) if n > 1 else n

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(503))

# f(100) -> f(99) -> f(98) 
#                 -> f(97)
#        -> f(98) -> f(97)
#                 -> f(96)