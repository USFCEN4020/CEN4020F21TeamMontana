import db_commands
import datetime


def experience_meets_qualifications(username):
    job_experiences = db_commands.query_list_of_experiences()
    num_of_experiences = 0
    for i in job_experiences:
        if i.username == username:
            num_of_experiences += 1
        if num_of_experiences > 3:
            print("There are already more than 3 experience listings for this profile, our system cannot handle anymore.")
            return False
    return True


#used for inputing dates
def input_date_info(date_text):
    date_info = ""
    while True:
        date_entry = input(date_text)
        try:
            month, day, year = map(int, date_entry.split('/'))
            date_info = datetime.date(year, month, day)
        except ValueError:
            print("This date is not in the proper format. Please try again. \n")
            return
        break
    return date_info

def create_experience_posting(username):
    print("Let's get started in creating a new job experience.")
    # There are no constraints on the actual experience posting
    title = input("Please enter a title for the job experience: ")
    employer = input("Please enter the employer for the job experience: ")
    location = input("Please enter the location for the job experience: ")
    description = input("Please enter a description for the job experience: ")
    start_date = input_date_info("Enter a start date in MM/DD/YYYY format")
    end_date = input_date_info("Enter an end date in MM/DD/YYYY format")

    experience_information = (title, description, employer, location, start_date, end_date, username)
    db_commands.create_row_in_experience_table(experience_information)


