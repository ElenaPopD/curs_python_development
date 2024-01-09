email = "ceva@ceva.com" # aa@gmail.com a@a.ro
if "@" in email and "." in email and len(email) > 6:
    print("Valid")
else:
    print("Invalid")


email = "ceva@mailinator.com" 

conditions = []
conditions.append("@" in email)
conditions.append("." in email)
conditions.append(len(email) > 6)
conditions.append(not email.endswith("@mailinator.com"))


if all(conditions): # map(bool, conditions)
    print("Valid")
else:
    print("Invalid")

