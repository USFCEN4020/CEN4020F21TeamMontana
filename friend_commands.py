import db_commands


def create_friend_posting(sender):
    print("Let's get started in sending a friend request")
    # There are no constraints on the actual experience posting
    status = "PENDING"

    user_choice_opt = input("How do you want to search for the user? \n1 - By last name\n2 - By university\n3 - By major\n4 - Return to previous menu")
    while(True):
        if user_choice_opt == "1":
            search_result = input("Please enter the users last name.")

            connection = db_commands.create_connection("userDB")
            cursor = connection.cursor()
            cursor.execute('''SELECT username FROM users WHERE lastname = ?''', (search_result,))
            usernames = cursor.fetchall()
            if len(usernames) == 0:
                print("No users with the last name of " + search_result + " exists in our system")
            else:
                print("Here is a list of results:\n")
                print(usernames)
                status = "PENDING"
                while (True):
                    select = input("\nSelect which one you want to send the request to, or enter 0 to exit.\n")
                    if 0 > int(select) > len(usernames):
                        print("Option selected is not part of the list.")
                        continue
                    elif int(select) == 0:
                        return
                    elif int(select) <= len(usernames):
                        friend_information = (sender, status, usernames[int(select) - 1])
                    else:
                        print("Please enter in a number as your choice")
                        continue
                    break
                db_commands.create_row_in_friend_table(connection, friend_information)

        elif user_choice_opt == "2":
            search_result = input("Please enter the users university.")

            connection = db_commands.create_connection("userDB")
            cursor = connection.cursor()
            cursor.execute('''SELECT username FROM users WHERE university = ?''', (search_result,))
            usernames = cursor.fetchall()
            if len(usernames) == 0:
                print("No users with the university of " + search_result + " exists in our system")
            else:
                print("Here is a list of results:\n")
                print(usernames)
                status = "PENDING"
                while (True):
                    select = input("\nSelect which one you want to send the request to, or enter 0 to exit.\n")
                    if 0 > int(select) > len(usernames):
                        print("Option selected is not part of the list.")
                        continue
                    elif int(select) == 0:
                        return
                    elif int(select) <= len(usernames):
                        friend_information = (sender, status, usernames[int(select) - 1])
                    else:
                        print("Please enter in a number as your choice")
                        continue
                    break
                db_commands.create_row_in_friend_table(friend_information)

        elif user_choice_opt == "3":
            search_result = input("Please enter the users major.")

            connection = db_commands.create_connection("userDB")
            cursor = connection.cursor()
            cursor.execute('''SELECT username FROM users WHERE major = ?''', (search_result,))
            usernames = cursor.fetchall()
            if len(usernames) == 0:
                print("No users with the major of " + search_result + " exists in our system")
            else:
                print("Here is a list of results:\n")
                print(usernames)
                status = "PENDING"
                while (True):
                    select = input("\nSelect which one you want to send the request to, or enter 0 to exit.\n")
                    if 0 > int(select) > len(usernames):
                        print("Option selected is not part of the list.")
                        continue
                    elif int(select) == 0:
                        return
                    elif int(select) <= len(usernames):
                        friend_information = (sender, status, usernames[int(select) - 1])
                    else:
                        print("Please enter in a number as your choice")
                        continue
                    break
                db_commands.create_row_in_friend_table(friend_information)

        elif user_choice_opt == "4":
            return
        else:
            print("Invalid input. Please enter in a digit between 1 thru 4.")
            continue

connection = db_commands.create_connection("userDB")
db_commands.fill_database(connection)
create_friend_posting("sender")
