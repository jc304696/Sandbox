__author__ = 'Lyle Martin'

from Assignment2.item import Item
from operator import attrgetter


class ItemList:
    def __init__(self):
        self.items = []

    def add_items_from_a_list(self, item_list):
        for item in item_list:
            new_item = Item(*item)
            self.items.append(new_item)
        self.sort()

    def get_items_as_a_list(self):
        item_list = []
        for item in self.items:
            new_list = [item.name, item.cost, item.priority, item.status]
            item_list.append(new_list)
        return item_list

    def add_item(self, new_item_criteria):
        self.items.append(Item(*new_item_criteria))
        self.sort()

    def get_total_cost(self):
        total_cost = sum(item.cost for item in self.items if item.status == 'r')
        return total_cost

    def sort(self):
        self.items.sort(key=attrgetter('priority'))

