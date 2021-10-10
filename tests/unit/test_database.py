import pytest
import sqlite3
from tests.unit.testDB import CacheDB
from job_commands import create_job_posting
import db_commands
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
    # db_commands.delete_all_database_info(connection)
    connection.close()


# setting up a database that will get filled with preset information
@pytest.fixture(autouse=True, scope='session')
def setup_db(verify_session):
    db_commands.fill_database(sqlite3.connect(db_path))
    db_commands.print_database(sqlite3.connect(db_path))
    db_commands.print_experiences(sqlite3.connect(db_path), "username2")


# fixture so we don't instantiate this DB multiple times
@pytest.fixture
def cache(verify_session):
    return CacheDB(verify_session)


def test_create_job_posting(cache, mocker):
    print("\n")
    # patching the builtin input function to provide the input to test.
    mocker.patch('builtins.input', side_effect=["tester", "test stuff", "James Anderson", "Florida", 100000])
    test = create_job_posting("Girl", "Test")

    mocker.patch('builtins.input', side_effect=["tester", "test stuff", "Bob", "New York", 10])
    test = create_job_posting("Test", "Guy")

    job_array1 = cache.get_job("Girl", "Test")
    job_array2 = cache.get_job("Test", "Guy")

    assert job_array1 == ("tester", "test stuff", "James Anderson", "Florida", 100000, "Girl", "Test")
    assert job_array2 == ("tester", "test stuff", "Bob", "New York", 10, "Test", "Guy")


def test_print(cache):
    print("\n")
    all_jobs = cache.get_all_job()
    for job in all_jobs:
        print(job)
