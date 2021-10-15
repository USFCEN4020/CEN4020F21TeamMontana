import db_commands


def create_experience_posting(sender):
    print("Let's get started in creating a new job experience.")
    # There are no constraints on the actual experience posting
    status = "PENDING"
    receiver = input("Please enter username of friend to send request to")

    friend_information = (sender, status, receiver)
    db_commands.create_row_in_experience_table(friend_information)