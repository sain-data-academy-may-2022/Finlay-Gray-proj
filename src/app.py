# imports
import json
from math import prod
import all_functions
import database
import Productfile
import Couriersfile
import Ordersfile
# this is how you get current time time.asctime( time.localtime(time.time()) )
# setting up inital variables


run = True

product_menu = False
order_menu = False
courier_menu = False


# setting up menu texts that will show up on screen
first_menu_text = f'''\nWelcome to Gray's Cafe!\n
Enter 1 to view product menu
Enter 2 to view courier menu
Enter 3 to view order menu
Enter 0 to quit
> '''
product_menu_text = '''Enter 1 to view products list
Enter 2 to create a new product
Enter 3 to update current product
Enter 4 to delete a product
Enter 0 to return to main menu 
> '''
prod_update_menu_text = '''Enter 1 to update products name
Enter 2 to update products price
Enter 3 to add to products quantity
Enter 4 to subtract from products quantity
Enter 0 to return to main menu
> '''
order_menu_text = '''Enter 1 to view orders
Enter 2 to create a new order
Enter 3 to update an existing order status
Enter 4 to update an existing order
Enter 5 to add products to your order
Enter 6 to remove products from your order
Enter 7 to delete an order
Enter 0 to return to main menu
> '''
order_update_menu_text = '''Enter 1 to update name of order
Enter 2 to update address of order
Enter 3 to update phone number of order
Enter 4 to change the courier of order
Enter 0 to return to main menu
> '''
courier_menu_text = '''Enter 1 to view courier list
Enter 2 to create a new courier
Enter 3 to update current courier
Enter 4 to delete a courier
Enter 0 to return to main menu 
> '''
courier_update_menu_text = '''Enter 1 to courier's name
Enter 2 to update courier's phone number
Enter 3 to update courier's vehicle
Enter 0 to return to main menu
> '''
status_list = ['PREPARING', 'QUALITY CHECK', 'OUT FOR DELIVERY', 'DELIVERED']
# function that prints out product list with corresponding index

def main_loop(run,product_menu,order_menu,courier_menu):
    while run:
        all_functions.clear_screen()
        to_continue = input(first_menu_text).strip()
        if to_continue == '0':
            run = False
        elif to_continue == '1':
            product_menu = True
            all_functions.clear_screen()
        elif to_continue == '2':
            courier_menu = True
            all_functions.clear_screen()
        elif to_continue == '3':
            order_menu = True
            all_functions.clear_screen()
        # runs production menu function
        while product_menu:
            cont = Productfile.product_menu_func(con,
                product_menu_text, prod_update_menu_text)
            if not(cont):
                product_menu = False
        while order_menu:
            cont = Ordersfile.order_menu_func(con,order_update_menu_text,
                status_list,order_menu_text)
            if not(cont):
                order_menu = False
        while courier_menu:
            cont = Couriersfile.courier_menu_func(con,
                courier_menu_text,courier_update_menu_text)
            if not(cont):
                courier_menu = False




con = database.get_connection()


# main loop

main_loop(run,product_menu,order_menu,courier_menu)


database.close_connection(con)


