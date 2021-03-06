# TO DO
# imports
import os
import time
import json
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

def clear_screen():
    os.system('clear')


# setting up inital variables


# setting up menu texts that will show up on screen
update_menu_text = '''Enter 1 to update a products name
Enter 2 to update a products price
Enter 3 to add to a products quantity
Enter 4 to subtract from a products quantity
Enter 0 to return to main menu
> '''

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

def product_list_index(list):
    for i in range(len(list)):
        print(f'Product name: {list[i]}\nIndex value: {i}\n')

def orders_list_index(list):
    for i in range(len(list)):
        print(f'Order: {list[i]}\nIndex value: {i}\n')

def status_list_index(list):
    for i in range(len(list)):
        print(f'Status: {list[i]}\nIndex value: {i}\n')

def couriers_list_index(list):
    for i in range(len(list)):
        print(f'Courier: {list[i]}\nIndex value: {i}\n')


class product_class:
    def __init__(self,price,quantity,name):
        self.price = price 
        self.quantity = quantity
        self.name = name

    
    def price_change(self,new_price):
        self.price = new_price

    def quantity_subtract(self,to_take_off):
        self.quantity -= to_take_off

    def quantity_add(self,to_add):
        self.quantity += to_add
    
    def name_change(self,new_name):
        self.name = new_name
        
    
    def can_order(self,no_to_order):
        if self.quantity > 0 and self.quantity > no_to_order:
            return True
        else:
            return False

class order_class:
    def __init__(self,name,address,phone_number,courier_index,status,order_time):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.courier_index = courier_index
        self.status = status 
        self.order_time = order_time


    def update_name(self):
        yes_or_no = input(f'Do you want to update the name from {self.name}? (y/n)\n> ')
        if yes_or_no == 'y':
            new_value = input('Enter new value\n> ')
            self.name = new_value
        
    def update_address(self):
        yes_or_no = input(f'Do you want to update the address from {self.address}? (y/n)\n> ')
        if yes_or_no == 'y':
            new_value = input('Enter new value\n> ')
            self.address = new_value

    def update_phone_number(self):
        yes_or_no = input(f'Do you want to update the phone number from {self.phone_number}? (y/n)\n> ')
        if yes_or_no == 'y':
            new_value = input('Enter new value\n> ')
            self.phone_number = new_value

    # def update_courier_index(self,co):
    # yes_or_no = input(f'Do you want to update the name from {self.name}? (y/n)\n> ')
    # if yes_or_no == 'y':
    #     new_value = input('Enter new value\n> ')
    #     self.name = new_value

    def update_status(self,status_list):
        yes_or_no = input(f'Do you want to update the status from {self.status}? (y/n)\n> ')
        if yes_or_no == 'y':
            status_list_index(status_list)
            new_value = int(input('Enter new value\n> '))
            self.name = new_value
       




# function that prints out product list with corresponding index

# function that handles the product menu
def product_menu_func(products):
    option = input(product_menu_text).strip()
    # prints product list
    if option == '1':
        product_list_index(products)
    # allows user to add a product to the list
    elif option == '2':
        product = input('Enter the name of the product you would like to add\n> ').lower().strip()
        product_price = float(input('Enter the price of this product\n> ').lower().strip())
        product_quantity = int(input('Enter the quantity of this product you have\n> ').strip())
        if product in products:
            print(f'\nThis product already exists in your list\n')
        else:
            new_product = product_class(product_price,product_quantity,product)
            products.append(new_product)
            print(f'\nYou have added {product} to your products\n')
    # allows user to update the name of a product in the list
    elif option == '3':
        if products != []:
            choice = input(update_menu_text).lower().strip()
            if choice == '1':
                product_list_index(products)
                # try:
                product_index = int(input('Enter index of product you would like to update\n> ').strip())
                product_old_name = products[product_index].name
                product_new_name = input('\nEnter new name of product\n> ').lower().strip()
                same = False
                for i in range(len(products)):
                    if products[i].name == product_new_name:
                        same = True
                if same:
                    print('\nThis name already exits in your list\n')
                else:
                    products[product_index].name_change(product_new_name)
                    print(f'\n{product_old_name} has been replaced with {product_new_name}\n')
                        
                # except:
                        # print('\nPLease enter valid input\n')
                
            if choice == '2':
                pass
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
    


