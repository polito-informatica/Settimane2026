import csv

with open('film.csv', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip().split(','))


print("differenza")

with open('film.csv', encoding='utf-8') as f:
    f.readline()
    reader = csv.reader(f)
    for row in reader:
        print(row)