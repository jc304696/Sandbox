"""
    Name:           Lyle Martin
    Date:           10/10/2016
    Description:
    URL:            https://github.com/jc304696/Sandbox.git
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from Assignment1.Functions import load_items, create_list, save_items

class ShoppingListApp(App):
    def __init__(self, **kwargs):
        super(ShoppingListApp, self).__init__(**kwargs)
        self.item_list = load_items('items.csv')
        #self.items = ['fish', 'waterbottle', 'pencil']

    def build(self):
        self.title = 'Shopping List App'
        self.root = Builder.load_file('Assignment2_layout.kv')
        self.create_item_buttons('r')
        return self.root

    def create_item_buttons(self, status):
        """
        Create Buttons for the items in the shopping list and add them to the GUI
        :return: reference to the root Kivy widget
        """
        required_items = create_list(self.item_list, status)
        for item in range(0, len(required_items)):
            temp_button = Button(text=required_items[item][0])
            self.root.ids.itemsButtons.add_widget(temp_button)

    def required_list(self):
        """

        :return:
        """
        self.root.ids.itemsButtons.clear_widgets()
        total_price_of_list = 0
        self.create_item_buttons('r')
        for item in self.item_list:
            if item[3] == 'r':
                total_price_of_list += item[1]
        self.root.ids.heading.text = 'Total price $' + str(total_price_of_list)
        self.root.ids.display.text = 'Click items to mark them as completed'

    def completed_list(self):
        """

        :return:
        """
        self.root.ids.itemsButtons.clear_widgets()
        total_cost_of_list = 0
        self.create_item_buttons('c')
        for item in self.item_list:
            if item[3] == 'c':
                total_cost_of_list += item[1]
        self.root.ids.heading.text = 'Total price $' + str(total_cost_of_list)
        self.root.ids.display.text = 'Completed items'

    def press_item(self, instance):
        """

        :param instance:
        :return:
        """
        name = instance.text
        for item in self.item_list:
            if item[0] == name:


    def add_item(self,item_name, item_price, item_priority):
        """

        :param item_name: name input as str (from GUI)
        :param item_price: price input as str (from GUI)
        :param item_priority: priority input as str (from GUI)
        :return: None
        """
        new_item = [str(item_name), float(item_price), int(item_priority), 'r']
        self.item_list.append(new_item)
        self.required_list()
        self.clear_entry_fields()

    def clear_entry_fields(self):
        """
        Clears all fields in the text box
        :return: None
        """
        self.root.ids.itemName.text = ''
        self.root.ids.itemPrice.text = ''
        self.root.ids.itemPriority.text = ''




ShoppingListApp().run()