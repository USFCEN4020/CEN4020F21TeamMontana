import random
import sqlite3
from sqlite3 import Error

# This file is for storing database commands
database_name = "userDB"
# SQLite queries

# create user table
user_table = """CREATE TABLE IF NOT EXISTS users (
    username text,
    password text NOT NULL,
    firstname text,
    lastname text, 
    tier text,
    language text NOT NULL,
    emails text NOT NULL,
    sms text NOT NULL,
    targetedads text NOT NULL,
    title text NOT NULL,
    major text NOT NULL,
    university text NOT NULL,
    studentinfo text NOT NULL,
    education text NOT NULL,
    PRIMARY KEY(username),
    UNIQUE(firstname, lastname)
    );"""

job_table = """CREATE TABLE IF NOT EXISTS jobs (
    jobID INTEGER PRIMARY KEY,
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

user_job_table = """CREATE TABLE IF NOT EXISTS job_applications (
    username text,
    jobID text,
    graduation_date text,
    start_date text,
    statement_of_purpose text,
    status text NOT NULL,
    PRIMARY KEY(username, jobID),
    FOREIGN KEY(username) REFERENCES users(username) ON DELETE CASCADE,
    FOREIGN KEY(jobID) REFERENCES jobs(jobID) ON DELETE CASCADE
    );"""

messages_table = """CREATE TABLE IF NOT EXISTS messages (
    sender text,
    recipient text,
    message text,
    messageID INTEGER PRIMARY KEY,
    status text NOT NULL,
    FOREIGN KEY(sender) REFERENCES users(username)
    FOREIGN KEY(recipient) REFERENCES users(username)
    );"""

# this table is to hold all of the jobs that was deleted until all of the users that applied to the job is notified.
deleted_jobs_table = """CREATE TABLE IF NOT EXISTS deleted_jobs (
    username text,
    title text NOT NULL,
    description text NOT NULL,
    employer text NOT NULL,
    location text NOT NULL,
    salary INTEGER NOT NULL,
    FOREIGN KEY(username) REFERENCES users(username) ON DELETE CASCADE, 
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
    sender text,
    status text NOT NULL,
    receiver text,
    PRIMARY KEY(sender, receiver)
    FOREIGN KEY(sender) REFERENCES users(username)
    FOREIGN KEY(receiver) REFERENCES users(username)
    );"""

create_new_account_sql = ''' INSERT INTO users(username,password,firstname,lastname,tier, language,emails,sms,targetedads,
                             title,major,university,studentinfo,education)
                             VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

create_message_sql = ''' INSERT INTO messages(sender,recipient,message, status)
                             VALUES(?,?,?,?) '''

create_new_job_posting_sql = ''' INSERT INTO jobs(title,description,employer,location,salary,firstname,lastname)
                                 VALUES(?,?,?,?,?,?,?) '''

create_new_job_application_sql = ''' INSERT INTO job_applications(username, jobID, graduation_date, start_date,
                                     statement_of_purpose, status) 
                                     VALUES(?,?,?,?,?,?) '''

create_new_deleted_notification_sql = ''' INSERT INTO deleted_jobs(username, title, description, employer, location,
                                          salary)
                                          VALUES(?,?,?,?,?,?)'''

create_new_job_experience_sql = ''' INSERT INTO experiences(title,employer,location,description,start_date,end_date,username)
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


# Queries for list of jobs
def query_jobs_list(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    return rows


def query_job_info_from_id(connection, jobID):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT title FROM jobs WHERE jobID = ?", (jobID,))
        return cursor.fetchall()
    except Error as e:
        print(e)


def query_job_apps(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT username, jobID, status from job_applications")
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
        # and not the actual username passed to the function parameter
        if user[0] == userPass:
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


# Called when a user sends a message
# Message formatting: sender, recipient, message
def create_row_in_message_table(connection, message):
    try:
        cursor = connection.cursor()
        cursor.execute(create_message_sql, message)
        connection.commit()
    except Error as e:
        print(e)


# Queries for first names
def query_names(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT firstname,lastname FROM users")
    return cursor.fetchall()


def query_names_user(username, connection):
    cursor = connection.cursor()
    cursor.execute("SELECT firstname,lastname FROM users WHERE username = ?", (username,))
    return cursor.fetchone()


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
    cursor.execute("SELECT sender FROM friends WHERE receiver = ? AND status = 'PENDING' ", (username,))
    return cursor.fetchall()


def query_list_of_new_meesage(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT sender, message FROM messages WHERE recipient = ? AND status = 'NEW' ", (username,))
    return cursor.fetchall()


def create_row_in_jobs_table(connection, job_info):
    try:
        cursor = connection.cursor()
        cursor.execute(create_new_job_posting_sql, job_info)
        connection.commit()
    except Error as e:
        print(e)


def create_row_in_job_applications_table(connection, job_app_info):
    try:
        cursor = connection.cursor()
        cursor.execute(create_new_job_application_sql, job_app_info)
        connection.commit()
    except Error as e:
        print(e)


def remove_row_in_job_applications_table(connection, username, jobID):
    try:
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM job_applications WHERE username = ? AND jobID = ?''', (username, jobID,))
        connection.commit()
    except Error as e:
        print(e)


def remove_row_in_message_table(sender, recipient, message):
    connection = create_connection(database_name)
    try:
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM messages WHERE sender = ? AND recipient = ? AND message = ?''',
                       (sender, recipient, message,))
        connection.commit()
    except Error as e:
        print(e)


# the paramater user_job_info will contain the user that is interacting with jobs
# it will also contain the jobID of the job that the user is interested in.
# it will also contains the status how how the student is trying to interact with the job
# user_job_info = (username, jobID, status)
def create_row_in_user_job_table(connection, user_job_info):
    try:
        cursor = connection.cursor()
        cursor.execute(create_new_friend_status_sql, user_job_info)
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
        cursor.execute("DELETE FROM friends WHERE sender = ? AND receiver = ?", (sender, receiver,))
    elif status == "PENDING" or status == "ACCEPT":
        cursor.execute("UPDATE friends SET status = ? WHERE sender = ? AND receiver = ?", (status, sender, receiver,))
    # This is just so that only valid statuses are passed to this function.
    else:
        print("Not a valid status")
    connection.commit()


def message_status(sender, recipient, status):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    if status == "DELETE":
        cursor.execute("DELETE FROM messages WHERE sender = ? AND recipient = ?", (sender, recipient,))
    elif status == "NEW" or status == "READ":
        cursor.execute("UPDATE messages SET status = ? WHERE sender = ? AND recipient = ?",
                       (status, sender, recipient,))
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
    cursor.execute("SELECT * FROM friends WHERE sender = ? OR receiver = ? AND status = 'ACCEPT' ",
                   (username, username,))
    print("Users friends: ")
    print(cursor.fetchall())


# Messages
def query_user_has_messages(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT sender, message FROM messages WHERE recipient = ?''', (username,))
    return cursor.fetchall()


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
    cursor.execute('''SELECT sender FROM friends WHERE receiver = ? AND status = 'ACCEPT' UNION 
                   SELECT receiver FROM friends WHERE sender = ? AND status = 'ACCEPT' ''', (username, username,))
    return cursor.fetchall()

def query_friend_profiles(friends_list):
    friends_list_profiles = []
    for friend in friends_list:
        # looking at each of friends individually and if any of their profile fields are empty
        if (query_student_title(friend) == "TITLE:NULL" and
                query_student_major(friend) == "MAJOR:NULL" and
                query_student_university(friend) == "UNIVERSITY:NULL" and
                query_student_info(friend) == "STUDENTINFO:NULL" and
                query_education(friend) == "EDUCATION:NULL"):
            # if all of the fields of the student profiles are not filled then the student does not have a
            # profile that can be viewd by others
            friends_list_profiles.append((friend, "No profile"))
        else:
            friends_list_profiles.append((friend, "profile"))
    return friends_list_profiles


# paramaters are the user that wants to look at jobs they have applied to
# and status is whether the user wants to check what jobs they have applied to or the ones they have yet to apply
# or if that status is saved
def query_applications(username, status):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    # this does not search for the status in the tables, but if the user wants to find the jobs that they have not applied
    # for, we will use a different query that will look for rows in jobs table where the user where the relationship
    # between user and job is not applied.
    if status == "NOT APPLIED":
        # we first get the query for the jobs that the user applied to and returns the jobID of that
        # then we querty for the jobs that does not have that jobID, or it other words the jobs that user has not applied to
        # this is only for spplications, so it will still show jobs that the user has saved.
        cursor.execute(
            "SELECT * FROM jobs WHERE NOT EXISTS(SELECT jobID FROM job_applications WHERE username = ? AND status = 'APPLIED' AND jobs.jobID = job_applications.jobID)",
            (username,))
    else:
        cursor.execute("SELECT * FROM job_applications WHERE username = ? AND status = ?", (username, status))
    return cursor.fetchall()


# This returns your status - premium or not
def query_membership_status(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT tier FROM users WHERE username = ?''', (username,))
    return cursor.fetchone()


def print_query_tiers(username):
    connection = create_connection(database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT username, tier FROM users WHERE username = ?''', (username,))
    print(cursor.fetchone())


# commit the deletes to remove all the data in each table.
def delete_all_database_info(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users")
    connection.commit()
    cursor.execute("DELETE FROM jobs")
    connection.commit()
    cursor.execute("DELETE FROM job_applications")
    connection.commit()
    cursor.execute("DELETE FROM experiences")
    connection.commit()
    cursor.execute("DELETE FROM friends")
    connection.commit()
    cursor.execute("DELETE FROM messages")
    connection.commit()


# function to fill in values to the database for testing purposes primarily
def fill_database(connection):
    create_table(connection, user_table)
    user1 = ("username2", "Password?2", "An", "Dinh", "Standard", "English", "Don't Send Emails", "Don't Send SMS",
             "Don't Target Ads", "Scrum Master", "Computer Science", "University of South Florida", "Blank",
             "You attended USF for 4 years to get a degree in BCS",)
    create_row_in_users_table(connection, user1)
    user2 = ("username3", "Password?3", "Nyan", "Cat", "Plus", "English", "Don't Send Emails", "Don't Send SMS",
             "Don't Target Ads", "Tester", "Computer Science", "University of South Florida", "Blank",
             "You attended USF for 4 years to get a degree in BCS",)
    create_row_in_users_table(connection, user2)
    user3 = ("username4", "Password?4", "John", "Smith", "Standard", "Spanish", "Don't Send Emails", "Don't Send SMS",
             "Don't Target Ads", "Tester", "Computer Science", "University of South Florida", "Blank",
             "You attended USF for 4 years to get a degree in BCS",)
    create_row_in_users_table(connection, user3)
    user4 = ("username5", "Password?5", "Bob", "Guy", "Plus", "English", "Don't Send Emails", "Don't Send SMS",
             "Don't Target Ads", "Software Developer", "Computer Science", "University of South Florida", "Blank",
             "You attended USF for 4 years to get a degree in BCS",)
    create_row_in_users_table(connection, user4)

    create_table(connection, job_table)
    job_info1 = ("Scrum Master", "It is to manage people", "Bob", "Florida", 1, "An", "Dinh",)
    create_row_in_jobs_table(connection, job_info1)
    job_info2 = ("Scrum Master", "Make sure people are doing work", "Guy", "Florida", 10, "An", "Dinh",)
    create_row_in_jobs_table(connection, job_info2)
    job_info3 = ("Tester", "Make sure code works", "Flo", "Florida", 1000000, "Nyan", "Cat",)
    create_row_in_jobs_table(connection, job_info3)
    job_info4 = ("Software Developer", "Write code that works", "Rida", "Florida", 54145, "Bob", "Guy",)
    create_row_in_jobs_table(connection, job_info4)

    create_table(connection, user_job_table)

    create_table(connection, experience_table)
    experience_info1 = ("Scrum Master", "Bob", "Florida", "It was boring", "2021-10-04", "2021-10-10", "username2",)
    create_row_in_experience_table(connection, experience_info1)
    experience_info2 = ("Tester", "Bob", "Florida", "It was okay", "2021-10-25", "2021-10-31", "username2",)
    create_row_in_experience_table(connection, experience_info2)
    experience_info3 = ("Software Developer", "Bob", "Florida", "Me write code",
                        "2021-10-25", "2021-10-31", "username3",)
    create_row_in_experience_table(connection, experience_info3)
    experience_info4 = ("Software Developer", "Bob", "Florida", "I write good code",
                        "2021-10-25", "2021-10-31", "username4",)
    create_row_in_experience_table(connection, experience_info4)
    experience_info5 = ("Software Developer", "Bob", "Florida", "My code sucks, but works.",
                        "2021-10-25", "2021-10-31", "username5",)
    create_row_in_experience_table(connection, experience_info5)

    create_table(connection, friend_table)
    friend_info1 = ("username2", "PENDING", "username3",)
    create_row_in_friend_table(connection, friend_info1)
    friend_info2 = ("username2", "ACCEPT", "username4",)
    create_row_in_friend_table(connection, friend_info2)
    friend_info3 = ("username2", "PENDING", "username5",)
    create_row_in_friend_table(connection, friend_info3)

    create_table(connection, messages_table)
    message_info1 = ("username3", "username2", "Test Message, reply to this message with Cat", "Plus")
    create_row_in_message_table(connection, message_info1)
    message_info2 = ("username3", "username2", "Test Message number 2 in case you did not read number 1", "Plus")
    create_row_in_message_table(connection, message_info2)
    message_info3 = ("username4", "username2", "This is John, reply back with Smith", "Standard")
    create_row_in_message_table(connection, message_info3)