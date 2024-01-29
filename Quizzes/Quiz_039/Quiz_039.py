from kivymd.app import MDApp


class MyQuizzApp39(MDApp):
    def build(self):
        return
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
    def add_counter(self):
        self.count += 1
        self.root.ids.label_counter.text = f"count {self.count}"
        if self.count == 20:

            self.count=0
    def reduce_counter(self):
        self.count -= 1
        self.root.ids.label_counter.text = f"count {self.count}"



text = MyQuizzApp39()
text.run()