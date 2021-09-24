import db_commands


def job_meets_qualifications():
    job_titles = db_commands.query_list_of_jobs()
    if len(job_titles) > 5:
        print("There are already more than 5 job listings, our system cannot handle anymore.")
        return False
    else:
        return True


def create_job_posting(first_name, last_name):
    # Check if there are > 5 job postings already
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

    job_information = (title, description, employer, location, salary, first_name, last_name)
    db_commands.create_row_in_jobs_table(job_information)

