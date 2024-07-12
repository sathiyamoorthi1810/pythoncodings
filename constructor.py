"""
2) Constructor:

Define a class Book with a parameterized constructor that initializes the title and author attributes. Create two objects of the Book class and print their details.

"""
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        print(f"Title is:{self.title},author is :{self.author}")

book1 = Book("pyhon","guido")
book2 = Book("Java","Gosling")