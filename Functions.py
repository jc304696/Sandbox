import csv
from operator import itemgetter

def store_file_data():
    """Import file and save to a list.

    No variables to be called in. The function opens a .csv file and returns a list containing the
    content of the file.
    """
    item_file = open("items.csv", "r")   # opens file
    reader = csv.reader(item_file)       # saves contents of file
    items = []                          # creates a open list
    for line in reader:                 # cycles through each line of the stored values in reader
        items.append(line)              # adds to list
    items.sort(key=itemgetter(2))       # order the list according to priority
    item_file.close()                    # closes the file
    return items

def create_list(main_list, search_value):
    """Creates a list

        Uses 2 call in variables (mainList & searchValue). mainList refers to the variable that
        contains the full list. searchValue refers to the parameter that you wish to scan through
        the mainList to save to a new list. Returns the new list as its output.
    """
    req_items = []                               # creates an open list
    for line in range(0, len(main_list)):        # repeats process until every line in the mainList have been searched
        if search_value == main_list[line][3]:    # check if searchValue is contained in the line
            req_items.append(main_list[line])     # saves line to reqItem list
    req_items.sort(key=itemgetter(2))            # sorts list by priority
    return req_items

def update_file(main_list):
    """Overwrites file content

        Users 1 call in variable (mainList). mainList refers to the variable that contains the
        full list that you want saved to the file.
    """
    out_file = open('newitems.csv', 'w')                 # open files and says I want to write to it
    writer = csv.writer(out_file, lineterminator='\n')   # stores writer to outFile and end each line with an enter
    writer.writerows(main_list)                          # tells writer where to get its information from
    out_file.close()                                     # closes the outFile
    print('{} items saved to items.csv'.format(len(main_list)))  # prints how many lines of information was saved

def print_list(working_list):
    """Prints a list

        Users 1 call in variable (woorkingList). workingList refers to the list that you want printed.
        The workingList needs to be set out as followed ['name','price','priority','status']
        This function is best used in conjunction with CreateList(), after a list has been created with
        the required criteria you can print it to the screen with this function.
    """
    TotalCost = 0                                   # creates variable
    for Item in range(0, len(working_list)):         # repeats process until every list value has been printed
        TotalCost += float(working_list[Item][1])    # adds 'price' parameter to variable
        print("{0:d}. {1:25s} ${2:>8.2f} ({3})".format(Item, working_list[Item][0], float(working_list[Item][1]),
                                                       working_list[Item][2]))   # prints list information in a perticular format
    print('Total expected price for {0} items: ${1:.2f}\n'.format(len(working_list), TotalCost)) # prints total price of all items

def mark_complete(main_list, working_list):
    """Changing parameter in list

        Users 2 call in variables (mainList & workingList). mainList refers to the variable that contains
        the full list. workingList refers to the variable that contains a list with certain criteria (i.e.
        this list usually equal to or smaller than the mainList)
    """
    print_list(working_list)                                      # user the PrintList() function to print the workingList
    print('Enter the number of an item to mark as completed')   # prints instructions
    while True:                                             # creates an infinite loop
        try:                                                # does no matter what
            item_number = int(input('>>> '))                 # gets user input
            if item_number > (len(working_list) - 1):         # checks the input against certain criteria
                print('Invalid item number')
            elif item_number < 0:                            # checks the input against certain criteria
                print('Invalid item number')
            else:                                           # if the earlier checks return False then does the following
                break                                       # breaks out of the infinite loop
        except ValueError:                                  # catches error response
            print('Invalid input; enter a number')

    item = working_list[item_number]                          # stores the value from the list to a new variable
    for line in range(0, len(main_list)):
        if item[0] == main_list[line][0]:                    # checks if the value in item matches any value in mainList
            main_list[line][3] = 'c'                         # changes a value in mainList

    print("{0} marked as completed\n".format(item[0]))      # tells user what was changed
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
    main_list.sort(key=itemgetter(2))
    print('{}, ${:.2f} (priority {}) added to shopping list\n'.format(name, float(price), priority))