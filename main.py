# Import statements
from re import match
import sqlite3
from sqlite3 import Error
from typing import Match
import db_commands
#import search_job
import random
import account_define
import user_options

database_name = "userDB"
# Main function
if __name__ == '__main__':

    connection = db_commands.create_connection(database_name)
    # Create tables if not exist
    db_commands.create_table(connection, db_commands.user_table)
    db_commands.create_table(connection, db_commands.job_table)
    # db_commands.print_database(connection)

    file = open("Student_story.txt")
    content = file.read()

    # Welcome everyone to InCollege, a story of success student
    # Prompt user for either logging in or creating an account <- if neither happens they quit
    print("Welcome to inCollege by Team Montana!")
    print(content)
    print("")
    print("Why you should join in InCollege? Watch the video!")
    print("")
    print("Please choose from the following menu:")
    print("1 - Log into an existing account")
    print("2 - Create an account")
    print("3 - Play a video")
    userChoice = input("Enter your selection here: ")

    # come back later to implement a way for the user to go back to the lines above
    if userChoice == "1":
        # variable used to continue the attempt by the user to login
        succLogin = False
        # returns usernames from the database
        existing_usernames = db_commands.query_usernames_list(connection)
        username_password_tuples = db_commands.query_username_password(connection)
        username_input = None
        password_input = None
        #Need to implement later on for user to go back, in that case we can just have a while true loop in main that encompasses all the code. 
        #And break out of this statement if for another user input like "Back", which will break out of this while loop
        while succLogin == False and username_input != "Q":
            username_input = input("Enter your username, or Q to quit the program: ")
            if username_input == "Q":
                exit()
            else:
                password_input = input("Enter your password: ")
                #If userLogin continues to return false then keep running this while loop and ask for usernames or if the user wants to quit the program
                succLogin = account_define.userLogin(username_input, password_input, existing_usernames, username_password_tuples)
            
    elif userChoice == "2":
        print("We are creating an account\n")
        username_input = input("Please enter a new username ")
        existing_usernames = db_commands.query_usernames_list(connection)

        # Otherwise, safe to create username
        # Tests if safe username
        while True:
            if not account_define.username_meets_qualifications(username_input, existing_usernames):
                username_input = input("Please enter another username ")
            else:
                break

        # Otherwise, safe to create password
        password_input = input("Please enter a password: ")
        while True:
            if not account_define.password_meets_qualifications(password_input):
                print("Your password does not meet the qualifications.")
                password_input = input("Please enter another password: ")
            else:
                break

        while True:
            # Prompt for first name
            firstname_input = input("Please enter your first name: ")
            # Prompt for second name
            lastname_input = input("Please enter your last name: ")
            # Check if those are in the system
            if account_define.does_user_exist(firstname_input, lastname_input):
                print("That name already exists in our system. Do you have a nickname you go by?")
            else:
                break

        # Create row in users table
        user_information = (username_input, password_input, firstname_input, lastname_input)
        db_commands.create_row_in_users_table(connection, user_information)

        print("Successfully created your account. You are now logged in.")
        user_options.additional_options(username_input, firstname_input, lastname_input)
    elif userChoice == "3":
        print("Video is now playing.")
    else:
        print("I did not recognize your input")
        connection.close()
        exit()


    # at the very end, close database connection
    connection.close()
