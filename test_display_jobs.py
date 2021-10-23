import db_commands
import job_commands
import pytest

database_name = "userDB"



db_commands.delete_all_database_info(db_commands.create_connection(database_name))
job_commands.display_applied_jobs("username")
job_commands.display_not_applied_jobs("username")
jobs = db_commands.query_jobs_list(db_commands.create_connection(database_name))
for job in jobs:
    job_commands.display_job(job)



user = ("username", "Password?", "Andy", "Dinner", "English", "Don't Send Emails", "Don't Send SMS", "Don't Target Ads",
            "Scrum Master", "Computer Science", "University of South Florida", "Blank",
            "You attended USF for 4 years to get a degree in BCS",)
db_commands.create_row_in_users_table(db_commands.create_connection(database_name), user)

user = ("username2", "Password?2", "An", "Dinh", "English", "Don't Send Emails", "Don't Send SMS", "Don't Target Ads",
            "Scrum Master", "Computer Science", "University of South Florida", "Blank",
            "You attended USF for 4 years to get a degree in BCS",)
db_commands.create_row_in_users_table(db_commands.create_connection(database_name), user)

job_info = ("Title 1", "Whatever that title means", "Bob", "Florida", 1, "Andy", "Dinner",)
db_commands.create_row_in_jobs_table(db_commands.create_connection(database_name), job_info)

job_info = ("Title 2", "Some other job description", "Bob", "Florida", 1, "An", "Dinh",)
db_commands.create_row_in_jobs_table(db_commands.create_connection(database_name), job_info)



job_commands.display_applied_jobs("username")
job_commands.display_not_applied_jobs("username")
jobs = db_commands.query_jobs_list(db_commands.create_connection(database_name))
for job in jobs:
    job_commands.display_job(job)



job_commands.job_application(jobs[1], "username", db_commands.create_connection(database_name))
#graduation_date = job_commands.is_proper_date("12/12/2020")
#start_date = job_commands.is_proper_date("12/12/2020")
#job_app = ["username", jobs[0], graduation_date, start_date, "description", "APPLIED"]
#db_commands.create_row_in_job_applications_table(db_commands.create_connection(database_name), job_app)



#job_commands.search_all_jobs("username")
job_commands.display_applied_jobs("username")
job_commands.display_not_applied_jobs("username")
jobs = db_commands.query_jobs_list(db_commands.create_connection(database_name))
for job in jobs:
    job_commands.display_job(job)