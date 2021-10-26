#import pytest
import builtins
#import mock
#import module
from os import major
from experience_commands import create_experience_posting
import db_commands
from tests.unit.testBases import get_display_ouput, set_keyboard_input
import user_portfolio


def test_print_portfolio_options(capsys):
    user_portfolio.print_portfolio_options()
    options = '''Please choose which options to modify
1 - Enter Title
2 - Enter Major
3 - Enter University name
4 - Enter Information about student
5 - Enter Experience
6 - Enter Education
7 - View Profile
0 - Return to previous menu
'''

    capture = capsys.readouterr()
    assert capture.out == options

#Test function Enter_Title:
def test_get_input_title():
    title_test = "The third year Computer Science student"
    set_keyboard_input(["1", title_test, "2", "0"])
    user_portfolio.Enter_Title("test")

    output = get_display_ouput()
    assert output == ["Would you like to enter your Title",
"1 - Enter Title",
"0 - Exit",
"Enter your selection here (0-1): ",
"Please enter your Title:\n",
"Would you like to enter your Title",
"1 - Enter Title",
"0 - Exit",
"Enter your selection here (0-1): ",
"\n Invalid Input \n",
"Would you like to enter your Title",
"1 - Enter Title",
"0 - Exit",
"Enter your selection here (0-1): "]



#Test function Enter_Major():
def test_get_input_major():
    set_keyboard_input(["1","art studies","2","0"])
    user_portfolio.Enter_Major("test")
    output = get_display_ouput()
    assert output == ["Would you like to enter your Major",
"1 - Enter Major",
"0 - Exit",
"Enter your selection here (0-1): ",
"Please enter your Major:\n",
"Would you like to enter your Major",
"1 - Enter Major",
"0 - Exit",
"Enter your selection here (0-1): ",
"\n Invalid Input \n",
"Would you like to enter your Major",
"1 - Enter Major",
"0 - Exit",
"Enter your selection here (0-1): "]

def test_Major_format():
    string_majors = ["art studies",
    "BIomedIcal EngIneerIng",
    "business Administration",
    "Civil engineering",
    "compuTer scIence",
    "cOMPUTER enGineerIng"
    ]
    major = ["","","","","",""]
    for i in range (len(string_majors)):
        major[i] = string_majors[i].title()
    assert major[0] == "Art Studies"
    assert major[1] == "Biomedical Engineering"
    assert major[2] == "Business Administration"
    assert major[3] == "Civil Engineering"
    assert major[4] == "Computer Science"
    assert major[5] == "Computer Engineering"

#Test function Enter_University_Name:
def test_get_input_university():
    set_keyboard_input(["1","University of South Florida","2","0"])
    user_portfolio.Enter_University_Name("test")
    output = get_display_ouput()
    assert output == ["Would you like to enter your Current University",
"1 - Enter University Name",
"0 - Exit",
"Enter your selection here (0-1): ",
"Please enter your University:\n",
"Would you like to enter your Current University",
"1 - Enter University Name",
"0 - Exit",
"Enter your selection here (0-1): ",
"\n Invalid Input \n",
"Would you like to enter your Current University",
"1 - Enter University Name",
"0 - Exit",
"Enter your selection here (0-1): "]

def test_University_Name_format():
    string_universities = ["university OF south florida",
        "HARVARD UNIVERSITY",
        "yALE uNIVERSITY",
        "Standford University",
        "university of chicago",
        "uNiversity Of peNNsylvania"]
    university_name = ["","","","","",""]
    for i in range (len(string_universities)):
        university_name[i] = string_universities[i].title()
    assert university_name[0] == "University Of South Florida"
    assert university_name[1] == "Harvard University"
    assert university_name[2] == "Yale University"
    assert university_name[3] == "Standford University"
    assert university_name[4] == "University Of Chicago"
    assert university_name[5] == "University Of Pennsylvania"

def test_create_experience_posting():

    set_keyboard_input(["Developer", "Amazon", "Florida", "Develop apps","05/30/2018", "07/14/2020"])
    create_experience_posting("test")

    conn = db_commands.create_connection(db_commands.database_name)
    cursor = conn.cursor()
    cursor.execute('''SELECT title FROM experiences WHERE username = ?''', ("test",))
    title = cursor.fetchone()
    cursor.execute('''SELECT employer FROM experiences WHERE username = ?''', ("test",))
    employer = cursor.fetchone()
    cursor.execute('''SELECT location FROM experiences WHERE username = ?''', ("test",))
    location = cursor.fetchone()
    cursor.execute('''SELECT description FROM experiences WHERE username = ?''', ("test",))
    description = cursor.fetchone()
    cursor.execute('''SELECT start_date FROM experiences WHERE username = ?''', ("test",))
    start_date = cursor.fetchone()
    cursor.execute('''SELECT end_date FROM experiences WHERE username = ?''', ("test",))
    end_date = cursor.fetchone()

    assert title == "Developer"
    assert employer == "Amazon"
    assert location == "Florida"
    assert description == "Develop apps"
    assert start_date == "05/30/2018"
    assert end_date == "07/14/2020"
