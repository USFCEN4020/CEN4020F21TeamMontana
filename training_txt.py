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
    print("\n\t\t\tPlease select a training option or enter 0 to return:")
    count = 0
    try:
        with open("newtraining.txt") as file:
            for line in file:
                print("\t\t\t{} - {}".format(count, line.strip()))
                count += 1
        print("\n")
    except FileNotFoundError:
        print("newtraining.txt is missing from directory")


def create_mycollege_raining():
    username_list = db_commands.query_usernames_list(db_commands.create_connection(db_commands.database_name))
    with open("MyCollege_training.txt", "w") as file:
        for user in username_list:
            i = 1
            line = "\n"
            while i < 6:
                if (db_commands.get_trainings_status(db_commands.create_connection(db_commands.database_name), user[0], i))[0] == 'FINISHED':
                    if i == 1:
                        line += "In College Learning" + "\n"
                    elif i == 2:
                        line += "Train the Trainer"+ "\n"
                    elif i == 3:
                        line += "Gamification"+ "\n"
                    elif i == 4:
                        line += "Architecture"+ "\n"
                    elif i == 5:
                        line += "Project Management"+ "\n"
                i += 1
            user_info = [user[0] + " " + line + "\n" + "=====" + "\n"]
            file.writelines(user_info)

