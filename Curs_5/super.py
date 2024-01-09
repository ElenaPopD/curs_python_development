class A:

    def ceva(self):
        print("Sunt in A")

class B(A):

    def ceva(self):
        super().ceva()
        print("Sunt in B")

b = B()

b.ceva()