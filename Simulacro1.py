import sys

list_books = []
genders_books = ["Fiction", "NonFiction", "Science", "Biography", "Children"]

def print_elements (book_position ):
    
    print(f'Title: {list_books[book_position]["Title"]} | Author: {list_books[book_position]["Author"]}')
    print(f'Quantity: {list_books[book_position]["Quantity"]} | Gender: {list_books[book_position]["Gender"]}')
    print("_" * 15)
    

def valid_quantity():
    while True:
        try:
            amount = int(input("Enter the quantity of copies of the book: \n"))
            if amount <= 0:
                print("Invalid quantity, please enter a positive integer.")
            else:
                return amount
        except ValueError:
            print("Please enter numeric characters only.")


def valid_text_input (text_input):
    while True:
        text_input = input(text_input)
        if not text_input:
            print("The input cannot be empty\n")
            continue
        return text_input
    
def valid_gender (text_input):
    while True:
        try:
            print(text_input)           
            gender = int(input(f'''
                                1. {genders_books[0]}
                                2. {genders_books[1]}
                                3. {genders_books[2]}
                                4. {genders_books[3]}
                                5. {genders_books[4]}'''))
            if 1<= gender <= 5:
                print("Invalid quantity, please enter a positive integer.")
            else:
                return genders_books[gender-1]
        except ValueError:
            print("Please enter numeric integer characters only.")

    

def check_existence(book_title):
    if list_books:
        for position in range(len(list_books)):
            current_product_title = list_books[position].get("Title", False)
            if current_product_title.upper().strip() == book_title.upper().strip():
                return position
        return False
    else:
        return False

def add_book():
    book = {
        "Title": "",
        "Author" : "",
        "Quantity": 0,
        "Copies" : 0,
        "Gender" : ""
    }
    while True:
        book_title = valid_text_input("Enter the title of your book: \n")
        existing = check_existence(book_title)
        if existing is not False:
            print("Books already exists \n")
            continue
        else:
            book["Title"] = book_title
            
        book_author = valid_text_input("Enter the author of your book: \n") 
        book["Author"] = book_author
 
        quantity = valid_quantity()
        book["Quantity"] = quantity
        
        book["Copies"] = quantity
        
        book_gender = valid_gender("Enter the number form gender of the book: ")
        book["Gender"] = book_gender
        
        list_books.append(book)
        break

while True:
    try:
        print("-" * 30)
        print('''
              
              What option would you like to choose?
              
                1. Add book
                2. Search book
                3. Borrow book
                4. Return book
                5. Delet book
                6. List books for gender
                7. See resume inventory
                8. Exit
                
            ''')
        print("-" * 30)
        option = int(input("Type your option: "))
        match option:
            case 1:
                add_book()
            case 2:
                if list_books:
                    while True:
                        book_title = valid_text_input("Enter the title of the book: \n")
                        book_position = check_existence(book_title)
                        if book_position is False:
                            print("Book not found")
                            break
                        else:
                            print_elements(book_position)                             
                            break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 3:
                if list_books:
                        while True:
                            book_title = valid_text_input("Enter the title of the book to borrow: \n")
                            book_position = check_existence(book_title)
                            if book_position is False:
                                print("Book not found")
                                break
                            else:
                                print_elements(book_position)      
                                if list_books[book_position]["Quantity"] >= 1:
                                    list_books[book_position]["Quantity"] -= 1  
                                    print(f"A copie of {list_books[book_position]["Title"]} was borrow now there is {list_books[book_position]["Quantity"]} left") 
                                else:
                                    print(f"There is no copies available to borrow of {list_books[book_position]["Title"]}")                        
                                break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 4:
                if list_books:
                        while True:
                            book_title = valid_text_input("Enter the title of the book to return: \n")
                            book_position = check_existence(book_title)
                            if book_position is False:
                                print("Book not found")
                                break
                            else:
                                print_elements(book_position)      
                                if list_books[book_position]["Quantity"] != list_books[book_position]["Copies"]:
                                    list_books[book_position]["Quantity"] += 1  
                                    print(f"A copie of {list_books[book_position]["Title"]} was return now there is {list_books[book_position]["Quantity"]} left") 
                                else:
                                    print(f"The {list_books[book_position]["Title"]} was not borrow in the past, there is not copies to be return")                        
                                break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 5:
                if list_books:
                        while True:
                            book_title = valid_text_input("Enter the title of the book to delet: \n")
                            book_position = check_existence(book_title)
                            if book_position is False:
                                print("Book not found")
                                break
                            else:
                                print_elements(book_position)      
                                if list_books[book_position]["Quantity"] == list_books[book_position]["Copies"]:
                                    list_books.pop(book_position)
                                    print(f"The book {book_title} was delet form the inventory") 
                                else:
                                    print(f"There is copies borrowed of {list_books[book_position]["Title"]}, the can not be delet")                        
                                break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 6:
                if list_books:
                        while True:
                            book_title = valid_gender("Enter the numbe of the gender you want see the list of books: \n")
                            print_elements(book_position)      
                            if list_books[book_position]["Quantity"] == list_books[book_position]["Copies"]:
                                list_books.pop(book_position)
                                print(f"The book {book_title} was delet form the inventory") 
                            else:
                                print(f"There is copies borrowed of {list_books[book_position]["Title"]}, the can not be delet")                        
                                break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
                
            case 7:
                if list_books:
                    total_inventory = list(map(lambda x: x["Price"] * x["Quantity"], list_books))
                    sum_inventory = sum(total_inventory)
                    print(f"The total is {sum_inventory}$")
                else:
                    print("*" * 20)
                    print("No products in the inventory")
                    print("*" * 20)
            case 8:
                print("*" * 20)
                sys.exit("See you next time")
            case _:
                print("Invalid number")
    except ValueError:
        print("*" * 20)
        print("[INVALID INPUT]")
        print("*" * 20)
