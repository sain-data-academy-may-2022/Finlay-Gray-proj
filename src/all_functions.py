# imports
import os
import time
import database
from tabulate import tabulate


# clearing the terminal function


def clear_screen():
    os.system('clear')

# all lost index functions print list with index to screen


class Product:
    def __init__(self, id:int, price, quantity, name):
        self.id = id
        self.price = price
        self.quantity = quantity
        self.name = name

    def price_change(self, new_price):
        self.price = new_price

    def quantity_subtract(self, to_take_off):
        self.quantity -= to_take_off

    def quantity_add(self, to_add):
        self.quantity += to_add

    def name_change(self, new_name):
        self.name = new_name

    def can_order(self, no_to_order):
        if self.quantity > 0 and self.quantity > no_to_order:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f'Product name: {self.name}\nPrice: £{self.price}\nQuantity: {self.quantity}\n'

class OrderProducts:
    pass


class Orders:
    def __init__(self, id:int, name, address, phone_num, status, order_time, courier_index, products_list):
        self.id = id
        self.name = name
        self.address = address
        self.phone_num = phone_num
        self.status = status
        self.order_time = order_time
        self.courier_index = int(courier_index)
        self.products_list = products_list

    def __repr__(self) -> str:
        return f'Order name: {self.name}\nAddress: {self.address}\nPhone_number: {self.phone_num}\nStatus: {self.status}\nOrder time: {self.order_time}\nCourier index: {self.courier_index}\nProducts in order: {self.products_list}\n'

    def __eq__(self, other):
        if (isinstance(other, Product)):
            return self.number == other.number and self.letter == other.letter
        return False


class Couriers:
    def __init__(self, id:int, name, phone, delivery):
        self.id = id
        self.name = name
        self.phone = phone
        self.delivery = delivery

    def name_change(self, new_name):
        self.name = new_name

    # each service has an order capacity
    # each servvice has a vehicle
    # each service has a average delivery time


def print_list(table,con):
    
    cur = database.get_cursor(con)
    database.sql_statement(cur,f'''SELECT * FROM {table}''')
    items = cur.fetchall()
    field_names = [i[0] for i in cur.description]
    print(tabulate(items, headers=field_names, tablefmt='psql'))
    database.close_cursor(cur)
    # for i in range(len(list)):
    #     print(
    #         f'Product name: {list[i].name}\nPrice: £{list[i].price}\nQuantity: {list[i].quantity}\n')


def orders_list_index(list):
    for i in range(len(list)):
        print(f'Order name: {list[i].name}\nAddress: {list[i].address}\nPhone_number: {list[i].phone_num}\nStatus: {list[i].status}\nOrder time: {list[i].order_time}\nCourier index: {list[i].courier_index}\nProducts in order: {list[i].products_list}\nIndex value: {i}\n')


def status_list_index(list):
    for i in range(len(list)):
        print(f'Status: {list[i]}\nIndex value: {i}\n')


def couriers_list_index(list):
    for i in range(len(list)):
        print(
            f'Courier name: {list[i].name}\nCourier phone number: {list[i].phone}\nCourier vehicle: {list[i].delivery}\nIndex value: {i}\n')


