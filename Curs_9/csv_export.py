import csv

prieteni = [
    {'nume': 'George', 'filme': ["Top Gun", "Wonka"]},
    {'nume': 'Ionel', 'filme': ["Top Gun", "Wonka",3,4]},
    {'nume': 'Gica', 'filme': [2,3,4,5,6]}
]

with open("export.csv", mode="w") as f:
    csv_file = csv.DictWriter(f, fieldnames=["nume", "filme"])
    csv_file.writeheader()
    csv_file.writerows(prieteni)