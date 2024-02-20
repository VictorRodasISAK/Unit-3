from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

from Lessons.Lesson_Library_Login import DatabaseWorker
from kivy.core.window import Window

class DropList(MDApp):
    def build(self):
        self.x = DatabaseWorker("/Users/m19-056/PycharmProjects/pythonProject1/Unit3/Quizzes/Quiz_049/bitcoin_exchange.db")
        query = """Select * from users"""
        results = self.x.search(query, multiple=True)
        self.users = results
        Window.size = (500, 700)

    def open_menu(self, drop_item_element):
        # self.menu_item = [name for name in self.users]
        self.menu_item = []
        for c in self.users:
            self.menu_item.append(c[1])

        buttons_menu = []
        for item in self.menu_item:
            buttons_menu.append({'text': item, 'viewclass': "OneLineListItem", 'on_release': lambda x=item: self.button_pressed(x)})

        self.menu = MDDropdownMenu(
            caller=drop_item_element,
            items=buttons_menu,
            width_mult=4,
        )
        self.menu.open()

    def button_pressed(self, x):
        user = self.x.search(f"Select * from users where username = '{x}'")
        if user:
            self.root.ids.customer.text = f"Customer: {user[1]} with id {user[0]}"
            self.root.ids.dropdown_user.text = f"{user[1]}"
        self.menu.dismiss()

test = DropList()
test.run()
test.x.close()