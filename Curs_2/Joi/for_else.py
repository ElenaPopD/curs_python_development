a = [1,2,3]
x = 3
# Var 1
if x in a:
    print("Este")
else:
    print("nu l-am gasit")

# Var 2
for element in a:
    if element == x:
        print("L-am gasit")
        break
else:
    print("Nu l-am gasit")

# Var 3
gasit = False
for element in a:
    if element == x:
        print("L-am gasit")
        gasit = True

if gasit is False:
    print("Nu l-am gasit")
