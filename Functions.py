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

def CreateList(mainList, searchValue):
    """Print a required list on the screen

    """
    inFile = open("items.csv", "r")
    reader = csv.reader(inFile)
    reqItems = []
    for line in range(0, len(mainList)):
        if searchValue == mainList[line][3]:
            reqItems.append(mainList[line])
    reqItems.sort(key=itemgetter(2))
    inFile.close()
    return reqItems

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
    """
    :param workingList:
    :return:
    """

    OutFile = open('newitems.csv', 'w')
    writer = csv.writer(OutFile, lineterminator='\n')
    writer.writerows(workingList)
    OutFile.close()
    print('{} items saved to items.csv'.format(len(workingList)))

def PrintList(workingList):
    """Prints a list

    """
    TotalCost = 0
    for Item in range(0, len(workingList)):
        TotalCost += float(workingList[Item][1])
        print("{0:d}. {1:25s} ${2:>8.2f} ({3})".format(Item, workingList[Item][0], float(workingList[Item][1]),
                                                       workingList[Item][2]))

    print('Total expected price for {0} items: ${1:.2f}\n'.format(len(workingList), TotalCost))

def MarkComplete(mainList, workingList):
    """Changing parameter in list

    """
    PrintList(workingList)
    print('Enter the number of an item to mark as completed')

    while True:
        try:
            ItemNumber = int(input('>>> '))
            if ItemNumber > len(workingList):
                print('Invalid item number')
            elif ItemNumber < 0:
                print('Invalid item number')
            else:
                break
        except ValueError:
            print('Invalid input; enter a number')

    mainList[ItemNumber][3] = "c"
    print("{0} marked as completed\n".format(mainList[ItemNumber][0]))
    return mainList