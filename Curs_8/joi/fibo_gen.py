def fib(n):
    a = 0
    b = 1
    count = 0 
    while count < n:
        yield a
        a, b = b, a + b
        count +=1

fibo = fib(10)
# print(next(fibo))
# print(next(fibo))
# print(next(fibo))
# print(next(fibo))
# print(next(fibo))
# print(next(fibo))
for nr in fib(100000):
    pass

print("Dupa for")
print(nr)