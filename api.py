import db_commands
import job_commands
import new_job_notifications


connection = db_commands.create_connection(db_commands.database_name)


def jobs_input_api():
    # Check if there are > 10 job postings already
    if not job_commands.job_meets_qualifications():
        return False

    try:
        file = open("newJobs.txt", "r")
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

    for job in new_jobs_list:
        new_job_notifications.add_job_notifications(connection, job[5], job[6], job[0])
        db_commands.create_row_in_jobs_table(connection, job)
        if not job_commands.job_meets_qualifications():
            return False


def output_jobs():
    # if file does not exist then create a new file to write to
    # if it does then we will update this output file
    file = open("MyCollege_jobs.txt", "w")
    jobs_list = db_commands.query_jobs_list(connection)
    for jobs in jobs_list:
        temp_job = ["Title: {}\n".format(jobs[1]), "Description: {}\n".format(jobs[2]), "Employer: {}\n".format(jobs[3]),
                    "Location: {}\n".format(jobs[4]), "Salary: {}\n".format(jobs[5]), "=====\n"]
        file.writelines(temp_job)
    file.close()
    return 0


def output_profiles():
    file = open("MyCollege_profiles.txt", "w")
    profiles_list = db_commands.query_profiles(connection)
    for profile in profiles_list:
        # experiences of the current profile of the user at this iteration
        temp_profile = ["Title: {}\n".format(profile[1]), "Major: {}\n".format(profile[2]),
                        "University Name: {}\n".format(profile[3]), "About: {}\n".format(profile[4]), "Experiences:\n"]
        file.writelines(temp_profile)
        # since a user can have multiple experiences I have to fetch all of the experiences and append them to the list above
        profile_experience_list = db_commands.query_user_experiences(connection, profile[0])
        for experiences in profile_experience_list:
            temp_experience = ["Title: {}\n".format(experiences[0]), "Employer: {}\n".format(experiences[1]),
                               "Location: {}\n".format(experiences[2]), "Description: {}\n".format(experiences[3]),
                               "Start Date: {}\n".format(experiences[4]), "End Date: {}\n".format(experiences[5])]
            file.writelines(temp_experience)
        temp_profile_education = ["Education: {}\n".format(profile[5]), "=====\n"]
        file.writelines(temp_profile_education)
    file.close()
    return 0


def output_applied_jobs():
    file = open("MyCollege_appliedJobs.txt", "w")
    # returns list of tuples that each contain (jobID, title)
    jobs_list = db_commands.query_jobs_title_id(connection)
    for job in jobs_list:
        file.write("Job Title: {}\n".format(job[1]))
        # query the application for that job that matches the jobID of the current job
        # returns list of tuple that contain (username, statement_of_purpose)
        job_application_list = db_commands.query_job_application_users(connection, job[0])
        for application in job_application_list:
            temp_application = ["Username: {}\n".format(application[0]),
                                "Reason for why they are the right candidate: {}\n".format(application[1]), "=====\n"]
            file.writelines(temp_application)
    file.close()
    return 0


def output_saved_jobs():
    file = open("MyCollege_savedJobs.txt", "w")
    # fetches list of user that are in the from (username,)
    users_who_saved_jobs_list = db_commands.query_saved_jobs_users(connection)
    for user in users_who_saved_jobs_list:
        file.write("Username: {}\n".format(user[0]))
        # returns a list of job titles that the user has saved in a form as a list of tuples where each tuple is (title,)
        user_saved_jobs_list = db_commands.query_user_saved_jobs(connection, user[0])
        file.write("Job Titles that {} has saved: \n".format(user[0]))
        for job in user_saved_jobs_list:
            file.write("{}\n".format(job[0]))
        file.write("=====\n")
    file.close()
    return 0
