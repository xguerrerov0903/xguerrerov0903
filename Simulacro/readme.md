

# Book Inventory System

This Python-based application allows you to manage a book inventory system. You can add books, search for books, borrow or return books, delete books, list books by genre, and see an inventory summary. This system is designed for managing a library or bookstore's stock of books.

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
   1. Add book
   2. Search book
   3. Borrow book
   4. Return book
   5. Delete book
   6. List books by genre
   7. See inventory summary
   8. Exit
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

---

## Input/Output Examples

### Example 1: Adding a Book

**Input**:

```
1. Add book
Enter the title of your book:
The Great Gatsby
Enter the author's name:
F. Scott Fitzgerald
Enter the number of copies of the book:
10
Enter the number corresponding to the book's genre:
1. Fiction
2. NonFiction
3. Science
4. Biography
5. Children
```

**Output**:

```
The book "The Great Gatsby" has been added to the inventory.
```

---

### Example 2: Searching for a Book

**Input**:

```
2. Search book
Enter the title of the book:
The Great Gatsby
```

**Output**:

```
Title: The Great Gatsby | Author: F. Scott Fitzgerald
Quantity: 10 | Genre: Fiction
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


