import pytest
import main
import important_links_group
import user_options
import db_commands
import sqlite3


# not fully implemented
#def test_user_language_pref(capsys, monkeypatch):
#    desired_output = """
#            "Default Language is now English\n"
#            """
    #inputs = iter('1')
    #monkeypatch.setattr('builtins.input', lambda _="": next(inputs))

#    try:
#        db_commands.ChangeLang('username', "English")
#    except(StopIteration):
#        output = capsys.readouterr().out
#        assert output == desired_output
#    except sqlite3.OperationalError:
#        output = capsys.readouterr().out
#        assert output == desired_output
