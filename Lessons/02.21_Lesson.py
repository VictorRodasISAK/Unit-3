from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from Lessons.Lesson_Library_Login import DatabaseWorker, make_hash


class TableScreen(MDScreen):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.data_tables = None
        self.selected_rows = []
    def on_pre_enter(self, *args):
        column_names = [('id', 40), ('Sender', 30), ('Receiver', 30), ('Amount', 40), ('Signature', 100)]
        self.data_tables = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            use_pagination=False,
            check=True,
            column_data=column_names,
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = TableApp.x.search('SELECT * FROM ledger', multiple=True)
        self.data_tables.update_row_data(
            None, data
        )

    def row_pressed(self, table, cell):
        print(f"Values Clicked {cell.text}")

    def checkbox_pressed(self, table, current_row):
        print(f"Record Checked {current_row}")

    def save(self):
        sender = self.ids.sender.text
        receiver = self.ids.receiver.text
        amount = self.ids.amount.text
        print(sender, receiver, amount)
        signature = f"sender_id {sender},receiver_id {receiver}, amount {amount}"
        save_query = f"""INSERT INTO ledger (sender_id, receiver_id, amount, signature) 
                        VALUES ({sender}, {receiver}, {amount}, '{make_hash(signature)}')"""
        TableApp.x.run_query(save_query)
        self.update()
class TableApp(MDApp):
    x = DatabaseWorker('../Quizzes/Quiz_049/bitcoin_exchange.db')
    def build(self):
        pass

test = TableApp()
test.run()
TableScreen.x.close()
