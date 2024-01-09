class A:
    def __init__(self, numar):
        self.numar = numar

    @property
    def chirie(self):
        return self.numar * 5
    
a = A(10)
print(a.chirie)
print(a.numar)