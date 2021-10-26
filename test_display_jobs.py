import db_commands
import job_commands
import random
import pytest

database_name = "userDB"
db_commands.delete_all_database_info(db_commands.create_connection(database_name))

def random_string():
    str_length = random.randint(3, 9)
    str_var = ""
    while str_length > 0:
        str_var += chr(random.randint(97, 122))
        str_length -= 1
    return str_var



job_commands.display_applied_jobs("username")
job_commands.display_not_applied_jobs("username")
jobs = db_commands.query_jobs_list(db_commands.create_connection(database_name))
for job in jobs:
    job_commands.display_job(job)


user1 = (random_string(), "Password?", random_string(), random_string(), "English", "Don't Send Emails", "Don't Send SMS", "Don't Target Ads",
            "Scrum Master", "Computer Science", "University of South Florida", "Blank",
            "You attended USF for 4 years to get a degree in BCS",)
db_commands.create_row_in_users_table(db_commands.create_connection(database_name), user1)

user2 = (random_string(), "Password?2", random_string(), random_string(), "English", "Don't Send Emails", "Don't Send SMS", "Don't Target Ads",
            "Scrum Master", "Computer Science", "University of South Florida", "Blank",
            "You attended USF for 4 years to get a degree in BCS",)
db_commands.create_row_in_users_table(db_commands.create_connection(database_name), user2)

user3 = (random_string(), "Password?2", random_string(), random_string(), "English", "Don't Send Emails", "Don't Send SMS", "Don't Target Ads",
            "Scrum Master", "Computer Science", "University of South Florida", "Blank",
            "You attended USF for 4 years to get a degree in BCS",)
db_commands.create_row_in_users_table(db_commands.create_connection(database_name), user3)




job_info = ("Title 1", "Whatever that title means", random_string(), "Florida", 1, user1[2], user1[3],)
db_commands.create_row_in_jobs_table(db_commands.create_connection(database_name), job_info)

job_info = ("Title 2", "Some other job description", random_string(), "Florida", 1, user2[2], user2[3],)
db_commands.create_row_in_jobs_table(db_commands.create_connection(database_name), job_info)

job_info = ("Title 3", "Some other job description", random_string(), "Florida", 1, user3[2], user3[3],)
db_commands.create_row_in_jobs_table(db_commands.create_connection(database_name), job_info)



job_commands.display_applied_jobs(user1[0])
job_commands.display_not_applied_jobs(user1[0])
jobs = db_commands.query_jobs_list(db_commands.create_connection(database_name))
for job in jobs:
    job_commands.display_job(job)



i = 0
while i < 3:
    first_name, last_name = db_commands.find_names_from_username(user1[0])
    if jobs[i][6] == first_name and jobs[i][7] == last_name:
        print("You cannot apply for a job that you created. Returning to previous menu\n")
        i += 1
        continue

    # Confirm this user has not applied for the job yet
    existing_job_apps = db_commands.query_job_apps(db_commands.create_connection(database_name))
    for j in existing_job_apps:
        if j[0] == user1[0] and str(j[1]) == str(jobs[i][0]) and j[2] == "APPLIED":
            print("You cannot apply for a job that you already applied for. Returning to previous menu\n")
            i += 1
            continue
    job_app = [user1[0], jobs[i][0], "12/12/2020", "12/12/2020", "description", "APPLIED"]
    db_commands.create_row_in_job_applications_table(db_commands.create_connection(database_name), job_app)
    i += 1



job_commands.display_applied_jobs(user1[0])
job_commands.display_not_applied_jobs(user1[0])
jobs = db_commands.query_jobs_list(db_commands.create_connection(database_name))
for job in jobs:
    job_commands.display_job(job)