#pytest file for main.py

import pytest           #used for testing different functions for a given file
import main             #name of file thats being tested
import random           #used to generate random test values

#test function
def test_challenge1():

    i = 0
    print("================ start of password_meets_qualifications tests =================")
    while i < 10:       #will test 10 passwords
        password = ""
        j = 0

        # generates up to 10 characters in case digit/capital letter needs to be added
        password_length = random.randint(8, 11)
        has_cap_letter = False
        has_digit = False
        while j < password_length:      #generates password of length password_length
            next_char = random.randint(33, 126)
            if 48 <= next_char <= 57:
                has_digit = True
            if 65 <= next_char <= 90:
                has_cap_letter = True
            password += chr(next_char)
            j += 1
        i += 1
        val = main.password_meets_qualifications(password)  #applies password function in main.py as test value
        if val is True:  #prints if password is good
            print("test #" + str(i) + ":\t" + str(password) + "\t\t PASSED")  # prints current password
        elif val is False: #prints if password is bad
            print("test #" + str(i) + ":\t" + str(password) + "\t\t FAILED")  # prints current password
    print("================= end of password_meets_qualifications tests ==================\n\n")

    i = 0
    existing_usernames = []
    print("================ start of username_meets_qualifications tests =================")
    while i < 5:  # creates 5 usernames that would already be created
        username_input = ""
        j = 0

        # generates usernames between 3 and 10 characters
        username_length = random.randint(3, 11)
        while j < username_length:  # generates password of length password_length
            next_char = random.randint(33, 126)
            username_input += chr(next_char)
            j += 1
        i += 1
        existing_usernames.append(username_input)
    i = 0
    print("- - - - - - - Here are the 5 accounts that are being compare to - - - - - - - -")
    while i < 5:
        print(existing_usernames[i])
        i += 1

    i = 0
    print("- - - - - - - - Here are the usernames that are being tested  - - - - - - - - -")
    while i < 10:  # will create 10 new usernames
        username_input = ""
        j = 0

        # generates usernames between 3 and 10 characters
        replace_username = random.randint(0, 1)
        if replace_username == 0:
            username_input = existing_usernames[random.randint(0, 4)]
        else:
            username_length = random.randint(3, 11)
            while j < username_length:  # generates password of length password_length
                next_char = random.randint(33, 126)
                username_input += chr(next_char)
                j += 1
        i += 1

        val = main.username_meets_qualifications(username_input, existing_usernames)  # applies username function in main.py as test value
        if val is True:  # prints if username is good
            print("test #" + str(i) + ":\t" + str(username_input) + "\t\t PASSED")  # prints current password
        elif val is False:  # prints if username is bad
            print("test #" + str(i) + ":\t" + str(username_input) + "\t\t FAILED")  # prints current password
    print("================= end of username_meets_qualifications tests ==================\n\n")
    print("Next test should return FAILED")
    assert val is 2 #ends test with FAILED while allowing for print statements to still show

#runs test on main
pytest.main()