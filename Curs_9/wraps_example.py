from functools import wraps

def decorator(func):
    @wraps(func) # good practice sa adaugam la fiecare decorator definit de noi
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner
 
@decorator
def sum(a, b):
    raise Exception("ceva")
    return a + b

print(sum(3,5))
print(sum.__name__)