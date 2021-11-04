import db_commands
from sqlite3 import Error

def check_profile_created(username):
    connection = db_commands.create_connection(db_commands.database_name)
    cursor = connection.cursor()

    cursor.execute('''SELECT title, major, university, studentinfo, education FROM users WHERE username = ?''', (username,))
    profile = cursor.fetchone()

    if (profile[0] == 'TITLE:NULL' and
            profile[1] == 'MAJOR:NULL' and
            profile[2] == 'UNIVERSITY:NULL' and
            profile[3] == 'STUDENTINFO:NULL' and
            profile[4] == 'EDUCATION:NULL'):
        print("Don't forget to create a profile.\n")
    else:
        print("You can edit your profile anytime!\n")

def new_message(username):
    message_list = db_commands.query_list_of_new_meesage(username)
    if(len(message_list) > 0):
        print("You have %d messages waiting for you!\n" %(len(message_list)))
    else:
        return 0

def job_applied_notifiction(username):
    connection = db_commands.create_connection(db_commands.database_name)
    cursor = connection.cursor()
    cursor.execute('''SELECT username, jobID, status from job_applications WHERE username = ? AND status = "APPLIED"''', (username,))
    jobs = cursor.fetchall()
    print("You have currently aplied for %d jobs.\n" %(len(jobs)))
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT title FROM deleted_jobs WHERE username = ?", (username,))
        deleted_jobs = cursor.fetchall()
        print("A job that you applied for has been deleted.\n")
        job_title = [x[0] for x in deleted_jobs]
        print(*job_title, sep="\n")
    except Error:
        print()
    
def print_notification(username):
    print("Notifications:\n")
    check_profile_created(username)
    new_message(username)
       