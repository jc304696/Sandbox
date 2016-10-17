__author__ = 'Lyle Martin'


class Item:
    def __init__(self, name, price, priority, status):
        """
        Constructs the Item class

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
        Overides how to print the string

        :return: new string format
        """
        return "{}, ${:.2f}, priority {} (completed)".format(self.name, self.price, self.priority)

    def mark_complete(self):
        """
        Changes the items status to complete

        :return: None
        """
        self.status = 'c'
