# Python program to
# demonstrate with
# statement

import message_options
import db_commands
import start_options
import main


def business_analysis_strategy_menu():
    business_analysis_strategy = """
            Please select a training option or enter 5 to return:
            1 - How to use In College learning
            2 - Train the trainer
            3 - Gamification of learning

            Not seeing what you're looking for? Sign in to see all 7,609 results.
            """
    connection = db_commands.create_connection(db_commands.database_name)

    while True:
        print(business_analysis_strategy)
        user_choice = start_options.get_user_option(1, 3)
        while user_choice < 1 or user_choice > 3:
            print("Invalid input. Try again")
            user_choice = start_options.get_user_option(1, 3)
        # come back later to implement a way for the user to go back to the lines above
        if user_choice == 1:
            db_commands.update_trainings(db_commands.create_connection(db_commands.database_name), 3)
        elif user_choice == 2:
            db_commands.update_trainings(db_commands.create_connection(db_commands.database_name), 4)
        elif user_choice == 3:
            db_commands.update_trainings(db_commands.create_connection(db_commands.database_name), 5)
        else:
            print("Returning to main menu...")


# Writing to file
def create_newtraining():
    username_list = db_commands.query_usernames_list(db_commands.create_connection(db_commands.database_name))
    with open("newtraining.txt", "w") as file:
        for user in username_list:
            user_info = [user[0] + " " + db_commands.query_membership_status(user[0])[0] + "\n"]
            file.writelines(user_info)


def get_newtraining():
    list = []
    try:
        with open("newtraining.txt") as file:
            for line in file:
                list.append(line.strip())
    except FileNotFoundError:
        print("newtraining.txt is missing from directory")
    return list


def menu_newtraining():
    connection = db_commands.create_connection(db_commands.database_name)

    print("Please select a training option or enter 0 to return:")
    while True:
        count = 0
        try:
            with open("newtraining.txt") as file:
                for line in file:
                    print("{} - {}".format(count, line.strip()))
                    count += 1
        except FileNotFoundError:
            print("newtraining.txt is missing from directory")
            break
        user_choice = start_options.get_user_option(0, len(get_newtraining())-1)
        while user_choice < 0 or user_choice > len(get_newtraining())-1:
            print("Invalid input. Try again")
            user_choice = start_options.get_user_option(0, len(get_newtraining())-1)
        # come back later to implement a way for the user to go back to the lines above
        if user_choice == 0:
            print("Returning to main menu...")
            break
        if user_choice == 1:
            db_commands.update_trainings(db_commands.create_connection(db_commands.database_name), 1)
            continue
        elif user_choice == 2:
            db_commands.update_trainings(db_commands.create_connection(db_commands.database_name), 2)
            continue
        elif user_choice == 3:
            business_analysis_strategy_menu()
            continue
        else:
            db_commands.update_trainings(db_commands.create_connection(db_commands.database_name), 6)
            continue
