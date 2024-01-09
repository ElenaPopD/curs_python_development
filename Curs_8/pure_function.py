class A:
    ceva = 10

def impure_function(a: A) -> A:
    a.ceva = 100
    return A


a = A()

print(a.ceva)

b = impure_function(a)
print(a.ceva)
