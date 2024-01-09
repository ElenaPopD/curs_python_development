from collections import namedtuple

class Dreptunghi(object):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

dr = Dreptunghi(3,2)
print(dr.lungime)
print(dr.latime)

dr.ceva = 100
print(dr.ceva)

Dreptunghi = namedtuple('Dreptunghi', ('lungime', 'latime'))

dr = Dreptunghi(3,2)

print(dr.lungime)
print(dr.latime)

print("Acces prin index")
print(dr[0])
print(dr[1])

# dr.ceva = 100
# print(dr.ceva)

