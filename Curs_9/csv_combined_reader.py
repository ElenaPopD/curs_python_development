fieldnames = ["nume", "prenume", "nota"]


import csv
with open("studenti.csv") as file:
    next(file) # consume the first line
    csv_file = csv.reader(file)
    for row in csv_file:
       if float(row[-1]) > 8:
           print(row)