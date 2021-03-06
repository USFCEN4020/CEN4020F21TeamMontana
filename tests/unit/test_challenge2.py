import pytest
import sqlite3
from testDB import CacheDB
# In cmd
# pip install pytest-mock
import mock
from account_define import user_login
from job_commands import create_job_posting
import start_options


# The scope of being session has this connection being active for only each individual run
@pytest.fixture(scope='session', params=[':memory:'])
def session(request):
    # create in memory database, just for testing purposes
    connection = sqlite3.connect(request.param)
    db_session = connection.cursor()
    yield db_session
    connection.close()


# autouse being True means that this fixture will be called for all the following tests
# this function is to fill in the empty temporary database in memory
@pytest.fixture(autouse=True, scope='session')
def setup_db(session):
    session.execute("""CREATE TABLE IF NOT EXISTS users (
                       username text PRIMARY KEY,
                       password text NOT NULL,
                       firstname text NOT NULL,
                       lastname text NOT NULL,
                       UNIQUE(firstname, lastname))""")
    session.execute('INSERT INTO users VALUES("username2", "Password?2", "An", "Dinh")')
    session.connection.commit()

    session.execute("""CREATE TABLE IF NOT EXISTS jobs (
                       title text NOT NULL,
                       description text NOT NULL,
                       employer text NOT NULL,
                       location text NOT NULL,
                       salary INTEGER NOT NULL,
                       firstname text NOT NULL,
                       lastname text NOT NULL,
                       FOREIGN KEY(firstname) REFERENCES users(firstname),
                       FOREIGN KEY(lastname) REFERENCES users(lastname))""")
    session.execute('INSERT INTO jobs VALUES("tester", "test stuff", "James Anderson", "Florida", 100000, "An", "Dinh")')
    session.connection.commit()


# fixture so we don't instantiate this DB multiple times
# CacheDB is a class that is created in testDB.py
@pytest.fixture
def cache(session):
    return CacheDB(session)


def test_user(cache):
    user_array = cache.get_user_info("username2")
    assert user_array == ("username2", "Password?2", "An", "Dinh")


# def test_login(session):
#    cache = CacheDB(session)


# This function in cache does not have the limit of 5 jobs
# To test that functionality of the limit of 5 jos go to test_database_tester1
def test_create_job_posting(cache, mocker):
    # patching the builtin input function to provide the input to test.
    mocker.patch('builtins.input', side_effect=["tester", "test stuff", "Bob", "New York", 10, "Test", "Guy"])
    test = cache.create_job("Test", "Guy")
    mocker.patch('builtins.input', side_effect=["tester", "test stuff", "George", "Georgia",
                                                "one hundred", "Test", "Girl"])
    test2 = cache.create_job("Test", "Girl")
    mocker.patch('builtins.input', side_effect=["100", "100", "100", "100", "100", "100", "100"])
    test3 = cache.create_job("100", "100")
    mocker.patch('builtins.input', side_effect=["\n", "\n", "\n", "\n", 100, "\n", "\n"])
    test4 = cache.create_job("\n", "\n")
    mocker.patch('builtins.input', side_effect=[" ", " ", " ", " ", 100, " ", " "])
    test5 = cache.create_job(" ", " ")
    mocker.patch('builtins.input', side_effect=["SELECT * FROM jobs WHERE firstname = 'An'", " ", " ", " ",
                                                100, "An", "Dinhh"])
    test5 = cache.create_job("An", "Dinhh")

    job_array = cache.get_job("Test", "Guy")
    job_array2 = cache.get_job("Test", "Girl")
    job_array3 = cache.get_job("100", "100")
    job_array4 = cache.get_job("\n", "\n")
    job_array5 = cache.get_job("An", "Dinhh")

    assert job_array == ("tester", "test stuff", "Bob", "New York", 10, "Test", "Guy")
    assert test2 is None
    assert job_array2 is None
    assert job_array3 == ("100", "100", "100", "100", 100, "100", "100")
    assert job_array4 == ("\n", "\n", "\n", "\n", 100, "\n", "\n")
    assert job_array5 == ("SELECT * FROM jobs WHERE firstname = 'An'", " ", " ", " ", 100, "An", "Dinhh")


def test_job_post(cache):
    user_array = cache.get_job("An", "Dinh")
    assert user_array == ("tester", "test stuff", "James Anderson", "Florida", 100000, "An", "Dinh")


def test_print(cache):
    print("\n")
    all_jobs = cache.get_all_job()
    for job in all_jobs:
        print(job)


# the capsys is a fixture of pytest, and it is being passed as a parameter to capture the system outputs and errors
def test_succ_story(capsys):
    user_succ_story = start_options.succ_story("../../Student_story.txt")
    # the end= '' was because the print statement alone appended a newline at the end
    # this was the solution to get rid of that newline at the end
    print(user_succ_story, end='')
    # capture will contain output, error data
    capture = capsys.readouterr()
    # only verifying the output for now.
    assert capture.out == user_succ_story


def test_video(capsys):
    start_options.play_video()
    capture = capsys.readouterr()
    assert capture.out == "Video is now playing."


