import pytest
import sqlite3
from tests.unit.testDB import CacheDB
import db_commands
import message_options
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


# testing the generation of the users friends list
def test_query_friend(cache):
    friends_list = db_commands.query_friend("username2")
    # Since what is returned is a list of tuples, and the only friend that username2 has is usernaem4
    assert friends_list == [("username4",)]


# this function will test, the reply, read, and delete messages
def test_check_new_message(cache, mocker):
    # test display messages
    message_options.display_inbox("username2")
    # testing read, reply, and delete messages.
    mocker.patch('builtins.input', side_effect=["1", "1", "1", "2", "1", "3", "Smith"])
    message_options.check_new_message("username2")

    message_statuses = cache.get_messages("username2")
    assert len(message_statuses) == 2
    assert message_statuses[0] == ('username3', 'username2', 'Test Message, reply to this message with Cat', 1, 'READ')
    assert message_statuses[1] == ('username4', 'username2', 'This is John, reply back with Smith', 3, 'READ')
    print(*message_statuses, sep="\n")

    message_sent = cache.get_messages("username4")
    assert message_sent[0] == ('username2', 'username4', 'Smith', 4, 'NEW')
    print(*message_sent, sep="\n")

