# Products Inventory System

This Python-based application allows you to manage a product inventory system. You can add products, search for products, update prices, remove products, calculate the total value of the inventory, and see a list of all the products.

## Instructions for Use

1. **Running the Program**:

   * Ensure you have Python installed on your machine.
     
   * Clone the repo
     ```bash
     git clone https://github.com/xguerrerov0903/xguerrerov0903/tree/main/Prueba_desempeno
     ```
   * Run the script in a terminal or command prompt:
     ```bash
     python Desempeno.py
     ```
     Check that you run the script in the folder where you clone the repo

2. **Menu Options**:
   When the program runs, you'll be presented with the following menu options:

   ```
   1. Add product
   2. Search product
   3. Update price
   4. Remove product
   5. Calculate the total value of inventory
   6. Show products
   7. Exit
   ```

   You can choose the desired option by entering the corresponding number.

3. **Actions**:

   * **Add a Product**: Allows you to add a new product to the inventory by entering the product's name, preci and quantity.
   * **Search a Product**: Allows you to search for a product by name and view its details.
   * **Update price**: Allows you to change the price of a product by its name.
   * **Remove a Product**: Allows you to delete a product from the inventory by its name.
   * **Calculate the total value of inventory**: Displays a sum of all the products.
   * **Show products**: Displays a summary of all products and its details.

4. **Exit**:

   * Selecting option `7` will exit the program.
     
5. **Default data**:
   The code has 5 default data that are in line 4, if you want you can delete them, they are not necessary, the code will work without them even with an empty list
   ```bash
     list_products = [{"Name": "Potato","Price": 2000.0,"Quantity": 12},
                 {"Name": "Apple","Price": 1000.0,"Quantity": 6},
                 {"Name": "Rice","Price": 1500.0,"Quantity": 20},
                 {"Name": "Meat","Price": 10000.0,"Quantity": 5},
                 {"Name": "Sugar","Price": 2200.0,"Quantity": 15}]
   ```
  
---

## Input/Output Examples

### Example 1: Adding a Product

**Input**:

```
Type your option: 1
Enter the name of your product: 
Eggs
Enter your product price: 
300
Enter the amount of your product: 
30
```

**Output**:

```
The product Eggs has been added to the inventory.
```

---

### Example 2: Search a Product

**Input**:

```
Type your option: 2
Enter the name of the product: 
eggs
```

**Output**:

```
Name: Eggs
Price: 300.0$ | Quantity: 30
_______________
```

---

### Example 3: Borrowing a Book

**Input**:

```
3. Borrow book
Enter the title of the book to borrow:
The Great Gatsby
```

**Output**:

```
Title: The Great Gatsby | Author: F. Scott Fitzgerald
Quantity: 10 | Genre: Fiction
_______________
A copy of The Great Gatsby was borrowed. 9 copies remaining.
```

---

### Example 4: Returning a Book

**Input**:

```
4. Return book
Enter the title of the book to return:
The Great Gatsby
```

**Output**:

```
Title: The Great Gatsby | Author: F. Scott Fitzgerald
Quantity: 9 | Genre: Fiction
_______________
A copy of The Great Gatsby was returned. 10 copies available now.
```

---

### Example 5: Deleting a Book

**Input**:

```
5. Delete book
Enter the title of the book to delete:
The Great Gatsby
```

**Output**:

```
Title: The Great Gatsby | Author: F. Scott Fitzgerald
Quantity: 10 | Genre: Fiction
_______________
The book "The Great Gatsby" was deleted from the inventory.
```

---

### Example 6: Listing Books by Genre

**Input**:

```
6. List books by genre
Enter the number of the genre you want to view:
1. Fiction
2. NonFiction
3. Science
4. Biography
5. Children
```

**Output**:

```
Title: The Great Gatsby | Author: F. Scott Fitzgerald
Quantity: 10 | Genre: Fiction
_______________
```

---

### Example 7: Viewing the Inventory Summary

**Input**:

```
7. See inventory summary
```

**Output**:

```
Title | Total Copies | Available to Borrow
_______________________________
The Great Gatsby | 10 | 10
_______________________________
Total books in the inventory: 10
Total books currently available to borrow: 10
_______________________________
```

---

### Example 8: Exiting the Program

**Input**:

```
8. Exit
```

**Output**:

```
See you next time
```

---

## Requirements

* **Python** (any version above 3.6 should work)
* **Operating System**: Cross-platform (Windows, macOS, Linux)

---

## License

This project is open-source and licensed under the MIT License. Feel free to modify and contribute!

---

