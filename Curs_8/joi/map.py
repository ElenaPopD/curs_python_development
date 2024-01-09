a = range(20)
# b = map(print, a)
# print(type(b))

# for x in b:
#     print(x)

def print_and_return(value):
    print(value)
    return value

for numar in map(print_and_return, range(20)):
    print(f"Am primit {numar}")


for numar in (print_and_return(x) for x in range(20)):
    print(f"Am primit {numar}")