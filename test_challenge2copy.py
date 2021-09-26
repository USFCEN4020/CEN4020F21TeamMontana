import pytest
import sqlite3
from testDB import CacheDB
import mock
from account_define import userLogin
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
def cache(verify_session): # 1
    return CacheDB(verify_session)


def test_create_job_posting(verify_session, mocker):
    cache = CacheDB(verify_session)
    # patching the builtin input function to provide the input to test.
    mocker.patch('builtins.input', side_effect=["tester", "test stuff", "James Anderson", "Florida", 100000, "An", "Dinhh"])
    test = create_job_posting("An", "Dinhh")

    job_array = cache.get_job("An", "Dinhh")

    assert job_array == ("tester", "test stuff", "James Anderson", "Florida", 100000, "An", "Dinhh")


def test_print(verify_session):
    cache = CacheDB(verify_session)
    all_jobs = cache.get_all_job()
    for job in all_jobs:
        print(job)

