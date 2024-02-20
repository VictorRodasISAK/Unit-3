from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from Lesson_Library_Login import DatabaseWorker

class SignupScreen(MDScreen):
    def try_signup(self):
        name = self.ids.uname.text
        email = self.ids.uemail.text
        password = self.ids.upass.text

class LoginScreen(MDScreen):
    pass
class LoginSystem(MDApp):
    def build(self):
        db_name = "project3.db"
        db = DatabaseWorker(db_name)
        db.create()
        db.close()

test = LoginSystem()
test.run()


# name = 'alice'
# email = 'alice@xyz.com'
# password = 'passw123'
# query = f"""INSERT INTO users (email, password, username) VALUES ('{name}', '{email}', '{password}')"""
#
# db.insert(query)
# print(db.search('SELECT * FROM users', multiple=True))
# db.close()

