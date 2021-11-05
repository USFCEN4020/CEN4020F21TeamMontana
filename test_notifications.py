import pytest
import sqlite3
from tests.unit.testDB import CacheDB
import db_commands
import job_commands
import user_notification
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


# Tests
# Test for job notifications
def test_job_notification(cache, capsys):
    user_notification.job_applied_notifiction("username3")
    output = capsys.readouterr().out
    assert output == "You have currently applied for 1 jobs.\n\nA job that you applied for has been deleted.\n\n\n"



# Test for if the user has not created a profile
def test_profile_created(cache, capsys):
    user_notification.check_profile_created("username3")
    output = capsys.readouterr().out
    assert output == "You can edit your profile anytime!\n\n"


# Test for if the user has messages
def test_messages(cache, capsys):
    user_notification.new_message("username2")
    output = capsys.readouterr().out
    assert output == ""

# Test for if the user has messages
def test_deleted_job(cache, capsys):
    connection = db_commands.create_connection(db_commands.database_name)
    job_commands.create_row_in_deleted_jobs_table(connection, 1)
    user_notification.job_applied_notifiction("username3")
    output = capsys.readouterr().out
    db_commands.delete_all_database_info(connection)
    assert output == "You have currently applied for 1 jobs.\n\nA job that you applied for has been deleted.\n\nScrum Master\n"



