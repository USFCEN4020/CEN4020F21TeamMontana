import db_commands
import message_options

def send_message_test(username, friend_to_message, message):
    # Add code here for sending a message
    # Get if we are a premium member or not
    membership_status = db_commands.query_membership_status(username)
    connection = db_commands.create_connection(db_commands.database_name)
    username_list = db_commands.query_friend(username)
    friends_list = [x[0] for x in username_list]
    status = "NEW"
    if membership_status[0] == "Standard":
        # Standard members can only send messages if they are friends
        print("\nYou are a Standard user, so you can only send messages to your friends.")
        print("Please choose a friend:\n\n")
        print(*friends_list, sep="\n")
        print()
        if friend_to_message in friends_list:
            info = (username, friend_to_message, message, status)
            db_commands.create_row_in_message_table(connection, info)
            print("\nMessage successfully sent\n")
        else:
            print("I'm sorry, you are not friends with that person")
    elif membership_status[0] == "Plus":
        print("\nYou are a Plus user, so you can send messages to anyone.")
        print("Please choose someone:")
        users_list = db_commands.query_usernames_list(connection)
        usernames_list = [x[0] for x in users_list]
        usernames_list.remove(username)
        print(*usernames_list, sep="\n")
        person_to_message = friend_to_message
        if person_to_message in usernames_list:
            print()
            info = (username, person_to_message, message, status)
            db_commands.create_row_in_message_table(connection, info)
            print("\nMessage successfully sent\n")
    return 0

def member_options_test(username):
    membership_status = db_commands.query_membership_status(username)
    if membership_status[0] == "Standard":
        message_options.list_friend_member(username)
    elif membership_status[0] == "Plus":
        message_options.list_member(username)
    else:
        print("Invalid member status.")

db_commands.delete_all_database_info(db_commands.create_connection("userDB"))
db_commands.fill_database(db_commands.create_connection("userDB"))

member_options_test("username2") #Should only list friends
member_options_test("username3") #Should list all members
member_options_test("username4") #Should only list friends
member_options_test("username5") #Should list all members

send_message_test("username2","username3","test2") #This should say it can't send a message (Standard messaging options)
send_message_test("username3","username5","test3") #This should send (Plus messaging options)
send_message_test("username4","username2","test4") #This should send (Standard messaging options)
send_message_test("username5","username3","test5") #This should send (Plus messaging options)
send_message_test("username3","username2","test6") #This should send (Plus messaging options)
message_options.display_inbox("username2") #This should have recieved test4 and test6 message (along with 3 others)
message_options.display_inbox("username3") #This should have recieved test5 message
message_options.display_inbox("username4") #This should have recieved no message
message_options.display_inbox("username5") #This should have recieved test3 message