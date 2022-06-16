import all_functions
import database
from tabulate import tabulate
import Productfile
class Orders:
    def __init__(self, id:int, name, address, phone_num, status, order_time, courier_index):
        self.id = id
        self.name = name
        self.address = address
        self.phone_num = phone_num
        self.status = status
        self.order_time = order_time
        self.courier_index = int(courier_index)
        

    def __repr__(self) -> str:
        return f'Order name: {self.name}\nAddress: {self.address}\nPhone_number: {self.phone_num}\nStatus: {self.status}\nOrder time: {self.order_time}\nCourier index: {self.courier_index}\n'


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

    


def update_order(con,order_update_menu_text):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    is_empty = database.check_if_table_empty(cur,'Orders')
    if not is_empty:
        try:
            all_functions.clear_screen()
            all_functions.print_list('Orders',con)
            order_id = int(
                        input('Enter The id of order you would like to update\n> ').strip())
            database.sql_statement(cur,f'''SELECT * FROM Orders WHERE id = {order_id}''')
            new_ord = cur.fetchone()
            order_class = Orders(new_ord[0],new_ord[1],new_ord[2],new_ord[3],new_ord[4],new_ord[5],new_ord[6])
            while True:
                all_functions.clear_screen()
                print(order_class)
                choice = input(order_update_menu_text)
                if choice == '0':
                    database.sql_statement(cur,f'''UPDATE Orders SET name = '{order_class.name}', address = '{order_class.address}', phone_num = '{order_class.phone_num}', courier_index = '{order_class.courier_index}' WHERE id = {order_id}''')
                    con.commit()
                    break
                elif choice == '1':
                    all_functions.clear_screen()
                    print(order_class)
                    
                    try:
                        order_old_name = order_class.name
                        order_new_name = input(
                            '\nEnter new name of order\n> ').strip()
                        order_class.name = order_new_name
                        print(
                            f'\n{order_old_name} has been replaced with {order_new_name}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')

                elif choice == '2':
                    all_functions.clear_screen()
                    print(order_class)
                    try:
                        new_address = input(
                            '\nEnter new address of order\n> ').lower().strip()
                        order_class.address = new_address
                        print(
                            f'\nThe address of {order_class.name} has been replaced with {new_address}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')

                elif choice == '3':
                    all_functions.clear_screen()
                    print(order_class)
                    try:
                        new_phone_num = input(
                            '\nEnter new phone number vehicle of order\n> ').lower().strip()
                        order_class.phone_num = new_phone_num
                        print(
                            f'\nThe phone number of {order_class.name} has been replaced with {new_phone_num}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')

                elif choice == '4':
                    all_functions.clear_screen()
                    is_empty = database.check_if_table_empty(cur,'Couriers')
                    if not is_empty:
                        all_functions.print_list('Couriers',con)
                        courier_index = int(
                                input('Enter the id of the courier for this order\n> '))

                        order_class.courier_index = courier_index
                        print(
                            f'\nThe phone number of {order_class.name} has been replaced with {new_phone_num}\n')
                        input('Press enter to continue')
                    else:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')
                    


        except:
            print('\nYou have not entered a valid input\n')
            input('Press enter to continue')


    else:
        print('\nYou do not have any Orders to update\n')
        input('Press enter to continue')

    database.close_cursor(cur)


def add_prod_to_order(con):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    try:
        is_empty_ord = database.check_if_table_empty(cur,'Orders')
        is_empty_prod = database.check_if_table_empty(cur,'Product')
        if not is_empty_ord and not is_empty_prod:
            try:
                all_functions.print_list('Orders',con)
                order_to_add_to = int(
                    input('Enter the index of the order you would like to add a product to\n> '))
                while True:
                    all_functions.clear_screen()
                    all_functions.print_list('Product',con)
                    product_index = int(
                        input('Enter the id of the product you would like to add\n> '))
                    quant = int(
                        input('Enter the quantity of the product you want to add\n> '))
                    
                    database.sql_statement(cur,f'''SELECT * FROM Product WHERE id = {product_index}''')
                    from_db = cur.fetchone()
                    prod_to_add = Productfile.Product(from_db[0],from_db[2],from_db[3],from_db[1])
                    if prod_to_add.can_order(quant):
                        prod_to_add.quantity_subtract(quant)
                        database.sql_statement(cur,f'''UPDATE Product SET quantity = {prod_to_add.quantity} WHERE id = {prod_to_add.id}''')
                        database.sql_statement(cur,f'''INSERT INTO OrderProducts (order_id,product_id,quantity) VALUES ({order_to_add_to},{product_index},{quant})''')
                        con.commit()
                        print(f'\nYou have added {prod_to_add.name} to your order\n')
                        input('\nPress enter to continue\n')
                    else:
                        print('\nYou can not enter that amount of this product as we do not have enough in stock\n')
                        input('\nPress enter to continue\n')

                    
                    all_functions.clear_screen()
                    to_cont = input(
                        'Do you want to add another product? (y/n) > ').strip().lower()
                    if to_cont == 'n':
                        break

            except:
                print('\nYou have not entered a valid input\n')
                input('\nPress enter to continue\n')

    except:
        pass
    database.close_cursor(cur)


