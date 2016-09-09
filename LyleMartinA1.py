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
        create new_list by searching for status in item_list
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
            get item_name
            while length of item_name equal to 0
                display error message
                get item_name

            while True
                try
                    get item_price
                    if item_price is less than 0
                        display error message
                    else
                        break
                except error type
                    display error message

            while True
                try
                    get item_priority
                    if item_priority is less than or equal to 0
                        display error message
                    else if item_priority is greater than 3
                        display error message
                    else
                        break
                except error type
                    display error message

            new_item = [item_name, item_price, item_priority, 'r']
            append new_item to item_list
            display contents of new_item
"""

import csv
from operator import itemgetter

def main():
    item_list = load_items('items.csv')
    menu = 'Menu:\nR - List required items\nC - List completed items\nA - Add new item\nM - Mark item as completed\nQ - Quit'

    print('Shopping List 1.0 - by Lyle Martin')
    print('{} items loaded from items.csv'.format(len(item_list)))
    print(menu)
    choice = input('>>> ').upper()

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
        choice = input('>>> ').upper()

    save_items(item_list, 'items.csv')
    print('Have a nice day :)')

def load_items(file_name):
    """Import file and save to a list.

    No variables to be called in. The function opens a .csv file and returns a list of lists containing the
    content of the file.
    :return items
    """
    item_file = open(file_name, "r")
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

        Uses 2 call in variables (item_list & status). item_list refers to the variable that
        contains all the items (completed or required). status refers to the parameter that needs to be satisfied
        before adding the item to the new_list.
        :return new_list
    """
    new_list = [item for item in item_list if item[3] == status]
    new_list.sort(key=itemgetter(2))            # sorts list by priority
    return new_list

def save_items(item_list, file_name):
    """Saves what is inside item_list to a csv file

        Calls in two parameters (item_list & file_name). item_list refers to the variable that contains the
        full list of items that you want save to the csv file. file_name is the name of the file you wish to
        save them too.
    """
    out_file = open(file_name, 'w')
    writer = csv.writer(out_file, lineterminator='\n')
    writer.writerows(item_list)
    out_file.close()
    print('{} items saved to {}'.format(len(item_list), file_name))

def print_list(item_list):
    """Prints a list

        Calls in one variable (item_list). item_list refers to the list that you want printed.
        The item_list lists' NEEDS to be set out as followed ['name','price','priority','status']
        This function is best used in conjunction with create_list(), after a list has been created with
        the required criteria.
    """
    total_cost = 0
    for item_number in range(0, len(item_list)):
        total_cost += item_list[item_number][1]
        print('{0:d}. {1:25s} ${2:>8.2f} ({3})'.format(item_number, item_list[item_number][0], item_list[item_number][1],
                                                       item_list[item_number][2]))
    print('Total expected price for {0} items: ${1:.2f}'.format(len(item_list), total_cost))

def mark_complete(item_list, required_list):
    """Changing a parameter in the list

        Calls in two variables (item_list & required_list). item_list refers to the list that contains
        the full list of items. required_list refers to the list that contains items that still need to
        be aquired
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

    print('{0} marked as completed'.format(required_list[item_number][0]))

def add_item(item_list):
    """Adding a list to a list

        Calls in one parameter (item_list). item_list is the list that contains every item no matter what its
        status is. Then asks the user for certain information (item name, item price & item priority) and adds
        it to new_item. Then new_item is added to item_list.
    """
    item_name = str(input('Item name: '))
    while len(item_name) == 0 :
        print('Input can not be blank')
        item_name = str(input('Item name: '))

    while True:
        try:
            item_price = float(input('Price: $ '))
            if item_price < 0:
                print('Price must be >= $0')
            else:
                break
        except ValueError:
            print('Invalid input; enter a valid number')

    while True:
        try:
            item_priority = int(input('Priority: '))
            if item_priority <= 0:
                print('Priority must be 1, 2 or 3')
            elif item_priority > 3:
                print('Priority must be 1, 2 or 3')
            else:
                break
        except ValueError:
            print('Invalid input; enter a valid number')

    new_item = [item_name, item_price, item_priority, 'r']
    item_list.append(new_item)
    print('{}, ${:.2f} (priority {}) added to shopping list'.format(item_name, float(item_price), item_priority))
    
main()