import csv
from operator import itemgetter

def StoreFileData():
    """Import file and save to a list.

    No variables need to be called in. The function will return 1 variable (a list containing the
    content of the file).
    """
    ItemFile = open("items.csv", "r")
    reader = csv.reader(ItemFile)
    Items = []
    for line in reader:
        Items.append(line)
    Items.sort(key=itemgetter(2))
    ItemFile.close()
    return Items

def CreateList(searchValue):
    """Print a required list on the screen

    """
    inFile = open("items.csv", "r")
    reader = csv.reader(inFile)
    reqItems = []
    for line in reader:
        if searchValue in line:
            reqItems.append(line)
    reqItems.sort(key=itemgetter(2))
    inFile.close()
    return reqItems

    """     print("{0:d}. {1:25s} ${2:>8.2f} ({3})".format(reader[0],reader[1],reader[2]))
    ItemNumber = 0
    TotalCost = 0
    NumberOfPrints = 0
    while ItemNumber < len(list):
        if list[ItemNumber][3] == "r":
            TotalCost += float(list[ItemNumber][1])
            print(
                "{0:d}. {1:25s} ${2:>8.2f} ({3})".format(ItemNumber, list[ItemNumber][0], float(list[ItemNumber][1]),
                                                         list[ItemNumber][2]))
            NumberOfPrints += 1
        ItemNumber += 1

    print('Total expected price for {0} items: ${1:.2f}\n'.format(NumberOfPrints, TotalCost))"""

def AddItem(workingList):
    """Adding a list to a list

    """

    while True:
        try:
            name = str(input('Item name: '))
            if len(name) == 0:
                print('Input can not be blank')
            else:
                break
        except Exception:
            print('Invalid input try again')

    while True:
        try:
            price = float(input('Price: $ '))
            if price < 0:
                print('Price must be >= $0')
            else:
                break
        except ValueError:
            print('Invalid input; enter a valid number')

    while True:
        try:
            priority = int(input('Priority: '))
            if priority <= 0:
                print('Priority must be 1, 2 or 3')
            elif priority > 3:
                print('Priority must be 1, 2 or 3')
            else:
                break
        except ValueError:
            print('Invalid input; enter a valid number')

    NewItem = [name, str(price), str(priority), 'r']
    workingList.append(NewItem)
    workingList.sort(key=itemgetter(2))
    print('{}, ${:.2f} (priority {}) added to shopping list\n'.format(name, float(price), priority))
    return workingList

def UpdateFile(workingList):
    OutFile = open('newitems.csv', 'w')
    writer = csv.writer(OutFile, lineterminator='\n')
    writer.writerows(workingList)
    OutFile.close()
    print('{} items saved to items.csv'.format(len(workingList)))
