import pytest
import main
import important_links_group
import user_options
import db_commands
import sqlite3
from testDB import CacheDB

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
    language text NOT NULL,
    emails text NOT NULL,
    sms text NOT NULL,
    targetedads text NOT NULL,
    title text NOT NULL,
    major text NOT NULL,
    university text NOT NULL,
    studentinfo text NOT NULL,
    education text NOT NULL,
    UNIQUE(firstname, lastname)
    );""")
    session.execute('INSERT INTO users VALUES("username2", "Password?2", "An", "Dinh", "English", "Send Emails", "Send SMS", "Target Ads", "TITLE:NULL", "MAJOR:NULL", "UNIVERSITY:NULL", "STUDENTINFO:NULL", "EDUCATION:NULL")')
    session.connection.commit()


# fixture so we don't instantiate this DB multiple times
# CacheDB is a class that is created in testDB.py
@pytest.fixture
def cache(session):
    return CacheDB(session)


def test_user_language_pref(cache):
    cache.change_language_prefs("username2", "Spanish")
    user_lang = cache.get_user_lang("username2")
    assert user_lang[0] == "Spanish"


def test_user_email_pref(cache):
    cache.change_email_prefs("username2", "Send Emails")
    user_lang = cache.get_user_email("username2")
    assert user_lang[0] == 'Send Emails'


def test_user_sms_pref(cache):
    cache.change_email_prefs("username2", 'Send SMS')
    user_lang = cache.get_user_email("username2")
    assert user_lang[0] == 'Send SMS'


def test_user_ads_pref(cache):
    cache.change_ads_prefs("username2", 'Target Ads')
    user_lang = cache.get_user_ads("username2")
    assert user_lang[0] == 'Target Ads'


