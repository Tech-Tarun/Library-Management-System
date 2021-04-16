def dump(a):
    with open('file.txt', 'w')as f:
        f.write(a)

def load():
    with open('file.txt','r')as f:
        j=convert(f.read())
        return j

def convert(string):
    li=list(string.split(","))
    return li
    
def convert2(input_seq,seperator):
    strr=seperator.join(input_seq)
    return strr

def displayAvailableBooks():
    k = load()
    print("\n *Books present in this library are: ")
    for book in k: 
        print(" >> " + book)

def requestBook():
    book = input("\n *Enter the name of the book you want to borrow: ")
    return book

def borrowBook(book):
    k = load()
    if book in k:
        print(f"\n *You have been issued {book}. Please keep it safe and return it within 30 days")
        k.remove(book)
        sep=','
        dump(convert2(k,sep))
        return True
    else:
        print("\n **Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
        return False

def returnBook(return_book):
    k = load() 
    k.append(return_book)
    sep=','
    dump(convert2(k,sep))
    print("\n *******Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!*******")

def return_book():
    book = input("\n *Enter the name of the book you want to return: ")
    return book

while True:

    welcomeMsg = ''' \n ====== Welcome to Central Library ======

      !!Please choose an option!!

        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
    print(welcomeMsg)
    a = int(input("Enter a choice: "))
    if a == 1:
        displayAvailableBooks()
    elif a == 2:
        borrowBook(requestBook())
    elif a == 3:
        returnBook(return_book())
    elif a == 4:
        print("\n Thanks for choosing Central Library. Have a great day ahead! \n")
        exit()
    else:
        print("Invalid Choice!")   
