import db_commands

def view_profile(username):


def print_portfolio_options():
    print("Please choose which options to modify")
    print("1 - Enter Title")
    print("2 - Enter Major")
    print("3 - Enter University name")
    print("4 - Enter Information about student")
    print("5 - Enter Experience")
    print("6 - Enter Education")

def Enter_Title(username):

def Enter_Major(username):

def Enter_University_Name(username):

def Enter_Student_Info(username):

def Enter_Experience(username):

def Enter_Education(username):


def portfolio_options(username):
    while True:
        print_portfolio_options()
        user_input = input("Enter Selection Here (0-6): ")

        if user_input == "1":
            Enter_Title(usernme)
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
            Enter_Experience(username)
            continue
        elif user_input == "6":
            Enter_Education(username)
            continue
        elif user_input == "0":
            break
        else:
            print("\nINVALID INPUT\n")
            continue

