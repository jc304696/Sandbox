import csv

in_file = open("items.csv","r")
reader = csv.reader(in_file)
items = []
for item in reader:
    item[1] = float(item[1])
    item[2] = int(item[2])
    print(item)
    items.append(item)
in_file.close()
print(items)


