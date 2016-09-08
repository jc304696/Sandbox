""" Name:            Lyle Martin
    Date:            18/08/2016
    Program Details: The following program will be able to open a file containing a shopping list. The list will be set
                     out as so "item name, item price, priority number, status(r/c)". This information will be
                     stored and used throughout the program. The user will have the ability to:
                     1. View a list required list
                     2. View a list completed list
                     3. Add new items to the list
                     4. Mark items as completed
                     Once the user has finished and chooses to exit the program, the list will be updated in the original
                     file.
    GitHub URL:      https://github.com/jc304696/Sandbox
    Pseudocode:

    function main()
        call store_file_data()

        display welcome message
        display number of items in file
        display menu
        get choice

        while choice is not Q
            if choice is R
                call create_list(item_list, 'r')
                if required_list is empty
                    display message
                else
                    call print_list(required_list)

            else if choice is C
                call create_list(item_list, 'c')
                if completed_list is empty
                    display message
                else
                    call print_list(required_list)

            else if choice is A
                call add_item(item_list)

            else if choice is M
                call create_list(item_list, 'r')
                if required_list is empty
                    display message
                else
                    call mark_complete(item_list, required_list)

            else
                display error message

            display menu
            get choice

        call update_file(item_list)
        display farewell message

    function load_items()
        open items.csv file for reading
        item_list = empty list

        for item in file
            change format item[1] to a float number (price)
            change format item[2] to an integer (priority)
            add item to item list

        close file
        return item_list

    function create_list(item_list, status('r' or 'c'))
        new_list = empty list

        for item_number from 0 to length of item_list
            if status is equal to status in item_list
                add item to new_list

        sort new_list by priority
        return new_list

    function save_items(item_list)
        open items.csv file as 'write'
        write each list inside of item_list to a line in items.csv
        close file
        display how many items were saved to the file

    function print_list(item_list)
        total_cost = 0

        for item_number from 0 to length of item_list
            total_cost = total_cost + item_list[item_number][1]
            display item_number, name of item, cost of item and priority

        display total cost

    function mark_completed(item_list, required_list)
        call print_list(required_list)
        while True
            try
                get item_number
                if item_number is greater than length of required_list or item_number is less than 0
                    display error message
                else
                    break
            except error type
                display error message

            for item in range from 0 to length of item_list
                if required_list[item_number][0] is equal to item_list[item][0]
                    change the status to complete ('c') in item_list

            display required_list[0] has been marked as completed

        function add_item(item_list)
            get name
            while length of name equal to 0
                display error message
                get name

            while True
                try
                    get price
                    if price is less than 0
                        display error message
                    else
                        break
                except error type
                    display error message

            while True
                try
                    get priority
                    if priority is less than or equal to 0
                        display error message
                    else if priority is greater than 3
                        display error message
                    else
                        break
                except error type
                    display error message

            new_list = [name, price, priority, 'r']
            append new list to item_list
            display contents of new_list
"""

import csv
from operator import itemgetter

def main():
    item_list = load_items()
    menu = "Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark item as completed\nQ - Quit"

    print('Shopping List 1.0 - by Lyle Martin')
    print("{} items loaded from items.csv".format(len(item_list)))
    print(menu)
    choice = input(">>> ").upper()

    while choice != 'Q':
        if choice == 'R':
            required_list = create_list(item_list, 'r')
            if len(required_list) == 0:
                print('No required items')
            else:
                print('Required items:')
                print_list(required_list)
        elif choice == 'C':
            completed_list = create_list(item_list, 'c')
            if len(completed_list) == 0:
                print('No completed items')
            else:
                print('Completed Items:')
                print_list(completed_list)
        elif choice == 'A':
            add_item(item_list)
        elif choice == 'M':
            required_list = create_list(item_list, 'r')
            if len(required_list) == 0:
                print('No required items')
            else:
                mark_complete(item_list, required_list)
        else:
            print('Invalid menu choice')
        print(menu)
        choice = input(">>> ").upper()

    save_items(item_list)
    print('Have a nice day :)')

def load_items():
    """Import file and save to a list.

    No variables to be called in. The function opens a .csv file and returns a list of lists containing the
    content of the file.
    """
    item_file = open("items.csv", "r")
    reader = csv.reader(item_file)
    items = []
    for item in reader:
        item[1] = float(item[1])
        item[2] = int(item[2])
        items.append(item)
    item_file.close()
    return items

def create_list(item_list, status):
    """Creates a list

        Uses 2 call in variables (mainList & searchValue). mainList refers to the variable that
        contains the full list. searchValue refers to the parameter that you wish to scan through
        the mainList to save to a new list. Returns the new list as its output.
    """
    new_item = []
    for item_number in range(0, len(item_list)):
        if status == item_list[item_number][3]:
            new_item.append(item_list[item_number])
    new_item.sort(key=itemgetter(2))            # sorts list by priority
    return new_item

def save_items(item_list):
    """Overwrites file content

        Users 1 call in variable (mainList). mainList refers to the variable that contains the
        full list that you want saved to the file.
    """
    out_file = open('items.csv', 'w')
    writer = csv.writer(out_file, lineterminator='\n')
    writer.writerows(item_list)
    out_file.close()
    print('{} items saved to items.csv'.format(len(item_list)))

def print_list(item_list):
    """Prints a list

        Users 1 call in variable (woorkingList). workingList refers to the list that you want printed.
        The workingList needs to be set out as followed ['name','price','priority','status']
        This function is best used in conjunction with CreateList(), after a list has been created with
        the required criteria you can print it to the screen with this function.
    """
    total_cost = 0
    for item_number in range(0, len(item_list)):
        total_cost += item_list[item_number][1]
        print("{0:d}. {1:25s} ${2:>8.2f} ({3})".format(item_number, item_list[item_number][0], item_list[item_number][1],
                                                       item_list[item_number][2]))
    print('Total expected price for {0} items: ${1:.2f}'.format(len(item_list), total_cost))

def mark_complete(item_list, required_list):
    """Changing parameter in list

        Users 2 call in variables (mainList & workingList). mainList refers to the variable that contains
        the full list. workingList refers to the variable that contains a list with certain criteria (i.e.
        this list usually equal to or smaller than the mainList)
    """
    print_list(required_list)
    print('Enter the number of an item to mark as completed')
    while True:
        try:
            item_number = int(input('>>> '))
            if item_number > (len(required_list) - 1) or item_number < 0:
                print('Invalid item number')
            else:
                break
        except ValueError:
            print('Invalid input; enter a number')

    for item in range(0, len(item_list)):
        if required_list[item_number][0] == item_list[item][0]:
            item_list[item][3] = 'c'

    print("{0} marked as completed".format(required_list[item_number][0]))

def add_item(item_list):
    """Adding a list to a list

        Asks the user for certain information (item name, item price & priority) and saves
        it to a list (newList). Then that list is saved to the mainList (ITEMLIST).
    """
    name = str(input('Item name: '))
    while len(name) == 0 :
        print('Input can not be blank')
        name = str(input('Item name: '))

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

    new_item = [name, price, priority, 'r']
    item_list.append(new_item)
    print('{}, ${:.2f} (priority {}) added to shopping list'.format(name, float(price), priority))
    
main()