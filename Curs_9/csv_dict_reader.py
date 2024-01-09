from csv import DictReader

with open("studenti.csv") as file:
    csv_file = DictReader(file)
    for row in csv_file:
        if float(row["nota"]) > 8:
            print(row)