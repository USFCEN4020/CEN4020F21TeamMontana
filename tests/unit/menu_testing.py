import pytest
import main
import useful_links_options


def test_main_menu(capsys, monkeypatch):
    desired_output = """
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

    try:
        useful_links_options.print_general_link()
    except(StopIteration):
        output = capsys.readouterr().out
        assert output == desired_output



