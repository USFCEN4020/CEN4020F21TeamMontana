import pytest
import sqlite3

import main
from tests.unit.testDB import CacheDB
import db_commands
import os
import incollege_learning

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
# Tests for Week 9

# Test menu for list of courses
def test_incollege_training_menu(cache, capsys):
    incollege_learning.print_incollege_training_menu()
    output = capsys.readouterr().out
    assert output == '''
    Please Select Which Course To Take
    1 - How to use In College Learning
    2 - Train the Trainer
    3 - Gamification of learning
    4 - Understanding the Architecture Design Process
    5 - Project Management Simplified 
    0 - Exit
    
'''


# Test training menu
def test_start_training_menu(cache, monkeypatch, capsys):
    desired_output = """"
            Please select a training option or enter 5 to return:
            1 - Training and Education
            2 - IT Help Desk
            3 - Business Analysis and Strategy
            4 - Security
            5 - Return to main menu

            """ + "Returning to main menu..."
    inputs = iter(["5"])
    monkeypatch.setattr('builtins.input', lambda _="": next(inputs))
    try:
        main.training_menu()
    except StopIteration:
        output = capsys.readouterr().out
        assert output == desired_output


# Test when student completes training
def test_complete_training(cache, monkeypatch, capsys):
    desired_output = "You have now completed this training! (InCollege Learning)"
    inputs = iter(["1", "1", "0"])
    monkeypatch.setattr('builtins.input', lambda _="": next(inputs))
    try:
        incollege_learning.incollege_training_options("username1")
    except StopIteration:
        output = capsys.readouterr().out
        assert output == desired_output


# Test when student completes training that has already been completed
def test_training_if_already_done(cache, monkeypatch, capsys):
    desired_output = "You have now completed this training! (InCollege Learning)"
    desired_output += """"
                Please select a training option or enter 5 to return:
                1 - Training and Education
                2 - IT Help Desk
                3 - Business Analysis and Strategy
                4 - Security
                5 - Return to main menu

                """
    desired_output += """You have already taken this course, do you want to take it again
                        0 - No
                        1 - Yes"""
    desired_output += "You have now completed this training! (InCollege Learning)"
    inputs = iter(["1", "1", "0", "0"])
    monkeypatch.setattr('builtins.input', lambda _="": next(inputs))
    try:
        incollege_learning.incollege_training_options("username1")
        incollege_learning.incollege_training_options("username1")
    except StopIteration:
        output = capsys.readouterr().out
        assert output == desired_output







