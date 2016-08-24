import csv
from operator import itemgetter


def StoreFileData():
    """Import file and save to a list.

    No variables to be called in. The function opens a .csv file and returns a list containing the
    content of the file.
    """
    ItemFile = open("items.csv", "r")   # opens file
    reader = csv.reader(ItemFile)       # saves contents of file
    Items = []                          # creates a open list
    for line in reader:                 # cycles through each line of the stored values in reader
        Items.append(line)              # adds to list
    Items.sort(key=itemgetter(2))       # order the list according to priority
    ItemFile.close()                    # closes the file
    return Items

def CreateList(mainList, searchValue):
    """Creates a list

        Uses 2 call in variables (mainList & searchValue). mainList refers to the variable that
        contains the full list. searchValue refers to the parameter that you wish to scan through
        the mainList to save to a new list. Returns the new list as its output.
    """
    reqItems = []                               # creates an open list
    for line in range(0, len(mainList)):        # repeats process until every line in the mainList have been searched
        if searchValue == mainList[line][3]:    # check if searchValue is contained in the line
            reqItems.append(mainList[line])     # saves line to reqItem list
    reqItems.sort(key=itemgetter(2))            # sorts list by priority
    return reqItems

def UpdateFile(mainList):
    """Overwrites file content

        Users 1 call in variable (mainList). mainList refers to the variable that contains the
        full list that you want saved to the file.
    """
    outFile = open('newitems.csv', 'w')                 # open files and says I want to write to it
    writer = csv.writer(outFile, lineterminator='\n')   # stores writer to outFile and end each line with an enter
    writer.writerows(mainList)                          # tells writer where to get its information from
    outFile.close()                                     # closes the outFile
    print('{} items saved to items.csv'.format(len(mainList)))  # prints how many lines of information was saved

def PrintList(workingList):
    """Prints a list

        Users 1 call in variable (woorkingList). workingList refers to the list that you want printed.
        The workingList needs to be set out as followed ['name','price','priority','status']
        This function is best used in conjunction with CreateList(), after a list has been created with
        the required criteria you can print it to the screen with this function.
    """
    TotalCost = 0                                   # creates variable
    for Item in range(0, len(workingList)):         # repeats process until every list value has been printed
        TotalCost += float(workingList[Item][1])    # adds 'price' parameter to variable
        print("{0:d}. {1:25s} ${2:>8.2f} ({3})".format(Item, workingList[Item][0], float(workingList[Item][1]),
                                                       workingList[Item][2]))   # prints list information in a perticular format

    print('Total expected price for {0} items: ${1:.2f}\n'.format(len(workingList), TotalCost)) # prints total price of all items

def MarkComplete(mainList, workingList):
    """Changing parameter in list

        Users 2 call in variables (mainList & workingList). mainList refers to the variable that contains
        the full list. workingList refers to the variable that contains a list with certain criteria (i.e.
        this list usually equal to or smaller than the mainList)
    """
    PrintList(workingList)                                      # user the PrintList() function to print the workingList
    print('Enter the number of an item to mark as completed')   # prints instructions

    while True:                                                 # creates an infinite loop
        try:                                                    # does no matter what
            ItemNumber = int(input('>>> '))                     # gets user input
            if ItemNumber > (len(workingList) - 1):             # checks the input against certain criteria
                print('Invalid item number')
            elif ItemNumber < 0:                                # checks the input against certain criteria
                print('Invalid item number')
            else:                                               # if the earlier checks where False then does the following
                break                                           # breaks out of the infinite loop
        except ValueError:                                      # catches error response
            print('Invalid input; enter a number')


    item = workingList[ItemNumber]

    for line in range(0, len(mainList)):
        if item[0] == mainList[line][0]:
            mainList[line][3] = 'c'

    print("{0} marked as completed\n".format(item[0]))  # tells user what was changed
    return mainList
