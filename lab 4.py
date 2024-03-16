"""

Program Description: Develop a simple inventory management system for a small retail business using Python lists.
This system will track the stock levels of various products and allow for adding, removing, and querying products.
Platform : Pycharm
Date Written : 02-14-2024
Date Modified : 02-15-2024
Programmers : Aldwin Guanzon

"""

product_name = []
quantity = []


# to find and get the index of the products
def id_product(new):
    for x in product_name:
        if new == x:
            return int(product_name.index(x))


# to know the stock level of the products
def stock_level(stock):
    if quantity[stock] == 0:
        return "Out"  # if product quantity is out of stock
    elif quantity[stock] <= 10:
        return "Low"  # if product quantity is low of stock
    elif quantity[stock] <= 20:
        return "Reorder"  # if product quantity is needed to reorder
    else:
        return ""  # if product quantity is above 20


# to view the product lists
def view_inventory():
    print("===========================================")
    print(f"   {"Product Name"} |  {"Quantity"} | {"Stock Level"}")
    for x in range(len(product_name)):
        print(f"     {product_name[x].title():9} {quantity[x]:9}       {stock_level(x)}")
    print("===========================================")


# To add a  product
def adding_product():
    add = input("What Product You want to Add: ").lower()
    assert add != "", "Error, Can't input a blank"  # if user input a empty or blank
    if add in product_name:  # if product already exists in a list
        id_no = id_product(add)  # To find the index
        print(f"The {add.title()} is already on the List")
        add_quantity = int(input("Please Enter the Quantity to Add: "))
        assert add_quantity > 0, "Error, Invalid Input Can't Input a Negative"  # if inputted a negative
        new_quantity = quantity.pop(id_no)  # To remove the quantity in the list, then assign it in new_quantity
        result_add = add_quantity + new_quantity  # add the new_quantity and add_quantity
        quantity.insert(id_no, result_add)  # To insert in list in specific index
        view_inventory()  # To see the result

    else:  # if new products
        product_name.append(add)  # To Add product name to the list
        print(f"The {add.title()} is added to the list")
        add_quantity = int(input("Please Enter the Product Quantity to Add: "))
        assert add_quantity > 0, "Error, Invalid Input Can't Input a Negative"  # if inputted a negative
        quantity.append(add_quantity)  # To Add product quantity to the list
        view_inventory()


# to remove product in the list
def removing_product():
    view_inventory()  # to see what product to remove
    remove = input("Enter the Product Name to Remove : ")
    assert remove in product_name, f"Error, The {remove.title()} is not in the List"  # if product is not on the list
    id_no = id_product(remove)  # To find the index
    product_name.pop(id_no)  # remove the product name
    quantity.pop(id_no)  # remove the  product quantity
    print("The Product is Removed.")
    view_inventory()  # the result


def updating_product():
    view_inventory()  # to see what product to update on the list
    update = input("Enter the Product Name : ").lower()
    assert update in product_name, f"Error, The {update.title()} is not on the list"  # if product is in the list
    id_no = id_product(update)  # find the index of the product
    input_quantity = int(input("Please Enter the Quantity to Update : "))  # It can be to add or to reduce the quantity
    product_quantity = quantity.pop(id_no)  # To remove the quantity in the list, then assign it in product_quantity
    result_add = input_quantity + product_quantity  # add the input_quantity and product_quantity
    quantity.insert(id_no, result_add)  # add the result in the list-specific index
    print(f"The {update.title()} Quantity is Updated")
    view_inventory()  # The  result


# to query a specific product name and its quantity
def querying_inventory():
    name = input("What Product You want to query : ").lower()
    assert name in product_name, f"Error, The {name.title()} is not on the list"
    id_no = id_product(name)  # to get the index in the list
    print("===========================================")
    print(f"   {"Product Name"} |  {"Quantity"} | {"Stock Level"}")
    print(f"     {product_name[id_no].title():9} {quantity[id_no]:9}       {stock_level(id_no)}")
    print("===========================================\n")


# Main Menu
while True:
    try:
        print("\n===================================")
        print("--- Inventory Management System ---")
        print("    [1] - Add Product  ")
        print("    [2] - Remove Product  ")
        print("    [3] - Update Product  ")
        print("    [4] - Querying Inventory ")
        print("    [5] - To Exit ")
        print("===================================")
        choice = int(input("Enter your choice: "))
        print("")
        assert 0 < choice < 6, "Invalid Input, Please Pick Only from 1 to 5"  # if choice is 1 to 5 only
        if choice == 1:
            adding_product()
        elif choice == 2:
            removing_product()
        elif choice == 3:
            updating_product()
        elif choice == 4:
            querying_inventory()
        elif choice == 5:
            print("Thanks for using Inventory Management System, Goodbye!")
            break

    except ValueError:
        print("Error, Invalid Input")

    except AssertionError as msg:
        print(msg)
