#pytest file for main.py

import pytest           #used for testing different functions for a given file
import db_commands      #used for retrieving/updating database information
import user_options     #name of file thats being tested
import random           #used to generate random test values

import sqlite3
from sqlite3 import Error
database_name = "userDB"

#test function
def test_challenge2():
    print("====================== start of does_user_exist tests ========================")

    connection = db_commands.create_connection(database_name)
    existing_names = db_commands.query_names(connection)

    print("- - - - Here are the existing names that are being compared - - - - - - -")
    for firstname, lastname in existing_names:
        firstname.lower()
        lastname.lower()
        print(firstname + " " + lastname)


    print("- - - - Here are the input names that are being tested for  - - - - - - -")

    i = 0
    while i < 10:       #will test 10 names
        first_name_input = ""
        last_name_input = ""

        # generates a first name from 2 to 12 characters
        first_name_length = random.randint(2, 12)
        last_name_length = random.randint(2, 12)

        j = 0
        while j < first_name_length:      #generates password of length password_length
            next_char = random.randint(33, 126)
            first_name_input += chr(next_char)
            j += 1

        j = 0
        while j < last_name_length:      #generates password of length password_length
            next_char = random.randint(33, 126)
            last_name_input += chr(next_char)
            j += 1
        i += 1

        #randomly tests an existing name
        real_name_input = random.randint(0, 2)
        if real_name_input == 0:
            random_existing_name = random.sample(existing_names, 1)
            for firstname, lastname in random_existing_name:
                first_name_input = firstname
                last_name_input = lastname


        val = user_options.does_user_exist(first_name_input, last_name_input)  #applies password function in main.py as test value
        if val is True:  #prints if password is good
            print("test #" + str(i) + ":\t" + str(first_name_input) + " " + str(last_name_input) + "\t\t PASSED")  # prints current password
        elif val is False: #prints if password is bad
            print("test #" + str(i) + ":\t" + str(first_name_input) + " " + str(last_name_input) + "\t\t FAILED")  # prints current password
    print("======================= end of does_user_exist tests =========================\n\n")

    i = 0
    print("Next test should return FAILED")
    assert val is 2 #ends test with FAILED while allowing for print statements to still show

#runs test on main
pytest.main()