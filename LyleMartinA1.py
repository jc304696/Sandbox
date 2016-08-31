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
        open file
        display raw data from file
        close file
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

"""

from Functions import print_list, store_file_data, update_file, create_list, mark_complete, add_item

def main():
    in_file = open("items.csv", "r")
    print(in_file.read())
    in_file.close()
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

main()