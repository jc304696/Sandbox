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

    Pseudocode

    import Functions
    function main
        call store_file_data

        display welcome message
        display number of items in file
        display menu
        get choice

        while choice is not Q
            if choice is R
                call create_list(main_list, status)
                    create a required list
                if required list empty
                    display message
                else
                    call print_list(working_list)
                        display required list and total cost

            else if choice C
                call create_list(main_list, status)
                    create a completed list
                if completed list empty
                    display message
                else
                    call print_list(working_list)
                        display completed list and total price

            else if choice A
                call add_item(main_list)

            else if choice M
                call create_list(main_list, status)
                if no items in list
                    display message
                else
                    call mark_complete(main_list, working_list)

            display menu
            get choice

        call update_file(main_list)
            saves main_list to csv file
        display farewell message

    function store_file_data()
        open file
        read each line of file
        items = []
        for each line in file
            add line to items
        sort items by priority
        close file
        return items

    function create_list(main_list, status)
        required_items = []
        for item_number from 0 to length of main_list
            if status is equal to status in main_list
                add item to required_items
        sort required_items by priority
        return required_items

    function update_file(main_list)
        open file
        write each line to file (as csv)
        close file
        display number of items

    function print_list(working_list)
        total_cost = 0
        for each item in working_list
            total_cost = total_cost + (cost of item)
            display item number, name, cost of item and priority
        display total cost

    function mark_completed(main_list, working_list)
        call print_list(working_list)
            display woking_list
        display instructions
        while True
            try
                get item_number
                if item_number greater than items in working list
                    display error message
                else if item_number less than 0
                    display error message
                else
                    break
                except type of error
                    display message
            for item in main_list
                if chosen item name is equal to item name from main_list
                    change the status to complete 'c' in main_list
            display what item has been completed
            return main_list

        function add_item(main_list)
            while True
                try
                    get name
                    if length of name less than 0
                        display error message
                    else
                        break
                except error type
                    display error message
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
                    if priority less than or equal to 0
                        display error message
                    else if priority greater than 3
                        display error message
                    else
                        break
                except error type
                    display error message
            new_list = name, price, priority and 'r'
            add new_list to main_list
            sort main list by priority
            display what was added to list

"""

import csv
from operator import itemgetter
from Functions import print_list, store_file_data, update_file, create_list, mark_complete, add_item

def main():
    item_list = store_file_data()
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
                print('No required items\n')
            else:
                mark_complete(item_list, required_list)

        print(menu)
        choice = input(">>> ").upper()

    update_file(item_list)
    print('Have a nice day :)')

def store_file_data():
    """Import file and save to a list.

    No variables to be called in. The function opens a .csv file and returns a list containing the
    content of the file.
    """
    item_file = open("items.csv", "r")
    reader = csv.reader(item_file)
    items = []
    for line in reader:
        items.append(line)
    items.sort(key=itemgetter(2))       # order the list according to priority
    item_file.close()
    return items

def create_list(main_list, status):
    """Creates a list

        Uses 2 call in variables (mainList & searchValue). mainList refers to the variable that
        contains the full list. searchValue refers to the parameter that you wish to scan through
        the mainList to save to a new list. Returns the new list as its output.
    """
    required_items = []
    for item_number in range(0, len(main_list)):
        if status == main_list[item_number][3]:
            required_items.append(main_list[item_number])
    required_items.sort(key=itemgetter(2))            # sorts list by priority
    return required_items

def update_file(main_list):
    """Overwrites file content

        Users 1 call in variable (mainList). mainList refers to the variable that contains the
        full list that you want saved to the file.
    """
    out_file = open('newitems.csv', 'w')
    writer = csv.writer(out_file, lineterminator='\n')
    writer.writerows(main_list)
    out_file.close()
    print('{} items saved to items.csv'.format(len(main_list)))

def print_list(working_list):
    """Prints a list

        Users 1 call in variable (woorkingList). workingList refers to the list that you want printed.
        The workingList needs to be set out as followed ['name','price','priority','status']
        This function is best used in conjunction with CreateList(), after a list has been created with
        the required criteria you can print it to the screen with this function.
    """
    total_cost = 0
    for Item in range(0, len(working_list)):
        total_cost += float(working_list[Item][1])
        print("{0:d}. {1:25s} ${2:>8.2f} ({3})".format(Item, working_list[Item][0], float(working_list[Item][1]),
                                                       working_list[Item][2]))
    print('Total expected price for {0} items: ${1:.2f}\n'.format(len(working_list), total_cost))

def mark_complete(main_list, working_list):
    """Changing parameter in list

        Users 2 call in variables (mainList & workingList). mainList refers to the variable that contains
        the full list. workingList refers to the variable that contains a list with certain criteria (i.e.
        this list usually equal to or smaller than the mainList)
    """
    print_list(working_list)
    print('Enter the number of an item to mark as completed')
    while True:
        try:
            item_number = int(input('>>> '))
            if item_number > (len(working_list) - 1):
                print('Invalid item number')
            elif item_number < 0:
                print('Invalid item number')
            else:
                break
        except ValueError:
            print('Invalid input; enter a number')

    for item in range(0, len(main_list)):
        if working_list[item_number] == main_list[item][0]:
            main_list[item][3] = 'c'

    print("{0} marked as completed\n".format(working_list[item_number]))
    return main_list

def add_item(main_list):
    """Adding a list to a list

        Asks the user for certain information (item name, item price & priority) and saves
        it to a list (newList). Then that list is saved to the mainList (ITEMLIST).
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

    new_item = [name, str(price), str(priority), 'r']
    main_list.append(new_item)
    main_list.sort(key=itemgetter(2))           # sorts main list by priority
    print('{}, ${:.2f} (priority {}) added to shopping list\n'.format(name, float(price), priority))
    
main()