def update_products(con, prod_update_menu_text):
    clear_screen()
    cur = database.get_cursor(con)
    is_empty = database.check_if_table_empty(cur,'Product')
    if not is_empty:
        try:
            clear_screen()
            print_list('Product',con)
            product_id = int(
                        input('Enter The id of product you would like to update\n> ').strip())
            database.sql_statement(cur,f'''SELECT * FROM Product WHERE id = {product_id}''')
            new_prod = cur.fetchone()
            prod_class = Product(new_prod[0],new_prod[2],new_prod[3],new_prod[1])
            while True:
                clear_screen()
                choice = input(prod_update_menu_text)
                if choice == '0':
                    database.sql_statement(cur,f'''UPDATE Product SET name = '{prod_class.name}', price = {float(prod_class.price)}, quantity = {prod_class.quantity} WHERE id = {product_id}''')
                    con.commit()
                    break
                elif choice == '1':
                    clear_screen()
                    print(prod_class)
                    try:
                        product_old_name = prod_class.name
                        product_new_name = input(
                            '\nEnter new name of product\n> ').lower().strip()
                        # if product_new_name in products.name:
                        #     print('\nThis name already exits in your list\n')
                        # else:
                        prod_class.name_change(product_new_name)
                        print(
                            f'\n{product_old_name} has been replaced with {product_new_name}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')

                elif choice == '2':
                    clear_screen()
                    print(prod_class)
                    try:
                        product_new_price = input(
                            '\nEnter new price of product\n> ').lower().strip()
                        prod_class.price_change(product_new_price)
                        print(
                            f'\nThe price of {prod_class.name} has been replaced with £{product_new_price}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')

                elif choice == '3':
                    clear_screen()
                    print(prod_class)
                    try:
                        quantity_to_add = int(input(
                            '\nEnter how much you would like to increase the quantity by\n> ').lower().strip())
                        prod_class.quantity_add(quantity_to_add)
                        print(
                            f'\nThe quantity of {prod_class.name} has been increased by {quantity_to_add} to become {prod_class.quantity}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')

                elif choice == '4':
                    clear_screen()
                    print(prod_class)
                    try:
                        quantity_to_sub = int(input(
                            '\nEnter how much you would like to decrease the quantity by\n> ').lower().strip())
                        prod_class.quantity_subtract(quantity_to_sub)
                        print(
                            f'\nThe quantity of {prod_class.name} has been decreased by {quantity_to_sub} to become {prod_class.quantity}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')

        except:
            print('\nYou have not entered a valid input\n')
            input('Press enter to continue')


    else:
        print('\nYou do not have any products to update\n')
        input('Press enter to continue')

    database.close_cursor(cur)


def delete_products(con):
    cur = database.get_cursor(con)
    clear_screen()
    print_list('Product',con)
    id_to_del = int(input('Enter the id of the product you would like to delete\n> ').strip())
    database.sql_statement(cur,f'''DELETE FROM Product WHERE id = {id_to_del}''')
    con.commit
    database.close_cursor(cur)


def add_products(con):
    cur = database.get_cursor(con)
    clear_screen()
    product_name = input(
        'Enter the name of the product you would like to add\n> ').lower().strip()
    product_price = float(
        input('Enter the price of this product\n> ').lower().strip())
    product_quantity = int(
        input('Enter the quantity of this product you have\n> ').strip())
    # if products != []:
    #     for product in products:
    #         if product_name == product.name:
    #             print(f'\nThis product already exists in your list\n')
    #             input('Press enter to continue')
    #             return products
    #             break
    if product_name == ''.strip():
        print(f'\nYou have not entered a valid input\n')
    else:
        database.sql_statement(cur,f'''INSERT INTO Product (name,price,quantity) VALUES ('{product_name}',{product_price},{product_quantity})''')
        con.commit()
        print(f'\nYou have added {product_name} to your products\n')
    input('Press enter to continue')

    database.close_cursor(cur)
    


def view_products(con):
    clear_screen()
    print_list('Product', con)
    input('Press enter to continue')


def view_orders(orders):
    clear_screen()
    if orders == []:
        print('There are no orders in your list!\n')
    else:
        orders_list_index(orders)
    input('Press enter to continue')


def add_orders(orders, couriers):
    clear_screen()
    try:
        if couriers != []:
            couriers_list_index(couriers)
            courier_index = int(
                input('Enter the index of the courier for this order\n> '))
            try:
                a = couriers[courier_index]
                clear_screen()
                name = input('Enter customer name\n> ')
                address = input('\nEnter customer address\n> ')
                phone_no = input('\nEnter customer phone number\n> ')
                if len(phone_no) < 10:
                    clear_screen()
                    print('\nYour phone number must be at least 10 digits long\n')
                    3/0
                status = 'PREPARING'
                new_order = Orders(name, address, phone_no, status, time.asctime(
                    time.localtime(time.time())), courier_index, [])

                orders.append(new_order)

            except:
                3/0
        else:
            print(
                'You have no avalible couriers and therefore can not create an order\n')
            input('Press enter to continue')
    except:
        print('\nYou have not entered a valid input\n')
        input('Press enter to continue')

    return orders


