import db_commands
import user_options


def userLogin(username_input, password_input, existing_usernames, username_password_tuples):
    succLogin = False
    # for loop to check to check each row of tuples returned by the query if the username is in the database
    for row in existing_usernames:
        if row[0] == username_input:
            # continue the infinite attempts by the user to try and enter the correct password
            # convert the list into a dictionary, since all usernames should be distinct
            userPass_lookup = dict(username_password_tuples)
            userPassword = userPass_lookup[username_input]
            while password_input != userPassword and password_input != "Q":
                print("Incorrect password, please try again")
                password_input = input("Enter your password, or Q to quit the program: ")
            if password_input == userPassword:
                print("You have successfully logged in")
                succLogin = True
                # call function here to get the user into inCollege and be able to use their functions
                firstname, lastname = db_commands.find_names_from_username(username_input)
                user_options.additional_options(username_input, firstname, lastname)
                #return that succLogin is true back to main. And it will break out of the userLogin while loop and users will then be greeted with the first options when program runs
                return succLogin
            elif password_input == "Q":
                print("Exiting program now, hope to see you again!")
                # succLogin False in this case
                return succLogin
    if username_input == "Q":
        print("Exiting program now, hope to see you again!")
        # succLogin False in this case
        return succLogin
    elif not succLogin:  # This is necessary so it doesn't print even if there was a successful login
        # Did not put this print statement into the for loop, because it would print this out multiple times if I had it in an else statement
        print("Incorrect username, please try again")
        # succLogin False in this case
        return succLogin


def username_meets_qualifications(username_input, existing_usernames):
    if len(existing_usernames) > 5:
        print("The system has too many users already.")
        return False

    for user in existing_usernames:
        if user[0] == username_input:
            print("This username already exists.")
            return False
    return True


def password_meets_qualifications(password):
    if len(password) < 8:
        return False
    if len(password) > 12:
        return False

    # Redo more efficiently
    # Checks to have 1 capitalized letter
    counter = False
    for letter in password:
        if letter.isupper():
            counter = True

    if not counter:
        return False

    # Checks to have 1 digit
    counter = False
    for letter in password:
        if letter.isdigit():
            counter = True

    if not counter:
        return False

    # Checks to have 1 non alpha character
    counter = False
    for letter in password:
        if not letter.isalpha():
            counter = True

    if not counter:
        return False

    return True


def does_user_exist(first_name_input, last_name_input):
    first_name_input.lower()
    last_name_input.lower()
    connection = db_commands.create_connection(db_commands.database_name)
    existing_names = db_commands.query_names(connection)
    for firstname, lastname in existing_names:
        firstname.lower()
        lastname.lower()
        if firstname == first_name_input and lastname == last_name_input:
            return True
    return False
