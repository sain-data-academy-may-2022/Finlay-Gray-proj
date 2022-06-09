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
products = []
try:
    with open('products.json') as product_file:
        temp_products = json.load(product_file)
        for product in temp_products:
            products.append(all_functions.Product(
                product['price'], product['quantity'], product['name']))
except:
    products = []
orders = []
try:
    with open('orders.json') as order_file:
        temp_orders = json.load(order_file)
        for order in temp_orders:
            orders.append(all_functions.Orders(order['name'], order['address'], order['phone_num'],
                          order['status'], order['order_time'], order['courier_index'], order['products_list']))

        for order in orders:
            temp_products_list = []
            for prod in order.products_list:
                temp_products_list.append(all_functions.Product(
                    prod['price'], prod['quantity'], prod['name']))

            order.products_list = temp_products_list


except:
    orders = []

couriers = []
try:
    with open('couriers.json') as courier_file:
        temp_couriers = json.load(courier_file)
        for courier in temp_couriers:
            couriers.append(all_functions.Couriers(
                courier['name'], courier['phone'], courier['delivery']))
except:
    couriers = []

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
prod_update_menu_text = '''Enter 1 to update a products name
Enter 2 to update a products price
Enter 3 to add to a products quantity
Enter 4 to subtract from a products quantity
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

con = database.get_connection()

# main loop
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
        cont, orders, couriers = Ordersfile.order_menu_func(con,
            orders, status_list, couriers, order_menu_text, products)
        if not(cont):
            order_menu = False
    while courier_menu:
        cont, orders = Couriersfile.courier_menu_func(con,
             orders, courier_menu_text,courier_update_menu_text)
        if not(cont):
            courier_menu = False


database.close_connection(con)


def create_json(file_path, list):
    with open(file_path, "w") as file:
        json.dump([ob.__dict__ for ob in list], file)


create_json('products.json', products)

for order in orders:
    order.products_list = [ob.__dict__ for ob in order.products_list]

create_json('orders.json', orders)

create_json('couriers.json', couriers)
