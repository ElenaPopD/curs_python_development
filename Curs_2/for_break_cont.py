for litera in "Ana are mere":
    #continue
    if litera.lower() == "a":
        continue
    print(litera)

for litera in "Ana are mere":
    if litera == "m":
        break
    print(litera)

# Stop at second e
number_of_e = 0

for litera in "Ana are mere":
    if litera == "e":
        number_of_e += 1
        if number_of_e == 2:
            break
    print(litera)
print("Am terminat")