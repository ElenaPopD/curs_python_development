from my_range import my_range
from gen_range import gen_range
print("Range")
for element in range(10):
    print(element)

print("Iterator")
for element in my_range(10):
    print(element)

print("Generator")
for element in gen_range(10):
    print(element)