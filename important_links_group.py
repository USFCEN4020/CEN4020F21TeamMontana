import start_options
import db_commands

# Changes Language setting
def ChangeLanguage(username):
    con = db_commands.create_connection(db_commands.database_name)
    db_commands.print_database(con)

    while True:
        print("Please choose a Language:")
        print("1 - English")
        print("2 - Spanish")
        print("0 - Exit Menu")
        user_input = input("Enter your selection here... (0-2): ")

        #lang passes language into database
        if user_input == "1":
            lang = 'English'
            db_commands.ChangeLang(username, lang)
            print("Default Language is now English\n")
            break
        elif user_input == "2":
            lang = 'Spanish'
            db_commands.ChangeLang(username, lang)
            print("Default Language is now Spanish\n")
            break
        elif user_input == "0":
            break
        else:
            print("Invalid Input")

# Prints Links for InCollege Members
def PrintImportantLinksForUsers():
    print("Please choose from the following menu:")
    print("1 - Copyright Notice")
    print("2 - About")
    print("3 - Accessibility")
    print("4 - User Agreement Policy ")
    print("5 - Privacy Policy")
    print("6 - Cookie Policy")
    print("7 - Brand Policy")
    print("0 - Exit Menu")

# Prints Links for InCollege Visitors
def PrintImportantLinksForVisitors():
    print("Please choose from the following menu:")
    print("1 - Copyright Notice")
    print("2 - About")
    print("3 - Accessibility")
    print("4 - User Agreement Policy ")
    print("5 - Cookie Policy")
    print("6 - Brand Policy")
    print("0 - Exit Menu")

#Changes User's Email Status
def EmailStatus(con, username):
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
            db_commands.SendEmailsStatus(username, 'Don\'t Send Emails')
            print("InCollege Will No Longer Send You Emails!")
            continue
        elif user_input == "0":
            break
        else:
            print("Invalid Input")

# Changes User SMS Status
def SMSStatus(con, username):
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
            db_commands.SendSMSStatus(username, 'Don\'t Send SMS')
            print("InCollege Will No Longer Send You SMS!")
            continue
        elif user_input == "0":
            break
        else:
            print("Invalid Input")

# Changes User's Advertising Status
def TargetedAdvertisingStatus(con, username):
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
            db_commands.TargetAdsStatus(username, 'Don\'t Target Ads')
            print("InCollege Will No Longer Send You Targeted Ads!")
            continue
        elif user_input == "0":
            break
        else:
            print("Invalid Input")

# Opens Guest Options for Users
def GuestOptions(username):
    connection = db_commands.create_connection(db_commands.database_name)
    print("Guest Options:")
    while True:
        print("Please choose from the following menu:")
        print("1 - Turn On/Off InCollege Emails")
        print("2 - Turn On/Off SMS Notifications")
        print("3 - Turn On/Off Targeted Advertisings")
        print("4 - Change Language")
        print("0 - Exit")
        userMenuChoice = input("Enter your Selection Here... (0-4)")

        if userMenuChoice == "1":
            EmailStatus(connection, username)
            continue
        elif userMenuChoice == "2":
            SMSStatus(connection, username)
            continue
        elif userMenuChoice == "3":
            TargetedAdvertisingStatus(connection, username)
            continue
        elif userMenuChoice == "4":
            ChangeLanguage(username)
            continue
        elif userMenuChoice == "0":
            break
        else:
            print("Invalid Input")
            continue

def important_links_Users(username):
    while True:
        PrintImportantLinksForUsers()
        userMenuChoice = input("Enter your selection here... (0-9): ")

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
                userMenuChoice = input("Enter Your Selection Here... (0-1): ")

                if userMenuChoice == "1":
                    GuestOptions(username)
                elif userMenuChoice == "0":
                    break
                else:
                    print("Invalid Input")
                    continue

        elif userMenuChoice == "6":
            print("Cookie Policy\n")
            continue
        elif userMenuChoice == "7":
            print("Brand Policy\n")
            continue
        elif userMenuChoice == "0":
            break
        else:
            print("Invalid Input")
            break


def important_links_Visitors():
    while True:
        PrintImportantLinksForVisitors()
        userMenuChoice = input("Enter your selection here... (0-9): ")

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
            print("Cookie Policy\n")
            continue
        elif userMenuChoice == "6":
            print("Brand Policy\n")
            continue
        elif userMenuChoice == "0":
            break
        else:
            print("Invalid Input")
            break
