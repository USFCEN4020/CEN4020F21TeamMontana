import db_commands
import experience_commands

def view_profile(username):
    print("Profile Information: \n --------------------- \n")
    db_commands.print_experiences(username)

def print_portfolio_options():
    print("Please choose which options to modify")
    print("1 - Enter Title")
    print("2 - Enter Major")
    print("3 - Enter University name")
    print("4 - Enter Information about student")
    print("5 - Enter Experience")
    print("6 - Enter Education")
    print("0 - Return to previous menu")

def Enter_Title(username):
    print("currently under construction")


def Enter_Major(username):
    print("currently under construction")


def Enter_University_Name(username):
    print("currently under construction")


def Enter_Student_Info(username):
    print("currently under construction")


def Enter_Education(username):
    print("currently under construction")


def portfolio_options(username):
    while True:
        print_portfolio_options()
        user_input = input("Enter Selection Here (0-6): ")

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
        elif user_input == "0":
            break
        else:
            print("\nINVALID INPUT\n")
            continue