from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel

class MyLabel(MDLabel):
    pass
class ClipMachine(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.money = 50000
        self.wire = 50
        self.price_wire = 500
    def build(self):
        Window.size = (900, 500)
        pass

    def buy_wire(self):
        if self.money >= self.price_wire:
            self.wire += 10
            self.money -= self.price_wire
            self.root.ids.wire_label.text = f'{self.wire}m'
            self.root.ids.money_label.text = f'{self.money}'

test = ClipMachine()
test.run()