#Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!
#no of books is integer and books is list   

class Library():
    def __init__(self, no_of_books, books):
        self.no_of_books = no_of_books
        self.books = books
        
    def displayBooks(self):
        print(f'The books available in this library are {self.books}')

    def addBook(self):
        ask=input("enter the name the book you want to add to the libaray: ")
        self.books.append(ask)
        self.no_of_books+=1

    def Books_no(self):
        print(f"No of books in this library {self.no_of_books}")
        
b = ['dfasdkfj', 'jhadf', 'asjdfsda', 'dfdksfd' , 'fkdsj' , 'dfjsdf', 'jsdfkjsdf' , 'dfmdkfjdsfds', 'fdsjfsd']
n = len(b)
a = Library(n,b)
while True:
    print('''
          Enter 1 for seeing the books available in the library.
          Enter 2 to add a book in the library.
          Enter 3 to see how many books are available in the library.
          Enter 4 to quit
          ''')
    choice=int(input("Enter a number: "))
    if choice==1:
        a.displayBooks()
    elif choice==2:
        a.addBook()
    elif choice==3:
        a.Books_no()
    elif choice==4:
        break
    else:
        print("Please enter a valid number")
        