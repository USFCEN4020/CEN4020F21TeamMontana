import start_options
import db_commands
import useful_links_options
import important_links_group
import user_options
import main
import user_portfolio

def test_title():
    testcase_majors = [
        "art studies",
        "Biomedical Engineering",
        "business Administration",
        "Civil engineering",
        "compuTer scIence",
        "cOMPUTER eGineerIng"
    ]

    assert title(testcase_majors[0]) == "Art Studies"
    assert title(testcase_majors[1]) == "Biomedical Engineering"
    assert title(testcase_majors[2]) == "Business Administration"
    assert title(testcase_majors[3]) == "Civil Engineering"
    assert title(testcase_majors[4]) == "Computer Science"
    assert title(testcase_majors[5]) == "Computer Engineering"
