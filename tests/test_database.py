import pytest
import sqlite3
from tests.unit.testDB import CacheDB
from job_commands import create_job_posting


@pytest.fixture(scope='session')
def verify_session():
    # create a connection with our program database as well for our specific database functions that access it
    connection = sqlite3.connect("userDB")
    db_session = connection.cursor()
    yield db_session
    connection.close()


# fixture so we don't instantiate this DB multiple times
@pytest.fixture
def cache(verify_session):
    return CacheDB(verify_session)


# This one is passing verify_session instead of cache because we need to access the connection to commit to userDB file
# deleting these rows before the calling job posting
# because we don't want to test the duplicates rows in userDB from the previous runs
def test_delete(verify_session):
    cache = CacheDB(verify_session)
    cache.delete_job("Test", "Guy")
    cache.delete_job("An", "Dinh")
    verify_session.connection.commit()


def test_create_job_posting(cache, mocker):
    print("\n")
    # patching the builtin input function to provide the input to test.
    mocker.patch('builtins.input', side_effect=["tester", "test stuff", "James Anderson", "Florida", 100000, "An", "Dinh"])
    test = create_job_posting("An", "Dinh")

    mocker.patch('builtins.input', side_effect=["tester", "test stuff", "Bob", "New York", 10, "Test", "Guy"])
    test = create_job_posting("Test", "Guy")

    job_array1 = cache.get_job("An", "Dinh")
    job_array2 = cache.get_job("Test", "Guy")

    assert job_array1 == ("tester", "test stuff", "James Anderson", "Florida", 100000, "An", "Dinh")
    assert job_array2 == ("tester", "test stuff", "Bob", "New York", 10, "Test", "Guy")


def test_print(cache):
    print("\n")
    all_jobs = cache.get_all_job()
    for job in all_jobs:
        print(job)


