import pytest
import start_options
import db_commands
import useful_links_options

database_name = "userDB"
connection = db_commands.create_connection(database_name)


def test_general_links(capsys, mocker):
    mocker.patch('builtins.input', side_effect=["2", "3", "4", "5", "6", "7", "8"])
    useful_links_options.general_link()
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

        """ + "\n"

    print_help = "We're here to help." + "\n"
    print_about = "InCollege: Welcome to InCollege, the world's largest college student network " \
                  "with many users in many countries and territories worldwide" + "\n"
    print_press = "InCollege Pressroom: Stay on top of the latest news, updates, and reports" + "\n"
    print_under_construction = "Under Construction" + "\n"
    print_go_back = "Going back to 'Useful Links' Menu" + "\n"
    option2 = links + print_help
    option3 = links + print_about
    option4 = links + print_press
    option5 = links + print_under_construction
    option6 = links + print_under_construction
    option7 = links + print_under_construction
    option8 = links + print_go_back

    result = option2 + option3 + option4 + option5 + option6 + option7 + option8
    capture = capsys.readouterr()
    assert capture.out == result


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

        """ + "\n"
    print_under_construction = "Under Construction" + "\n"
    print_go_back = "Going back to the Main Menu" + "\n"
    option2 = links + print_under_construction
    option3 = links + print_under_construction
    option4 = links + print_under_construction
    option5 = links + print_go_back

    # result = 3*(links + "\n" + under_construction + "\n") + (links + "\n" + go_back + "\n")
    # the "\n" because of the print() statement creates a new line after printing out its output
    result = option2 + option3 + option4 + option5

    capture = capsys.readouterr()
    assert capture.out == result



