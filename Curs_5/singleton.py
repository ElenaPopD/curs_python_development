class Singleton(object):
    _instance = None

    def __new__(self, *args, **kwargs):
        if self._instance is None:
            print("Creating new connection")
            self._instance = super().__new__(self, *args, **kwargs)
        else:
            print("Already have a connection")
        return self._instance


class DatabaseConnection(Singleton):
    pass

a = DatabaseConnection()
b = DatabaseConnection()
c = DatabaseConnection()

print(a is b)
print(a is c)
print(a is b is c)
print(a)
