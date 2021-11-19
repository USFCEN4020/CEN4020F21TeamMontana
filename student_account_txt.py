# Python program to
# demonstrate with
# statement

import message_options
import db_commands


# Writing to file
def create_mycollege_users():
    username_list = db_commands.query_usernames_list(db_commands.create_connection(db_commands.database_name))
    with open("MyCollege_users.txt", "w") as file:
        for user in username_list:
            user_info = [user[0] + " " + db_commands.query_membership_status(user[0])[0] + "\n"]
            file.writelines(user_info)


def get_mycollege_users():
    list = []
    with open("MyCollege_users.txt") as file:
        for line in file:
            list.append(line.strip())
    return list


def print_mycollege_users():
    with open("MyCollege_users.txt") as file:
        for line in file:
            print("{}".format(line.strip()))


# Writing to file
def create_student_accounts():
    user_list = db_commands.create_connection(db_commands.database_name).cursor().execute("SELECT * FROM users")
    #user_list = db_commands.query_usernames_list(db_commands.create_connection(db_commands.database_name))
    with open("studentAccounts.txt", "w") as file:
        for user in user_list:
            user_info = [user[0] + " " + user[2] + " " + user[3] + " " + "\n" + db_commands.query_membership_status(user[0])[0] + "\n" + user[1] + "\n" + "=====" + "\n"]
            file.writelines(user_info)


def print_student_accounts():
    with open("studentAccounts.txt") as file:
        for line in file:
            print("{}".format(line.strip()))
