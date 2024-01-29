from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen



class PageA(MDScreen):
    pass


class PageB(MDScreen):
    pass


class LoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Window.size = (700, 700)

    def logger(self):
        if self.root.current_screen.ids.user.text == "Victor" and self.root.current_screen.ids.password.text == "1701":
            self.root.current = "Second"
    def return_main(self):
        self.root.current = "First"


    def clear(self):
        self.root.current_screen.ids.user.text = ""
        self.root.current_screen.ids.password.text = ""


LoginApp().run()

