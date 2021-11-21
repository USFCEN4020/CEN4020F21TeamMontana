# Python program to
# demonstrate with
# statement

import message_options
import db_commands
import user_options
import start_options


# Writing to file
def create_mycollege_users():
    username_list = db_commands.query_usernames_list(db_commands.create_connection(db_commands.database_name))
    with open("MyCollege_users.txt", "w") as file:
        for user in username_list:
            user_info = [user[0] + " " + db_commands.query_membership_status(user[0])[0] + "\n"]
            file.writelines(user_info)


def get_mycollege_users():
    list = []
    try:
        with open("MyCollege_users.txt") as file:
            for line in file:
                list.append(line.strip())
    except FileNotFoundError:
        print("MyCollege_users.txt is missing from directory")
    return list


def print_mycollege_users():
    try:
        with open("MyCollege_users.txt") as file:
            for line in file:
                print("{}".format(line.strip()))
    except FileNotFoundError:
        print("MyCollege_users.txt is missing from directory")


def read_student_accounts():
    try:
        with open("studentAccounts.txt", "r") as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if count % 4 == 0:
                    values = line.split(' ')
                elif count % 4 == 1:
                    values.append(line.split('\n'))
                elif count % 4 == 2:
                    values.append(line.split('\n'))
                elif count % 4 == 3:
                    values.append(line.split('\n'))
                    if user_options.does_user_exist(values[1], values[2]):
                        continue

                    user = (values[0], values[5][0], values[1], values[2], values[4][0], "English", "Send Emails", "Send SMS",
                    "Target Ads", "TITLE:NULL", "MAJOR:NULL", "UNIVERSITY:NULL", "STUDENTINFO:NULL", "EDUCATION:NULL")
                    db_commands.create_row_in_users_table(db_commands.create_connection(db_commands.database_name), user)
                count += 1
    except FileNotFoundError:
        print("studentAccounts.txt is missing from directory")


def print_student_accounts():
    with open("studentAccounts.txt") as file:
        for line in file:
            print("{}".format(line.strip()))
