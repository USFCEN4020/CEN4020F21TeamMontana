import db_commands


def send_message(username):
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
        friend_to_message = input("Enter which friend you want to message:")
        if friend_to_message in friends_list:
            message = input("What message do you want to send?\n")
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
        person_to_message = input("Enter which person you want to message:")
        if person_to_message in usernames_list:
            print()
            message = input("What message do you want to send?\n")
            info = (username, person_to_message, message, status)
            db_commands.create_row_in_message_table(connection, info)
            print("\nMessage successfully sent\n")
    return 0

# Display user's inbox
def display_inbox(username):
    # Checks if user is recipient of any messages
    messages = db_commands.query_user_has_messages(username)
    if len(messages) == 0:
        print("Sorry, you have an empty inbox. Returning to previous menu\n")
        return 0
    else:
        print("You have", len(messages), "messages!\n")
        for message in messages:
            # Print this out so they select which message they want to response/delete
            print(messages.index(message)+1, end=". ")
            print("Message from:", message[0])
            print("Message:\n", message[1])
            print()
           
def check_new_message(receiver):
    options = '''Do you want to read the message?
    1 - Yes
    2 - No'''
    message_options = '''What would you like to do with this message:
    1 - Leave it in the inbox
    2 - Delete it
    3 - Reply to the sender
    4 - Return to previous menu'''
    message_list = db_commands.query_list_of_new_meesage(receiver)
    # If there are no unread message in the inbox, then the function returns back to additional_options
    if len(message_list) == 0:
        print("You have no new message!")
        return 0
    for message in message_list:
        # If there are no unread message in the inbox, then the function returns back to additional_options
        if len(message_list) == 0:
            print("You have no new message!")
            return 0
        print("You have ", len(message_list), "new messages!\n")
        print("Message from:", message[0])
        print(options)
        selection = input("Select you options:")
        if selection == "1":
            print("Message:\n", message[1])
            status = "READ"
            db_commands.message_status(message[0], receiver, status, message[2])
            message_list = db_commands.query_list_of_new_meesage(receiver)
            while True:
                print(message_options)
                user_choice = input("Please choose an option: ")
                if user_choice == "1":
                    # Leave message in the inbox
                    status = "READ"
                    db_commands.message_status(message[0], receiver, status, message[2])
                    break
                elif user_choice == "2":
                    #Delete the message
                    status = "DELETE"
                    db_commands.message_status(message[0], receiver, status, message[2])
                    db_commands.remove_row_in_message_table(message[0], receiver, message[1])
                    print("Message deleted!")
                    break
                elif user_choice == "3":
                    # Reply to a message
                    connection = db_commands.create_connection(db_commands.database_name)
                    status = "NEW"
                    message_reply = input("What message do you want to send?\n")
                    info = (receiver, message[0], message_reply, status)
                    db_commands.create_row_in_message_table(connection, info)
                    print("\nMessage successfully sent\n")
                    break
                elif user_choice == "4":
                    return 0
                else:
                    print("Invalid command, please enter 1, 2, 3 or 4")

        elif selection == "2":
            status = "NEW"
            db_commands.message_status(message[0], receiver, status, message[2])
            continue
        else:
            print("Invalid command, please enter 1 or 2")

def list_friend_member(username):
    # User can generate a list of InCollege members who are their friends.
    print("InCollege member who are your friends:")
    username_list = db_commands.query_friend(username)
    friends_list = [x[0] for x in username_list]
    for friend in friends_list:
        db_commands.print_query_tiers(friend)

def list_member(username):
    # User has Plus member can generate a list of all InCollege members 
    print("All member of InCollege system:")
    username_list = db_commands.query_usernames_list(username)
    for user in username_list:
        db_commands.print_query_tiers(user)

def member_options(username):
    member_option = '''What would you like to do:
    1 - Send an message
    2 - Generate list of the member
    3 - Display your inbox
    4 - Return to previous menu'''
    
    while True:
        print(member_option)
        choice = input("Please enter your choice: ")
        if choice == "1":
            send_message(username)
        elif choice == "2":
            membership_status = db_commands.query_membership_status(username)
            if membership_status[0] == "Standard":
                list_friend_member(username)
            elif membership_status[0] == "Plus":
                list_member(username)
            else: 
                print("Invalid member status.")
        elif choice == "3":
            display_inbox(username)
        elif choice == "4":
            return 0
        else:
            print("Invalid input, please enter 1, 2, 3 or 4.")