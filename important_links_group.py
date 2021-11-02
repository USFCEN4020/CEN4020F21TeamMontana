import start_options
import db_commands


# Changes Language setting
def change_language(username):
    con = db_commands.create_connection(db_commands.database_name)

    while True:
        print("Please choose a Language:")
        print("1 - English")
        print("2 - Spanish")
        print("0 - Exit Menu")
        user_input = input("Enter your selection here... (0-2): ")

        # lang passes language into database
        if user_input == "1":
            lang = 'English'
            db_commands.ChangeLang(username, lang)
            print("Default Language is now English")
            break
        elif user_input == "2":
            lang = 'Spanish'
            db_commands.ChangeLang(username, lang)
            print("Default Language is now Spanish")
            break
        elif user_input == "0":
            break
        else:
            print("Invalid Input")
            continue


# Prints Links for InCollege Members
def print_important_links_for_users():
    print("Please choose from the following menu:")
    print("1 - Copyright Notice")
    print("2 - About")
    print("3 - Accessibility")
    print("4 - User Agreement Policy")
    print("5 - Privacy Policy")
    print("6 - Cookie Policy")
    print("7 - Brand Policy")
    print("8 - Exit Menu")


# Prints Links for InCollege Visitors
def print_important_links_for_visitors():
    print("Please choose from the following menu:")
    print("1 - Copyright Notice")
    print("2 - About")
    print("3 - Accessibility")
    print("4 - User Agreement Policy")
    print("5 - Cookie Policy")
    print("6 - Brand Policy")
    print("7 - Exit Menu")


# Changes User's Email Status
def email_status(con, username):
    while True:
        print("Would You like To Receive Emails:")
        print("1 - Send Emails")
        print("2 - Don't Send Emails")
        print("0 - Exit Menu")
        user_input = input("Enter your selection here... (0-2): ")

        if user_input == "1":
            db_commands.SendEmailsStatus(username, 'Send Emails')
            print("InCollege Will Now Send You Emails!")
            continue
        elif user_input == "2":
            db_commands.SendEmailsStatus(username, "Don't Send Emails")
            print("InCollege Will No Longer Send You Emails!")
            continue
        elif user_input == "0":
            break
        else:
            print("Invalid Input")
            continue


# Changes User SMS Status
def sms_status(con, username):
    while True:
        print("Would You like To Receive SMS:")
        print("1 - Send SMS")
        print("2 - Don't Send SMS")
        print("0 - Exit Menu")
        user_input = input("Enter your selection here... (0-2): ")
        if user_input == "1":
            db_commands.SendSMSStatus(username, 'Send SMS')
            print("InCollege Will Now Send You SMS!")
            continue
        elif user_input == "2":
            db_commands.SendSMSStatus(username, "Don't Send SMS")
            print("InCollege Will No Longer Send You SMS!")
            continue
        elif user_input == "0":
            break
        else:
            print("Invalid Input")
            continue


# Changes User's Advertising Status
def targeted_advertising_status(con, username):
    while True:
        print("Would You like To Have Targeted Advertising:")
        print("1 - Target Ads")
        print("2 - Don't Target Ads")
        print("0 - Exit Menu")
        user_input = input("Enter your selection here... (0-2): ")
        if user_input == "1":
            db_commands.TargetAdsStatus(username, 'Target Ads')
            print("InCollege Will Now Send You Targeted Ads!")
            continue
        elif user_input == "2":
            db_commands.TargetAdsStatus(username, "Don't Target Ads")
            print("InCollege Will No Longer Send You Targeted Ads!")
            continue
        elif user_input == "0":
            break
        else:
            print("Invalid Input")
            continue


# Opens Guest Options for Users
def guest_options(username):
    connection = db_commands.create_connection(db_commands.database_name)
    print("Guest Options:")
    while True:
        print("Please choose from the following menu:")
        print("1 - Turn On/Off InCollege Emails")
        print("2 - Turn On/Off SMS Notifications")
        print("3 - Turn On/Off Targeted Advertisings")
        print("4 - Change Language")
        print("0 - Exit")
        user_menu_choice = input("Enter your Selection Here... (0-4): ")

        if user_menu_choice == "1":
            email_status(connection, username)
            continue
        elif user_menu_choice == "2":
            sms_status(connection, username)
            continue
        elif user_menu_choice == "3":
            targeted_advertising_status(connection, username)
            continue
        elif user_menu_choice == "4":
            change_language(username)
            continue
        elif user_menu_choice == "0":
            break
        else:
            print("Invalid Input")
            continue


