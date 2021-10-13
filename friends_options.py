import db_commands


def check_friend_requests(username):
    # function to call db_commands to find if the friends tables
    # FROM friends SELECT * WHERE usernameRecipient = 'username' AND friends = false;
    # friends contains all user that sent a friend request to the current user which has not been accepted
    senders_usernames = db_commands.get_friend_requests()
    print("Do you want to accept or reject any friend request?")
    start_menu = """Please choose from the following menu:
1 - Accept friend request
2 - Reject friend request
3 - Exit friend requests 
"""
    while True:
        print(start_menu)
        user_choice_opt = input("Enter your selection here: ")
        if user_choice_opt == 1:
            accept_friend = input("Which friend request do you want to accept:")
            if accept_friend in senders_usernames:
                # will update friends column to true
                db_commands.accept_friend_request()
            else:
                print("The user entered does not exist or did not send you a friend request.")
            continue
        elif user_choice_opt == 2:
            reject_friend = input("Which friend request do you want to accept:")
            if reject_friend in senders_usernames:
                # will delete friend request in the friends table
                db_commands.reject_friend_request()
            else:
                print("The user entered does not exist or did not send you a friend request.")
            continue
        elif user_choice_opt == 3:
            return 0
        else:
            print("Invalid Input")
            continue
