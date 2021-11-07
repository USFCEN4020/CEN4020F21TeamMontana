import db_commands
from datetime import datetime

# Adds new row to logout_time table
# register time, logout time
# YY-MM-DD HH:MM:SS
def add_user_logout_times(connection, username, first, last):
    reg_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_time = (username, first, last, reg_time, reg_time)
    db_commands.create_row_in_logout_times_table(connection, user_time)
    # db_commands.print_logout_times_table(connection)

# updates logout time when user goes back to log main menu
def update_logout_time(connection, username):
    logout_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db_commands.update_logout_time(connection, username, logout_time)

# Compares the current users log out time with every other users register time
# If an account was created after the current user logged out, the current user will be sent a notifcation for them
def show_new_user_notifications(username):
    connection = db_commands.create_connection(db_commands.database_name)
    all_logouts = db_commands.query_all_logout_times(connection)

    curr_user_logout = db_commands.query_user_logout_time(connection, username)
    datetime_curr_user = datetime.strptime(curr_user_logout[2], '%Y-%m-%d %H:%M:%S')

    for user in all_logouts:
        datetime_user_in_table = datetime.strptime(user[2], '%Y-%m-%d %H:%M:%S')
        # print("Log out times", user[0], user[1], "reg: ", user[2], "logout: ", user[3])
        if(datetime_user_in_table > datetime_curr_user):
            print(user[0], user[1], "has joined InCollege!")




