import db_commands
import account_define
import user_options
import new_user_notifications
from datetime import datetime

def succ_story(filename):
    try:
        file = open(filename)
    except IOError:
        print("Error: File could not open or does not exist.")
        return 0
    content = file.read()
    # returning the
    return content


def login_account(connection):
    # variable used to continue the attempt by the user to login
    succ_login = False
    # returns usernames from the database
    existing_usernames = db_commands.query_usernames_list(connection)
    username_password_tuples = db_commands.query_username_password(connection)
    username_input = None
    password_input = None
    # Need to implement later on for user to go back, in that case we can
    # just have a while true loop in main that encompasses all the code.
    # And break out of this statement if for another user input like "Back", which will break out of this while loop
    while succ_login is False and username_input != "Q":
        username_input = input("Enter your username, or Q to quit the program: ")
        if username_input == "Q":
            exit()
        else:
            password_input = input("Enter your password: ")
            # If userLogin continues to return false then keep running this while loop
            # and ask for usernames or if the user wants to quit the program
            succ_login = account_define.user_login(username_input, password_input, existing_usernames,
                                                   username_password_tuples)
            if succ_login == True:
                # Epic 8
                new_user_notifications.update_logout_time(connection, username_input)


def create_account(connection):
    print("We are creating an account\n")
    username_input = input("Please enter a new username ")
    existing_usernames = db_commands.query_usernames_list(connection)

    # Otherwise, safe to create username
    # tests if safe username
    while True:
        if len(existing_usernames) > 10:
            print("The system has too many users already.")
            return 0
        elif not account_define.username_meets_qualifications(username_input, existing_usernames):
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
        if user_options.does_user_exist(firstname_input, lastname_input):
            print("That name already exists in our system. Do you have a nickname you go by?")
        else:
            break
    #Choose tier of membership
    print("You are signing up for an InCollege account. You can now choose to be a Standard or Plus membership.")
    student_mem = tier_member()
    # Create row in users table
    # Adds English as Language and sets defaults for Privacy settings
    #Add tier of student to user table
    user_information = (username_input, password_input, firstname_input, lastname_input, student_mem, 
                        "English", "Send Emails", "Send SMS", "Target Ads", "TITLE:NULL", "MAJOR:NULL", "UNIVERSITY:NULL", "STUDENTINFO:NULL", "EDUCATION:NULL")
    db_commands.create_row_in_users_table(connection, user_information)
    new_user_notifications.add_user_logout_times(connection, username_input, firstname_input, lastname_input)

    training_info = (username_input, )
    db_commands.create_row_in_trainings_table(connection, training_info)

    print("Successfully created your account. You are now logged in.")
    user_options.additional_options(username_input)

    # Updates users log out time
    new_user_notifications.update_logout_time(connection, username_input)

def play_video():
    # end='' removes the new line that comes after the print statement
    print("Video is now playing.", end='')
    return 0


def join_contact(contact_firstname, contact_lastname, connection):
    contact_exist = user_options.does_user_exist(contact_firstname, contact_lastname)
    if contact_exist is True:
        print("They are part of the InCollege system.")
        print("Do you want to connect with this contact?")
        print("1 - Log into an existing account")
        print("2 - Create an account")
        print("3 - Return to the previous menu")
        user_choice = input("Enter your selection here: ")
        if user_choice == "1":
            login_account(connection)
        elif user_choice == "2":
            create_account(connection)
        elif user_choice == "3":
            return 0
    else:
        print("They are not part of the InCollege system.")
        return 0


def get_user_option(limit1, limit2):
    while True:
        try:
            option1 = int(
                input(f"Please enter your option ({limit1}-{limit2}): "))
            return option1
        except ValueError:
            print("Input has to be an integer")

#Epic 7
def tier_member():
    message = '''Please choose tier of membership:
    1 - Standard for free
    2 - Plus for 10$/month'''
    print(message)
    
    while True:
        user_choice = input("Enter your selection here: ")
        if user_choice == "1":
            member_tier = "Standard"
            break
        elif user_choice == "2":
            member_tier = "Plus"
            break
        else:
            print("Invalid input. Please enter 1 for Standard, or 2 for Plus member.")
    return member_tier
###   