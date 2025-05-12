import sys

# List to store books in the inventory
list_books = []

# Predefined genres list
genders_books = ["Fiction", "NonFiction", "Science", "Biography", "Children"]

# Function to print details of a specific book from the list
def print_elements(book_position):
    print(f'Title: {list_books[book_position]["Title"]} | Author: {list_books[book_position]["Author"]}')
    print(f'Quantity: {list_books[book_position]["Quantity"]} | Genre: {list_books[book_position]["Gender"]}')
    print("_" * 15)

# Function to validate and request the quantity of book copies
def valid_quantity():
    while True:
        try:
            amount = int(input("Enter the number of copies of the book:\n"))
            if amount <= 0:
                print("Invalid quantity. Please enter a positive integer.")  # If quantity is not positive, it asks again
            else:
                return amount  # Returns the valid quantity
        except ValueError:
            print("Please enter numbers only.")  # If input is not a number, it shows an error message

# Function to validate that the text input is not empty
def valid_text_input(text_input):
    while True:
        text_input = input(text_input)  # Asks for a text input
        if not text_input:
            print("Input cannot be empty.\n")  # If the text is empty, it asks for input again
            continue
        return text_input  # Returns the valid input

# Function to validate and select the genre of a book
def valid_gender(text_input):
    while True:
        try:
            print(text_input)
            gender = int(input(f'''
                                1. {genders_books[0]}
                                2. {genders_books[1]}
                                3. {genders_books[2]}
                                4. {genders_books[3]}
                                5. {genders_books[4]}'''))  # Displays predefined genres to the user
            if 1 <= gender <= 5:
                return genders_books[gender-1]  # Returns the selected genre
            else:
                print("Invalid option. Please enter a number from 1 to 5.")  # If invalid option, asks again
        except ValueError:
            print("Please enter numeric integer characters only.")  # If input is not a number

# Function to check if a book with a given title already exists in the list
def check_existence(book_title):
    if list_books:
        for position in range(len(list_books)):
            current_product_title = list_books[position].get("Title", False)
            if current_product_title.upper().strip() == book_title.upper().strip():
                return position  # If the book exists, returns its position in the list
        return False  # If the book doesn't exist, returns False
    else:
        return False  # If the list is empty, returns False

# Function to add a new book to the inventory
def add_book():
    # Initialize a dictionary for the new book
    book = {
        "Title": "",
        "Author": "",
        "Quantity": 0,
        "Copies": 0,
        "Gender": ""
    }
    while True:
        # Ask for the title of the book
        book_title = valid_text_input("Enter the title of your book:\n")
        existing = check_existence(book_title)  # Check if the book already exists
        if existing is not False:
            print("Book already exists.\n")  # If the book exists, it asks for another title
            continue
        else:
            book["Title"] = book_title  # Set the book title

        # Ask for the author's name
        book_author = valid_text_input("Enter the author's name:\n")
        book["Author"] = book_author  # Set the author's name

        # Ask for the quantity of copies
        quantity = valid_quantity()
        book["Quantity"] = quantity  # Set the quantity of the book
        book["Copies"] = quantity  # Set the copies to the same quantity as the stock

        # Ask for the genre of the book
        book_gender = valid_gender("Enter the number corresponding to the book's genre:")
        book["Gender"] = book_gender  # Set the book genre

        # Add the book to the inventory
        list_books.append(book)

        break

