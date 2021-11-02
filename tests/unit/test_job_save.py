import db_commands
import job_commands
from tests.unit.testBases import get_display_ouput, set_keyboard_input
import pytest

def test_save_job():
    database_name = "userDB"
    connection = db_commands.create_connection(db_commands.database_name)
    db_commands.create_table(connection, db_commands.user_table)
    db_commands.create_table(connection, db_commands.job_table)
    db_commands.create_table(connection, db_commands.user_job_table)
    db_commands.create_table(connection, db_commands.deleted_jobs_table)
    db_commands.create_table(connection, db_commands.experience_table)
    db_commands.create_table(connection, db_commands.friend_table)
    # db_commands.delete_all_database_info(connection)

    usernames = ["username", "username2"]

    user = ("username", "Password?", "Andy", "Dinner", "English", "Don't Send Emails", "Don't Send SMS", "Don't Target Ads",
            "Scrum Master", "Computer Science", "University of South Florida", "Blank",
            "You attended USF for 4 years to get a degree in BCS",)
    db_commands.create_row_in_users_table(connection, user)

    user = ("username2", "Password?2", "An", "Dinh", "English", "Don't Send Emails", "Don't Send SMS", "Don't Target Ads",
            "Scrum Master", "Computer Science", "University of South Florida", "Blank",
            "You attended USF for 4 years to get a degree in BCS",)
    db_commands.create_row_in_users_table(connection, user)

    job_info = ("Title 1", "Whatever that title means", "Bob", "Florida", 1, "Andy", "Dinner",)
    db_commands.create_row_in_jobs_table(connection, job_info)

    job_info = ("Title 2", "Some other job description", "Bob", "Florida", 1, "An", "Dinh",)
    db_commands.create_row_in_jobs_table(connection, job_info)

    job_info = ("Title 3", "Some other job description", "Rob", "Maine", 1, "Gucci", "Bucci",)
    db_commands.create_row_in_jobs_table(connection, job_info)



    jobs = db_commands.query_jobs_list(connection)
    job_apps = db_commands.query_job_apps(connection)
    print("help")
    for job in jobs:
        print(jobs[0])
        job_commands.save_job(jobs[job], "username", connection)
        for j in job_apps:
            if j[0] == usernames[0] and str(j[1]) == str(jobs[job][0]):
                assert j[2] == "SAVED"


