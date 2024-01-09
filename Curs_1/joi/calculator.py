operatie = input("Choose: + , - , * , / \n")
if operatie not in "+=*/":
    print("Wrong!")
    exit()
n1 = int(input("Numarul 1: "))
n2 = int(input("Numarul 2: "))

if operatie == "+":
    print(n1 + n2)
elif operatie == "-":
    print(n1 - n2)
elif operatie == "*":
    print(n1 * n2)
elif operatie == "/":
    print(n1 // n2)
# else:
#     print("nesuportat")