# Main loop to display options and perform actions
while True:
    try:
        print("-" * 30)
        print('''
              Choose an option:

                1. Add book
                2. Search book
                3. Borrow book
                4. Return book
                5. Delete book
                6. List books by genre
                7. See inventory summary
                8. Exit
            ''')
        print("-" * 30)

        # Ask for the user's choice
        option = int(input("Enter your choice: "))
        match option:
            case 1:  # Add a new book
                add_book()
            case 2:  # Search for a book
                if list_books:
                    while True:
                        # Ask for the title of the book to search
                        book_title = valid_text_input("Enter the title of the book:\n")
                        book_position = check_existence(book_title)
                        if book_position is False:
                            print("Book not found")  # If the book is not found, display a message
                            break
                        else:
                            print_elements(book_position)  # Print book details
                            break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 3:  # Borrow a book
                if list_books:
                    while True:
                        # Ask for the title of the book to borrow
                        book_title = valid_text_input("Enter the title of the book to borrow:\n")
                        book_position = check_existence(book_title)
                        if book_position is False:
                            print("Book not found")  # If the book is not found, display a message
                            break
                        else:
                            print_elements(book_position)  # Print book details
                            if list_books[book_position]["Quantity"] >= 1:
                                # Decrease the available quantity of the book when borrowed
                                list_books[book_position]["Quantity"] -= 1
                                print(f'A copy of {list_books[book_position]["Title"]} was borrowed. {list_books[book_position]["Quantity"]} copies remaining.')
                            else:
                                print(f'There are no copies of {list_books[book_position]["Title"]} available to borrow.')  # If no copies left
                            break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 4:  # Return a book
                if list_books:
                    while True:
                        # Ask for the title of the book to return
                        book_title = valid_text_input("Enter the title of the book to return:\n")
                        book_position = check_existence(book_title)
                        if book_position is False:
                            print("Book not found")  # If the book is not found, display a message
                            break
                        else:
                            print_elements(book_position)  # Print book details
                            if list_books[book_position]["Quantity"] != list_books[book_position]["Copies"]:
                                # Increase the quantity of the book when returned
                                list_books[book_position]["Quantity"] += 1
                                print(f'A copy of {list_books[book_position]["Title"]} was returned. {list_books[book_position]["Quantity"]} copies available now.')
                            else:
                                print(f'The book {list_books[book_position]["Title"]} was not borrowed, so there are no copies to return.')  # If the book was not borrowed
                            break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 5:  # Delete a book
                if list_books:
                    while True:
                        # Ask for the title of the book to delete
                        book_title = valid_text_input("Enter the title of the book to delete:\n")
                        book_position = check_existence(book_title)
                        if book_position is False:
                            print("Book not found")  # If the book is not found, display a message
                            break
                        else:
                            print_elements(book_position)  # Print book details
                            if list_books[book_position]["Quantity"] == list_books[book_position]["Copies"]:
                                # If no copies are borrowed, delete the book from the inventory
                                list_books.pop(book_position)
                                print(f'The book {book_title} was deleted from the inventory.')
                            else:
                                print(f'There are borrowed copies of {list_books[book_position]["Title"]}. It cannot be deleted.')  # If there are borrowed copies, cannot delete
                            break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 6:  # List books by genre
                if list_books:
                    while True:
                        book_gender = valid_gender("Enter the number of the genre you want to view:\n")
                        # Filter books by the selected genre
                        books_for_gender = filter(lambda x: x["Gender"] == book_gender, list_books)
                        books_for_gender = list(books_for_gender)  # Convert the filter object to a list
                        if books_for_gender:
                            for book in books_for_gender:
                                print_elements(list_books.index(book))  # Print book details for the filtered books
                            break
                        else:
                            print("No books found in this genre")  # If no books match the genre
                            break
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 7:  # See inventory summary
                if list_books:
                    print("Title | Total Copies | Available to Borrow")
                    total_quantity = 0
                    total_to_borrow = 0
                    # Iterate through the list of books and calculate the total copies and available books
                    for book in list_books:
                        print("_" * 30)
                        print(f'{book["Title"]} | {book["Copies"]} | {book["Quantity"]}')
                        total_quantity += book["Copies"]
                        total_to_borrow += book["Quantity"]
                    print("_" * 30)
                    print(f'Total books in the inventory: {total_quantity}')
                    print(f'Total books currently available to borrow: {total_to_borrow}')
                    print("_" * 30)
                else:
                    print("*" * 20)
                    print("No books in the inventory")
                    print("*" * 20)
            case 8:  # Exit the program
                print("*" * 20)
                sys.exit("See you next time")  # Exit message and end the program
            case _:
                print("Invalid number")  # If the user enters an invalid option
    except ValueError:
        print("*" * 20)
        print("[INVALID INPUT]")
        print("*" * 20)