def important_links_users(username):
    while True:
        print_important_links_for_users()
        user_menu_choice = input("Enter your selection here... (1-8): ")

        if user_menu_choice == "1":
            print("This work is copyrighted")
            continue
        elif user_menu_choice == "2":
            print("About InCollege")
            continue
        elif user_menu_choice == "3":
            print("Accessibility Remarks")
            continue
        elif user_menu_choice == "4":
            print("Agree with User Agreement")
            continue
        elif user_menu_choice == "5":
            print("Would you like to open Guest Options")

            while True:
                print("1 - Yes")
                print("0 - Exit")
                user_menu_choice = input("Enter Your Selection Here... (0-1): ")

                if user_menu_choice == "1":
                    guest_options(username)
                elif user_menu_choice == "0":
                    return 0

def important_link():
    while True:
        print("Please choose from the following menu:")
        print("1 - Copyright Notice")
        print("2 - About")
        print("3 - Accessibility")
        print("4 - User Agreement Policy ")
        print("5 - Privacy Policy")
        print("6 - Cookie Policy")
        print("7 - Brand Policy")
        print("8 - Guest Controls")
        print("9 - Languages")
        print("0 - Exit Menu")
        userMenuChoice = input("Enter your selection here... (0-9")

        if userMenuChoice == "1":
            print("This work is copyrighted\n")
            continue
        elif userMenuChoice == "2":
            print("About InCollege\n")
            continue
        elif userMenuChoice == "3":
            print("Accessibility Remarks\n")
            continue
        elif userMenuChoice == "4":
            print("Agree with User Agreement\n")
            continue
        elif userMenuChoice == "5":
            print("Would you like to open Guest Options\n")
            while True:
                print("1 - Yes")
                print("0 - Exit")
                userMenuChoice = input("Enter Your Selection Here... (0-1)")

                if userMenuChoice == "1":
                    print("Guest Options:")
                    while True:
                        print("Please choose from the following menu:")
                        print("1 - Turn Off InCollege Email")
                        print("2 - Turn Off SMS Notifications")
                        print("3 - Turn Off Targeted Advertising")
                        print("0 - Exit")
                        userMenuChoice = input("Enter your Selection Here... (0-3)")

                        if userMenuChoice == "1":
                            sendEmails = False
                            continue
                        elif userMenuChoice == "2":
                            sendSMS = False
                            continue
                        elif userMenuChoice == "3":
                            targetedAdvertising = False
                            continue
                        elif userMenuChoice == "0":
                            break
                        else:
                            print("Invalid Input")
                            continue
                    continue
                elif userMenuChoice == "0":

                    break
                else:
                    print("Invalid Input")
                    continue
        elif userMenuChoice == "6":
            print("Cookie Policy")
            continue
        elif userMenuChoice == "7":
            print("Brand Policy")
            continue
        elif userMenuChoice == "8":
            print("Going back to 'User Options' Menu")
            break
        else:
            print("Invalid Input")
            continue


def important_links_visitors():
    while True:
        print_important_links_for_visitors()
        user_menu_choice = input("Enter your selection here... (1-7): ")

        if user_menu_choice == "1":
            print("This work is copyrighted")
            continue
        elif user_menu_choice == "2":
            print("About InCollege")
            continue
        elif user_menu_choice == "3":
            print("Accessibility Remarks")
            continue
        elif user_menu_choice == "4":
            print("Agree with User Agreement")
            continue
        elif user_menu_choice == "5":
            print("Cookie Policy")
            continue
        elif user_menu_choice == "6":
            print("Brand Policy")
            continue
        elif user_menu_choice == "7":
            print("Going back to 'Main' Menu")
            break
        else:
            print("Invalid Input")
            continue



