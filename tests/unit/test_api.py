import pytest
import sqlite3
from tests.unit.testDB import CacheDB
import db_commands


def test_jobs_input_api():
    try:
        file = open("../../newJobs.txt", "r")
    except IOError:
        # print("Error: File could not open or does not exist.")
        return 0

    # iterating though the lines in the file
    new_jobs_list = []
    temp_job_information = tuple()
    temp_description = ""
    line_count = 0
    # used to fine the line where the poster's name is, used to determine when we are between &&& and =====
    description_flag = False
    # used to detmermine when wer are between ===== and &&&
    job_flag = True
    temp_first_name = ""
    temp_last_name = ""
    for line in file:
        # read the description
        if job_flag is True and line != "&&&\n" and line_count >= 1:
            temp_line_description = line.strip("\n")
            temp_description += temp_line_description + " "
        # indicate when we have encountered the &&& symbol and the description stays true until we see ===== line
        # job_flag is true so that this only can trigger if it comes after start of file or =====
        # line_count != in case title line is &&&
        elif job_flag is True and line == "&&&\n" and line_count != 0:
            # since all the description lines are parsed we add it to the job tuple
            temp_job_information += (temp_description,)
            # after adding to the tuple we want to replace the outer defined variable with an empty string
            temp_description = ""
            # reset line count as we are now dealing with the section from &&& to =====
            # and because the line count will vary at this point because of the amount of description lines
            line_count = 0
            description_flag = True
            job_flag = False
        elif description_flag is True and line_count == 1:
            first_last_name = line.split()
            temp_first_name = first_last_name[0]
            temp_last_name = first_last_name[1]
        elif description_flag is True and line == "=====\n" and line_count == 5:
            # since we defined the first and last name in our table schema at the end we have to add the first and
            # last name last
            temp_job_information += (temp_first_name,) + (temp_last_name,)
            new_jobs_list.append(temp_job_information)
            temp_job_information = tuple()
            line_count = 0
            description_flag = False
            job_flag = True
            continue
        else:
            # concatenate onto the existing temporary job tuple
            temp_job_information += (line.strip("\n"),)
        line_count += 1

    file.close()

    ####TESTING
    print("Testing if file reading correctly")

    #Job number 1:
    title_1 = "title"
    description_1 = "this bad description "
    poster_1_first = "poster"
    poster_1_last = "name"
    employer_1 = "Employer"
    location_1 = "Florida"
    salary_1 = "100"
    assert title_1 == new_jobs_list[0][0]
    assert description_1 == new_jobs_list[0][1]
    assert employer_1 == new_jobs_list[0][2]
    assert location_1 == new_jobs_list[0][3]
    assert salary_1 == new_jobs_list[0][4]
    assert poster_1_first == new_jobs_list[0][5]
    assert poster_1_last == new_jobs_list[0][6]

    #Job number 2:
    title_2 = "Intern"
    description_2 = "Do random stuff. Do a lot of random stuff. Do the most random stuff. "
    poster_2_first = "An"
    poster_2_last = "Dinh"
    employer_2 = "Trevor"
    location_2 = "Florida"
    salary_2 = "1"
    assert title_2 == new_jobs_list[1][0]
    assert description_2 == new_jobs_list[1][1]
    assert employer_2 == new_jobs_list[1][2]
    assert location_2 == new_jobs_list[1][3]
    assert salary_2 == new_jobs_list[1][4]
    assert poster_2_first == new_jobs_list[1][5]
    assert poster_2_last == new_jobs_list[1][6]

def test_output_job():
    jobs_list = db_commands.query_jobs_list(db_commands.create_connection(db_commands.database_name))
    cursor = db_commands.create_connection(db_commands.database_name).cursor()
    cursor.execute("SELECT * FROM jobs")
    assert jobs_list == cursor.fetchall()

def test_output_profiles():
    profiles_list = db_commands.query_profiles(db_commands.create_connection(db_commands.database_name))
    cursor = db_commands.create_connection(db_commands.database_name).cursor()
    cursor.execute("SELECT username, title FROM users")
    assert profiles_list == cursor.fetchall()
    for user in profiles_list:
        profile_experience_list = db_commands.query_user_experiences(db_commands.create_connection(db_commands.database_name), user[0])
        cursor = db_commands.create_connection(db_commands.database_name).cursor()
        cursor.execute("SELECT * FROM experiences WHERE username = ?", (user[0],))
        assert profile_experience_list == cursor.fetchall()

def test_output_applied_jobs():
    jobs_list = db_commands.query_jobs_title_id(db_commands.create_connection(db_commands.database_name))
    cursor = db_commands.create_connection(db_commands.database_name).cursor()
    cursor.execute("SELECT jobID,title FROM jobs")
    assert jobs_list == cursor.fetchall()
    for job in jobs_list:
        job_application_list = db_commands.query_job_application_users(db_commands.create_connection(db_commands.database_name), job[0])
        cursor = db_commands.create_connection(db_commands.database_name).cursor()
        cursor.execute("SELECT username,statement_of_purpose FROM job_applications WHERE jobID = ? AND status = 'APPLIED'", (job[0],))
        assert job_application_list == cursor.fetchall()

def test_output_saved_jobs():
    users_who_saved_jobs_list = db_commands.query_saved_jobs_users(db_commands.create_connection(db_commands.database_name))
    cursor = db_commands.create_connection(db_commands.database_name).cursor()
    cursor.execute("SELECT username FROM job_applications WHERE status = 'SAVED'")
    assert users_who_saved_jobs_list == cursor.fetchall()
    for user in users_who_saved_jobs_list:
        user_saved_jobs_list = db_commands.query_user_saved_jobs(db_commands.create_connection(db_commands.database_name), user[0])
        cursor = db_commands.create_connection(db_commands.database_name).cursor()
        cursor.execute("SELECT title FROM job_applications NATURAL JOIN jobs WHERE username = ? AND status = 'SAVED'", (user[0],))
        assert user_saved_jobs_list == cursor.fetchall()






