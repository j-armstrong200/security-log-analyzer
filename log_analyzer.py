import csv

findings = []

with open("security_logs.csv", newline="") as file:
    reader = csv.DictReader(file)