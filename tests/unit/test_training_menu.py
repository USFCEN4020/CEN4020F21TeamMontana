import main
from start_options import login_account
from db_commands import create_connection
from tests.unit.testBases import get_display_ouput, set_keyboard_input

def test_training_menu():
    # database_name = "userDB"
    menu = """
            Please select a training option or enter 5 to return:
            1 - Training and Education
            2 - IT Help Desk
            3 - Business Analysis and Strategy
            4 - Security
            5 - Return to main menu

            """

    business_analysis_strategy = """
            Please select a training option or enter 5 to return:
            1 - How to use In College learning
            2 - Train the trainer
            3 - Gamification of learning

            Not seeing what you're looking for? Sign in to see all 7,609 results.
            """
    set_keyboard_input(["0", "1", "2", "3", "0", "4", "4", "5"])
    main.training_menu()
    output = get_display_ouput()
    assert output == [menu, "Please enter your option (1-5): ", "Invalid input. Try again", 
    "Please enter your option (1-5): ", "Under Construction", menu, 
    "Please enter your option (1-5): ", "Coming Soon", menu, 
        "Please enter your option (1-5): ", business_analysis_strategy, 
        "Please enter your option (1-4): ", "Invalid input. Try again",
        "Please enter your option (1-4): ", "Returning to main menu...", menu,
    "Please enter your option (1-5): ", "Coming Soon", menu, 
    "Please enter your option (1-5): ", "Returning to main menu..."]