def rem_prod_to_order(con):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    try:
        is_empty = database.check_if_table_empty(cur,'OrderProducts')
        
        if not is_empty:
            try:
                all_functions.print_list('Orders',con)
                order_to_rem_from = int(
                    input('Enter the index of the order you would like to remove a product from\n> '))
                while True:
                    database.sql_statement(cur,f'''SELECT id from Orders''')
                    all_ids = cur.fetchall()
                    if (int(order_to_rem_from),) in all_ids:
                        
                        database.sql_statement(cur, f'''SELECT Product.id, Product.name, OrderProducts.quantity
                                                        FROM OrderProducts, Product
                                                        WHERE Product.id = OrderProducts.product_id 
                                                        AND {order_to_rem_from} = OrderProducts.order_id''')
                        items = cur.fetchall()
                        field_names = [i[0] for i in cur.description]
                        all_functions.clear_screen()
                        print(tabulate(items, headers=field_names, tablefmt='psql',stralign='center',numalign='center'))
                        to_del = int(input('\nEnter the id of the product you would like to remove\n'))
                        database.sql_statement(cur,f'''SELECT * FROM Product WHERE id = {to_del}''')
                        from_db = cur.fetchone()
                        database.sql_statement(cur, f'''SELECT quantity FROM OrderProducts WHERE order_id = {order_to_rem_from} and product_id = {to_del}''')
                        from_db_2 = cur.fetchone()
                        prod_to_rem = Productfile.Product(from_db[0],from_db[2],from_db[3],from_db[1])
                        prod_to_rem.quantity_add(from_db_2[0])
                        database.sql_statement(cur,f'''UPDATE Product SET quantity = {prod_to_rem.quantity} WHERE id = {to_del}''')
                        database.sql_statement(cur, f'''DELETE FROM OrderProducts WHERE order_id = {order_to_rem_from} and product_id = {to_del}''')
                        con.commit()


                    all_functions.clear_screen()
                    to_cont = input(
                        'Do you want to remove another product? (y/n) > ').strip().lower()
                    if to_cont == 'n':
                        break
                
            except:
                pass


    except:
        pass      

    database.close_cursor(cur)


def delete_order(con):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    is_empty = database.check_if_table_empty(cur,'Orders')
    if not is_empty:
        all_functions.print_list('Orders',con)
        id_to_del = int(input('Enter the id of the order you would like to delete\n> ').strip())
        database.sql_statement(cur,f'''DELETE FROM Orders WHERE id = {id_to_del}''')
        con.commit()
    
    else:
        print('You do not have any orders in your order list\n')
    input('Press enter to continue')
    database.close_cursor(cur)





def view_orders(con):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    all_functions.print_list('Orders', con)
    view_prod = input('Enter order id to view products in order or enter any other key to continue\n> ')
    database.sql_statement(cur,f'''SELECT id from Orders''')
    all_ids = cur.fetchall()
    try:
        if (int(view_prod),) in all_ids:
            is_empty = database.check_if_table_empty(cur,'OrderProducts')
            if not is_empty:
                database.sql_statement(cur, f'''SELECT Product.name, OrderProducts.quantity
                                                FROM OrderProducts, Product
                                                WHERE Product.id = OrderProducts.product_id 
                                                AND {view_prod} = OrderProducts.order_id''')
                items = cur.fetchall()
                field_names = [i[0] for i in cur.description]
                all_functions.clear_screen()
                print(tabulate(items, headers=field_names, tablefmt='psql',stralign='center',numalign='center'))
                input('\nPress enter to coninue')
    except:
        pass


    database.close_cursor(cur)




def order_menu_func(con,order_update_menu_text, status_list, order_menu_text):
    all_functions.clear_screen()
    option = input(order_menu_text).strip()
    if option == '1':
        view_orders(con)
    elif option == '2':
        add_orders(con)
    elif option == '3':
        update_order_status(con, status_list)
    elif option == '4':
        update_order(con,order_update_menu_text)
    elif option == '5':
        add_prod_to_order(con)
    elif option == '6':
        orders = rem_prod_to_order(con)
    elif option == '7':
        delete_order(con)
    elif option == '0':
        return False

    return True