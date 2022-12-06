from asyncore import write
import csv
from dataclasses import field
from email import header

dataset1 = []
dataset2 = []

with open("bright_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset1.append(i)
with open("dwarf_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset2.append(i)
#print(dataset1)
#print(dataset2)

header1 = dataset1[0]
data1 = dataset1[1:]
header2 = dataset2[0]
data2 = dataset2[1:]
header3 = header1 + header2
print(header3)

data = []
for i, row in enumerate(data1):
    data.append(data1 + data2)
with open("merged.csv", "w") as g:
    csv_writer = csv.writer(g)
    csv_writer.writerow(header3)
    csv_writer.writerows(data)
with open("merged.csv", "r") as g1,  open("merged2.csv", "w") as w2:
    csv_reader = csv.reader(g1)
    csv_writer = csv.writer(w2)
    for i in csv_reader(g1):
        if any(field.strip()):
            csv_writer.writerow(i)