def courier_menu_func(couriers,orders):
    clear_screen()
    option = input(courier_menu_text).strip()
    # prints courier list
    if option == '1':
        clear_screen()
        if couriers == []:
            print('There are no couriers in your list!\n')
        else:
            couriers_list_index(couriers)
        input('Press enter to continue')
    # allows user to add a courier to the list
    elif option == '2':
        clear_screen()
        courier = input('Enter the name of the courier you would like to add\n> ').lower().strip()
        if courier in couriers:
            print(f'\nThis courier already exists in your list\n')
        else:
            couriers.append(courier)
            print(f'\nYou have added {courier} to your couriers\n')
        input('Press enter to continue')
    # allows user to update the name of a courier in the list
    elif option == '3':
        clear_screen()
        if couriers != []:
            couriers_list_index(couriers)
            try:
                courier_index = int(input('Enter index of courier you would like to update\n> ').strip())
                courier_old_name = couriers[courier_index]
                courier_new_name = input('\nEnter new name of courier\n> ').lower().strip()
                if courier_new_name in couriers:
                    print('\nThis name already exits in your list\n')
                else:
                    couriers[courier_index] = courier_new_name
                    print(f'\n{courier_old_name} has been replaced with {courier_new_name}\n')
                input('Press enter to continue')
            except:
                print('\nPLease enter valid input\n')
                input('Press enter to continue')
        else:
            print('\nYou do not have any couriers to update\n')
            input('Press enter to continue')
    # allows user to delete a courier from the list
    elif option == '4':
        clear_screen()
        if couriers != []:
            couriers_list_index(couriers)
            try:
                courier_index = int(input('Enter index of courier you would like to remove\n> ').strip())
                clear_screen()
                courier_order = []
                for i in range(len(orders)):
                    if orders[i]["courier index"] == courier_index:
                        courier_order.append(i)
                print(f'this is the courier order list {courier_order}')
                while True:
                    choice = input(f'''This courier is currently active in {len(courier_order)} orders

Therefore please pick what you would like to do:

Enter 1 to delete the courier and delete all orders associated with it

Enter 2 to delete the courier and change the courier of all the associated couriers

Enter 3 to not delete the courier
> ''')

                    # IMPORTANT
                    # the order list is updating so I AM DELETING THE WRONG INDEXES AFTER THE FIRST ONW.
                    # now need to fix the other indexes from unrelated orders if removed courier is bedore 
                    # step through see if index greater then removed index and if so minus 1
                    if choice == '1':
                        clear_screen()
                        courier_name = couriers[courier_index]
                        couriers.pop(courier_index)
                        print(f'\n{courier_name} has been removed from your couriers\n')
                        for i in courier_order[::-1]:
                            orders.pop(i)
                        break
                    elif choice =='2':
                        clear_screen()
                        courier_name = couriers[courier_index]
                        couriers.pop(courier_index)
                        print(f'\n{courier_name} has been removed from your couriers\n')
                        for i in courier_order:
                            print(f'order to change: {orders[i]}')
                            couriers_list_index(couriers)
                            cour = int(input('\nWhich courier index would you like to switch to\n> '))
                            orders[i]["courier index"] = cour
                            clear_screen()
                        break

                    elif choice =='3':
                        break


                    
                
            except:
                print('\nYou have not entered a valid index\n')
        else:
            print('\nYou do not have any couriers to delete\n')
        input('Press enter to continue')
    # allows user to go back to previous menu
    elif option == '0':
        return False

    # keeps the loop running
    return True











def order_menu_func(orders,status_list,couriers):
    clear_screen()
    option = input(order_menu_text).strip()
    if option == '1':
        clear_screen()
        if orders == []:
            print('There are no orders in your list!\n')
        else:
            orders_list_index(orders)
        input('Press enter to continue')
    elif option == '2':
        clear_screen()
        try:
            if couriers != []:
                couriers_list_index(couriers)
                courier_index = int(input('Enter the index of the courier for this order\n> '))
                name = input('Enter customer name\n> ')
                address = input('\nEnter customer address\n> ')
                phone_no = input('\nEnter customer phone number\n> ')
                status = 'PREPARING'
                new_order = {
                    "customer_name": name,
                    "customer_address": address,
                    "customer_phone": phone_no,
                    "courier index": courier_index,
                    "status": status,
                    "order-time":time.asctime( time.localtime(time.time()) )
                }
                orders.append(new_order)
            else:
                print('You have no avalible couriers and therefore can not create an order\n')
                input('Press enter to continue')
        except:
            print('\nYou have not entered a valid input\n')
            input('Press enter to continue')
    elif option == '3':
        clear_screen()
        if orders != []:
            orders_list_index(orders)
            try:
                order_to_update = int(input('Enter the index of the order status you would like to update\n> '))
                clear_screen()
                status_list_index(status_list)
                status_index = int(input('Enter the index of the status you would like to update to\n> '))
                orders[order_to_update]["status"] = status_list[status_index]
            except:
                print('\nYou have not entered a valid input\n')
                
        else:
            print('You do not have any orders in your order list\n')
        input('Press enter to continue')
    elif option == '4':
        clear_screen()
        if orders != []:
            orders_list_index(orders)
            try:
                order_to_update = int(input('Enter the index of the order status you would like to update\n> '))
                for key,value in orders[order_to_update].items():
                    if key == "status" or key == "order-time":
                        continue
                    yes_or_no = input(f'Do you want to update the {key} from {value}? (y/n)\n> ')
                    if yes_or_no == 'y':
                        new_value = input('Enter new value\n> ')
                        orders[order_to_update][key] = new_value
                    else:
                        continue
            except:
                print('\nYou have not entered a valid input\n')
        else:
            print('You do not have any orders in your order list\n')
        input('Press enter to continue')
    elif option == '5':
        clear_screen()
        if orders != []:
            orders_list_index(orders)
            try:
                to_delete = int(input('Enter the index of the order you would like to delete\n> '))
                orders.pop(to_delete)
            except:
                print('\nYou have not entered a valid input\n')
        else:
            print('You do not have any orders in your order list\n')
        input('Press enter to continue')

    elif option == '0':
        return False
    

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
        courier_menu = True
        clear_screen()
    elif to_continue == '3':
        order_menu = True
        clear_screen()
    # runs production menu function
    while product_menu:
        cont = product_menu_func(products)
        if not(cont):
            product_menu = False
    while order_menu:
        cont = order_menu_func(orders,status_list,couriers)
        if not(cont):
            order_menu = False
    while courier_menu:
        cont = courier_menu_func(couriers,orders)
        if not(cont):
            courier_menu = False

with open('orders.json',mode='w') as file:
    to_file = json.dumps(orders,indent='    ')
    file.write(to_file)

with open('products.json',mode='w') as product_file:
    json.dump(product_file,products)
    # product_file.write(to_file)

with open('couriers.json',mode='w') as couriers_file:
    to_file = json.dumps(couriers)
    couriers_file.write(to_file)






class basket:
    def __init__(self,items):
        self.items = items



        