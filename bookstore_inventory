
"""
Program Description: Managing a Bookstore Inventory with 2D Lists
IDE Platform : Pycharm
Date Written : 04-02-2024
Date Modified : 04-16-2024
Programmers : Aldwin Guanzon
"""

# Inventory dictionary containing categories of books, each category has a list of dictionaries with details of books
inventory = {'fiction': [],
             'non-Fiction': [],
             'educational': []
             }


# To Input and Validate the Category Name
def add_input_category():
    while True:
        user_input = input("Enter the New Category to Add (Type '0' to Exit) : ").lower()  # input
        if user_input.strip() != "":  # if input is not a blank by using strip
            return user_input
        else:
            print("Error! Invalid Input")


# To Add New Category
def add_category():
    while True:
        new_category = input("Enter the name of the new category (type '0' to Quit): ")
        if new_category == '0':  # if input a '0' it will return to the main menu
            return

        if new_category.lower() in inventory:
            print(f"Category '{new_category}' already exists.")
        else:
            inventory[new_category.lower()] = []  # Create an empty list for the new category
            print(f"Category '{new_category.title()}' added successfully.")
            break  # Exit  when a new category is added


# if inventory is empty
def if_no_category():
    if not inventory:  # if inventory is empty
        print("Error! No Categories Found")
        to_add = input(" Do you want to add a new category? (yes/no): ").strip()
        if to_add.lower() == "yes":
            add_category()  # if input 'yes' calls a method to add new category
        elif to_add.lower() == "no":
            print("Exit...")
            return  # will return to the main menu
        else:
            print("Invalid Input")


# to choose what category
def category_of_book():
    while True:
        try:
            if_no_category()  # if there is no category to choose
            print(" --| Category of Book |--")
            for x, category in enumerate(inventory):  # show all categories to choose
                print(f"  [{x + 1}] - {category.title()}")

            category = int(input("Enter the Category of the book (Type 0 to Exit ) : "))
            if category == 0:
                return category

            elif category > len(inventory):
                print(f"Invalid Input. Please enter a number between 1 to {len(inventory)}")
                continue

            # convert the key into a list then the use index to get the element to put in selected variable
            selected = list(inventory.keys())[category - 1]
            return selected  # return the selected categories
        except ValueError:
            print("Invalid Input. Please enter a valid number.")


# To Input and Validate
def add_input(x):
    while True:
        user_input = input(f"Enter the {x.title()} of the book (Type 0 to Exit ) : ").lower()
        if user_input.strip() != "":  # if input is not a blank using strip
            return user_input
        else:
            print("Error! Invalid Input")


# To Input and Validate
def numb_input(x):
    while True:
        try:
            num = int(input(f"Enter the {x.title()} of the book: "))
            if x.lower() == "isbn":
                if len(str(num)) > 13:  # the ISBN limit is 13 numerical digits
                    print("Error! Invalid ISBN. ISBN should be 13 digits or below .")
                else:
                    return num
            else:
                return num

        except ValueError:
            print("Invalid Input")


# to know if isbn have duplicate
def is_isbn_duplicate(isbn):
    for category in inventory.values():
        for book in category:
            if book["isbn"] == isbn:  # if input and ISBN are the same
                return True  # a duplicate
    return False  # not a duplicate


# To Add Book
def add_book():
    title = add_input("title")  # call for input and validate
    if title == '0':
        return

    author = add_input('author')  # call for input and validate
    if author == '0':
        return

    isbn = numb_input("ISBN")  # call for input and validate
    if is_isbn_duplicate(isbn):  # checking for duplicates based on ISBN.
        print("ISBN is already in use. Please Try Again")
        return

    quantity = numb_input("Quantity")  # call for input and validate
    category = category_of_book()  # call for what category
    if category == 0:
        return

    input_book = {"title": title,  # put all details into input_book
                  "author": author,
                  "isbn": isbn,
                  "quantity": quantity}
    inventory[category].append(input_book.copy())  # its duplicate or copy the input_book then add to the inventory
    print("Added successful")


# To Update What Book
def what_book(selected_category):
    while True:
        try:
            print("            Title              Author       ISBN       Quantity")
            for x, book in enumerate(inventory[selected_category]):  # Iterate and get their index and value in inventory
                print(
                    f" [{x + 1}] -  {book['title'].title():14}{book['author'].title():16}{book['isbn']:5} {book['quantity']:5}")

            updates = int(input("Enter the Book You Want to Update ( Type '0' to Exit ) : "))
            if updates == 0:
                return 'exit'
            elif updates in range(1, len(inventory[selected_category]) + 1):
                return updates - 1
            else:
                print("The Selected book is Invalid. Please try again")
        except ValueError:
            print("Input Invalid")


# To Update What Book Detail
def what_to_update_():
    while True:
        try:
            detail_list = ['title', 'author', 'ISBN', 'quantity']  # the book details
            for x in range(len(detail_list)):  # show all book details
                print(f" [{x + 1}]  -  {detail_list[x]}")
            select = int(input("What do you want to update (Type 0 to Exit): "))
            if select == 0:
                return 'exit'
            if select in range(1, len(detail_list) + 1):
                detail = detail_list[select - 1]  # To Get Value by their index
                return detail  # return
            else:
                print("Invalid Input Please Input 1 to 4 only")
        except ValueError:
            print("Invalid Input")


