from AddBook import AddBook
from ViewBooks import ViewBooks
from DeleteBook import DeleteBook
from BorrowedBook import BorrowedBook
from ReturnBook import ReturnBook

class Book:
    def __init__(self, bid, title, author, status):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status
        self.next = None

class BorrowedBook:
    def __init__(self, bid, borrower):
        self.bid = bid
        self.borrower = borrower
        self.next = None
    
class BooksLinkedList:
    def __init__(self):
        self.head = None
    def AddBook(self, bid, title, author, status):
        new_node = Book(bid, title, author, status)
        if self.head == None:
            self.head = new_node
        else:
            previous_node = self.head
            while previous_node.next:
                previous_node = previous_node.next
            prvious_node.next = new_node
    def ViewBooks(self):
        print("bid | title | author | status")
                
    
def main():
    while True:
        option = input("Choose your option: \n1. AddBook\n2.ViewBooks\n3.DeleteBook\n4.BorrowedBook\n5.ReturnBook")
        if option == 1:
            AddBook()
        elif option == 2:
            ViewBooks()
        elif option == 3:
            DeleteBook()
        elif option == 4:
            BorrowedBook()
        elif option == 5:
            ReturnBook()
        else:
            continue
