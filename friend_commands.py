import db_commands
import sqlite3


def query_friend_paramater(username_paramater, search_parameter):
    connection = db_commands.create_connection("userDB")
    cursor = connection.cursor()
    if search_parameter == "lastname":
        cursor.execute("SELECT username FROM users WHERE lastname = ?", (username_paramater,))
    elif search_parameter == "university":
        cursor.execute("SELECT username FROM users WHERE university = ?", (username_paramater,))
    elif search_parameter == "major":
        cursor.execute("SELECT username FROM users WHERE major = ?", (username_paramater,))
    usernames = cursor.fetchall()
    # returns a list of usernames that match the paramter entered
    return usernames


# checks to see if there is a pair between sender and reciver in the friends table
def check_friend_exist(sender, receiver):
    connection = db_commands.create_connection("userDB")
    cursor = connection.cursor()
    # either you already sent to them or the person you are sending to has already sent you a friend request
    # this also takes into account if sender and receiver are both already friends.
    cursor.execute('''SELECT * FROM friends WHERE sender = ? AND receiver = ? UNION
                   SELECT * FROM friends WHERE sender = ? AND receiver = ?''', (sender, receiver, receiver, sender,))
    friend_exist = cursor.fetchall()
    if len(friend_exist) == 0:
        return False
    elif len(friend_exist) > 0:
        return True


def create_friend_posting(sender):
    print("Let's get started in sending a friend request")
    # There are no constraints on the actual experience posting
    status = "PENDING"

    while True:
        user_choice_opt = input("How do you want to search for the user? \n1 - By last name\n2 - By university\n3 - By major\n4 - Return to previous menu\n")
        if user_choice_opt == "1":
            search_result = input("Please enter the users last name:\n")
            search_parameter = "lastname"
            username_list = query_friend_paramater(search_result, search_parameter)
            found_usernames = [x[0] for x in username_list]

            if len(found_usernames) == 0:
                print("No users with the last name of " + search_result + " exists in our system")
                continue
            elif len(found_usernames) > 0:
                print("Here is a list of results:\n")
                print(*found_usernames, sep="\n")
                while True:
                    friend_receiver = input("\nEnter the username you want to send a friend request to, or enter exit to find another user.\n")
                    if check_friend_exist(sender, friend_receiver):
                        print("You are both already friends, or there is already an existing friend request between you and them that is still pending")
                        continue
                    if friend_receiver in found_usernames:
                        # Tries to enter into a row into the friends table,
                        friend_info = (sender, status, friend_receiver)
                        db_commands.create_row_in_friend_table(db_commands.create_connection("userDB"), friend_info)
                        break
                    if friend_receiver == "exit":
                        break
                    else:
                        print("The user entered does not exist, you entered the username wrong, or did not specify to exit")
                        continue

        elif user_choice_opt == "2":
            search_result = input("Please enter the users university:\n")
            search_parameter = "university"
            username_list = query_friend_paramater(search_result, search_parameter)
            found_usernames = [x[0] for x in username_list]

            if len(found_usernames) == 0:
                print("No users with the university of " + search_result + " exists in our system")
                continue
            elif len(found_usernames) > 0:
                print("Here is a list of results:\n")
                print(*found_usernames, sep="\n")
                while True:
                    friend_receiver = input("\nEnter the username you want to send a friend request to, or enter exit to find another user.\n")
                    if check_friend_exist(sender, friend_receiver):
                        print("You are both already friends, or there is already an existing friend request between you and them that is still pending")
                        continue
                    if friend_receiver in found_usernames:
                        friend_info = (sender, status, friend_receiver)
                        db_commands.create_row_in_friend_table(db_commands.create_connection("userDB"), friend_info)
                        break
                    elif friend_receiver == "exit":
                        break
                    else:
                        print("The user entered does not exist, you entered the username wrong, or did not specify to exit")
                        continue

        elif user_choice_opt == "3":
            search_result = input("Please enter the users major:\n")
            search_parameter == "major"
            username_list = query_friend_paramater(search_result, search_parameter)
            found_usernames = [x[0] for x in username_list]

            if len(found_usernames) == 0:
                print("No users with the major of " + search_result + " exists in our system")
                continue
            elif len(found_usernames) > 0:
                print("Here is a list of results:\n")
                print(*found_usernames, sep="\n")
                while True:
                    friend_receiver = input("\nEnter the username you want to send a friend request to, or enter exit to find another user.\n")
                    if check_friend_exist(sender, friend_receiver):
                        print("You are both already friends, or there is already an existing friend request between you and them that is still pending")
                        continue
                    if friend_receiver in found_usernames:
                        friend_info = (sender, status, friend_receiver)
                        db_commands.create_row_in_friend_table(db_commands.create_connection("userDB"), friend_info)
                        break
                    elif friend_receiver == "exit":
                        break
                    else:
                        print("The user entered does not exist, you entered the username wrong, or did not specify to exit")
                        continue

        elif user_choice_opt == "4":
            return 0
        else:
            print("Invalid input. Please enter in a digit between 1 thorugh 4.")
            continue
