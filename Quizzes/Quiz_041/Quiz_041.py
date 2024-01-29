from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton


class MyButton(MDFlatButton):
    pass
class MyQuizzApp41(MDApp):
    def build(self):
        Window.size = (500, 500)
        pass
    def button_pressed(self, btn):
        btn.md_bg_color = "red"
        if self.root.ids.player_turn.text == "X player's turn":
            btn.text = "X"
            self.root.ids.player_turn.text = "Y player's turn"
        else:
            self.root.ids.player_turn.text = "X player's turn"
            btn.text = "O"
            btn.md_bg_color = "yellow"


test = MyQuizzApp41()
test.run()
