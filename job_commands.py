import db_commands
from sqlite3 import Error

# Prints the jobs
# Format: id, title, description, employer, location, salary, first/last name
import start_options

# After we query for all the deleted jobs that the user has applied to we will save it and return that
# And since the rows of tuples are saved then we can delete the jobs as well.
def query_and_delete_deleted_jobs(username):
    connection = db_commands.create_connection(db_commands.database_name)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM deleted_jobs WHERE username = ?", (username,))
        deleted_jobs_for_user = cursor.fetchall()
        cursor.execute("DELETE FROM deleted_jobs WHERE username = ?", (username,))
        return deleted_jobs_for_user
    except Error:
        print()


def remove_row_in_jobs_table(connection, jobID):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM jobs WHERE jobID = ?", (jobID, ))
        connection.commit()
    except Error as e:
        print(e)

def jobs_menu(username):
    
    menu = """Please choose from the following menu:
1 - View jobs you have applied to
2 - View jobs you have not applied to yet
3 - Apply for a job
4 - Exit Search for a job (Return back to previous menu)
"""
    while True:
        print(menu)
        user_choice_opt = input("Enter your selection here: ")
        if user_choice_opt == "1":
            display_applied_jobs(username)
        elif user_choice_opt == "2":
            display_not_applied_jobs(username)
        elif user_choice_opt == "3":
            search_all_jobs(username)
        elif user_choice_opt == "4":
            return 0
        else:
            print("Invalid Input, Enter a value between 1-4 inclusive")
            continue


def search_all_jobs(username):
    connection = db_commands.create_connection(db_commands.database_name)
    jobs = db_commands.query_jobs_list(connection)
    while True:
        print("Select a job from the list to apply for it, or press Q to quit:")
        for i in range(0, len(jobs)):
            print(i + 1, ":", jobs[i][1])
        print()
        user_selection = input("Enter selection: ")
        if user_selection < 1 or user_selection > len(jobs):
            print("Invalid input. Try again")
            continue
        elif user_selection == "Q":
            return 0
        else:
            job = jobs[user_selection -1]
            display_job(job)
            # After displaying the job, prompt user to apply
            print("1 - Apply for this job")
            print("2 - Save this job")
            print("3 - Unsave this job")
            user_choice = input("Otherwise, press any button to go back: ")
            if user_choice == "1":
                job_application(job, username, connection)
            elif user_choice == "2":
                save_job(job, username, connection)
            elif user_choice == "3":
                unsave_job(job, username, connection)
            else:
                continue


def display_applied_jobs(username):
    print("Jobs you have applied for:")
    connection = db_commands.create_connection(db_commands.database_name)
    jobs = db_commands.query_job_apps(connection)
    # 0 = username, 1 = jobID, 2 = status
    for job in jobs:
        if username == job[0] and job[2] == "APPLIED":
            # This student has applied for the job, display it
            rows = db_commands.query_job_info_from_id(connection, job[1])
            for row in rows:
                print(row[0])
    print()


# retrieves the list of jobs that the user has yet to apply to
def display_not_applied_jobs(username):
    print("Jobs you have not applied for:")
    status = "NOT APPLIED"
    not_applied_jobs = db_commands.query_applications(username, status)
    print(not_applied_jobs)


def display_saved_jobs(username):
    connection = db_commands.create_connection(db_commands.database_name)
    print("Jobs you have saved:")
    connection = db_commands.create_connection(db_commands.database_name)
    jobs = db_commands.query_job_apps(connection)
    # 0 = username, 1 = jobID, 2 = status
    for job in jobs:
        if username == job[0] and job[2] == "SAVED":
            # This student has applied for the job, display it
            rows = db_commands.query_job_info_from_id(connection, job[1])
            for row in rows:
                print(row[0])
    print()


def display_job(job):
    print("Displaying specifics about that job:\n")
    print("Title:", job[1])
    print("Description:", job[2])
    print("Employer:", job[3])
    print("Location:", job[4])
    print("Salary:", job[5])
    print("This job was posted by:", job[6], job[7])
    print()


def job_application(job, username, connection):
    # Apply for job
    # Confirm this user is not the one that posted the job
    first_name, last_name = db_commands.find_names_from_username(username)
    if job[6] == first_name and job[7] == last_name:
        print("You cannot apply for a job that you created. Returning to previous menu\n")
        return 0

    # Confirm this user has not applied for the job yet
    existing_job_apps = db_commands.query_job_apps(connection)
    for j in existing_job_apps:
        # 0 = username, 1 = job id
        if j[0] == username and str(j[1]) == str(job[0]) and j[2] == "APPLIED":
            print("You cannot apply for a job that you already applied for. Returning to previous menu\n")
            return 0
    # Graduation Date
    while True:
        graduation_date = input("Please enter the date you graduate, in format mm/dd/yyyy: ")
        if is_proper_date(graduation_date):
            break
    # Start Date
    while True:
        start_date = input("Please enter the date you want to start, in format mm/dd/yyyy: ")
        if is_proper_date(start_date):
            break
    description = input("Please enter why you would be a good fit for this job: ")
    job_app = [username, job[0], graduation_date, start_date, description, "APPLIED"]
    db_commands.create_row_in_job_applications_table(connection, job_app)
    print("Application sent successfully!\n")


