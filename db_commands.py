import sqlite3
from sqlite3 import Error
# This file is for storing database commands
database_name = "userDB"
# SQLite queries

# create user table
user_table = """CREATE TABLE IF NOT EXISTS users (
    username text PRIMARY KEY,
    password text NOT NULL,
    firstname text NOT NULL,
    lastname text NOT NULL,
    language text NOT NULL,
    UNIQUE(firstname, lastname)
    );"""

job_table = """CREATE TABLE IF NOT EXISTS jobs (
    title text NOT NULL,
    description text NOT NULL,
    employer text NOT NULL,
    location text NOT NULL,
    salary INTEGER NOT NULL,
    firstname text NOT NULL,
    lastname text NOT NULL,
    FOREIGN KEY(firstname) REFERENCES users(firstname),
    FOREIGN KEY(lastname) REFERENCES users(lastname)
    );"""

create_new_account_sql = ''' INSERT INTO users(username,password,firstname,lastname)
                  VALUES(?,?,?,?) '''

create_new_job_posting_sql = ''' INSERT INTO jobs(title,description,employer,location,salary,firstname,lastname)
                  VALUES(?,?,?,?,?,?,?) '''


# Function for creating sqlite database
def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    finally:
        return conn


# Creating a table
# Inputs: connection, SQLite create table command
def create_table(connection, create_table_command):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_command)
    except Error as e:
        print(e)


# Queries for list of usernames
def query_usernames_list(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM users")
    rows = cursor.fetchall()
    return rows


# Queries for the password of the username
# Useful for finding the password connected to the username passed to function parameter.
# Created this function to return the password string associated with the username,
# so that I did not have to deal with tuple out of range error.
def query_password(connection, userPass):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    # fetchall returns a row of tuples, so using brackets to access the data in the respective column
    rows = cursor.fetchall()
    # goes through all the usernames from the database
    for user in rows:
        # userPass is used to search for the password that cooresponded to the username
        # did not use the query SELECT password FROM users WHERE username = 'userPass'
        # because I think it would try to exactly search for a username that is named userPass, and not the actual username passed to the function parameter
        if user[0]== userPass:
            password = user[1]
            return password


# Query to get the tuples for each row of (username, password) from the users table
# Going to be used to be passed into a function argument for testing purposes
def query_username_password(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT username,password FROM users")
    users = cursor.fetchall()
    return users


def create_row_in_users_table(connection, user):
    try:
        cursor = connection.cursor()
        cursor.execute(create_new_account_sql, user)
        connection.commit()
    except Error as e:
        print(e)


# Queries for first names
def query_names(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT firstname,lastname FROM users")
    return cursor.fetchall()


def find_names_from_username(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT firstname,lastname FROM users WHERE username=?", (username,))
    names = cursor.fetchall()[0]
    firstname = names[0]
    lastname = names[1]
    return firstname, lastname


def query_list_of_jobs():
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT title FROM jobs")
    return cursor.fetchall()


def create_row_in_jobs_table(job_info):
    connection = create_connection(database_name)
    try:
        cursor = connection.cursor()
        cursor.execute(create_new_job_posting_sql, job_info)
        connection.commit()
    except Error as e:
        print(e)

# def ChangeLang(db_name):
#     connection = create_connection(db_name)
#     cursor = connection.cursor()
#     cursor.execute("SELECT language FROM users")
#     print(cursor.fetchall())

# These are helper functions specifically to help testers and developers
# Helper function for testing purposes
def print_database(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    print("Users table: ")
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM jobs")
    print("Jobs table: ")
    print(cursor.fetchall())


def delete_all_database_info(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM jobs")


