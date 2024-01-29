class Book:
    def __init__(self, genre, rating, title, author, language, price):
        self.genre = genre
        self.rating = rating
        self.title = title
        self.author = author
        self.language = language
        self.price = price

    def introduce_book(self):
        return f"The title of the book is: {self.title}, the author is: {self.author}, the language is in: {self.language}"

    def quality_book(self):
        if self.price > 40:
            price = "Really expensive"
        else:
            price = "Really cheap"
        return f"The price of the book is: {price}"



