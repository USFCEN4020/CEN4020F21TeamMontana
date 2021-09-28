from important_links_group import important_link
from useful_links import useful_link
import account_define
import random
import job_commands
import db_commands



def searchJob(username):
    print("Under construction")
    return 0


#This function isn't necessary
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


def newSkill(username):
    while True:
        #Decided have this list of skills rather than just hardcode 5 skills that will be the same for all users.
        #Add more skills here later on
        skillList = ["Software Engineering", "Software Development",  "Waterfall", "Agile", "Scrum", "Jira", "Python"]
        #gets 5 unique random skills from skillList, so that Users don't have multiple of the same options
        sampledList = random.sample(skillList, 5)

        print("Please choose from the following menu:")
        print("1 - {}".format(sampledList[0]))
        print("2 - {}".format(sampledList[1]))
        print("3 - {}".format(sampledList[2]))
        print("4 - {}".format(sampledList[3]))
        print("5 - {}".format(sampledList[4]))
        print("6 - Return back to previous options.")
        userChoiceSkill = input("Enter your selection here: ")

        #Have the remove function on the list to remove the skills that the user has already selected
        #Did type casting on userChoiceSkill and subtracted by 1 so that it can print out the skill at the index that the user selected
        #the if checks for between 1 and 5 just so I don't have to deal with out of bound cases
        if 6 > int(userChoiceSkill) > 0:
            for i in sampledList:
                #i represents the string in the sampledList
                if sampledList[int(userChoiceSkill) - 1] == i:
                    #Since the skillList gets declared each time again in the function at the top, it does not get removed.
                    #The skillList is a local varaible, so to fix that probably create a profile or something per user, and have the skills they selected.
                    #So, there are no future appearences of duplicate skills, and it is user specific.
                    skillList.remove(sampledList[int(userChoiceSkill) - 1])
                    print("Under construction")

        if userChoiceSkill == "6":
            #At first I thought to call the function again, but if I return 0 it accomplishes the same thing as it returns 0 back to the previous function.
            #additionalOptions(username)
            return 0
        elif int(userChoiceSkill) > 6 and int(userChoiceSkill) < 1:
            print("Not a valid input")
    return 0


def additional_options(username):
    while True:
        print("Please choose from the following menu:")
        print("1 - Post a job")
        print("2 - Search for a job")
        print("3 - Find someone you know")
        print("4 - Learn a new skill")
        print("5 - Useful links group options")
        print("6 - InCollege important links group options")
        print("7 - Return to previous menu")
        userChoiceOpt = input("Enter your selection here: ")

        # Potentially use switch
        if userChoiceOpt == "1":
            first_name_input = input("Enter the first name: ")
            last_name_input = input("Enter the last name: ")
            job_commands.create_job_posting(first_name_input, last_name_input)
        elif userChoiceOpt == "2":
            searchJob(username)
        elif userChoiceOpt == "3":
            print("Looking for someone you know?")
            first_name_input = input("Enter the first name: ")
            last_name_input = input("Enter the last name: ")
            user_exists = does_user_exist(first_name_input, last_name_input)
            if user_exists:
                print("They are part of the InCollege system.")
            else:
                print("They are not part of the InCollege system.")
        elif userChoiceOpt == "4":
            newSkill(username)
        elif userChoiceOpt == "5":
            useful_link()
        elif userChoiceOpt == "6":
            important_link()
        elif userChoiceOpt == "7":
            break
        else:
            print("Not a valid input")
    return 0

