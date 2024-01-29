class Person:
    def __init__(self, name):
        self.name = name
        self.email = None
        self.age = None
        self.height = None
        self.shoe_size = None
    def set_email(self, email):
        self.email = email

    def make_name_email(self, domain="isak.jp"): #Domain is the ending
        self.set_email(f"{self.name}@{domain}")
    def get_age(self):
        return self.age

yuiko = Person("yuiko")
yuiko.set_email("y@zx")
yuiko.age = 17
print(yuiko.get_age())

class Student(Person):
    def __init__(self, id, name):
        super(Student, self).__init__(name)
        self.id = id
        self.subjects = []
        self.grade_level = None

may = Student(1, "May")
may.set_email("m@zx")
print(may.email)