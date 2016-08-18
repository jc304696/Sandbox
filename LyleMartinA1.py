__author__ = "Lyle Martin"
""" Name:            Lyle Martin
    Date:            18/08/2016
    Program Details: The following program will be able to open a file containing a shopping list. The list will be set
                     out as so "item name, price of the item, priority number, status(r/c)". This information will be
                     stored and used throughout the program. The user will have the ability to:
                     1. View a list of what is still required
                     2. View a list that has been completed
                     3. Add new items to the list
                     4. Mark items as completed
                     Once the user has finished and chooses to exit the program will save and update the file with any
                     new items or changes to the status.
"""

import csv
from operator import itemgetter

ItemFile = open("items.csv","r")
reader = csv.reader(ItemFile)

Items = []
for line in reader:
    Items.append(line)

Items.sort(key=itemgetter(2))


print(Items)
print("{0:25s}{1:>2s}{2:>8.2f} ({3})".format(Items[0][0],'$',float(Items[0][1]),Items[0][2]))
print("{0:25s}{1:>2s}{2:>8.2f} ({3})".format(Items[1][0],'$',float(Items[1][1]),Items[1][2]))
print("{0:25s}{1:>2s}{2:>8.2f} ({3})".format(Items[2][0],'$',float(Items[2][1]),Items[2][2]))

"""ItemName = []
ItemPrice = []
ItemPriority = []
ItemStatus = []

for line in Items:
    ItemName.append(line[0])
    ItemPrice.append(float(line[1]))
    ItemPriority.append(int(line[2]))
    ItemStatus.append(line[3])

print(ItemName)
print(ItemPrice)
print(ItemPriority)
print(ItemStatus)"""

ItemFile.close()

