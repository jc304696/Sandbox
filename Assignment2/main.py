__author__ = 'Lyle Martin'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from Assignment1.Functions import load_items, save_items
from Assignment2.itemlist import ItemList, Item

class ShoppingListApp(App):
    heading = StringProperty()
    display = StringProperty()

    def __init__(self, **kwargs):
        """
        Construst main App
        """
        super(ShoppingListApp, self).__init__(**kwargs)
        item_list = load_items('items.csv')
        self.items = ItemList()
        self.items.add_items_from_a_list(item_list)

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = 'Shopping List App'
        self.root = Builder.load_file('Assignment2_layout.kv')
        self.required_button()
        return self.root

    def create_item_buttons(self, status):
        """
        Creates Buttons for the items in the shopping list and adds them to the GUI. When status is equal to required
        then the buttons will be coloured red, green or blue depending on the priority (1, 2 or 3) and display the items
        name. When status is equal to completed the buttons will be grey and display the items name.
        :param status: The criteria on how to construct button
        :return: None
        """
        if status == 'r':
            for item in self.items.items:
                if item.status == status:
                    if item.priority == 1:
                        temp_button = Button(text=item.name, background_color=(1, 0, 0, 1))
                        temp_button.bind(on_release=self.press_item)
                        self.root.ids.itemsButtons.add_widget(temp_button)
                    elif item.priority == 2:
                        temp_button = Button(text=item.name, background_color=(0, 1, 0, 1))
                        temp_button.bind(on_release=self.press_item)
                        self.root.ids.itemsButtons.add_widget(temp_button)
                    elif item.priority == 3:
                        temp_button = Button(text=item.name, background_color=(0, 0, 1, 1))
                        temp_button.bind(on_release=self.press_item)
                        self.root.ids.itemsButtons.add_widget(temp_button)

        elif status == 'c':
            for item in self.items.items:
                if item.status == status:
                    temp_button = Button(text=item.name)
                    temp_button.bind(on_release=self.press_item)
                    self.root.ids.itemsButtons.add_widget(temp_button)

    def required_button(self):
        """
        Clears the item field and creates item buttons depending on its status being equal to 'r'
        :return: None
        """
        self.root.ids.completedList.state = 'normal'
        self.root.ids.itemsButtons.clear_widgets()
        self.create_item_buttons('r')
        total_cost = self.items.get_total_cost()
        self.display = 'Click items to mark them as completed'
        self.heading = 'Total price: ${:.2f}'.format(total_cost)

    def completed_button(self):
        """
        Clears the item field and creates item buttons depending on its status being equal to 'c'
        :return: None
        """
        self.root.ids.requiredList.state = 'normal'
        self.root.ids.itemsButtons.clear_widgets()
        self.create_item_buttons('c')
        self.heading = 'Showing completed items'
        self.display = 'Click item to view'

    def press_item(self, instance):
        """

        :param instance:
        :return: None
        """
        name = instance.text
        for item in self.items.items:
            if item.name == name and item.status == 'r':
                item.status = 'c'
                self.display = "Completed: {}".format(Item.__str__(item))
                self.required_button()

            if item.name == name and item.status == 'c':
                self.display = "{}".format(Item.__str__(item))

    def add_item(self,item_name, item_price, item_priority):
        """

        :param item_name: name input as str (from GUI)
        :param item_price: price input as str (from GUI)
        :param item_priority: priority input as str (from GUI)
        :return: None
        """
        if len(item_name) == 0 or len(item_price) == 0 or len(item_priority) == 0:
            self.display = 'All fields must be completed'
        else:
            try:
                price = float(item_price)
                if price < 0:
                    self.display = 'Price must not be negative'
                    return
            except ValueError:
                self.display = 'Please enter a valid entry'
                return

            try:
                priority = int(item_priority)
                if priority > 3 or priority < 1:
                    self.display = 'Priority must be 1, 2 or 3'
                    return
            except ValueError:
                self.display = 'Please enter a valid number'
                return

            new_item = [str(item_name), price, priority, 'r']
            self.items.add_item(new_item)
            self.clear_entry_fields()
            self.required_button()

    def clear_entry_fields(self):
        """
        Clears all fields in the text box
        :return: None
        """
        self.root.ids.itemName.text = ''
        self.root.ids.itemPrice.text = ''
        self.root.ids.itemPriority.text = ''

    def on_stop(self):
        item_list = self.items.get_items_as_a_list()
        save_items(item_list, 'new_items')

ShoppingListApp().run()