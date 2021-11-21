from important_links_group import important_links_users
from useful_links_options import useful_link
import account_define
import random
import job_commands
import db_commands
from user_portfolio import portfolio_options
import friends_options
import friend_commands
import message_options
import user_notification
import new_user_notifications
import new_job_notifications
import incollege_learning
import api


def search_job(username):
    job_commands.jobs_menu(username)
    return 0


# This function isn't necessary
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


def new_skill(username):
    while True:
        # Decided have this list of skills rather than just hardcode 5 skills that will be the same for all users.
        # Add more skills here later on
        skill_list = ["Software Engineering", "Software Development",  "Waterfall", "Agile", "Scrum", "Jira", "Python"]
        # gets 5 unique random skills from skill_list, so that Users don't have multiple of the same options
        sampled_list = random.sample(skill_list, 5)

        print("Please choose from the following menu:")
        print("1 - {}".format(sampled_list[0]))
        print("2 - {}".format(sampled_list[1]))
        print("3 - {}".format(sampled_list[2]))
        print("4 - {}".format(sampled_list[3]))
        print("5 - {}".format(sampled_list[4]))
        print("6 - Return back to previous options.")
        user_choice_skill = input("Enter your selection here: ")

        # Have the remove function on the list to remove the skills that the user has already selected
        # Did type casting on user_choice_skill and subtracted by 1 so that it can print out the skill at the index that the user selected
        # the if checks for between 1 and 5 just so I don't have to deal with out of bound cases
        if 6 > int(user_choice_skill) > 0:
            for i in sampled_list:
                # i represents the string in the sampled_list
                if sampled_list[int(user_choice_skill) - 1] == i:
                    # Since the skill_list gets declared each time again in the function at the top, it does not get removed.
                    # The skill_list is a local varaible, so to fix that probably create a profile or something per user, and have the skills they selected.
                    # So, there are no future appearences of duplicate skills, and it is user specific.
                    skill_list.remove(sampled_list[int(user_choice_skill) - 1])
                    print("Under construction")

        if user_choice_skill == "6":
            # At first I thought to call the function again, but if I return 0 it accomplishes the same thing
            # as it returns 0 back to the previous function.
            # additionalOptions(username)
            return 0
        elif 6 < int(user_choice_skill) < 1:
            print("Not a valid input")
    return 0


def print_additional_options():
    print("Please choose from the following menu:")
    print("0 - Message options")
    print("1 - Post/Delete a job")
    print("2 - Search for a job")
    print("3 - Find someone you know")
    print("4 - Show my network")
    print("5 - Learn a new skill")
    print("6 - Useful links group options")
    print("7 - InCollege important links group options")
    print("8 - Edit user profile")
    print("9 - Send friend request")
    print("10 - InCollege Learning ")
    print("11 - Return to previous menu")


def additional_options(username):
    # Check to see if the user has any pending friend requests that were sent to them.
    friends_options.check_friend_requests(username)

    # Check for saved/applied jobs
    job_commands.display_saved_jobs(username)
    job_commands.display_applied_jobs(username)
    
    # Check if user has new message to read
    message_options.check_new_message(username)
    #check if profile is already created
    user_notification.print_notification(username)

    # Epic 8
    # Shows Notifications for new users and jobs and reminders
    new_user_notifications.show_new_user_notifications(username)
    new_job_notifications.show_new_jobs(db_commands.create_connection(db_commands.database_name))
    new_job_notifications.check_applied_job_time(db_commands.create_connection(db_commands.database_name), username)

    while True:
        print_additional_options()
        user_choice_opt = input("Enter your selection here: ")

        # Potentially use switch
        if user_choice_opt == "0":
            # Message options
            message_options.member_options(username)
        if user_choice_opt == "1":
            user_notification.job_applied_notifiction(username)
            print("Do you want to post or delete a job?\n"
                  "1 - Post a job\n"
                  "2 - Delete a job I posted")
            user_choice_opt = input("Enter your selection here: ")
            if user_choice_opt == "1":
                user_first_last = db_commands.query_names_user(username, db_commands.create_connection(db_commands.database_name))
                job_commands.create_job_posting(user_first_last[0], user_first_last[1])
                api.output_jobs()
            elif user_choice_opt == "2":
                user_first_last = db_commands.query_names_user(username, db_commands.create_connection(db_commands.database_name))
                job_commands.delete_job_posting(user_first_last[0], user_first_last[1])
                api.output_jobs()
            else:
                print("Invalid Input, Enter either the value 1 or 2")
        elif user_choice_opt == "2":
            user_notification.job_applied_notifiction(username)
            search_job(username)
        elif user_choice_opt == "3":
            print("Looking for someone you know?")
            first_name_input = input("Enter the first name: ")
            last_name_input = input("Enter the last name: ")
            user_exists = does_user_exist(first_name_input, last_name_input)
            if user_exists:
                print("They are part of the InCollege system.")
            else:
                print("They are not part of the InCollege system.")
        elif user_choice_opt == "4":
            friends_options.show_network(username)
        elif user_choice_opt == "5":
            new_skill(username)
        elif user_choice_opt == "6":
            useful_link()
        elif user_choice_opt == "7":
            important_links_users(username)
        elif user_choice_opt == "8":
            portfolio_options(username)
            api.output_profiles()
        elif user_choice_opt == "9":
            friend_commands.create_friend_posting(username)
        elif user_choice_opt == "10":
            incollege_learning.incollege_training_options(username)
        elif user_choice_opt == "11":
            break
        else:
            print("Not a valid input")
    return 0
