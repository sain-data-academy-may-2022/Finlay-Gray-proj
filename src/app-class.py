# TO DO








# setting up inital variables
products = []
run = True
product_menu = False

# setting up menu texts that will show up on screen
first_menu_text = '''Welcome to Gray's Cafe!\n
Enter 1 to view prouct menu
Enter 0 to quit
> '''
product_menu_text = '''Enter 1 to view products list
Enter 2 to create a new product
Enter 3 to update current product
Enter 4 to delete a product
Enter 0 to return to main menu 
> '''

update_menu_text = '''Enter 1 to update a products name
Enter 2 to update a products price
Enter 3 to add to a products quantity
Enter 4 to subtract from a products quantity
Enter 0 to return to main menu
> '''

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
# function that prints out product list with corresponding index
def product_list_index(list):
    for i in range(len(list)):
        print(f'Product name: {list[i].name}\nIndex value: {i}\n')

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
        product_quantity = int(input('Enter the number of this product you would like to add\n> '))
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
    
# main loop
while run:
    to_continue = input(first_menu_text)
    if to_continue == '0':
        run = False
    elif to_continue == '1':
        product_menu = True
    else:
        print('\nPlease enter 1 or 0!\n')
    # runs production menu function
    while product_menu:
        cont = product_menu_func(products)
        if not(cont):
            product_menu = False






class basket:
    def __init__(self,items):
        self.items = items



        