from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
class SecondScreen(MDScreen):
    pass
class FirstScreen(MDScreen):
    def try_change(self):
        self.parent.current = "Second"
class MultipleScreen(MDApp):
    def build(self):
        Window.size = (400, 700)

t = MultipleScreen()
t.run()