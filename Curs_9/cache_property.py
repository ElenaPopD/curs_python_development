from functools import cached_property
import time
class Bancomat:

    @cached_property
    #@property
    def sold(self):
        print("S-a apelat metoda sold")
        time.sleep(5)
        return 10
    
b = Bancomat()
# print(b.sold())
print(b.sold) # b.sold()
print(b.sold)
print(b.sold)
