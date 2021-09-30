import pytest
import start_options
import db_commands
import useful_links_options

database_name = "userDB"
connection = db_commands.create_connection(database_name)


def test_general_links(capsys, mocker):
    mocker.patch('builtins.input', side_effect=["2", "3", "4", "5"])
    links = """
    General links available:
    1. Sign Up
    2. Help Center
    3. About
    4. Press
    5. Blog
    6. Careers
    7. Developers
    8. Go Back

    """


def test_useful_link(capsys, mocker):
    mocker.patch('builtins.input', side_effect=["2", "3", "4", "5"])
    useful_links_options.useful_link()
    links = """
    Useful links available:
    1. General
    2. Browse InCollege
    3. Business Solutions
    4. Directories
    5. Go Back

    """
    under_construction = "Under construction"

    go_back = "Going back to the Main Menu"

    result = 3*(links + "\n" + under_construction + "\n") + (links + "\n" + go_back + "\n")

    capture = capsys.readouterr()
    assert capture.out == result



