import db_commands
import friend_commands


def check_friend_requests(username):
    # function to call db_commands to find if the friends tables
    # FROM friends SELECT sender, status WHERE usernameRecipient = 'username' AND status = false;
    # friends contains all user that sent a friend request to the current user which has not been accepted
    senders_usernames = db_commands.query_list_of_friend_requests(username)
    # If there are no pending friend request then the function returns back to additional_options
    if len(senders_usernames) == 0:
        return 0
    print("Pending friend requests:")
    # prints each Friend request on a new line
    print(*senders_usernames, sep="\n")

    print("Do you want to accept or reject any friend request?")
    menu = """Please choose from the following menu:
1 - Accept friend request
2 - Reject friend request
3 - Exit friend requests (Return back to previous menu)
"""
    while True:
        print(menu)
        user_choice_opt = input("Enter your selection here: ")
        if user_choice_opt == 1:
            status_accept = "ACCEPT"
            accept_friend = input("Enter which friend request you want to accept:")
            if accept_friend in senders_usernames:
                # will update friends status to ACCEPT
                db_commands.Friend_Status(accept_friend, username, status_accept)
            else:
                print("The user entered does not exist or did not send you a friend request.")
            continue
        elif user_choice_opt == 2:
            status_reject = "REJECT"
            reject_friend = input("Enter which friend request you want to reject:")
            if reject_friend in senders_usernames:
                # will delete friend request in the friends table
                db_commands.Friend_Status(reject_friend, username, status_reject)
            else:
                print("The user entered does not exist or did not send you a friend request.")
            continue
        elif user_choice_opt == 3:
            return 0
        else:
            print("Invalid Input, Enter a value that is either 1, 2 or 3")
            continue


def show_network(username):
    friends_list = db_commands.query_friend(username)
    print("These are the people that you have connected with:")
    if len(friends_list) == 0:
        print("You have not connected with anybody")
        print("Returning back to previous menu.")
        return 0
    print(*friends_list, sep="\n")

    print("How do you want to interact with your connections")
    menu = """Please choose from the following menu:
1 - Disconnect from someone on the list
2 - View profile of one your friends (Display list of friends with a profile)
3 - Exit Show my network (Return back to previous menu)
"""
    while True:
        print(menu)
        user_choice_opt = input("Enter your selection here: ")
        if user_choice_opt == 1:
            status_disconnect = "DISCONNECT"
            disconnect_friend = input("Enter who you want to disconnect from:")
            if disconnect_friend in friends_list:
                # will delete friend row from the friends table where the user to disconnect from is your friend
                db_commands.Friend_Status(disconnect_friend, username, status_disconnect)
            else:
                print("The user entered does not exist or did not send you a friend request.")
            continue
        elif user_choice_opt == 2:
            # checks to see if the users in friends_list has a profile or not
            friends_list_with_profiles = db_commands.query_friend_profiles()
            view_friend_profile = input("Enter who's profile you want to view:")
            if db_commands.query_student_title(username) == "TITLE:NULL" and db_commands.query_student_major(username) == "MAJOR:NULL" and db_commands.query_student_university(username) == "UNIVERSITY:NULL" and db_commands.query_student_info(username) == "STUDENTINFO:NULL" and db_commands.query_education(username) == "education:NULL":
                print("The user entered did not update their profile yet.")
            if view_friend_profile in friends_list_with_profiles:
                # will delete friend row from the friends table where the user to disconnect from is your friend
                db_commands.Friend_Status(disconnect_friend, username, status_disconnect)
            else:
                print("The user entered does not exist or did not send you a friend request.")
            continue
        elif user_choice_opt == 3:
            return 0
        else:
            print("Invalid Input, Enter either the value 1, 2 or 3")
            continue