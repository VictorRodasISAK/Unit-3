from kivymd.app import MDApp

class MyQuizzApp40(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return

    def button_pressed(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"
        btn = self.root.ids.my_btn
        if btn.md_bg_color == [0, 0, 1, 1]:
            btn.md_bg_color = "red"
            self.root.ids.my_btn.text = "Light mode"
        else:
            btn.md_bg_color = "blue"
            self.root.ids.my_btn.text = "Dark mode"

text = MyQuizzApp40()
text.run()