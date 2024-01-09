f = open("fisier.txt", mode="r")
continut = f.read()
#f.write("Ceva")
print(continut)
f.close()

f2 = open("fisier2.txt", mode="w")
continut += "\nSi portocale"
f2.write(continut)
f2.close()