def update_order_status(orders, status_list):
    clear_screen()
    if orders != []:
        orders_list_index(orders)
        try:
            order_to_update = int(
                input('Enter the index of the order status you would like to update\n> '))
            clear_screen()
            status_list_index(status_list)
            status_index = int(
                input('Enter the index of the status you would like to update to\n> '))
            orders[order_to_update].status = status_list[status_index]
        except:
            print('\nYou have not entered a valid input\n')

    else:
        print('You do not have any orders in your order list\n')
    input('Press enter to continue')

    return orders


def update_order(orders, couriers):
    clear_screen()
    if orders != []:
        orders_list_index(orders)
        try:
            order_to_update = int(
                input('Enter the index of the order you would like to update\n> '))
            clear_screen()
            for attribute in vars(orders[order_to_update]):
                if attribute == "status" or attribute == "order_time" or attribute == "products_list":
                    continue
                yes_or_no = input(
                    f'Do you want to update the {attribute} from {getattr(orders[order_to_update],attribute)}? (y/n)\n> ').strip().lower()
                if attribute == "courier_index" and yes_or_no == 'y':
                    clear_screen()
                    couriers_list_index(couriers)
                    index = int(
                        input('\nEnter the index of the new courier\n> '))
                    setattr(orders[order_to_update], attribute, index)
                    continue
                elif yes_or_no == 'y':
                    new_value = input('Enter new value\n> ')
                    setattr(orders[order_to_update], attribute, new_value)
                else:
                    continue
        except:
            print('\nYou have not entered a valid input\n')
    else:
        print('You do not have any orders in your order list\n')
    input('Press enter to continue')
    return orders


def add_prod_to_order(orders, products):
    clear_screen()
    if orders != []:
        orders_list_index(orders)
        try:
            order_to_add_to = int(
                input('Enter the index of the order you would like to add a product to\n> '))
            while True:
                clear_screen()
                to_cont = input(
                    'Do you want to add another product? (y/n) > ').strip().lower()
                if to_cont == 'n':
                    break
                else:
                    clear_screen()
                    product_list_index(products)
                    product_index = int(
                        input('Enter the index of the product you would like to add\n> '))
                    quant = int(
                        input('Enter the quantity of the product you want to add\n> '))
                    orders[order_to_add_to].products_list.append(
                        Product(products[product_index].price, quant, products[product_index].name))

        except:
            print('\nYou have not entered a valid input\n')

    return orders


def rem_prod_to_order(orders):
    clear_screen()
    if orders != []:
        orders_list_index(orders)
    try:
        order_to_add_to = int(
            input('Enter the index of the order you would like to delete a product from\n> '))
        for i in range(len(orders[order_to_add_to].products_list)):
            print(
                f'Product name: {orders[order_to_add_to].products_list[i].name}\tIndex: {i}')
        to_del = int(input('Enter index of product you want to remove\n> '))
        orders[order_to_add_to].product_list.pop(to_del)
    except:
        print('\nYou have not entered a valid input\n')
        input('Press enter to continue')

    return orders


def delete_order(orders):
    clear_screen()
    if orders != []:
        orders_list_index(orders)
        try:
            to_delete = int(
                input('Enter the index of the order you would like to delete\n> '))
            orders.pop(to_delete)
        except:
            print('\nYou have not entered a valid input\n')
    else:
        print('You do not have any orders in your order list\n')
    input('Press enter to continue')
    return orders


def view_courier(couriers):
    clear_screen()
    if couriers == []:
        print('There are no couriers in your list!\n')
    else:
        couriers_list_index(couriers)
    input('Press enter to continue')


def add_courier(couriers):
    clear_screen()
    courier_name = input(
        'Enter the name of the courier you would like to add\n> ').lower().strip()
    courier_phone = input('Enter the phone number of your courier\n> ')
    courier_vehicle = input('Enter the vehicle your courier uses\n> ')
    new_courier = Couriers(courier_name, courier_phone, courier_vehicle)
    couriers.append(new_courier)
    print(f'\nYou have added {courier_name} to your couriers\n')
    input('Press enter to continue')

    return couriers


