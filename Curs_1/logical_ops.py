print(1 < 2 and 2 < 3 )
print(1 < 2 and 2 > 3 )
print(1 < 2 and 2 < 3 and 3 < 5)
print(1 > 2 and 2 < 3 and 3 < 5)
# AND
# True and True > True
# True and False > False
# False and True > False
# False and False > False

print(1 > 2 or 1 < 3)
# OR
# True or True > True
# True or False > True
# False or True > True
# False or False > False

print(not 1 < 2)
# not True > False
# not False > True

print(1 < 2 and 2 < 3)
print(not (1 < 2 and 2 < 3))