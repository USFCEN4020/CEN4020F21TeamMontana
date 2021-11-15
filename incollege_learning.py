import db_commands

def print_incollege_training_menu():
    learning_menu = '''
    Please Select Which Course To Take
    1 - How to use In College Learning
    2 - Train the Trainer
    3 - Gamification of learning
    4 - Understanding the Architecture Design Process
    5 - Project Management Simplified 
    0 - Exit
    '''
    print(learning_menu)

def incollege_training_options(username):
    connection = db_commands.create_connection(db_commands.database_name)
    while True:
        print_incollege_training_menu()
        user_choice = input("Enter Selection Here... (0-5)")

        if user_choice == "1":
            if db_commands.get_trainings_status(connection, username, 1)[0] == "FINISHED":
                while True:
                    print("You have already taken this course, do you want to take it again")
                    print("0 - No\n"
                          "1 - Yes")

                    user_choice = input("Enter Selection Here... (0-1)")
                    if user_choice == "1":
                        print("You have now completed this training! (InCollege Learning)")
                        break
                    elif user_choice == "0":
                        print("Course Canceled")
                        break
                    else:
                        print("Invalid Input")
                        continue
            elif db_commands.get_trainings_status(connection, username, 1)[0] == "UNFINISHED":
                print("You have now completed this training! (InCollege Learning)")
                db_commands.update_trainings(connection, username, 1)

        elif user_choice == "2":
            if db_commands.get_trainings_status(connection, username, 2)[0] == "FINISHED":
                while True:
                    print("You have already taken this course, do you want to take it again")
                    print("0 - No\n"
                          "1 - Yes")
                    user_choice = input("Enter Selection Here... (0-1)")
                    if user_choice == "1":
                        print("You have now completed this training! (InCollege Learning)")
                        break
                    elif user_choice == "0":
                        print("Course Canceled")
                        break
                    else:
                        print("Invalid Input")
                        continue
            elif db_commands.get_trainings_status(connection, username, 2)[0] == "UNFINISHED":
                print("You have now completed this training! (InCollege Learning)")
                db_commands.update_trainings(connection, username, 2)

        elif user_choice == "3":
            if db_commands.get_trainings_status(connection, username, 3)[0] == "FINISHED":
                while True:
                    print("You have already taken this course, do you want to take it again")
                    print("0 - No\n"
                          "1 - Yes")
                    user_choice = input("Enter Selection Here... (0-1)")
                    if user_choice == "1":
                        print("You have now completed this training! (InCollege Learning)")
                        break
                    elif user_choice == "0":
                        print("Course Canceled")
                        break
                    else:
                        print("Invalid Input")
                        continue
            elif db_commands.get_trainings_status(connection, username, 3)[0] == "UNFINISHED":
                print("You have now completed this training! (InCollege Learning)")
                db_commands.update_trainings(connection, username, 3)

        elif user_choice == "4":
            if db_commands.get_trainings_status(connection, username, 4)[0] == "FINISHED":
                while True:
                    print("You have already taken this course, do you want to take it again")
                    print("0 - No\n"
                          "1 - Yes")
                    user_choice = input("Enter Selection Here... (0-1)")
                    if user_choice == "1":
                        print("You have now completed this training! (InCollege Learning)")
                        break
                    elif user_choice == "0":
                        print("Course Canceled")
                        break
                    else:
                        print("Invalid Input")
                        continue
            elif db_commands.get_trainings_status(connection, username, 4)[0] == "UNFINISHED":
                print("You have now completed this training! (InCollege Learning)")
                db_commands.update_trainings(connection, username, 4)

        elif user_choice == "5":
            if db_commands.get_trainings_status(connection, username, 5)[0] == "FINISHED":
                while True:
                    print("You have already taken this course, do you want to take it again")
                    print("0 - No\n"
                          "1 - Yes")
                    user_choice = input("Enter Selection Here... (0-1)")
                    if user_choice == "1":
                        print("You have now completed this training! (InCollege Learning)")
                        break
                    elif user_choice == "0":
                        print("Course Canceled")
                        break
                    else:
                        print("Invalid Input")
                        continue
            elif db_commands.get_trainings_status(connection, username, 5)[0] == "UNFINISHED":
                print("You have now completed this training! (InCollege Learning)")
                db_commands.update_trainings(connection, username, 5)

        elif user_choice == "0":
            print("exit")
            break

        else:
            print("Invalid Input\n")
            continue