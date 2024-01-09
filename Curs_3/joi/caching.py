# if key in cache:
#     return cache[key]
# else:
#     cache[key] = func()
#     return cache[key]
def cache(func):
    cache_dict = {}
    def inner(*args, **kwargs):
        key = args
        if key in cache_dict:
            print("HIT")
            return cache_dict[key]
        else:
            print("MISS")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
    return inner

@cache
def suma(a, b):
    import time; time.sleep(5)
    return a + b

print(suma(1,2))
print(suma(1,2))
print(suma(1,2))