from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton


class MyButton(MDFlatButton):
    pass
class Game2048(MDApp):
    def build(self):
        Window.size = (500, 700)
    pass

    def button_pressed(self, button):
        pass

t = Game2048()
t.run()