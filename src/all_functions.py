# imports
import os
import time
import database
from tabulate import tabulate


# clearing the terminal function


def clear_screen():
    os.system('clear')

# all lost index functions print list with index to screen




class OrderProducts:
    def __init__(self,order_id,product_id,quantity) -> None:
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        






def print_list(table,con):
    
    cur = database.get_cursor(con)
    database.sql_statement(cur,f'''SELECT * FROM {table}''')
    items = cur.fetchall()
    field_names = [i[0] for i in cur.description]
    print(tabulate(items, headers=field_names, tablefmt='psql',stralign='center',numalign='center'))
    database.close_cursor(cur)
    # for i in range(len(list)):
    #     print(
    #         f'Product name: {list[i].name}\nPrice: £{list[i].price}\nQuantity: {list[i].quantity}\n')


def orders_list_index(list):
    for i in range(len(list)):
        print(f'Order name: {list[i].name}\nAddress: {list[i].address}\nPhone_number: {list[i].phone_num}\nStatus: {list[i].status}\nOrder time: {list[i].order_time}\nCourier index: {list[i].courier_index}\nProducts in order: {list[i].products_list}\nIndex value: {i}\n')



