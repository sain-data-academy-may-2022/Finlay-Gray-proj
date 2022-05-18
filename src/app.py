# imports
import os
# work
# setting up inital variables
products = []
orders = []
run = True
product_menu = False
order_menu = False

def clear_screen():
    os.system('clear')

# setting up menu texts that will show up on screen
first_menu_text = '''\nWelcome to Gray's Cafe!\n
Enter 1 to view prouct menu
Enter 2 to view order menu
Enter 0 to quit
> '''
product_menu_text = '''Enter 1 to view products list
Enter 2 to create a new product
Enter 3 to update current product
Enter 4 to delete a product
Enter 0 to return to main menu 
> '''
order_menu_text = '''Enter 1 to view orders
Enter 2 to create a new order
Enter 3 to update an existing order status
Enter 4 to update an existing order
Enter 5 to delete an order
Enter 0 to return to main menu
> '''

status_list = ['PREPARING','COMPLETED']
# function that prints out product list with corresponding index
def product_list_index(list):
    for i in range(len(list)):
        print(f'Product name: {list[i]}\nIndex value: {i}\n')

def orders_list_index(list):
    for i in range(len(list)):
        print(f'Order: {list[i]}\nIndex value: {i}\n')

def status_list_index(list):
    for i in range(len(list)):
        print(f'Status: {list[i]}\nIndex value: {i}\n')

# function that handles the product menu
def product_menu_func(products):
    option = input(product_menu_text).strip()
    clear_screen()
    # prints product list
    if option == '1':
        product_list_index(products)
    # allows user to add a product to the list
    elif option == '2':
        product = input('Enter the name of the product you would like to add\n> ').lower().strip()
        if product in products:
            print(f'\nThis product already exists in your list\n')
        else:
            products.append(product)
            print(f'\nYou have added {product} to your products\n')
    # allows user to update the name of a product in the list
    elif option == '3':
        if products != []:
            product_list_index(products)
            try:
                product_index = int(input('Enter index of product you would like to update\n> ').strip())
                product_old_name = products[product_index]
                product_new_name = input('\nEnter new name of product\n> ').lower().strip()
                if product_new_name in products:
                    print('\nThis name already exits in your list\n')
                else:
                    products[product_index] = product_new_name
                    print(f'\n{product_old_name} has been replaced with {product_new_name}\n')
            except:
                print('\nPLease enter valid input\n')
        else:
            print('\nYou do not have any products to update\n')
    # allows user to delete a product from the list
    elif option == '4':
        if products != []:
            product_list_index(products)
            try:
                product_index = int(input('Enter index of product you would like to remove\n> ').strip())
                product_name = products[product_index]
                products.pop(product_index)
                print(f'\n{product_name} has been removed from your products\n')
            except:
                print('\nYou have not entered a valid index\n')
        else:
            print('\nYou do not have any products to delete\n')
    # allows user to go back to previous menu
    elif option == '0':
        return False
    # handles if user does not input a valid entry
    else:
        print('\nPlease enter a valid input\n')

    # keeps the loop running
    return True

def order_menu_func(orders,status_list):
    option = input(order_menu_text).strip()
    if option == '1':
        orders_list_index(orders)

    elif option == '2':
        name = input('Enter customer name\n> ')
        address = input('Enter customer address\n> ')
        phone_no = input('Enter customer phone number\n>')
        status = 'PREPARING'
        new_order = {
            "customer_name": name,
            "customer_address": address,
            "customer_phone": phone_no,
            "status": status
        }
        orders.append(new_order)
    elif option == '3':
        orders_list_index(orders)
        order_to_update = int(input('Enter the index of the order status you would like to update\n> '))
        status_list_index(status_list)
        status_index = int(input('Enter the index of the status you would like to update to\n> '))
        orders[order_to_update]["status"] = status_list[status_index]
    elif option == '4':
        orders_list_index(orders)
        order_to_update = int(input('Enter the index of the order status you would like to update\n> '))
        for key,value in orders[order_to_update].items():
            if key == "status":
                continue
            yes_or_no = input(f'Do you want to update the {key} from {value}? (y/n)\n> ')
            if yes_or_no == 'y':
                new_value = input('Enter new value\n> ')
                orders[order_to_update][key] = new_value
            else:
                continue

    elif option == '0':
        return False
    else:
        print('\nPlease enter a valid input\n')

    return True
    
# main loop
while run:
    clear_screen()
    to_continue = input(first_menu_text).strip()
    if to_continue == '0':
        run = False
    elif to_continue == '1':
        product_menu = True
        clear_screen()
    elif to_continue == '2':
        order_menu = True
        clear_screen()
    else:
        print('\nPlease enter 0, 1 or 2!\n')
    # runs production menu function
    while product_menu:
        cont = product_menu_func(products)
        if not(cont):
            product_menu = False
    while order_menu:
        cont = order_menu_func(orders,status_list)
        if not(cont):
            order_menu = False

# hello