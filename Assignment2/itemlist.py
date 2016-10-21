"""Name:        Lyle Martin
   Date:        20/10/2016
   Description: ItemList class creates different methods to sort through the item list. The class contains methods to:
                - change a list of list into a list of objects
                - change a list of objects to a list of lists and returns the new list
                - add an item (object) to a object list
                - calculates and returns the total price of required items
                - sort a list of objects by priority
                - find and return an item (object) with a particular name
                
   URL:         https://github.com/jc304696/Sandbox.git
"""

from Assignment2.item import Item
from operator import attrgetter

__author__ = 'Lyle Martin'


class ItemList:
    """
    Creates different methods to use on item lists
    """

    def __init__(self):
        """
        Constructs the ItemList class

        Creates an empty list. The list will be used to hold the objects created by other methods
        :return None
        """
        self.items = []

    def add_items_from_a_list(self, item_list):
        """
        Adds an object to a list

        Converts a list to an object and adds it to a list
        :param item_list: A list of lists containing items (name, price, priority and status)
        :return: None
        """
        for item in item_list:
            new_item = Item(*item)
            self.items.append(new_item)
        self.sort()

    def get_items_as_a_list(self):
        """
        Adds a list to a list

        Converts an object to a list and adds it to a list
        :return: item_list: A list of lists
        """
        item_list = []
        for item in self.items:
            new_list = [item.name, item.price, item.priority, item.status]
            item_list.append(new_list)
        return item_list

    def add_item(self, new_item_criteria):
        """
        Adds a new object to a list

        Takes in a list of criteria (name, price, priority & status) and converts it to an object. Once the list has
        been converted into an object the object is appended to the list created in the init method.
        :param new_item_criteria: a list containing the items name, price, priority and status
        :return: None
        """
        self.items.append(Item(*new_item_criteria))
        self.sort()

    def get_total_price(self):
        """
        Calculates total price of required list

        If the status of an item is set to required ('r') this method will add its price to calculate the total of all
        the required items.
        :return: total_price
        """
        return sum(item.price for item in self.items if item.status == 'r')

    def sort(self):
        """
        Sorts the objects list by priority

        :return: None
        """
        self.items.sort(key=attrgetter('priority'))

    def get_item_by_name(self, name):
        """
        Gets an item from the object list

        Searches through the object list until the items name matches the name passed into the method.
        :param name: items name (search criteria)
        :return: item
        """
        for item in self.items:
            if item.name == name:
                return item
