__author__ = 'Lyle Martin'


class Item:
    def __init__(self, name, cost, priority, status):
        self.name = name
        self.cost = float(cost)
        self.priority = int(priority)
        self.status = status

    def __str__(self):
        return "{}, ${:.2f}, priority {} (completed)".format(self.name, self.cost, self.priority)

    def mark_complete(self, name):
            if self.name == name:
                self.status = 'c'
