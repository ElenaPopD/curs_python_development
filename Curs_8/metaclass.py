class Meta(type):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.attr = 100
        obj.__slots__ = ('unu', 'doi')
        return obj

class Test(metaclass=Meta):
    pass

print(Test.attr)
test = Test()
test.unu = 1
test.trei = 3