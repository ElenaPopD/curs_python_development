def generic_func(*args, **kwargs):
    print("*args = ", args)
    print("**kwargs =", kwargs)

generic_func(1,2,3)
generic_func(1,2, ceva=0)
generic_func(1,2, ceva=0, altceva=None)
