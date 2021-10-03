# CEN4020F21TeamMontana

Install to run the tests:
pip install pytest
pip install mock

The tests are in the directory tests/unit

userDB
The main database

Added the functionalities of Epic# 2 
Which includes extending the create_account in start_options.py
To ask for first and last name 

Added a success story that gets printed out on the start of the program as a form of built in advertisement

play_video
Asks the user to watch a video of InCollege if they so please, which jsut prints out a simple showing video output for now

join_contact
If the user has a contact they know they can search them up and if they exist prompt the user to create an account or login.
The user is also able to find more contacts when they are logged in with the menu from additional_options

create_job_posting
The user is able to create a job posting, but currently the job does not get displayed.

test_challenge2_tester1
Is testing most of the functionalites that were implemnted in Epic#2.
Which include the job posting, play video, show success story.
It tests the job posting primarily by using an in memory database for quick entry and deletion that does not effect the main database.

test_challenge2_tester2
tests the finding contact functions

test_database_tester1
tests the how the job postings interact with the actual database. 
