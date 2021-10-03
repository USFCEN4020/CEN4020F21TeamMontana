import pytest
import start_options
import db_commands
import useful_links_options
import important_links_group

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


def test_important_links_visitors(capsys, mocker):
    mocker.patch('builtins.input', side_effect=["1", "2", "3", "4", "5", "6", "0", "7"])
    important_links_group.important_links_visitors()
    links = """Please choose from the following menu:
1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement Policy
5 - Cookie Policy
6 - Brand Policy
7 - Exit Menu
"""

    print_copyright = "This work is copyrighted" + "\n"
    print_about = "About InCollege" + "\n"
    print_acess = "Accessibility Remarks" + "\n"
    print_agree = "Agree with User Agreement" + "\n"
    print_cookie = "Cookie Policy" + "\n"
    print_brand = "Brand Policy" + "\n"
    print_go_back = "Going back to 'Main' Menu" + "\n"
    print_invalid = "Invalid Input" + "\n"
    option1 = links + print_copyright
    option2 = links + print_about
    option3 = links + print_acess
    option4 = links + print_agree
    option5 = links + print_cookie
    option6 = links + print_brand
    option0 = links + print_invalid
    option7 = links + print_go_back

    result = option1 + option2 + option3 + option4 + option5 + option6 + option0 + option7
    capture = capsys.readouterr()
    assert capture.out == result


def test_important_links_users(capsys, mocker):
    mocker.patch('builtins.input', side_effect=["1", "2", "3", "4", "5", "0",
                                                "5", "2", "0",  "6", "7", "0", "8"])
    important_links_group.important_links_users("test")
    links = """Please choose from the following menu:
1 - Copyright Notice
2 - About
3 - Accessibility
4 - User Agreement Policy
5 - Privacy Policy
6 - Cookie Policy
7 - Brand Policy
8 - Exit Menu
"""

    print_copyright = "This work is copyrighted" + "\n"
    print_about = "About InCollege" + "\n"
    print_acess = "Accessibility Remarks" + "\n"
    print_agree = "Agree with User Agreement" + "\n"
    print_privacy = "Would you like to open Guest Options" + "\n"
    print_privacy_options = "1 - Yes" + "\n" "0 - Exit" + "\n"
    print_cookie = "Cookie Policy" + "\n"
    print_brand = "Brand Policy" + "\n"
    print_go_back = "Going back to 'User Options' Menu" + "\n"
    print_invalid = "Invalid Input" + "\n"
    option1 = links + print_copyright
    option2 = links + print_about
    option3 = links + print_acess
    option4 = links + print_agree
    option5_0 = links + print_privacy + print_privacy_options
    # option5_1 = links + print_privacy + print_privacy_options
    option5_2 = links + print_privacy + print_privacy_options + print_invalid + print_privacy_options
    option6 = links + print_cookie
    option7 = links + print_brand
    option0 = links + print_invalid
    option8 = links + print_go_back

    result = option1 + option2 + option3 + option4 + option5_0 + option5_2 + option6 + option7 + \
             option0 + option8
    capture = capsys.readouterr()
    assert capture.out == result


