class Racket:
    # initializer function
    def __init__(self, size, color, weight, price):
        self.size = size
        self.color = color
        self.weight = weight
        self.price = price

    def get_color(self):
        return f"This racket color is {self.color}"

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def level(self):
        letter = ""
        if self.size == "L" and self.weight <= 90:
            letter += "D"
        if self.size == "M" and self.weight > 90:
            letter += "A"
        return letter


# create an instance of the class Racket
training_racket = Racket(size="L", color="blue", weight=90, price=30000)
tournament_racket = Racket(size="M", color="red", weight=75, price=40000)

print(training_racket.level())