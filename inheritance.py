class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(self.title)
        print(self.author)
class Python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        super().__init__(name,title, author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        super().display()
        print(self.price)
        print(self.no_of_pages)
P1=Python("abc","py","robert",200,300)
P1.display()