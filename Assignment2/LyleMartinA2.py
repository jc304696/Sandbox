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
    """
    Main program - Shopping list 2.0
    """
    heading = StringProperty()
    display = StringProperty()

    def __init__(self, **kwargs):
        super(ShoppingListApp, self).__init__(**kwargs)
        self.item_list = load_items('items.csv')

    def build(self):
        self.title = 'Shopping List App'
        self.root = Builder.load_file('Assignment2_layout.kv')
        self.required_list()
        return self.root

    def create_item_buttons(self, status):
        """
        Create Buttons for the items in the shopping list and add them to the GUI
        :return: reference to the root Kivy widget
        """
        button_list = create_list(self.item_list, status)
        if status == 'r':
            for item in button_list:
                if item[2] == 1:
                    temp_button = Button(text=item[0], background_color=(1, 0, 0, 1))
                    temp_button.bind(on_release=self.press_item)
                    self.root.ids.itemsButtons.add_widget(temp_button)
                elif item[2] == 2:
                    temp_button = Button(text=item[0], background_color=(0, 1, 0, 1))
                    temp_button.bind(on_release=self.press_item)
                    self.root.ids.itemsButtons.add_widget(temp_button)
                elif item[2] == 3:
                    temp_button = Button(text=item[0], background_color=(0, 0, 1, 1))
                    temp_button.bind(on_release=self.press_item)
                    self.root.ids.itemsButtons.add_widget(temp_button)
        else:
            for item in button_list:
                temp_button = Button(text=item[0])
                temp_button.bind(on_release=self.press_item)
                self.root.ids.itemsButtons.add_widget(temp_button)

    def required_list(self):
        """

        :return: None
        """
        self.root.ids.requiredList.state = 'down'
        self.root.ids.completedList.state = 'normal'
        self.root.ids.itemsButtons.clear_widgets()
        total_price = 0
        self.create_item_buttons('r')
        for item in self.item_list:
            if item[3] == 'r':
                total_price += item[1]
        self.heading = 'Total price ${:.2f}'.format(float(total_price))
        self.display = 'Click items to mark them as completed'

    def completed_list(self):
        """

        :return: None
        """
        self.root.ids.completedList.state = 'down'
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
        for item_number in range(0, len(self.item_list)):
            if self.item_list[item_number][0] == name and self.root.ids.requiredList.state == 'down':
                self.item_list[item_number][3] = 'c'
                self.display = "Completed: {}, ${}, priority {} (completed)".format(name,
                                            float(self.item_list[item_number][1]), int(self.item_list[item_number][2]))
                self.root.ids.itemsButtons.clear_widgets()
                self.create_item_buttons('r')

            if self.item_list[item_number][0] == name and self.root.ids.completedList.state == 'down':
                self.display = "{}, ${}, priority {} (completed)".format(name, float(self.item_list[item_number][1]),
                                                                         int(self.item_list[item_number][2]))

    def add_item(self,item_name, item_price, item_priority):
        """

        :param item_name: name input as str (from GUI)
        :param item_price: price input as str (from GUI)
        :param item_priority: priority input as str (from GUI)
        :return: None
        """
        flag = False
        if len(item_name) == 0 or len(item_price) == 0 or len(item_priority) == 0:
            self.display = 'All fields must be completed'
        else:
            flag = True

        while flag:
            try:
                price = float(item_price)
                if price < 0:
                    self.display = 'Price must not be negative'
                    break
            except ValueError:
                self.display = 'Please enter a valid entry'
                break

            try:
                priority = int(item_priority)
                if priority > 3 or priority < 1:
                    self.display = 'Priority must be 1, 2 or 3'
                    break
            except ValueError:
                self.display = 'Please enter a valid number'
                break

            new_item = [str(item_name), price, priority, 'r']
            self.item_list.append(new_item)
            self.required_list()
            self.clear_entry_fields()
            flag = False

    def clear_entry_fields(self):
        """
        Clears all fields in the text box
        :return: None
        """
        self.root.ids.itemName.text = ''
        self.root.ids.itemPrice.text = ''
        self.root.ids.itemPriority.text = ''

ShoppingListApp().run()