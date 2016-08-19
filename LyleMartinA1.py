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

def PrintRawFileData():
    InFile = open("items.csv","r")
    print(InFile.read())
    InFile.close()
PrintRawFileData()

def main():
    StoreFileData()
    print('Shopping List 1.0 - by Lyle Martin')
    print("{} items loaded from items.csv".format(NumberOfItems))

    menu = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark item as completed\nQ - Quit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == "R":
            CheckStatus(Items,NumberOfItems)
            if required == 0:
                print('No required items\n')
            else:
                print('Required items: ')
                PrintRequiredList(Items,NumberOfItems)
            print(menu)
            choice = input('>>> ').upper()

        elif choice == "C":
            CheckStatus(Items,NumberOfItems)
            if completed == 0:
                print('No completed items')
            else:
                print('Completed items: ')
                PrintCompletedList(Items, NumberOfItems)
            print(menu)
            choice = input('>>> ').upper()

        elif choice == "A":
            AddItem()
            print(menu)
            choice = input('>>> ').upper()

        elif choice == "M":
            MarkComplete(Items)
            print(menu)
            choice = input('>>> ').upper()

        else:
            print("Invalid menu choice\n")
            print(menu)
            choice = input('>>> ').upper()
    UpdateFile(Items,NumberOfItems)
    print('Have a nice day :)')

def StoreFileData():
    global Items, NumberOfItems
    ItemFile = open("items.csv", "r")
    reader = csv.reader(ItemFile)
    Items = []
    for line in reader:
        Items.append(line)
    Items.sort(key=itemgetter(2))
    NumberOfItems = len(Items)
    ItemFile.close()
    return Items, NumberOfItems

def PrintRequiredList(Items, NumberOfItems):
    ItemNumber = 0
    TotalCost = 0
    NumberOfPrints = 0
    while ItemNumber < NumberOfItems:
        if Items[ItemNumber][3] == "r":
            TotalCost += float(Items[ItemNumber][1])
            print("{0:d}. {1:25s} ${2:>8.2f} ({3})".format(ItemNumber, Items[ItemNumber][0], float(Items[ItemNumber][1]),
                                                       Items[ItemNumber][2]))
            NumberOfPrints += 1
        ItemNumber += 1

    print('Total expected price for {0} items: ${1:.2f}\n'.format(NumberOfPrints,TotalCost))

def MarkComplete(Items):
    PrintRequiredList(Items,NumberOfItems)
    print('Enter the number of an item to mark as completed')
    ItemNumber = int(input('>>> '))
    if ItemNumber > NumberOfItems:
        print('Invalid number. Enter a number from the list')
        ItemNumber = int(input('>>> '))
    Items[ItemNumber][3] = "c"
    print("{0} marked as completed\n".format(Items[ItemNumber][0]))

def PrintCompletedList(Items, NumberOfItems):
    ItemNumber = 0
    TotalCost = 0
    NumberOfPrints = 0
    while ItemNumber < NumberOfItems:
        if Items[ItemNumber][3] == "c":
            TotalCost += float(Items[ItemNumber][1])
            print("{0:d}. {1:25s} ${2:>8.2f} ({3})".format(ItemNumber, Items[ItemNumber][0], float(Items[ItemNumber][1]),
                                                       Items[ItemNumber][2]))
            NumberOfPrints += 1
        ItemNumber += 1

    print('Total expected price for {0} items: ${1:.2f}\n'.format(NumberOfPrints, TotalCost))

def CheckStatus(Items,NumberOfItems):
    global completed, required
    completed = 0
    required = 0
    ItemNumber = 0
    while ItemNumber < NumberOfItems:
        if Items[ItemNumber][3] == "c":
            completed += 1
        elif Items[ItemNumber][3] == "r":
            required += 1
        ItemNumber += 1
    return completed, required

def AddItem():
    global Items, NumberOfItems
    name = str(input('Item name: '))
    price = str(input('Price: $ '))
    priority = str(input('Priority: '))
    NewItem = [name,price,priority,'r']
    Items.append(NewItem)
    Items.sort(key=itemgetter(2))
    NumberOfItems = len(Items)
    print('\n')
    return Items, NumberOfItems

def UpdateFile(Items,NumberOfItems):

    OutFile = open('newitems.csv','w')
    writer = csv.writer(OutFile,lineterminator='\n')
    writer.writerows(Items)
    OutFile.close()
    print('{} items saved to items.csv'.format(NumberOfItems))

main()