# Products Inventory System

This Python-based application allows you to manage a product inventory system. You can add products, search for products, update prices, remove products, calculate the total value of the inventory, and see a list of all the products.

## Instructions for Use

1. **Running the Program**:

   * Ensure you have Python installed on your machine.
   * Run the script in a terminal or command prompt:

     ```bash
     python book_inventory.py
     ```

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

   * **Add a Book**: Allows you to add a new book to the inventory by entering the book's title, author, quantity, and genre.
   * **Search a Book**: Allows you to search for a book by title and view its details, including available copies.
   * **Borrow a Book**: Allows you to borrow a book, decreasing the available copies in the inventory.
   * **Return a Book**: Allows you to return a book, increasing the available copies in the inventory.
   * **Delete a Book**: Allows you to delete a book from the inventory if no copies are borrowed.
   * **List Books by Genre**: Allows you to filter books based on their genre (e.g., Fiction, NonFiction, etc.).
   * **See Inventory Summary**: Displays a summary of all books, their total copies, and how many are available to borrow.

4. **Exit**:

   * Selecting option `8` will exit the program.
