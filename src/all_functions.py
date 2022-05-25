# imports
import os
import time

# clearing the terminal function


def clear_screen():
    os.system('clear')


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


def update_products(products):
    clear_screen()
    if products != []:
        product_list_index(products)
        try:
            product_index = int(
                input('Enter index of product you would like to update\n> ').strip())
            product_old_name = products[product_index]
            product_new_name = input(
                '\nEnter new name of product\n> ').lower().strip()
            if product_new_name in products:
                print('\nThis name already exits in your list\n')
            else:
                products[product_index] = product_new_name
                print(
                    f'\n{product_old_name} has been replaced with {product_new_name}\n')
            input('Press enter to continue')
        except:
            print('\nPLease enter valid input\n')
            input('Press enter to continue')
    else:
        print('\nYou do not have any products to update\n')
        input('Press enter to continue')

    return products


def delete_products(products):
    clear_screen()
    if products != []:
        product_list_index(products)
        try:
            product_index = int(
                input('Enter index of product you would like to remove\n> ').strip())
            product_name = products[product_index]
            products.pop(product_index)
            print(f'\n{product_name} has been removed from your products\n')
        except:
            print('\nYou have not entered a valid index\n')
    else:
        print('\nYou do not have any products to delete\n')
    input('Press enter to continue')

    return products


def add_products(products):
    clear_screen()
    product = input(
        'Enter the name of the product you would like to add\n> ').lower().strip()
    if product in products:
        print(f'\nThis product already exists in your list\n')
    elif product == ''.strip():
        print(f'\nYou have not entered a valid input\n')
    else:
        products.append(product)
        print(f'\nYou have added {product} to your products\n')
    input('Press enter to continue')

    return products


def view_products(products):
    clear_screen()
    if products == []:
        print('There are no products in your list!\n')
    else:
        product_list_index(products)
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
                name = input('Enter customer name\n> ')
                address = input('\nEnter customer address\n> ')
                phone_no = input('\nEnter customer phone number\n> ')
                if len(phone_no) < 10:
                    print('\nYour phone number must be at least 10 digits long\n')
                    3/0
                status = 'PREPARING'
                new_order = {
                    "customer_name": name,
                    "customer_address": address,
                    "customer_phone": phone_no,
                    "courier index": courier_index,
                    "status": status,
                    "order-time": time.asctime(time.localtime(time.time()))
                }
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
            orders[order_to_update]["status"] = status_list[status_index]
        except:
            print('\nYou have not entered a valid input\n')

    else:
        print('You do not have any orders in your order list\n')
    input('Press enter to continue')

    return orders


def update_order(orders):
    clear_screen()
    if orders != []:
        orders_list_index(orders)
        try:
            order_to_update = int(
                input('Enter the index of the order status you would like to update\n> '))
            for key, value in orders[order_to_update].items():
                if key == "status" or key == "order-time":
                    continue
                yes_or_no = input(
                    f'Do you want to update the {key} from {value}? (y/n)\n> ')
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

# function that handles the product menu


def product_menu_func(products, product_menu_text):
    clear_screen()
    option = input(product_menu_text).strip()
    # prints product list
    if option == '1':
        view_products(products)
    # allows user to add a product to the list
    elif option == '2':
        products = add_products(products)
    # allows user to update the name of a product in the list
    elif option == '3':
        products = update_products(products)
    # allows user to delete a product from the list
    elif option == '4':
        products = delete_products(products)
    # allows user to go back to previous menu
    elif option == '0':
        return False, products

    # keeps the loop running
    return True, products


def courier_menu_func(couriers, orders, courier_menu_text):
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
        courier = input(
            'Enter the name of the courier you would like to add\n> ').lower().strip()
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
                courier_index = int(
                    input('Enter index of courier you would like to update\n> ').strip())
                courier_old_name = couriers[courier_index]
                courier_new_name = input(
                    '\nEnter new name of courier\n> ').lower().strip()
                if courier_new_name in couriers:
                    print('\nThis name already exits in your list\n')
                else:
                    couriers[courier_index] = courier_new_name
                    print(
                        f'\n{courier_old_name} has been replaced with {courier_new_name}\n')
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
                courier_index = int(
                    input('Enter index of courier you would like to remove\n> ').strip())
                clear_screen()
                courier_order = []
                for i in range(len(orders)):
                    if orders[i]["courier index"] == courier_index:
                        courier_order.append(i)
                    elif orders[i]["courier index"] > courier_index:
                        orders[i]["courier index"] -= 1

                while True:
                    choice = input(f'''This courier is currently active in {len(courier_order)} orders

Therefore please pick what you would like to do:

Enter 1 to delete the courier and delete all orders associated with it

Enter 2 to delete the courier and change the courier of all the associated couriers

Enter 3 to not delete the courier
> ''')

                    if choice == '1':
                        clear_screen()
                        courier_name = couriers[courier_index]
                        couriers.pop(courier_index)
                        print(
                            f'\n{courier_name} has been removed from your couriers\n')
                        for i in courier_order[::-1]:
                            orders.pop(i)
                        break
                    elif choice == '2':
                        clear_screen()
                        courier_name = couriers[courier_index]
                        couriers.pop(courier_index)
                        print(
                            f'\n{courier_name} has been removed from your couriers\n')
                        for i in courier_order:
                            print(f'order to change: {orders[i]}')
                            couriers_list_index(couriers)
                            cour = int(
                                input('\nWhich courier index would you like to switch to\n> '))
                            orders[i]["courier index"] = cour
                            clear_screen()
                        break

                    elif choice == '3':
                        for i in range(len(orders)):
                            if orders[i]["courier index"] > courier_index:
                                orders[i]["courier index"] += 1
                        break

            except:
                print('\nYou have not entered a valid index\n')
        else:
            print('\nYou do not have any couriers to delete\n')
        input('Press enter to continue')
    # allows user to go back to previous menu
    elif option == '0':
        return False, couriers, orders

    # keeps the loop running
    return True, couriers, orders


def order_menu_func(orders, status_list, couriers, order_menu_text):
    clear_screen()
    option = input(order_menu_text).strip()
    if option == '1':
        view_orders(orders)
    elif option == '2':
        orders = add_orders(orders, couriers)
    elif option == '3':
        orders = update_order_status(orders, status_list)
    elif option == '4':
        orders = update_order(orders)
    elif option == '5':
        orders = delete_order(orders)
    elif option == '0':
        return False, orders, couriers

    return True, orders, couriers
