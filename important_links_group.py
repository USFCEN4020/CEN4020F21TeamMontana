import start_options
import db_commands

def important_link():
    print("under construction.")
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
        userMenuChoice = input("Enter your selection here: ")

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
            print("Agree with Privacy Policy\n")
            continue
        elif userMenuChoice == "6":
            print("Accept Cookie Policy\n")
            continue
        elif userMenuChoice == "7":
            print("Accept Brand Policy\n")
            continue
        elif userMenuChoice == "8":
            print("Guest Controls\n")
            continue
        elif userMenuChoice == "9":
            print("Languages\n")
            continue
        elif userMenuChoice == "0":
            break
        else:
            print("Invalid Input")
            break