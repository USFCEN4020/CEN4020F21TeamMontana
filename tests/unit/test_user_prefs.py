import pytest
import main
import important_links_group
import user_options
import db_commands


def test_fake_database_setup():
    test_connection = db_commands.create_connection("testDB")
    db_commands.create_table(test_connection, db_commands.user_table)
    user_information = (
    "username", "Password?2", "John", "Smith", "English", "Send Emails", "Send SMS", "Target Ads")
    db_commands.create_row_in_users_table(test_connection, user_information)

    return test_connection


def test_user_language_pref(capsys, monkeypatch):
    desired_output = """
            "Default Language is now English\n"
            """
    inputs = iter('1')
    test_connection = fake_databasesetup()
    monkeypatch.setattr('builtins.input', lambda _="": next(inputs))
    try:
        important_links_group.ChangeLanguage("username")
    except(StopIteration):
        output = capsys.readouterr().out
        assert output == desired_output
