import all_functions
import database

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


def status_list_index(list):
    for i in range(len(list)):
        print(f'Status: {list[i]}\nIndex value: {i}\n')



def add_orders(con):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    try:
        is_empty = database.check_if_table_empty(cur,'Couriers')
        if not is_empty:
            all_functions.print_list('Couriers',con)
            courier_index = int(
                input('Enter the id of the courier for this order\n> '))
            try:
                all_functions.clear_screen()
                name = input('Enter customer name\n> ')
                address = input('\nEnter customer address\n> ')
                phone_no = input('\nEnter customer phone number\n> ')
                if len(phone_no) < 10:
                    all_functions.clear_screen()
                    print('\nYour phone number must be at least 10 digits long\n')
                    3/0
                status = 'PREPARING'
    

                database.sql_statement(cur,f'''INSERT INTO Orders (name,address,phone_num,status,order_time,courier_index) VALUES ('{name}','{address}','{phone_no}','{status}',now(),{courier_index})''')

                con.commit()

            except:
                3/0
        else:
            print(
                'You have no avalible couriers and therefore can not create an order\n')
            input('Press enter to continue')
    except:
        print('\nYou have not entered a valid input\n')
        input('Press enter to continue')

    database.close_cursor(cur)


def update_order_status(con, status_list):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    is_empty = database.check_if_table_empty(cur,'Orders')
    if not is_empty:
        all_functions.print_list('Orders',con)
        try:
            order_to_update = int(
                input('Enter the index of the order status you would like to update\n> '))
            all_functions.clear_screen()
            status_list_index(status_list)
            status_index = int(
                input('Enter the index of the status you would like to update to\n> '))
            database.sql_statement(cur,f'''UPDATE Orders SET status = '{status_list[status_index]}' WHERE id = {order_to_update}''')
            con.commit()
        except:
            print('\nYou have not entered a valid input\n')

    else:
        print('You do not have any orders in your order list\n')
    input('Press enter to continue')

    database.close_cursor(cur)

    


def update_order(orders, couriers):
    all_functions.clear_screen()
    if orders != []:
        orders_list_index(orders)
        try:
            order_to_update = int(
                input('Enter the index of the order you would like to update\n> '))
            all_functions.clear_screen()
            for attribute in vars(orders[order_to_update]):
                if attribute == "status" or attribute == "order_time" or attribute == "products_list":
                    continue
                yes_or_no = input(
                    f'Do you want to update the {attribute} from {getattr(orders[order_to_update],attribute)}? (y/n)\n> ').strip().lower()
                if attribute == "courier_index" and yes_or_no == 'y':
                    all_functions.clear_screen()
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
    all_functions.clear_screen()
    if orders != []:
        orders_list_index(orders)
        try:
            order_to_add_to = int(
                input('Enter the index of the order you would like to add a product to\n> '))
            while True:
                all_functions.clear_screen()
                to_cont = input(
                    'Do you want to add another product? (y/n) > ').strip().lower()
                if to_cont == 'n':
                    break
                else:
                    all_functions.clear_screen()
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
    all_functions.clear_screen()
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


def delete_order(con):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    is_empty = database.check_if_table_empty(cur,'Orders')
    if not is_empty:
        all_functions.print_list('Orders',con)
        id_to_del = int(input('Enter the id of the order you would like to delete\n> ').strip())
        database.sql_statement(cur,f'''DELETE FROM Orders WHERE id = {id_to_del}''')
        con.commit
    
    else:
        print('You do not have any orders in your order list\n')
    input('Press enter to continue')
    database.close_cursor(cur)





def view_orders(con):
    all_functions.clear_screen()
    all_functions.print_list('Orders', con)
    input('Press enter to continue')




def order_menu_func(con,orders, status_list, couriers, order_menu_text, products):
    all_functions.clear_screen()
    option = input(order_menu_text).strip()
    if option == '1':
        view_orders(con)
    elif option == '2':
        add_orders(con)
    elif option == '3':
        update_order_status(con, status_list)
    elif option == '4':
        orders = update_order(orders, couriers)
    elif option == '5':
        orders = add_prod_to_order(orders, products)
    elif option == '6':
        orders = rem_prod_to_order(orders)
    elif option == '7':
        delete_order(con)
    elif option == '0':
        return False, orders, couriers

    return True, orders, couriers