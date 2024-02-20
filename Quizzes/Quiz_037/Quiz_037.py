class Compound_Interest:
    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate
        self.years = years

    def calculate(self):
        return self.principal * (1 + self.rate) ** (self.years)

class Accounting(Compound_Interest):
    def __init__(self, name, email, principal, rate, years):
        super(Accounting, self).__init__(principal, rate, years)
        self.name = name
        self.email = email

    def get_message(self):
        return f"{self.name} will have ${self.calculate():.2f} in {self.years} years if the principal is {self.principal} USD, with {self.rate} annual compund interest"

victor = Accounting(name="Victor", email="vic@gmail.com", principal= 1000, rate = 0.1, years = 10)
print(victor.get_message())
