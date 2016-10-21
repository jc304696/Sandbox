"""Name:        Lyle Martin
   Date:        20/10/2016
   Description: Item class is used to create an object with certain variables that are passed in at the init stage. It
                also overrides the str method so that the object will be printed in a particular format and has an added
                method to change the status of the item to complete ('c').
   URL:         https://github.com/jc304696/Sandbox.git
"""

__author__ = 'Lyle Martin'


class Item:
    """
    Creates an object to hold an items criteria
    """
    COMPLETED = 'c'
    REQUIRED = 'r'

    def __init__(self, name, price, priority, status):
        """
        Constructs the Item class

        Creates an object with particular values that are passed into the class
        :param name: name of the item (string)
        :param price: cost of the item (float number)
        :param priority: priority of the item (1, 2 or 3)
        :param status: status of the item (required or completed)
        """
        self.name = name
        self.price = float(price)
        self.priority = int(priority)
        self.status = status

    def __str__(self):
        """
        Overrides the string format

        This method will change the format of the object so that it is printed in a particular form
        :return: new string format
        """
        return "{}, ${:.2f}, priority {} (completed)".format(self.name, self.price, self.priority)

    def mark_complete(self):
        """
        Changes the items status to complete

        :return: None
        """
        self.status = Item.COMPLETED
