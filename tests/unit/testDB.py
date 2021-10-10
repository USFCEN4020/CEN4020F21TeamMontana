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
        self.session.connection.commit()

    def delete_job(self, first_name, last_name):
        self.session.execute('DELETE FROM jobs WHERE firstname = ? AND lastname = ?', (first_name, last_name,))

    def get_experience(self, username):
        self.session.execute("SELECT * FROM experiences WHERE username = ?", (username,))
        return self.session.fetchone()
    
    def get_all_experience(self):
        self.session.execute("SELECT * FROM experiences")
        return self.session.fetchall()

    def change_language_prefs(self, username, lang):
        self.session.execute('''UPDATE users SET language = ? WHERE username = ?''', (lang, username))

    def get_user_lang(self, username):
        self.session.execute("SELECT language FROM users WHERE username = ?", (username,))
        return self.session.fetchone()

    def change_email_prefs(self, username, email):
        self.session.execute('''UPDATE users SET emails = ? WHERE username = ?''', (email, username))

    def get_user_email(self, username):
        self.session.execute("SELECT emails FROM users WHERE username = ?", (username,))
        return self.session.fetchone()

    def change_sms_prefs(self, username, sms):
        self.session.execute('''UPDATE users SET sms = ? WHERE username = ?''', (sms, username))

    def get_user_sms(self, username):
        self.session.execute("SELECT sms FROM users WHERE username = ?", (username,))
        return self.session.fetchone()

    def change_ads_prefs(self, username, ads):
        self.session.execute('''UPDATE users SET targetedads = ? WHERE username = ?''', (ads, username))

    def get_user_ads(self, username):
        self.session.execute("SELECT targetedads FROM users WHERE username = ?", (username,))
        return self.session.fetchone()

