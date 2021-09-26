import account_define
import db_commands
import random
import job_commands


def additional_options(username, first_name, last_name):
    while True:
        print("Please choose from the following menu:")
        print("1 - Post a job")
        print("2 - Search for a job")
        print("3 - Find someone you know")
        print("4 - Learn a new skill")
        print("Q to quit the program")
        userChoiceOpt = input("Enter your selection here: ")

        # Potentially use switch
        if userChoiceOpt == "1":
            job_commands.create_job_posting(first_name, last_name)
        elif userChoiceOpt == "2":
            searchJob(username)
        elif userChoiceOpt == "3":
            findAssociate(username)
        elif userChoiceOpt == "4":
            newSkill(username)
        elif userChoiceOpt == "Q":
            break
        else:
            print("Not a valid input")
    return 0


def searchJob(username):
    print("Under construction")
    return 0


def findAssociate(username):
    print("Looking for someone you know?")
    fname = input("Enter the first name: ")
    lname = input("Enter the last name: ")
    user_exists = account_define.does_user_exist(fname, lname)
    if user_exists:
        print("They are part of the InCollege system.")
    else: 
        print("They are not part of the InCollege system.")
    return 0


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
        print("Q to quit the program")
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
        elif userChoiceSkill == "Q":
            break
        elif int(userChoiceSkill) > 5 and int(userChoiceSkill) < 1:
            print("Not a valid input")
    return 0

