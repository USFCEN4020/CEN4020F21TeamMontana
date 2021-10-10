import pytest
import user_portfolio
import db_commands
import sqlite3
from testDB import CacheDB

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


def test_user_info(cache, capsys):
    user_info = "Test User Info"
    db_commands.User_Info("username2", user_info)
    output = capsys.readouterr().out
    assert output == ""
    #  if no output/no errors, the database successfully called
    # check by getting user info and comparing to user_info
    assert ('Test User Info',) == db_commands.query_student_info("username2")[0]


def test_education(cache, capsys):
    user_info = "Test User Info"
    db_commands.User_University("username2", user_info)
    db_commands.User_Major("username2", user_info)
    db_commands.User_Education("username2", user_info)
    output = capsys.readouterr().out
    assert output == ""
    print("test")
    assert ('Test User Info', 'Test User Info', 'Test User Info') == db_commands.query_education("username2")[0]
    #  if no output/no errors, the database successfully called
    # check by getting user info and comparing to user_info


