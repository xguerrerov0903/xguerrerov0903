import sys

# Global list with 5 data default as requested
list_products = [{"Name": "Potato","Price": 2000.0,"Quantity": 12},
                 {"Name": "Apple","Price": 1000.0,"Quantity": 6},
                 {"Name": "Rice","Price": 1500.0,"Quantity": 20},
                 {"Name": "Meat","Price": 10000.0,"Quantity": 5},
                 {"Name": "Sugar","Price": 2200.0,"Quantity": 15}]

# Function that validates the amount of a product.It must be a positive integer.
def valid_quantity():
    while True:
        try:
            quantity = int(input("Enter the amount of your product: \n"))
            if quantity <= 0:
                print("Invalid quantity, enter a positive integer value.")  # Validates that the amount is greater than zero
            else:
                return quantity  # Returns the valid amount
        except ValueError:
            print("Enter numerical characters only.")  # In case it is not a number

# Function that validates the price of a product.It must be a floating number greater than zero.
def valid_price():
    while True:
        try:
            price = float(input("Enter your product price: \n"))
            if (price <= 0):  # Validates that the price is greater than zero
                print("Invalid price, entered a positive value")
                continue
        except ValueError:
            print("Enter numerical characters only")  # In case it is not a number
            continue
        price = round(price, 2)  # Round the price to two decimals
        return price  # Returns the valid price
    
# Function to validate that the text input is not empty
def valid_text_input(text_enter):
    while True:
        text_input = input(text_enter)  # Asks for a text input
        if not text_input:
            print("Input cannot be empty.\n")  # If the text is empty, it asks for input again
            continue
        return text_input  # Returns the valid input

# Function that verifies if a product already exists in the inventory (based on the name).
def check_existence(name_product):
    if (list_products):  # If the product list is not empty
        for position in range(len(list_products)):  # Browse the list of products
            current_product_name = list_products[position].get("Name", False)  # Get the name of the current product
            if (current_product_name.upper().strip() == name_product.upper().strip()):  # Compare without considering capital letters or spaces
                return position  # Returns the product position if it already exists
        return False  # If do not find the product, return false
    else:
        return False  # If the list is empty, False returns

# Function adding a new product to the inventory
def add_product():
    product = {
        "Name": "",
        "Price": 0.0,
        "Quantity": 0
    }
    while True:
        name_product = valid_text_input("Enter the name of your product: \n")  # Request the name of the product
        existing = check_existence(name_product)  # Verify if the product already exists in the inventory
        if not existing is False:  # If the product already exists
            print("Existing product \n")
            continue
        else:
            product["Name"] = name_product  # Assign the name to the product
        
        price = valid_price()  # Request and validate the product price
        product["Price"] = price
        
        quantity = valid_quantity()  # Request and validate the amount of the product
        product["Quantity"] = quantity
        
        list_products.append(product) # Add the product to the list
        break  # Leaves the loop once the product has been added

# Main loop where the user selects menu options
while True:
    try:
        # User options menu
        print("-" * 30)
        print('''
              
              Which option do you want to choose?
              
                1. Add product
                2. Search product
                3. Update price
                4. Remove product
                5. Calculate the total value of inventory
                6. Show products
                7. Exit
                
            ''')
        print("-" * 30)
        entry = int(input("Type your option: "))  # Ask the user to enter an option
        match entry:
            case 1:
                add_product()  # Calls the function to add a product
            case 2:
                if list_products:  # If the product list is not empty
                    while True:
                        name_product = valid_text_input("Enter the name of the product: \n")  # Request the name of the product to search
                        product_position = check_existence(name_product) # Look for the product in the inventory
                        if product_position is False:  # If the product is not find
                            print("Not existing product")
                            break
                        else:
                            # If you find the product, show the information
                            print(f'Name: {list_products[product_position]["Name"]}')
                            print(f'Price: {list_products[product_position]["Price"]}$ | Quantity: {list_products[product_position]["Quantity"]}')
                            break
                else:
                    print("*" * 20)
                    print("There are no products in the inventory")  # If there are no products in the inventory
                    print("*" * 20)
            case 3:
                if list_products:  # If the product list is not empty
                    while True:
                        name_product = valid_text_input("Enter the name of the product: \n")  # Request the name of the product to be updated
                        product_position = check_existence(name_product)  # Look for the product
                        if product_position is False:  # If the product is not find
                            print("Not existing product")
                            break
                        else:
                            new_price = valid_price()  # Request a new price for the product
                            list_products[product_position]["Price"] = new_price  # Update the product price
                            # Shows updated product information
                            print("The new information of your product is:")
                            print(f'Name: {list_products[product_position]["Name"]}')
                            print(f'Price: {list_products[product_position]["Price"]}$ | Quantity: {list_products[product_position]["Quantity"]}')
                            break
                else:
                    print("*" * 20)
                    print("There are no products in the inventory")  # If there are no products in the inventory
                    print("*" * 20)
            case 4:
                if list_products:  # If the product list is not empty
                    while True:
                        name_product = valid_text_input("Enter the name of the product: \n")  # Request the name of the product to delete
                        product_position = check_existence(name_product)  # Look for the product
                        if product_position is False:  # If the product is not find
                            print("Not existing product")
                            break
                        else:
                            list_products.pop(product_position)  # Eliminate the product from the list
                            print(f"Successful elimination of {name_product}")
                            break
            case 5:
                if list_products:  # If the product list is not empty
                    total_inventory = list(map(lambda x: x["Price"] * x["Quantity"], list_products))  # Calculate the total for each product
                    sum_inventory = sum(total_inventory)  # Sum the total of all products
                    print(f"Your total is {sum_inventory}$")  # Shows the total inventory value
                else:
                    print("*" * 20)
                    print("There are no products in the inventory")  # If there are no products in the inventory
                    print("*" * 20)
            case 6:
                for product_position in range(len(list_products)):
                    print("_"*30)
                    print(f'Name: {list_products[product_position]["Name"]}')
                    print(f'Price: {list_products[product_position]["Price"]}$ | Quantity: {list_products[product_position]["Quantity"]}')
            case 7:
                print("*" * 20)
                sys.exit("See you next time :)")  # Leaves the program
            case _:
                print("Invalid number")  # If the user enters an invalid option
    except ValueError:
        print("*" * 20)
        print("[Invalid Type]")  # If the user enters something that is not a number in an option
        print("*" * 20)
