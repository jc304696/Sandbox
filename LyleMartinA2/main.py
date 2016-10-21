"""Name:        Lyle Martin
   Date:        20/10/2016
   Description: ShoppingListApp class creates a GUI using kivy. The GUI will have the following functionality:
                - Required list button
                - Completed list button
                - Add item button
                - Clear button
                - Entry capabilities to add a new item (entries will be name, price and priority)
                - Display window to show commands to the user
                - Heading window to show particular statements
                - Widgets to display the list of items

   URL:         https://github.com/jc304696/Sandbox.git
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button
from LyleMartinA2.Functions import load_items, save_items
from LyleMartinA2.itemlist import ItemList, Item

__author__ = 'Lyle Martin'

BUTTON_COLOUR_DICT = {1: (1, 0, 0, 1), 2: (0, 1, 0, 1), 3: (0, 0, 1, 1)}
FILE_NAME = 'items.csv'


class ShoppingListApp(App):
    """
    Creates a graphical user interface (GUI) that displays a shopping list and methods to handle different events
    """
    heading_string = StringProperty()
    display_string = StringProperty()

    def __init__(self, **kwargs):
        """
        Constructs the ShoppingList App

        :return None
        """
        super(ShoppingListApp, self).__init__(**kwargs)
        item_list = load_items(FILE_NAME)
        self.items = ItemList()
        self.items.add_items_from_a_list(item_list)

    def build(self):
        """
        Builds the Kivy GUI

        :return: reference to the root Kivy widget
        """
        self.title = 'Shopping List App'
        self.root = Builder.load_file('App.kv')
        self.required_button()
        return self.root

    def required_button(self):
        """
        Creates required item buttons

        Clears the widgets from the GUI and creates item buttons if the item's status is equal to 'r'
        :return: None
        """
        self.root.ids.completedList.state = 'normal'
        self.root.ids.itemsButtons.clear_widgets()
        for item in self.items.items:
            if item.status == Item.REQUIRED:
                colour = BUTTON_COLOUR_DICT[item.priority]
                temp_button = Button(text=item.name, background_color=(colour))
                temp_button.bind(on_release=self.press_item_button)
                self.root.ids.itemsButtons.add_widget(temp_button)
        total_price = self.items.get_total_price()
        self.display_string = 'Click items to mark them as completed'
        self.heading_string = 'Total price: ${:.2f}'.format(total_price)

    def completed_button(self):
        """
        Creates completed item button

        Clears the widgets from the GUI and creates item buttons if the item's status is equal to 'c'
        :return: None
        """
        self.root.ids.requiredList.state = 'normal'
        self.root.ids.itemsButtons.clear_widgets()
        for item in self.items.items:
            if item.status == Item.COMPLETED:
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.press_item_button)
                self.root.ids.itemsButtons.add_widget(temp_button)
        self.heading_string = 'Showing completed items'
        self.display_string = 'Click item to view'

    def press_item_button(self, instance):
        """
        Handler for pressing item buttons

        :param instance: the information from the Kivy button instance
        :return: None
        """
        name = instance.text
        item = self.items.get_item_by_name(name)
        if item.status == Item.REQUIRED:
            item.mark_complete()
            self.display_string = str(item)
            self.required_button()
        elif item.status == Item.COMPLETED:
            self.display_string = str(item)

    def add_item(self, item_name, item_price, item_priority):
        """
        Adds item to the list

        Error checks entry making sure that all fields have been filled out correctly then creates a list of the results
        to be converted to an object and added to the list.
        :param item_name: name input as str (from GUI)
        :param item_price: price input as str (from GUI)
        :param item_priority: priority input as str (from GUI)
        :return: None
        """
        if len(item_name) == 0 or len(item_price) == 0 or len(item_priority) == 0:
            self.display_string = 'All fields must be completed'
        else:
            try:
                price = float(item_price)
                if price < 0:
                    self.display_string = 'Price must not be negative'
                    return
            except ValueError:
                self.display_string = 'Please enter a valid entry'
                return

            try:
                priority = int(item_priority)
                if priority > 3 or priority < 1:
                    self.display_string = 'Priority must be 1, 2 or 3'
                    return
            except ValueError:
                self.display_string = 'Please enter a valid number'
                return

            new_item = [str(item_name), price, priority, Item.REQUIRED]
            self.items.add_item(new_item)
            self.clear_entry_fields()
            self.required_button()

    def clear_entry_fields(self):
        """
        Clears all fields in the text boxes

        :return: None
        """
        self.root.ids.itemName.text = ''
        self.root.ids.itemPrice.text = ''
        self.root.ids.itemPriority.text = ''

    def on_stop(self):
        """
        Saves item list to csv file after closing the program down

        :return: None
        """
        item_list = self.items.get_items_as_a_list()
        save_items(item_list, FILE_NAME)


ShoppingListApp().run()
