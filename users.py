import sqlite3
from sqlite3 import Error
from time import ctime


def post_sql_query(sql_query):
    with sqlite3.connect("users.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error:
            pass
        result = cursor.fetchall()
        return result


def create_tables():
    users_query = "CREATE TABLE IF NOT EXISTS USERS (user_id INTEGER PRIMARY KEY NOT NULL, username TEXT,first_name " \
                  "TEXT,last_name TEXT,reg_date TEXT) "
    post_sql_query(users_query)


def register_user(user, username, first_name, last_name):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO USERS (user_id, username, first_name,  last_name, reg_date) VALUES ({user}, "{username}", "{first_name}", "{last_name}", "{ctime()}"); '
        post_sql_query(insert_to_db_query)


def get_users_info():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM USERS;")
    user_information = cur.fetchall()
    return user_information
