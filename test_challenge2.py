import pytest
import sqlite3
from testDB import CacheDB
import mock
from account_define import userLogin
from job_commands import create_job_posting


@pytest.fixture(scope='session', params=[':memory:'])
def session(request):
    # create in memory database, just for testing purposes
    connection = sqlite3.connect(request.param)
    db_session = connection.cursor()
    yield db_session
    connection.close()


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
@pytest.fixture
def cache(session):
    return CacheDB(session)


def test_user(session):
    username = "username2"
    password = "Password?2"
    firstname = "An"
    lastname = "Dinh"

    cache = CacheDB(session)

    user_array = cache.get_user_info("username2")
    assert user_array == ("username2", "Password?2", "An", "Dinh")


# def test_login(session):
#    cache = CacheDB(session)


def test_create_job_posting(session, mocker):
    cache = CacheDB(session)

    # patching the builtin input function to provide the input to test.
    mocker.patch('builtins.input', side_effect=["tester", "test stuff", "Bob", "New York", 10, "Test", "Guy"])
    test = cache.create_job("Test", "Guy")

    job_array = cache.get_job("Test", "Guy")

    assert job_array == ("tester", "test stuff", "Bob", "New York", 10, "Test", "Guy")


def test_job_post(session):
    cache = CacheDB(session)

    user_array = cache.get_job("An", "Dinh")
    assert user_array == ("tester", "test stuff", "James Anderson", "Florida", 100000, "An", "Dinh")


def test_print(session):
    cache = CacheDB(session)
    print("\n")
    all_jobs = cache.get_all_job()
    for job in all_jobs:
        print(job)