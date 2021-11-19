import db_commands
import job_commands
import new_job_notifications


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
        if job_flag is True and line_count >= 1:
            temp_line_description = line.strip("\n")
            temp_description += temp_line_description
        # indicate when we have encountered the &&& symbol and the description stays true until we see ===== line
        # job_flag is true so that this only can trigger if it comes after start of file or =====
        # line_count != in case title line is &&&
        elif job_flag is True and line == "&&&\n" and line_count != 0:
            # since all the description lines are parsed we add it to the job tuple
            temp_job_information += (temp_description,)
            # after adding to the tuple we want to replace the outer defined variable with an empty string
            temp_description.replace(temp_description, "")
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
            temp_first_name.replace(temp_first_name, "")
            temp_last_name.replace(temp_last_name, "")
            new_jobs_list.append(temp_job_information)
            temp_job_information = tuple()
            line_count = 0
            description_flag = False
            job_flag = True
            continue
        else:
            # concatenate onto the existing temporary job tuple
            temp_job_information += (line.strip("\n"),)
        line_count += line_count + 1
    file.close()
    for job in new_jobs_list:
        new_job_notifications.add_job_notifications(db_commands.create_connection(db_commands.database_name), job[5], job[6], job[0])
        db_commands.create_row_in_jobs_table(db_commands.create_connection(db_commands.database_name), job)
        if not job_commands.job_meets_qualifications():
            return False





