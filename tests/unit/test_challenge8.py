import pytest
import sqlite3
from tests.unit.testDB import CacheDB
import db_commands
import new_user_notifications
import new_job_notifications
import os

# this is the absolute path to the directory CEN4020F21TeamMontana/tests/unit
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# this joins the directory with the file so that we access the file in this directory
db_path = os.path.join(ROOT_DIR, "userDB")


# this is so that the fixture is automatically used for all the functions to have them operate in this local directory
@pytest.fixture(autouse=True, scope="function")
def change_test_dir(request):
    # local path at the directory CEN4020F21TeamMontana/tests/unit
    os.chdir(request.fspath.dirname)
    yield
    # returns back to the folder where the pytest is executed.
    os.chdir(request.config.invocation_dir)


@pytest.fixture(scope='session')
def verify_session():
    # create a connection with our program database as well for our specific database functions that access it
    connection = sqlite3.connect(db_path)
    db_session = connection.cursor()
    yield db_session
    # delete all the data of the database after test is done
    db_commands.delete_all_database_info(connection)
    connection.close()


# setting up a database that will get filled with preset information
@pytest.fixture(autouse=True, scope='session')
def setup_db(verify_session):
    db_commands.fill_database(sqlite3.connect(db_path))


# fixture so we don't instantiate this DB multiple times
@pytest.fixture
def cache(verify_session):
    return CacheDB(verify_session)


def test_show_new_user_notifications(cache, capsys):
    new_user_notifications.show_new_user_notifications("username2")
    capture = capsys.readouterr()
    assert capture.out == "New Guy has joined InCollege!\n" + "New Girl has joined InCollege!\n"
    new_user_notifications.update_logout_time(cache.session.connection, "username2")
    new_user_notifications.show_new_user_notifications("username2")
    capture = capsys.readouterr()
    assert capture.out == ""


def test_show_new_jobs(cache, capsys):
    new_job_notifications.show_new_jobs(cache.session.connection)
    capture = capsys.readouterr()
    assert capture.out == "A new job < Intern > has been posted\n" + "A new job < Intern > has been posted\n\n\n"


def test_check_applied_job_time(cache, capsys):
    db_commands.update_user_apply_time(cache.session.connection, "username2", "2021-10-31 00:00:00")
    new_job_notifications.check_applied_job_time(cache.session.connection, "username2")
    capture = capsys.readouterr()
    assert capture.out == "Number of Days Since Last Application:  7\n" + \
                          "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!\n"







