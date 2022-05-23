# imports
import json
import all_functions
# this is how you get current time time.asctime( time.localtime(time.time()) )
# setting up inital variables
try:
    with open('products.json') as product_file:
        products = json.load(product_file)
except:
    products = []
try:
    with open('orders.json','r') as file:
        orders = json.load(file)
except:
    orders = []

try:
    with open('couriers.json') as couriers_file:
        couriers = json.load(couriers_file)
except:
    couriers = []

run = True

product_menu = False
order_menu = False
courier_menu = False


# setting up menu texts that will show up on screen
first_menu_text = '''\nWelcome to Gray's Cafe!\n
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
order_menu_text = '''Enter 1 to view orders
Enter 2 to create a new order
Enter 3 to update an existing order status
Enter 4 to update an existing order
Enter 5 to delete an order
Enter 0 to return to main menu
> '''
courier_menu_text= '''Enter 1 to view courier list
Enter 2 to create a new courier
Enter 3 to update current courier
Enter 4 to delete a courier
Enter 0 to return to main menu 
'''

status_list = ['PREPARING','QUALITY CHECK','OUT FOR DELIVERY','DELIVERED']
# function that prints out product list with corresponding index

    
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
        cont, products = all_functions.product_menu_func(products,product_menu_text)
        if not(cont):
            product_menu = False
    while order_menu:
        cont,orders,couriers = all_functions.order_menu_func(orders,status_list,couriers,order_menu_text)
        if not(cont):
            order_menu = False
    while courier_menu:
        cont,couriers,orders = all_functions.courier_menu_func(couriers,orders,courier_menu_text)
        if not(cont):
            courier_menu = False

with open('orders.json',mode='w') as file:
    to_file = json.dumps(orders,indent='    ')
    file.write(to_file)

with open('products.json',mode='w') as product_file:
    to_file = json.dumps(products)
    product_file.write(to_file)

with open('couriers.json',mode='w') as couriers_file:
    to_file = json.dumps(couriers)
    couriers_file.write(to_file)