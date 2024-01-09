a = [1,2,3]
try:
    a[100]
except IndexError as e:
    print("IndexError", type(e), id(e), e)
except LookupError as e:
    print("Lookup", type(e), id(e), e)
except Exception as e:
    print("Exception", type(e), id(e), e)
