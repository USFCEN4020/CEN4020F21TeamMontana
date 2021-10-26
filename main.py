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
import useful_links_options
import important_links_group

database_name = "userDB"


def print_start_menu():
    start_menu = """
            Please choose from the following menu:
            1 - Log into an existing account
            2 - Create an account
            3 - Play a video
            4 - Find a contact in InCollege
            5 - Useful Links Group
            6 - InCollege Important Links Group
            7 - Exit the program

            """
    print(start_menu)


# Main function
def main_menu():
    connection = db_commands.create_connection(database_name)
    # Create tables if not exist
    db_commands.create_table(connection, db_commands.user_table)
    db_commands.create_table(connection, db_commands.job_table)
    db_commands.create_table(connection, db_commands.user_job_table)
    db_commands.create_table(connection, db_commands.deleted_jobs)
    db_commands.create_table(connection, db_commands.experience_table)
    db_commands.create_table(connection, db_commands.friend_table)
    # db_commands.print_database(connection)

    user_story = start_options.succ_story("Student_story.txt")
    # log_in_status = False
    # Welcome everyone to InCollege, a story of success student
    # Prompt user for either logging in or creating an account <- if neither happens they quit
    print("Welcome to inCollege by Team Montana!")
    print(user_story)
    print("")
    print("Why you should join in InCollege? Watch the video!")
    print("")

    while True:
        print_start_menu()
        user_choice = start_options.get_user_option(1, 7)
        while user_choice < 1 or user_choice > 7:
            print("Invalid input. Try again")
            user_choice = start_options.get_user_option(1, 7)
        # come back later to implement a way for the user to go back to the lines above
        if user_choice == 1:
            start_options.login_account(connection)
            continue
        elif user_choice == 2:
            start_options.create_account(connection)
            continue
        elif user_choice == 3:
            start_options.play_video()
            continue
        elif user_choice == 4:
            contact_firstname = input("Please enter contact's first name: ")
            contact_lastname = input("Please enter contact's last name: ")
            start_options.join_contact(contact_firstname, contact_lastname, connection)
            continue
        elif user_choice == 5:
            useful_links_options.useful_link()
            continue
        elif user_choice == 6:
            important_links_group.important_links_visitors()
            continue
        else:
            print("Exit the program.")
            connection.close()
            exit()


if __name__ == '__main__':
    main_menu()
