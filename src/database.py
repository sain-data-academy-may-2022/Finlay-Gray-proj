import pymysql
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
# Establish a database connection

def get_connection():
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    return connection

def get_cursor(con):
    cursor = con.cursor()
    return cursor







def close_cursor(cursor):
    cursor.close()

def close_connection(con):
    con.close()