# To Update Book
def update_book():
    selected_category = category_of_book()
    if selected_category == 0:
        return  # if input a 0, it will return to the main menu

    if len(inventory[selected_category]) == 0:
        print("The Category is Empty")
        return  # if the category is empty and will return to the main menu

    updates = what_book(selected_category)  # calls for what book to update
    if updates == 'exit':
        return  # if input a 0, it will return to the main menu

    detail = what_to_update_()  # calls for what detail to update
    new_detail = None  # the default value of new_detail before calling a method
    if detail == 0:
        return  # if input a 0, it will return to the main menu
    elif detail == 'title' or detail == 'author':
        new_detail = add_input(detail)  # calls add_input for input and validation
    elif detail == 'ISBN' or detail == 'quantity':
        new_detail = numb_input(detail)  # calls num_input for input and validation

    inventory[selected_category][updates][detail] = new_detail  # change the value with new inputted
    print("Update successful")


# To Delete Book
def delete_book():
    selected_category = category_of_book()
    if selected_category == 0:
        return  # if input a 0, it will return to the main menu
    if len(inventory[selected_category]) == 0:
        print("The Category is Empty")
        return  # if the category is empty and will return to the main menu
    delete = what_book(selected_category)
    if delete == 'exit':
        return  # if input a 0, it will return to the main menu
    del inventory[selected_category][delete]
    print("Delete successful")


# To Show What Category to Delete
def show_category():
    while True:
        try:
            print(" ====== Category ======")
            for x, category in enumerate(inventory):  # iterate and use to get the index and the value
                print(f"  [{x + 1}]  - {category}")  # show all categories in inventory
            to_delete = int(input("What the Category to Delete (Type '0' to Exit) : "))
            if to_delete == 0:
                return to_delete
            elif to_delete in range(1, len(inventory) + 1):  # if input is 1 to length of keys in inventory
                # convert the key into a list then the index to get the element to put in selected variable
                selected = list(inventory.keys())[to_delete - 1]
                return selected
            else:
                print(f"Error, Please Choose 1 to {len(inventory)}")
        except ValueError:
            print("Invalid Input")


# To Delete Category
def delete_category():
    to_delete = show_category()  # call to know what to category to delete
    if to_delete == 0:
        return  # if input a 0, it will return to the main menu
        # To confirm because the content will also be deleted
    confirm = input(
        f"Are you sure you want to delete {to_delete.title()},it will also delete all books within this category. (Yes / No): ").lower()
    if confirm == 'yes':
        del inventory[to_delete]  # deleting the category
        print(f"{to_delete.title()} has been deleted.")
    elif confirm == 'no':
        return  # returning to the main menu
    else:
        print("Error, invalid Input")


# Menu for Category and Book management
def menu(x, y, z):  # x for label, y and z are to change the number
    while True:
        try:
            print(f"\n  -- {x} Management --")
            print("=============================")
            print(f"    [1] - New {x}")  # To Add a new book / Categories
            if x == "Book":
                print(f"    [2] - Update {x}")  # To Update a new book / Categories
            print(f"    [{y}] - Delete {x}")  # To Delete a new book / Categories
            print(f"    [{z}] - To Exit")  # Exit
            print("=============================")
            select = int(input(" Please Select an Option : "))
            assert 1 <= select <= z, f"Invalid Input! Please Enter a Number Between 1 and {z} Only."
            return select

        except ValueError:
            print("Invalid Input")
        except AssertionError as error:
            print(error)


# Menu for Category Management
def category_manage():
    user_input = menu("Category", 2, 3)  # call to show the menu
    if user_input == 1:
        add_category()  # To Add New Category
    elif user_input == 2:
        delete_category()  # To Delete Category
    elif user_input == 3:
        return  # To Return to the Main menu


# Menu for book Management
def book_manage():
    user_input = menu("Book", 3, 4)  # call to show the menu
    if user_input == 1:
        add_book()  # To Add a New book
    elif user_input == 2:
        update_book()  # To Update a book
    elif user_input == 3:
        delete_book()  # To Delete a book
    elif user_input == 4:
        return  # To Return to the Main menu


# Inventory Report
def inventory_report():
    total_books = 0  # default value
    print("=======================================================================")
    print("                         Inventory Report")
    # Iterate over each category and its corresponding books and access their value in inventory
    for category, books in inventory.items():
        print("=======================================================================")
        print("                             ", category.title())
        category_books = 0  # default value
        print("-----------------------------------------------------------------------")
        print("     TITLE                AUTHOR               ISBN            QUANTITY")

        for book in books:  # Iterate through each book in the books
            print(f"{book['title']:15}      {book['author']:15}    {book['isbn']:15}          {book['quantity']:3}")
            category_books += book['quantity']  # To add the quantity of each book to category_book
        print(f"\n Total {category.title()} Books = {category_books}")  # To show the quantity per categories

        total_books += category_books  # To add the quantity of each category to total_book
    print("=======================================================================")
    print(" Total Books = ", total_books)  # To show the quantity of all books


# The Main Menu
while True:
    try:
        print("\n- Welcome to the Bookstore Manager -")
        print("=======================================")
        print("   |           MAIN MENU           |")
        print("=======================================")
        print("       [1] - Category Management")  # Add or delete categories
        print("       [2] - Book Management")  # Add, update, or delete books
        print("       [3] - Inventory Report")  # Show categories with books
        print("       [4] - To Exit")  # Exit
        print("=======================================")
        choice = int(input(" Please enter your selection : "))
        assert 0 < choice < 5, "Invalid Input! Please Enter a Number Between 1 and 4 Only."  # input is 1 to 4 only
        if choice == 1:
            category_manage()  # call the category manager
        elif choice == 2:
            book_manage()  # call the book manager
        elif choice == 3:
            inventory_report()  # call the inventory report
        elif choice == 4:
            print("Exit, Thank You For Using Bookstore Manager")
            break  # to exit
    except ValueError:
        print("Error, Invalid Input")
    except AssertionError as msg:
        print(msg)
