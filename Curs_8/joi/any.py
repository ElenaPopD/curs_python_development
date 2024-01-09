print(any((False, False, False)))

print(any((False, False, True, False)))  # False or Flase or True or False

print(any((True, True, True))) # True or True or True

print("Evaluare")
a = 8
print(any((
    a < 5,
    a % 2 == 0,  
)))