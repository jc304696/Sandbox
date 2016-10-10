"""
    Author:           Lyle Martin
    Date:             31/08/2016
    Program Details:  The following script contains different functions to be used in other programs
    Pseudocode:

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
    new_list.sort(key=itemgetter(2))  # sorts list by priority
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
        print(
            '{0:d}. {1:25s} ${2:>8.2f} ({3})'.format(item_number, item_list[item_number][0], item_list[item_number][1],
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
    while len(item_name) == 0:
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