def save_job(job, username, connection):
    # Confirm this user has not saved the job yet
    existing_job_apps = db_commands.query_job_apps(connection)
    for j in existing_job_apps:
        # 0 = username, 1 = job id
        if j[0] == username and str(j[1]) == str(job[0]) and j[2] == "SAVED":
            print("You cannot save a job that you already saved. Returning to previous menu\n")
            return 0
    job_app = [username, job[0], "", "", "", "SAVED"]
    db_commands.create_row_in_job_applications_table(connection, job_app)
    print("Successfully saved this job\n")
    return


def unsave_job(job, username, connection):
    # Confirm this user has saved the job
    existing_job_apps = db_commands.query_job_apps(connection)
    for j in existing_job_apps:
        # 0 = username, 1 = job id
        if j[0] == username and str(j[1]) == str(job[0]) and j[2] == "SAVED":
            # Job was saved- unsave it
            db_commands.remove_row_in_job_applications_table(connection, username, job[0])
            print("Successfully unsaved this job\n")
            return 0
    print("You never saved this job.")
    return


# Helper function for determining if a string is in format mm/dd/yyyy
def is_proper_date(date):
    if len(date) != 10:
        print("Not in mm/dd/yyyy format")
    if date[2] == "/" and date[5] == "/":
        date = date.replace("/", "")
        try:
            date = int(date)
            return True
        except ValueError:
            print("Not in mm/dd/yyyy format")
    return False


def job_meets_qualifications():
    job_titles = db_commands.query_list_of_jobs()
    if len(job_titles) >= 10:
        print("There are already more than 10 job listings, our system cannot handle anymore.")
        return False
    else:
        return True


def create_job_posting(first_name, last_name):
    # Check if there are > 10 job postings already
    if not job_meets_qualifications():
        return False

    print("Let's get started in creating a new job posting.")
    # There are no constraints on the actual job posting
    title = input("Please enter a title for the job posting: ")
    description = input("Please enter a description for the job posting: ")
    employer = input("Please enter the employer for the job posting: ")
    location = input("Please enter the location for the job posting: ")
    salary = input("Please enter the salary for the job posting: ")
    try:
        salary = int(salary)
    except ValueError:
        print("This salary is not an integer. Please try again. \n")
        return

    job_information = (title, description, employer, location, salary, first_name, last_name,)
    db_commands.create_row_in_jobs_table(db_commands.create_connection(db_commands.database_name), job_information)


def query_user_job_posting(first_name, last_name):
    connection = db_commands.create_connection(db_commands.database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs WHERE firstname = ? AND lastname = ?", (first_name, last_name,))
    return cursor.fetchall()


# saves all the realtionship between the job and the users that applied to the soon to be deleted job
def create_row_in_deleted_jobs_table(connection, jobID):
    try:
        cursor = connection.cursor()
        # NATURAL JOIN both the jobs table and the job_applications table, and select what we want from them
        # this will give us
        cursor.execute('''SELECT username, title, description, employer, location, salary FROM jobs NATURAL JOIN job_applications
                          WHERE jobID = ?''', (jobID,))
        notify_job_deletion_list = cursor.fetchall()
        for notification in notify_job_deletion_list:
            cursor.execute(db_commands.create_new_deleted_notification_sql, notification)
            connection.commit()
    except Error as e:
        print(e)


# passes to this function the first and last name of the user
def delete_job_posting(first_name, last_name):
    jobID_exist = False
    while True:
        print("Here are the jobs that you have posted")
        user_job_posting = query_user_job_posting(first_name, last_name)
        print(*user_job_posting, sep="\n")
        print("Select a job from the list to apply for it, or press Q to quit:")
        jobID_delete = input("Enter the jobID of one of the job you want to delete: ")
        for job in user_job_posting:
            if int(jobID_delete) == job[0]:
                create_row_in_deleted_jobs_table(db_commands.create_connection(db_commands.database_name), jobID_delete)
                remove_row_in_jobs_table(db_commands.create_connection(db_commands.database_name), jobID_delete)
                jobID_exist = True
                break
            else:
                print("The jobID entered is wrong, or it does not exist.")
                break
        if jobID_delete == "Q":
            return 0
        elif jobID_delete != "Q" and jobID_exist is False:
            print("Invalid Input, Enter either a valid jobID or Q to quit")
            continue
