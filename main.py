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
import start_options


database_name = "userDB"
# Main function
if __name__ == '__main__':

    connection = db_commands.create_connection(database_name)
    # Create tables if not exist
    db_commands.create_table(connection, db_commands.user_table)
    db_commands.create_table(connection, db_commands.job_table)
    # db_commands.print_database(connection)

    user_story = start_options.succ_story("Student_story.txt")

    # Welcome everyone to InCollege, a story of success student
    # Prompt user for either logging in or creating an account <- if neither happens they quit
    print("Welcome to inCollege by Team Montana!")
    print(user_story)
    print("")
    print("Why you should join in InCollege? Watch the video!")
    print("")
    print("Please choose from the following menu:")
    print("1 - Log into an existing account")
    print("2 - Create an account")
    print("3 - Play a video")
    print("4 - Find a contact in InCollege")
    userChoice = input("Enter your selection here: ")

    # come back later to implement a way for the user to go back to the lines above
    if userChoice == "1":
        start_options.login_account(connection)
    elif userChoice == "2":
        start_options.create_account(connection)
    elif userChoice == "3":
        start_options.play_video()
    elif userChoice == "4":
        contact_firstname = input("Please enter contact's first name: ")
        contact_lastname = input("Please enter contact's last name: ")
        start_options.join_contact(contact_firstname, contact_lastname, connection)
    else:
        print("I did not recognize your input")
        connection.close()
        exit()

    # at the very end, close database connection
    connection.close()
