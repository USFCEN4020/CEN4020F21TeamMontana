import pytest
import main
import useful_links_options
import user_options
import user_portfolio


def test_main_menu(capsys, monkeypatch):
    desired_output = """
            Please choose from the following menu:
            1 - Log into an existing account
            2 - Create an account
            3 - Play a video
            4 - Find a contact in InCollege
            5 - Useful Links Group
            6 - InCollege Important Links Group
            7 - Exit the program

            """
    try:
        main.print_start_menu()
    except(StopIteration):
        output = capsys.readouterr().out
        assert output == desired_output


def test_inside_main_menu(capsys, monkeypatch):
    desired_output = """
    Please choose from the following menu:
    1 - Post a job
    2 - Search for a job
    3 - Find someone you know
    4 - Learn a new skill
    5 - Useful links group options
    6 - InCollege important links group options
    7 - Return to previous menu
    """

    try:
        user_options.print_additional_options()
    except(StopIteration):
        output = capsys.readouterr().out
        assert output == desired_output


def test_profile_menu(capsys, monkeypatch):
    desired_output = """
    Please choose which options to modify
    1 - Enter Title
    2 - Enter Major
    3 - Enter University name
    4 - Enter Information about student
    5 - Enter Experience
    6 - Enter Education
    7 - View Profile
    0 - Return to previous menu"""

    try:
        user_portfolio.print_portfolio_options()
    except(StopIteration):
        output = capsys.readouterr().out
        assert output == desired_output



