__author__ = 'Lyle Martin'

from Assignment2.item import Item
from operator import attrgetter


class ItemList:
    def __init__(self):
        """
        Constructs the ItemList class

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
        :return: item_list
        """
        item_list = []
        for item in self.items:
            new_list = [item.name, item.price, item.priority, item.status]
            item_list.append(new_list)
        return item_list

    def add_item(self, new_item_criteria):
        """
        Adds new item object to list

        Takes in a list of criteria and converts it to an object and add it to a list
        :param new_item_criteria: a list containing the items name, price, priority and status
        :return: None
        """
        self.items.append(Item(*new_item_criteria))
        self.sort()

    def get_total_price(self):
        """
        Calculates total price of required list

        :return: total_price
        """
        total_price = sum(item.price for item in self.items if item.status == 'r')
        return total_price

    def sort(self):
        """
        Sorts the objects list by priority

        :return: None
        """
        self.items.sort(key=attrgetter('priority'))

    def get_item_by_name(self, name):
        """
        Gets an item from the object list

        Searches through the object list until the items name matches with the name passed in
        :param name: items name (search criteria)
        :return: item
        """
        for item in self.items:
            if item.name == name:
                return item



