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
from Functions import PrintMenu, PrintList
from Functions import StoreFileData, UpdateFile
from Functions import CreateList, MarkComplete

InFile = open("items.csv", "r")
print(InFile.read())
InFile.close()
ITEMLIST = StoreFileData()

def main():

    print('Shopping List 1.0 - by Lyle Martin')
    print("{} items loaded from items.csv".format(len(ITEMLIST)))

    options = {'R' : caseR, 'C' : caseC, 'A' : AddItem, 'M' : caseM}
    choice = PrintMenu()

    while choice != 'Q':

        try: options[choice]()
        except KeyError:
            print("Invalid menu choice\n")

        choice = PrintMenu()

    UpdateFile(ITEMLIST)
    print('Have a nice day :)')

def caseR():
    reqList = CreateList(ITEMLIST, 'r')
    if len(reqList) == 0:
        print('No required items')
    else:
        PrintList(reqList)

def caseC():
    comList = CreateList(ITEMLIST, 'c')
    if len(comList) == 0:
        print('No completed items')
    else:
        PrintList(comList)

def AddItem():
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
    ITEMLIST.append(NewItem)
    ITEMLIST.sort(key=itemgetter(2))
    print('{}, ${:.2f} (priority {}) added to shopping list\n'.format(name, float(price), priority))

def caseM():
    reqList = CreateList(ITEMLIST, 'r')
    if len(reqList) == 0:
        print('No required items\n')
    else:
        MarkComplete(ITEMLIST, reqList)

main()