import database
import all_functions
import Ordersfile
from tabulate import tabulate

class Couriers:
    def __init__(self, id:int, name, phone, delivery):
        self.id = id
        self.name = name
        self.phone = phone
        self.delivery = delivery

    def name_change(self, new_name):
        self.name = new_name

    def __repr__(self) -> str:
        return f'Courier name: {self.name}\nPhone number: {self.phone}\nCouriers delivery vehicle: {self.delivery}\n'

    # each service has an order capacity
    # each servvice has a vehicle
    # each service has a average delivery time




def view_courier(con):
    all_functions.clear_screen()
    all_functions.print_list('Couriers', con)
    input('Press enter to continue')


def add_courier(con):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    courier_name = input(
        'Enter the name of the courier you would like to add\n> ').title().strip()
    courier_phone = input('Enter the phone number of your courier\n> ')
    courier_vehicle = input('Enter the vehicle your courier uses\n> ')
    database.sql_statement(cur,f'''INSERT INTO Couriers (name,phone,delivery) VALUES ('{courier_name}','{courier_phone}','{courier_vehicle}')''')
    con.commit()
    print(f'\nYou have added {courier_name} to your couriers\n')
    input('Press enter to continue')

    database.close_cursor(cur)


def update_courier(con,courier_update_menu_text):
    all_functions.clear_screen()
    cur = database.get_cursor(con)
    is_empty = database.check_if_table_empty(cur,'Couriers')
    if not is_empty:
        try:
            all_functions.clear_screen()
            all_functions.print_list('Couriers',con)
            courier_id = int(
                        input('Enter The id of courier you would like to update\n> ').strip())
            database.sql_statement(cur,f'''SELECT * FROM Couriers WHERE id = {courier_id}''')
            new_cour = cur.fetchone()
            cour_class = Couriers(new_cour[0],new_cour[1],new_cour[2],new_cour[3])
            while True:
                all_functions.clear_screen()
                print(cour_class)
                choice = input(courier_update_menu_text)
                if choice == '0':
                    database.sql_statement(cur,f'''UPDATE Couriers SET name = '{cour_class.name}', phone = '{cour_class.phone}', delivery = '{cour_class.delivery}' WHERE id = {courier_id}''')
                    con.commit()
                    break
                elif choice == '1':
                    all_functions.clear_screen()
                    print(cour_class)
                    
                    try:
                        cour_old_name = cour_class.name
                        cour_new_name = input(
                            '\nEnter new name of Courier\n> ').title().strip()
                        cour_class.name_change(cour_new_name)
                        print(
                            f'\n{cour_old_name} has been replaced with {cour_new_name}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')

                elif choice == '2':
                    all_functions.clear_screen()
                    print(cour_class)
                    try:
                        new_number = input(
                            '\nEnter new number of courier\n> ').lower().strip()
                        cour_class.phone = new_number
                        print(
                            f'\nThe phone number of {cour_class.name} has been replaced with {new_number}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')

                elif choice == '3':
                    all_functions.clear_screen()
                    print(cour_class)
                    try:
                        new_vehicle = input(
                            '\nEnter new delivery vehicle of courier\n> ').lower().strip()
                        cour_class.delivery = new_vehicle
                        print(
                            f'\nThe delivery vehicle of {cour_class.name} has been replaced with {new_vehicle}\n')
                        input('Press enter to continue')
                    except:
                        print('\nPLease enter valid input\n')
                        input('Press enter to continue')


        except:
            print('\nYou have not entered a valid input\n')
            input('Press enter to continue')


    else:
        print('\nYou do not have any couriers to update\n')
        input('Press enter to continue')

    database.close_cursor(cur)


def delete_courier(con):
    all_functions.clear_screen()
    cur = database.get_cursor(con)
    is_empty = database.check_if_table_empty(cur,'Couriers')
    if not is_empty:
        all_functions.print_list('Couriers',con)
        try:
            courier_index = int(
                input('Enter the id of courier you would like to remove\n> ').strip())
            database.sql_statement(cur,f'''SELECT * from Couriers WHERE id = {courier_index}''')
            data = cur.fetchone()
            cour_class = Couriers(data[0],data[1],data[2],data[3])
            database.sql_statement(cur,f'''select count(courier_index) from Orders where courier_index = {courier_index}''')
            count = cur.fetchone()
            all_functions.clear_screen()

            while True:
                choice = input(f'''This courier is currently active in {count[0]} orders

Therefore please pick what you would like to do:

Enter 1 to delete the courier and delete all orders associated with it

Enter 2 to delete the courier and change the courier of all the associated orders

Enter 3 to not delete the courier
> ''')

                if choice == '1':
                    all_functions.clear_screen()
                    courier_name = cour_class.name
                    database.sql_statement(cur,f'''DELETE FROM Couriers WHERE id = {courier_index}''')
                    con.commit()
                    print(
                        f'\n{courier_name} has been removed from your couriers\n')
                    
                    break
                elif choice == '2':
                    all_functions.clear_screen()
                    orders = []
                    database.sql_statement(cur,f'''SELECT * FROM Orders WHERE courier_index = {courier_index}''')
                    data = cur.fetchall()
                    for i in data:
                        all_functions.clear_screen()
                        order_class = Ordersfile.Orders(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                        print(order_class)
                        database.sql_statement(cur,f'''SELECT * FROM Couriers WHERE id != {courier_index}''')
                        items = cur.fetchall()
                        field_names = [i[0] for i in cur.description]
                        print(tabulate(items, headers=field_names, tablefmt='psql',stralign='center',numalign='center'))
                        cour = int(
                            input('\nWhich courier index would you like to switch to\n> '))
                        order_class.courier_index = cour
                        database.sql_statement(cur,f'''UPDATE Orders SET courier_index = {cour} WHERE ID = {order_class.id}''')
                        con.commit()
                    database.sql_statement(cur,f'''DELETE FROM Couriers WHERE id = {courier_index}''')
                    con.commit()
                    break

                elif choice == '3':
                    break

        except:
            print('\nYou have not entered a valid index\n')
    else:
        print('\nYou do not have any couriers to delete\n')
    input('Press enter to continue')
    database.close_cursor(cur)


def courier_menu_func(con, courier_menu_text,courier_update_menu_text):
    all_functions.clear_screen()
    option = input(courier_menu_text).strip()
    # prints courier list
    if option == '1':
        view_courier(con)
    # allows user to add a courier to the list
    elif option == '2':
        add_courier(con)
    # allows user to update the name of a courier in the list
    elif option == '3':
        update_courier(con,courier_update_menu_text)
    # allows user to delete a courier from the list
    elif option == '4':
        delete_courier(con)
    # allows user to go back to previous menu
    elif option == '0':
        return False

    # keeps the loop running
    return True


