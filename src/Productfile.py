import database
import all_functions

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


    

def update_products(con, prod_update_menu_text):
    all_functions.clear_screen()
    cur = database.get_cursor(con)
    is_empty = database.check_if_table_empty(cur,'Product')
    if not is_empty:
        try:
            all_functions.clear_screen()
            all_functions.print_list('Product',con)
            product_id = int(
                        input('Enter The id of product you would like to update\n> ').strip())
            database.sql_statement(cur,f'''SELECT * FROM Product WHERE id = {product_id}''')
            new_prod = cur.fetchone()
            prod_class = Product(new_prod[0],new_prod[2],new_prod[3],new_prod[1])
            while True:
                all_functions.clear_screen()
                print(prod_class)
                choice = input(prod_update_menu_text)
                if choice == '0':
                    database.sql_statement(cur,f'''UPDATE Product SET name = '{prod_class.name}', price = {float(prod_class.price)}, quantity = {prod_class.quantity} WHERE id = {product_id}''')
                    con.commit()
                    break
                elif choice == '1':
                    all_functions.clear_screen()
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
                    all_functions.clear_screen()
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
                    all_functions.clear_screen()
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
                    all_functions.clear_screen()
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
    all_functions.clear_screen()
    all_functions.print_list('Product',con)
    id_to_del = int(input('Enter the id of the product you would like to delete\n> ').strip())
    database.sql_statement(cur,f'''DELETE FROM Product WHERE id = {id_to_del}''')
    con.commit()
    database.close_cursor(cur)


def add_products(con):
    cur = database.get_cursor(con)
    all_functions.clear_screen()
    product_name = input(
        'Enter the name of the product you would like to add\n> ').lower().strip()
    product_price = float(
        input('Enter the price of this product\n> ').lower().strip())
    product_quantity = int(
        input('Enter the quantity of this product you have\n> ').strip())

    if product_name == ''.strip():
        print(f'\nYou have not entered a valid input\n')
    else:
        database.sql_statement(cur,f'''INSERT INTO Product (name,price,quantity) VALUES ('{product_name}',{product_price},{product_quantity})''')
        con.commit()
        print(f'\nYou have added {product_name} to your products\n')
    input('Press enter to continue')

    database.close_cursor(cur)
    


def view_products(con):
    all_functions.clear_screen()
    all_functions.print_list('Product', con)
    input('Press enter to continue')



def product_menu_func(con,product_menu_text, prod_update_menu_text):
    all_functions.clear_screen()
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

