import db_commands
import experience_commands


def view_profile(username):
    connection = db_commands.create_connection(db_commands.database_name)
    cursor = connection.cursor()

    cursor.execute('''SELECT title FROM users WHERE username = ?''', (username,))
    title = cursor.fetchone()

    cursor.execute('''SELECT major FROM users WHERE username = ?''', (username,))
    major = cursor.fetchone()

    cursor.execute('''SELECT university FROM users WHERE username = ?''', (username,))
    university = cursor.fetchone()

    cursor.execute('''SELECT studentinfo FROM users WHERE username = ?''', (username,))
    info = cursor.fetchone()

    cursor.execute('''SELECT education FROM users WHERE username = ?''', (username,))
    education = cursor.fetchone()

    cursor.execute('''SELECT firstname FROM users WHERE username = ?''', (username,))
    firstname = cursor.fetchone()

    cursor.execute('''SELECT lastname FROM users WHERE username = ?''', (username,))
    lastname = cursor.fetchone()

    print(firstname, " ", lastname)
    print("Profile Information: \n --------------------- \n")
    print("Title: ", title)
    print("Major: ", major)
    print("University: ", university)
    print("Student Info: ", info)
    print("Education: ", education)

    db_commands.print_experiences(connection, username)
 
def print_portfolio_options():
    print("Please choose which options to modify")
    print("1 - Enter Title")
    print("2 - Enter Major")
    print("3 - Enter University name")
    print("4 - Enter Information about student")
    print("5 - Enter Experience")
    print("6 - Enter Education")
    print("7 - View Profile")
    print("0 - Return to previous menu")


def Enter_Title(username):
    while True:
        print("Would you like to enter your Title")
        print("1 - Enter Title")
        print("0 - Exit")

        user_input = input("Enter your selection here (0-1): ")

        if user_input == "1":
            user_title = input("Please enter your Title:\n")
            db_commands.User_Title(username, user_title)
            continue
        elif user_input == "0":
            break
        else:
            print("\n Invalid Input \n")
            continue


def Enter_Major(username):
    while True:
        print("Would you like to enter your Major")
        print("1 - Enter Major")
        print("0 - Exit")

        user_input = input("Enter your selection here (0-1): ")

        if user_input == "1":
            user_response = input("Please enter your Major:\n")
            user_response.title()
            db_commands.User_Major(username, user_response)
            continue
        elif user_input == "0":
            break
        else:
            print("\n Invalid Input \n")
            continue


def Enter_University_Name(username):
    while True:
        print("Would you like to enter your Current University")
        print("1 - Enter University Name")
        print("0 - Exit")

        user_input = input("Enter your selection here (0-1): ")

        if user_input == "1":
            user_response = input("Please enter your University:\n")
            user_response.title()
            db_commands.User_University(username, user_response)
            continue
        elif user_input == "0":
            break
        else:
            print("\n Invalid Input \n")
            continue


def Enter_Student_Info(username):
    while True:
        print("Would you like to enter some Student Information")
        print("1 - Enter Student Information")
        print("0 - Exit")

        user_input = input("Enter your selection here (0-1): ")

        if user_input == "1":
            user_response = input("Please enter your Student Information:\n")
            db_commands.User_Info(username, user_response)
            continue
        elif user_input == "0":
            break
        else:
            print("\n Invalid Input \n")
            continue


def Enter_Education(username):
    while True:
        print("Would you like to enter your Education")
        print("1 - Enter Education")
        print("0 - Exit")

        user_input = input("Enter your selection here (0-1): ")

        if user_input == "1":
            user_university = input("Please enter your University:\n")
            user_university.title()
            user_degree = input("Please enter your Degree at that University:\n")
            user_years = input("Please enter your how many years attended at that university:\n")
            user_response = "You attended " + user_university + " for " + user_years + " years to get a degree in " + user_degree
            db_commands.User_Education(username, user_response)
            continue
        elif user_input == "0":
            break
        else:
            print("\n Invalid Input \n")
            continue


def portfolio_options(username):
    while True:
        print_portfolio_options()
        user_input = input("Enter Selection Here (0-7): ")

        if user_input == "1":
            Enter_Title(username)
            continue
        elif user_input == "2":
            Enter_Major(username)
            continue
        elif user_input == "3":
            Enter_University_Name(username)
            continue
        elif user_input == "4":
            Enter_Student_Info(username)
            continue
        elif user_input == "5":
            experience_commands.create_experience_posting(username)
            continue
        elif user_input == "6":
            Enter_Education(username)
            continue
        elif user_input == "7":
            view_profile(username)
            continue
        elif user_input == "0":
            break
        else:
            print("\nINVALID INPUT\n")
            continue
