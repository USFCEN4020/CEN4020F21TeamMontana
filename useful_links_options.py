import start_options
import db_commands

database_name = "userDB"
connection = db_commands.create_connection(database_name)


def print_general_link():
    links = """
        General links available:
        1. Sign Up
        2. Help Center
        3. About
        4. Press
        5. Blog
        6. Careers
        7. Developers
        8. Go Back

        """
    print(links)


def general_link():

    while True:
        print_general_link()
        options = start_options.get_user_option(1, 8)
        while options < 1 or options > 8:
            print("Invalid input. Try again")
            options = start_options.get_user_option(1, 8)
        if options == 1:
            start_options.create_account(connection)
            continue
        elif options == 2:
            print("We're here to help.")
            continue
        elif options == 3:
            print("InCollege: Welcome to InCollege, the world's largest college student network "
                  "with many users in many countries and territories worldwide")
            continue
        elif options == 4:
            print("InCollege Pressroom: Stay on top of the latest news, updates, and reports")
            continue
        elif options == 5:
            print("Under Construction")
            continue
        elif options == 6:
            print("Under Construction")
            continue
        elif options == 7:
            print("Under Construction")
            continue
        elif options == 8:
            print("Going back to 'Useful Links' Menu")
            return False


def print_useful_link():
    links = """
        Useful links available:
        1. General
        2. Browse InCollege
        3. Business Solutions
        4. Directories
        5. Go Back

        """
    print(links)


def useful_link():

    while True:
        print_useful_link()
        option = start_options.get_user_option(1, 5)
        while option < 1 or option > 5:
            print("Invalid input. Try again")
            option = start_options.get_user_option(1, 5)
        if option == 1:
            general_link()
        elif option == 2:
            print("Under Construction")
            
        elif option == 3:
            print("Under Construction")
            
        elif option == 4:
            print("Under Construction")
           
        elif option == 5:
            print("Going back to the Main Menu")
            return False
