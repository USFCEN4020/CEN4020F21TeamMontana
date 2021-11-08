import db_commands
from datetime import datetime

# Adds new job title to job notification table
def add_job_notifications(connection, first, last, title):
    job = (first, last, title)
    db_commands.create_row_in_job_notifications_table(connection, job)

# Prints new job notifications
def show_new_jobs(connection):
    all_notifications = db_commands.query_all_job_notifications(connection)
    for notif in all_notifications:
        print("A new job <", notif[0], "> has been posted")
    print("\n")
# Updates the time the user applied to the job to current time
# YY-MM-DD HH:MM:SS
def update_applied_job_time(connection, user):
    curr_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(curr_time)
    db_commands.update_user_apply_time(connection, user, curr_time)

# Checks if user has applied to a job after 7 days
def check_applied_job_time(connection, user):
    user_time = datetime.strptime(db_commands.query_user_applied_time(connection, user)[0], '%Y-%m-%d %H:%M:%S')
    curr_time = datetime.now()
    delta = (curr_time.date() - user_time.date()).days
    print("Number of Days Since Last Application: ", delta)
    if delta >= 7:
        print("Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")