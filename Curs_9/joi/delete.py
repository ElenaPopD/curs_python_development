import os

filename = 'steam.txt'

with open(filename, 'w') as f:
    f.write(str("Ceva"))

f = open(filename, 'w')
f.write(str("Ceva"))
f.close()

os.remove(filename)
