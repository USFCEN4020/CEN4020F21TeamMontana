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
    emails text NOT NULL,
    sms text NOT NULL,
    targetedads text NOT NULL,
    title text NOT NULL,
    major text NOT NULL,
    university text NOT NULL,
    studentinfo text NOT NULL,
    education text NOT NULL,
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

experience_table = """CREATE TABLE IF NOT EXISTS experiences (
    title text NOT NULL,
    employer text NOT NULL,
    location text NOT NULL,
    description text NOT NULL,
    start_date INTEGER NOT NULL,
    end_date INTEGER NOT NULL,
    username text NOT NULL,
    FOREIGN KEY(username) REFERENCES users(username)
    );"""

friend_table = """CREATE TABLE IF NOT EXISTS friends (
    sender text NOT NULL,
    status text NOT NULL,
    receiver text NOT NULL,
    UNIQUE(sender, receiver)
    FOREIGN KEY(receiver) REFERENCES users(receiver)
    FOREIGN KEY(sender) REFERENCES users(sender)
    );"""

create_new_account_sql = ''' INSERT INTO users(username,password,firstname,lastname,language,emails,sms,targetedads,
                             title,major,university,studentinfo,education)
                             VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''

create_new_job_posting_sql = ''' INSERT INTO jobs(title,description,employer,location,salary,firstname,lastname)
                                 VALUES(?,?,?,?,?,?,?) '''

create_new_job_experience_sql = ''' INSERT INTO experience(title,employer,location,description,start_date,end_date,username)
                  VALUES(?,?,?,?,?,?,?) '''


create_new_friend_status_sql = ''' INSERT INTO friends(sender,status,receiver)
                  VALUES(?,?,?) '''
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
        # userPass is used to search for the password that corresponded to the username
        # did not use the query SELECT password FROM users WHERE username = 'userPass'
        # because I think it would try to exactly search for a username that is named userPass,
        # and not the actual username passed to the function parameter        if user[0]== userPass:
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


def query_list_of_experiences():
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM experiences")
    return cursor.fetchall()


# This gets the rows where someone is requesting to be your friend
def query_list_of_friend_requests(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT sender FROM friends WHERE receiver = ? AND status = PENDING''', (username,))
    return cursor.fetchall()


def create_row_in_jobs_table(connection, job_info):
    try:
        cursor = connection.cursor()
        cursor.execute(create_new_job_posting_sql, job_info)
        connection.commit()
    except Error as e:
        print(e)


def create_row_in_experience_table(connection, experience_info):
    try:
        cursor = connection.cursor()
        cursor.execute(create_new_job_experience_sql, experience_info)
        connection.commit()
    except Error as e:
        print(e)


def create_row_in_friend_table(connection, friend_info):
    try:
        cursor = connection.cursor()
        cursor.execute(create_new_friend_status_sql, friend_info)
        connection.commit()
    except Error as e:
        print(e)


# These next 4 functions modify a User's privacy settings (ChangeLang, SendEmailsStatus, SendSMSStatus, TargetAdsStatus)
def ChangeLang(username, lang):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET language = ? WHERE username = ?''', (lang, username,))
    connection.commit()


def SendEmailsStatus(username, status):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET emails = ? WHERE username = ?''', (status, username,))
    connection.commit()


def SendSMSStatus(username, status):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET sms = ? WHERE username = ?''', (status, username,))
    connection.commit()


def TargetAdsStatus(username, status):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET targetedads = ? WHERE username = ?''', (status, username,))
    connection.commit()


def User_Title(username, title):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET title = ? WHERE username = ?''', (title, username,))
    connection.commit()

def User_Major(username, major):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET major = ? WHERE username = ?''', (major, username,))
    connection.commit()


def User_University(username, university_name):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET university = ? WHERE username = ?''', (university_name, username,))
    connection.commit()


def User_Info(username, student_info):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET studentinfo = ? WHERE username = ?''', (student_info, username,))
    connection.commit()


def User_Education(username, education):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET education = ? WHERE username = ?''', (education, username,))
    connection.commit()


def Friend_Status(sender, receiver, status):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    if status == "REJECT" or status == "DISCONNECT":
        cursor.execute("DELETE * FROM friends WHERE sender = ? AND receiver = ?", (sender, receiver,))
    elif status == "PENDING" or status == "ACCEPT":
        cursor.execute("UPDATE friends SET status = ? WHERE sender = ? AND receiver = ?", (status, sender, receiver,))
    # This is just so that only valid statuses are passed to this function.
    else:
        print("Not a valid status")
    connection.commit()


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

    cursor.execute("SELECT * FROM experiences")
    print("Experiences table: ")
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM friends")
    print("Friends table: ")
    print(cursor.fetchall())


def print_experiences(connection, username):
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM experiences WHERE username = ?''', (username,))
    print("Users job experiences: ")
    print(cursor.fetchall())



def print_friends(connection, username):
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM friends WHERE sender = ? OR receiver = ?''', (username, username,))
    print("Users friends: ")
    print(cursor.fetchall())


# commit the deletes to remove all the data in each table.
def delete_all_database_info(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users")
    connection.commit()
    cursor.execute("DELETE FROM jobs")
    connection.commit()
    cursor.execute("DELETE FROM experiences")
    connection.commit()
    cursor.execute("DELETE FROM friends")
    connection.commit()


# For testing purposes
def query_student_title(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT title FROM users WHERE username = ?''', (username,))
    return cursor.fetchall()

def query_student_major(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT major FROM users WHERE username = ?''', (username,))
    return cursor.fetchall()

def query_student_university(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT university FROM users WHERE username = ?''', (username,))
    return cursor.fetchall()

def query_student_info(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT studentinfo FROM users WHERE username = ?''', (username,))
    return cursor.fetchall()


def query_education(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT university, major, education FROM users WHERE username = ?''', (username,))
    return cursor.fetchall()


# This just returns the name of all your friends
def query_friend(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    # Union the two cases where we are either the sender or receiver of a friend request, so we take the other username
    # since that would be the friend, if they accepted our friend request
    cursor.execute('''SELECT sender FROM friends WHERE receiver = ? AND status = ACCEPT UNION 
                   SELECT receiver FROM friends WHERE sender = ? AND status = ACCEPT''', (username, username,))
    return cursor.fetchall()

# function to fill in values to the database for testing purposes primarily
def fill_database(connection):
    create_table(connection, user_table)
    user = ("username2", "Password?2", "An", "Dinh", "English", "Don't Send Emails", "Don't Send SMS", "Don't Target Ads",
            "Scrum Master", "Computer Science", "University of South Florida", "Blank",
            "You attended USF for 4 years to get a degree in BCS",)
    create_row_in_users_table(connection, user)
    create_table(connection, job_table)
    job_info = ("Scrum Master", "It is to manage people", "Bob", "Florida", 1, "An", "Dinh",)
    create_row_in_jobs_table(connection, job_info)
    create_table(connection, experience_table)
    experience_info = ("Scrum Master", "Bob", "Florida", "It was boring", "2021-10-04", "2021-10-10", "username2",)
    create_row_in_experience_table(connection, experience_info)
    experience_info = ("person_sending_request", "PENDING", "person_logged_in",)
    create_row_in_experience_table(connection, experience_info)


