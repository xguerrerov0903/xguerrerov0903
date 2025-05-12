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
```

---

### Example 3: Update price

**Input**:

```
Type your option: 3
Enter the name of the product: 
EGGS
Enter your product price: 
250
```

**Output**:

```
The new information of your product is:
Name: Eggs
Price: 250.0$ | Quantity: 30
```

---

### Example 4: Remove a Product

**Input**:

```
Type your option: 4
Enter the name of the product: 
EgGs
```

**Output**:

```
Successful elimination of EgGs
```

---

### Example 5: Calculate the total value of inventory

**Input**:

```
Type your option: 5
```

**Output**:
* Note: The code has defaults data, the default total without changes is this

```
Your total is 143000.0$
```

---

### Example 6: Show products

**Input**:

```
Type your option: 6
```

**Output**:

```
______________________________
Name: Potato
Price: 2000.0$ | Quantity: 12
______________________________
Name: Apple
Price: 1000.0$ | Quantity: 6
______________________________
Name: Rice
Price: 1500.0$ | Quantity: 20
______________________________
Name: Meat
Price: 10000.0$ | Quantity: 5
______________________________
Name: Sugar
Price: 2200.0$ | Quantity: 15
```

---

### Example 7: Exiting the Program

**Input**:

```
Type your option: 7
```

**Output**:

```
********************
See you next time :)
```

---

## Requirements

* **Python** (any version above 3.6 should work)
* **Operating System**: Cross-platform (Windows, macOS, Linux)

---