def update_courier(couriers):
    clear_screen()
    if couriers != []:
        couriers_list_index(couriers)
        try:
            courier_to_update = int(
                input('Enter the index of the courier you would like to update\n> '))
            clear_screen()
            for attribute in vars(couriers[courier_to_update]):
                yes_or_no = input(
                    f'Do you want to update the {attribute} from {getattr(couriers[courier_to_update],attribute)}? (y/n)\n> ').strip().lower()
                if yes_or_no == 'y':
                    new_value = input('Enter new value\n> ')
                    setattr(couriers[courier_to_update], attribute, new_value)
                else:
                    continue
        except:
            print('\nYou have not entered a valid input\n')
    else:
        print('You do not have any couriers in your order list\n')
    input('Press enter to continue')
    return couriers


def delete_courier(couriers, orders):
    clear_screen()
    if couriers != []:
        couriers_list_index(couriers)
        try:
            courier_index = int(
                input('Enter index of courier you would like to remove\n> ').strip())
            clear_screen()
            courier_order = []
            for i in range(len(orders)):
                if orders[i].courier_index == courier_index:
                    courier_order.append(i)
                elif orders[i].courier_index > courier_index:
                    orders[i].courier_index -= 1

            while True:
                choice = input(f'''This courier is currently active in {len(courier_order)} orders

Therefore please pick what you would like to do:

Enter 1 to delete the courier and delete all orders associated with it

Enter 2 to delete the courier and change the courier of all the associated couriers

Enter 3 to not delete the courier
> ''')

                if choice == '1':
                    clear_screen()
                    courier_name = couriers[courier_index].name
                    couriers.pop(courier_index)
                    print(
                        f'\n{courier_name} has been removed from your couriers\n')
                    for i in courier_order[::-1]:
                        orders.pop(i)
                    break
                elif choice == '2':
                    clear_screen()
                    courier_name = couriers[courier_index].name
                    couriers.pop(courier_index)
                    print(
                        f'\n{courier_name} has been removed from your couriers\n')
                    for i in courier_order:
                        print(f'order to change:\n {repr(orders[i])}')
                        couriers_list_index(couriers)
                        cour = int(
                            input('\nWhich courier index would you like to switch to\n> '))
                        orders[i].courier_index = cour
                        clear_screen()
                    break

                elif choice == '3':
                    for i in range(len(orders)):
                        if orders[i].courier_index >= courier_index:
                            orders[i].courier_index += 1
                    break

        except:
            print('\nYou have not entered a valid index\n')
    else:
        print('\nYou do not have any couriers to delete\n')
    input('Press enter to continue')
    return couriers, orders


# function that handles the product menu


def product_menu_func(con,product_menu_text, prod_update_menu_text):
    clear_screen()
    option = input(product_menu_text).strip()
    # prints product list
    if option == '1':
        view_products(con)
    # allows user to add a product to the list
    elif option == '2':
        add_products(con)
    # allows user to update the name of a product in the list
    elif option == '3':
        update_products(con,prod_update_menu_text)
    # allows user to delete a product from the list
    elif option == '4':
        delete_products(con)
    # allows user to go back to previous menu
    elif option == '0':
        return False

    # keeps the loop running
    return True


def courier_menu_func(couriers, orders, courier_menu_text):
    clear_screen()
    option = input(courier_menu_text).strip()
    # prints courier list
    if option == '1':
        view_courier(couriers)
    # allows user to add a courier to the list
    elif option == '2':
        couriers = add_courier(couriers)
    # allows user to update the name of a courier in the list
    elif option == '3':
        couriers = update_courier(couriers)
    # allows user to delete a courier from the list
    elif option == '4':
        couriers, orders = delete_courier(couriers, orders)
    # allows user to go back to previous menu
    elif option == '0':
        return False, couriers, orders

    # keeps the loop running
    return True, couriers, orders


def order_menu_func(orders, status_list, couriers, order_menu_text, products):
    clear_screen()
    option = input(order_menu_text).strip()
    if option == '1':
        view_orders(orders)
    elif option == '2':
        orders = add_orders(orders, couriers)
    elif option == '3':
        orders = update_order_status(orders, status_list)
    elif option == '4':
        orders = update_order(orders, couriers)
    elif option == '5':
        orders = add_prod_to_order(orders, products)
    elif option == '6':
        orders = rem_prod_to_order(orders)
    elif option == '7':
        orders = delete_order(orders)
    elif option == '0':
        return False, orders, couriers

    return True, orders, couriers
