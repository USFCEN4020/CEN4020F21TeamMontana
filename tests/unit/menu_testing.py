import pytest
import main
import useful_links_options

# ignore this
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



