from tests.unit.testDB import CacheDB
import db_commands
import job_commands
import api


def test_jobs_input_api():
    if not job_commands.job_meets_qualifications():
        return 0
    try:
        file = open("newJobs.txt", "r")
    except IOError:
        # print("Error: File could not open or does not exist.")
        return 0

    #new_jobs_list = db_commands.create_row_in_jobs_table(db_commands.create_connection(db_commands.database_name), job)
    cursor = db_commands.create_connection(db_commands.database_name).cursor()
    cursor.execute("SELECT title, description, employer, location, salary, firstname, lastname FROM jobs")
    assert cursor.fetchall() == [("title", "this bad description ", "Employer", "Florida", 100, "poster", "name"),
    ("Intern", "Do random stuff. Do a lot of random stuff. Do the most random stuff. ", "Trevor", "Florida", 1, "An", "Dinh")]
    file.close()

def test_output_job():
    api.output_jobs()
    try:
        file = open("MyCollege_jobs.txt", "r")
    except IOError:
        return False

    job_list_from_file = []
    temp_job_information = tuple()
    line_count = 0
    for line in file:
        if(line != "=====\n"):
            temp_job_information += (line.strip("\n"),)
        elif (line == "=====\n" and line_count == 6):
            job_list_from_file.append(temp_job_information)
            temp_job_information = tuple()
            line_count = 0
            continue
        line_count += 1

    db_commands.query_jobs_list(db_commands.create_connection(db_commands.database_name))
    cursor = db_commands.create_connection(db_commands.database_name).cursor()
    cursor.execute("SELECT title, description, employer, location, salary FROM jobs")
    
    for jobs in job_list_from_file:
        assert (cursor.fetchall(), "=====\n") == [format(jobs[1]), format(jobs[2]), format(jobs[3]),
                    format(jobs[4]), format(jobs[5]), "=====\n"]

def test_output_profiles():
    api.output_profiles()
    try:
        file = open("MyCollege_profiles.txt", "r")
    except IOError:
        return False

    profile_list_from_file = []
    temp_profile_information = tuple()
    line_count = 0
    for line in file:
        if(line != "=====\n"):
            temp_profile_information += (line.strip("\n"),)
        elif (line_count == 4):
            temp_profile_information += (line.strip("Experienxe:\n"),)
        elif (line == "=====\n" and line_count == 13):
            profile_list_from_file.append(temp_profile_information)
            temp_profile_information = tuple()
            line_count = 0
            continue
        line_count += 1

    profile_list = db_commands.query_profiles(db_commands.create_connection(db_commands.database_name))
    cursor = db_commands.create_connection(db_commands.database_name).cursor()
    for profile in profile_list:
        username = profile[0]
        cursor = db_commands.create_connection(db_commands.database_name).cursor()
        cursor.execute("""SELECT title, major, university, studentinfo, title, employer, location, description, start_date, end_date, 
            education FROM users NATURAL JOIN experiences WHERE username = ?""",(username,))
        for profiles in profile_list_from_file:
            assert (cursor.fetchall(), "=====\n") == [format(profiles[0]), format(profiles[1]), format(profiles[2]), format(profiles[3]),
            format(profiles[4]), format(profiles[5]), format(profiles[6]), format(profiles[7]), format(profiles[8]), format(profiles[9]),
            format(profiles[10]), "=====\n"]

def test_output_applied_jobs():
    api.output_applied_jobs()
    try:
        file = open("MyCollege_appliedJobs.txt", "r")
    except IOError:
        return False

    applied_job_list_from_file = []
    temp_applied_job_information = tuple()
    line_count = 0
    for line in file:
        if(line != "=====\n"):
            temp_applied_job_information += (line.strip("\n"),)
        elif (line == "=====\n"):
            applied_job_list_from_file.append(temp_applied_job_information)
            temp_applied_job_information = tuple()
            line_count = 0
            continue
        line_count += 1

    applied_jobs_ID = db_commands.query_jobs_title_id(db_commands.create_connection(db_commands.database_name))
    cursor = db_commands.create_connection(db_commands.database_name).cursor()
    for jobs_ID in applied_jobs_ID:
        job_ID = jobs_ID[0]
        cursor = db_commands.create_connection(db_commands.database_name).cursor()
        cursor.execute("""SELECT title, username,statement_of_purpose 
                FROM jobs NATURAL JOIN job_applications WHERE jobID = ? AND status = 'APPLIED'""",(job_ID,))
        for applied_job in applied_job_list_from_file:
            assert (cursor.fetchall(), "=====\n") == [format(applied_job[0]), format(applied_job[1]), format(applied_job[2]), "=====\n"]

def test_output_saved_jobs():
    api.output_saved_jobs()
    try:
        file = open("MyCollege_savedJobs.txt", "r")
    except IOError:
        return False

    saved_job_list_from_file = []
    temp_saved_job_information = tuple()
    line_count = 0
    for line in file:
        if(line != "=====\n"):
            temp_saved_job_information += (line.strip("\n"),)
        elif (line == "=====\n"):
            saved_job_list_from_file.append(temp_saved_job_information)
            temp_saved_job_information = tuple()
            line_count = 0
            continue
        line_count += 1
    user_saved_job = db_commands.query_saved_jobs_users(db_commands.create_connection(db_commands.database_name))
    cursor = db_commands.create_connection(db_commands.database_name).cursor()
    for users in user_saved_job:
        user = users[0]
        cursor = db_commands.create_connection(db_commands.database_name).cursor()
        cursor.execute("SELECT username, title FROM job_applications NATURAL JOIN jobs WHERE username = ? AND status = 'SAVED'", (user,))
        for job in saved_job_list_from_file:
            assert (cursor.fetchall(), "=====\n") == [format(job[0]), format(job[1]), "=====\n"]






