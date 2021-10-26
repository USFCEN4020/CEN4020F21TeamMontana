import builtins
from os import major
import pytest
import sqlite3
from tests.unit.testDB import CacheDB
from experience_commands import create_experience_posting
import start_options
import db_commands
import useful_links_options
import important_links_group
import user_options
import main
import user_portfolio


def test_print_portfolio_options(capsys):
    user_portfolio.print_portfolio_options()
    options = """Please choose which options to modify
1 - Enter Title
2 - Enter Major
3 - Enter University name
4 - Enter Information about student
5 - Enter Experience
6 - Enter Education
7 - View Profile
0 - Return to previous menu
"""
    capture = capsys.readouterr()
    assert capture.out == options


def test_Enter_Title_func():
    title_test = "The third year Computer Science student"
    conn = db_commands.create_connection(db_commands.database_name)
    cursor = conn.cursor()
    cursor.execute('''SELECT username FROM users''')
    username = cursor.fetchone()
    user_portfolio.Enter_Title(username)

    db_commands.User_Title(username, title_test)
    cursor.execute('''SELECT title FROM users WHERE username = ?''', (username,))
    title = cursor.fetchone()

    assert title == "The third year Computer Science student"
    print(title)


def test_Enter_Major_func():
    testcase_majors = [
        "art studies",
        "Biomedical Engineering",
        "business Administration",
        "Civil engineering",
        "compuTer scIence",
        "cOMPUTER eGineerIng"
    ]

    conn = db_commands.create_connection(db_commands.database_name)
    cursor = conn.cursor()
    cursor.execute('''SELECT username FROM users''')
    username = cursor.fetchone()
    user_portfolio.Enter_Major(username)

    db_commands.User_Major(username, testcase_majors[0])
    cursor.execute('''SELECT major FROM users WHERE username = ?''', (username,))
    major = cursor.fetchone()
    assert major.title() == "Art Studies"

    db_commands.User_Major(username, testcase_majors[1])
    cursor.execute('''SELECT major FROM users WHERE username = ?''', (username,))
    major = cursor.fetchone()
    assert major.title() == "Biomedical Engineering"

    db_commands.User_Major(username, testcase_majors[2])
    cursor.execute('''SELECT major FROM users WHERE username = ?''', (username,))
    major = cursor.fetchone()
    assert major.title() == "Business Administration"

    db_commands.User_Major(username, testcase_majors[3])
    cursor.execute('''SELECT major FROM users WHERE username = ?''', (username,))
    major = cursor.fetchone()
    assert major.title() == "Civil Engineering"

    db_commands.User_Major(username, testcase_majors[4])
    cursor.execute('''SELECT major FROM users WHERE username = ?''', (username,))
    major = cursor.fetchone()
    assert major.title() == "Computer Science"

    db_commands.User_Major(username, testcase_majors[5])
    cursor.execute('''SELECT major FROM users WHERE username = ?''', (username,))
    major = cursor.fetchone()
    assert major.title() == "Computer Engineering"


def test_Enter_University_Name_func():
    testcase_universities = [
        "university OF south florida",
        "HARVARD UNIVERSITY",
        "yALE uNIVERSITY",
        "Standford University",
        "university if chicago",
        "uNiversity Of peNNsylvania" 
    ]

    conn = db_commands.create_connection(db_commands.database_name)
    cursor = conn.cursor()
    cursor.execute('''SELECT username FROM users''')
    username = cursor.fetchone()
    user_portfolio.Enter_University_Name(username)

    db_commands.User_University(username, testcase_universities[0])
    cursor.execute('''SELECT university FROM users WHERE username = ?''', (username,))
    university = cursor.fetchone()
    assert university.title() == "University Of South Florida"

    db_commands.User_University(username, testcase_universities[0])
    cursor.execute('''SELECT university FROM users WHERE username = ?''', (username,))
    university = cursor.fetchone()
    assert university.title() == "Harvard University"

    db_commands.User_University(username, testcase_universities[0])
    cursor.execute('''SELECT university FROM users WHERE username = ?''', (username,))
    university = cursor.fetchone()
    assert university.title() == "Yale University"

    db_commands.User_University(username, testcase_universities[0])
    cursor.execute('''SELECT university FROM users WHERE username = ?''', (username,))
    university = cursor.fetchone()
    assert university.title() == "Standford University"

    db_commands.User_University(username, testcase_universities[0])
    cursor.execute('''SELECT university FROM users WHERE username = ?''', (username,))
    university = cursor.fetchone()
    assert university.title() == "University Of Chicago"

    db_commands.User_University(username, testcase_universities[0])
    cursor.execute('''SELECT university FROM users WHERE username = ?''', (username,))
    university = cursor.fetchone()
    assert university.title() == "University Of Pennsylvania"


def test_create_experience_posting_func(cache, mocker):

    mocker.patch('builtins.input', side_effect=["Developer", "Amazon", "Florida", "05/30/2018", "07/14/2020", "Username1"])
    test = create_experience_posting("Username1")

    mocker.patch('builtins.input', side_effect=["Tester", "Google", "Florida", "08/30/2017", "09/15/2021", "UsernameTest"])
    test = create_experience_posting("Username2")

    experience_array1 = cache.get_experience("Username1")
    experience_array2 = cache.get_experience("UsernameTest")

    assert experience_array1 == ("Developer", "Amazon", "Florida", "05/30/2018", "07/14/2020", "Username1")
    assert experience_array2 == ("Tester", "Google", "Florida", "08/30/2017", "09/15/2021", "UsernameTest")

    all_experience = cache.get_all_experience()
    for experience in all_experience:
        print(experience)
    