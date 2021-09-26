import sqlite3


# operations to get data from the temporary database
class CacheDB:
    def __init__(self, session):
        self.session = session

    def get_user_info(self, username):
        self.session.execute("SELECT * FROM users WHERE username = ?", (username,))
        return self.session.fetchone()

    def get_job(self, firstname, lastname):
        self.session.execute("SELECT * FROM jobs WHERE firstname = ? AND lastname = ?", (firstname, lastname,))
        return self.session.fetchone()

    def get_all_job(self):
        self.session.execute("SELECT * FROM jobs")
        return self.session.fetchall()

    def create_job(self, first_name, last_name):
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
        create_new_job_posting_sql = ''' INSERT INTO jobs(title,description,employer,location,salary,firstname,lastname)
                          VALUES(?,?,?,?,?,?,?) '''
        self.session.execute(create_new_job_posting_sql, job_information)
        self.session.commit()

