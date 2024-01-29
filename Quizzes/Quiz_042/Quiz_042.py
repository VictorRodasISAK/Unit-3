from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
class MysteryPageB(MDScreen):
    def message2(self):
        self.parent.current = "First"
        print("This is mystery page A you pressed the button")
class MysteryPageA(MDScreen):
    def message1(self):
        self.parent.current = "Second"
        print("This is mystery page B you pressed the button")
class MyQuizApp42(MDApp):
    def build(self):
        Window.size = (900, 900)

t = MyQuizApp42()
t.run()