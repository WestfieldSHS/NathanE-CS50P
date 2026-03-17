import csv

with open("unit12_information_technology_vocab.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Word"], "-", row["Definition"])