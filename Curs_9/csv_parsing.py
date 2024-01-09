with open("studenti.csv") as file:
    next(file) # skip header line
    for row in file:
        if int(row.split(",")[-1]) > 8:
            print(row)