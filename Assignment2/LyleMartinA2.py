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
        self.create_item_buttons()
        return self.root

    def create_item_buttons(self):
        """

        :return:
        """
        required_items = create_list(self.item_list, 'r')
        for item in range(0, len(required_items)):
            temp_button = Button(text=required_items[item][0])
            self.root.ids.itemsButtons.add_widget(temp_button)

ShoppingListApp().run()