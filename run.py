"""
Main python file for defining and running the functions of the program
"""
# Modules
import re
from datetime import date
import random
import time
from os import system
from art import tprint
import gspread
from google.oauth2.service_account import Credentials


# API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("practice_log")

# Variables for spreadsheet worksheets
log = SHEET.worksheet("log")
technique_sheet = SHEET.worksheet("my-technical-exercises")
musicianship_sheet = SHEET.worksheet("my-musicianship-exercises")
creativity_sheet = SHEET.worksheet("my-creative-exercises")
repertoire_sheet = SHEET.worksheet("my-repertoire-exercises")

# Global Variables
today = None
session_date = None
session_duration = None
prod_score = None
user_exercises = None
user_diffs = None
user_wins = None
data = None
tech_data = None
musicianship_data = None
creative_data = None
repertoire_data = None


# General Functions
def sleep():
    """
    Set a general timer to delay text printing
    """
    time.sleep(1.5)


def long_sleep():
    """
    Set a longer timer to delay text printing
    """
    time.sleep(2.5)


def short_sleep():
    """
    Set a longer timer to delay text printing
    """
    time.sleep(0.7)


def clear_screen():
    """
    Clear the user terminal
    """
    system('clear')


def return_to_main():
    """
    Clear the screen of content and return to the beginning of the program
    """
    clear_screen()
    tprint("Returning...")
    print("\n\nTakin' it to the bridge...... (Main Menu)")
    long_sleep()
    start()


def main_title():
    """
    Prints the program's main title using print art
    """
    tprint("        Nick's")
    tprint("Practice")
    tprint("           Log")


# 1. Log Practice Functions
def get_date():
    """
    Get the current date to reference the users inputs in the spreadsheet
    """
    global today
    date_today = date.today()
    today = date_today.strftime('%d/%m/%y')
    return today


def log_practice():
    """
    Log a new practice session.
    Log duration and date of session and productivity score
    """
    clear_screen()
    tprint("Log  Practice\n\n")
    short_sleep()
    print("""
          Alright now! In this menu option I will take you through a number
          of questions for you to answer about your practice session.
          This will include date, duration, a self-productivity score,
          a list of exercises worked on, any particular difficulties
          experienced, and anything to claim as a win!
    """)
    long_sleep()
    print("\nLet's get this party started!")
    input('\nPress "Enter" to continue...\n')


def log_date():
    """
    Ask user if their practice date was today,
    If yes - store today's date,
    If no - ask for date input and validate for correct format,
    Validate for y/n correct input
    """
    global session_date
    # session_date = ""
    user_input = False
    while user_input is False:
        clear_screen()
        tprint("Date")
        session_today = input("\nWas your practice session today? (y/n)\n")
        if session_today.lower() == "y":
            user_input = True
            print(f"\nCoolio, Today's date is {today}. I'll log that...\n")
        elif session_today.lower() == "n":
            user_input = True
            while True:
                try:
                    clear_screen()
                    tprint("Date")
                    # Validate for correct date input format (Code Ref.1)
                    session_date = input("\nPlease input the date of your"
                                         " practice session (DD/MM/YY):\n")
                    valid = re.match(
                        r"^[0-3][0-9]['/'][0-1][0-9]['/'][2][2-3]$",
                        session_date)
                    valid_date = bool(valid)
                    if valid_date is False:
                        raise ValueError("Please enter a valid date in the"
                                         " correct format (DD/MM/YY):")
                    else:
                        break
                except ValueError as e:
                    print(f"\nInvalid Date Format: {e}")
            if valid_date is True:
                print("\nNice, I'll log that you practiced on "
                      f"{session_date}\n")
        elif session_today.lower() != "y" or "n":
            input('\n"Please, please, please"..... either "y" or "n"...'
                  '\nPress "Enter" to try again...')
    sleep()


def log_duration():
    """
    Ask user for duration of practice session and validate for an integer
    """
    global session_duration
    session_duration = 0
    clear_screen()
    tprint("Duration")
    while True:
        try:
            session_duration = int(input("How long was your practice session"
                                         " in minutes?\n"))
        except ValueError:
            print("\n6, 3, 4, 5, 7, 8, 9... That's my number....."
                  "Please enter yours\n")
        else:
            print(f"\nWell done! You practiced for {session_duration} mins!")
            break
    sleep()


def log_score():
    """
    Ask user for self-assesed productivity score input,
    and validate for an integer
    """
    clear_screen()
    tprint("Score")
    global prod_score
    prod_score = int(input("\nOn a scale of 0 - 10, how productive do you"
                           " feel the session was?\n"))
    if prod_score <= 3:
        print(f"\n{prod_score} is ok, you still practiced!\n"
              "It's the consistency that counts\n")
        sleep()
    elif prod_score <= 5:
        print(f"\n{prod_score} is a good score!"
              " All progress is good progress!\n")
        sleep()
    elif prod_score <= 8:
        print(f"\n{prod_score} is fantastic! Well done!\n")
        sleep()
    elif prod_score <= 10:
        print(f"\n{prod_score} is awesome! You are smashing it!\n")
        sleep()
    elif prod_score > 10:
        print("Whoa there! More than 10? Let's stay within the bounds ;)")
        sleep()
    if prod_score != int():
        print("Whoops, 0-10 needs a number...")



def log_exercises():
    """
    Asks the user to provide details of the specific exercises they worked on
    in the practice session, saved in a variable
    """
    clear_screen()
    tprint("Exercises")
    global user_exercises
    user_exercises = input('\nWhat exercises did you work on in this practice'
                           ' session?\n(Seperate exercises with ",")\n')
    sleep()
    print("\nYou're simply the BEST!\n")
    sleep()
    print(f"\nI have made a note of the following:\n {user_exercises}")
    long_sleep()


def log_wins():
    """
    Asks the user to detail particular problems experienced in the
    practice session, then asks for details on what positive
    outcomes they achieved. 
    """
    clear_screen()
    tprint("Difficulties")
    global user_diffs
    global user_wins
    # Ask for info on difficulties in the practice session
    user_diffs_yn = input("\nDid you experience any particular difficulties"
                          " during this practice session? (y/n)\n")
    if user_diffs_yn.lower() == "y":
        user_diffs = input("\nPlease detail them here"
                           " (seperate them with ','):\n")
        sleep()
        print("\nThank you. Remember that experiencing difficulties in your"
              " practice session is a natural part of the learning process!\n")
    elif user_diffs_yn.lower() == "n":
        user_diffs = "None"
        print("\nGreat! Moving on up...")
    sleep()

    # Ask for info on wins in the practice session
    clear_screen()
    tprint("Wins")
    user_wins_yn = input("\nAny successes to brag about? (y/n)\n")
    if user_wins_yn.lower() == "y":
        user_wins = input('Amazing! What were they? '
                          '(seperate your wins with ",")\n')
        sleep()
        print("\nYou are the champion my friend! "
              "You are making great progress!")
    elif user_wins_yn.lower() == "n":
        print("\nThat's ok, you practiced! Don't give up")
        user_wins = "None"

    sleep()
    clear_screen()
    print("\nOk, so let me reflect those back to you:\n")
    sleep()
    print("\nDifficulties:")
    print(f"\n{user_diffs}\n")
    sleep()
    print("\nWins:")
    print(f"\n{user_wins}\n")
    sleep()
    input('Press "Enter" to complete your log')
    clear_screen()
    tprint("Log Complete!")
    print("\nYou completed another log, you are SMASHING IT!\n")
    long_sleep()

    # Commit log to spreadsheet
    push = ""
    # Check for a valid input
    while push != 'y' or push != 'n':
        push = input("\nWould you like to save this log? (y/n)\n")
        if push.lower() == "y":
            collate_data()
            sleep()
            print("\nSave me, save me, SAAAAVE ME...")
            push_log_data(data)
            sleep()
            print("\nReady Freddie, Let's go back...")
            sleep()
            start()
        elif push.lower() == "n":
            print("\nAre you sure?? You've come all this way!")
            confirm = input('\n"y" = Quit and lose all changes.'
                            ' "n" = Save and return to Main Menu.\n')
            if confirm.lower() == "y":
                quit_program()
            elif confirm.lower() == "n":
                collate_data()
                print("\nCaught in a trap... but you got out! Saving log...")
                sleep()
                push_log_data(data)
                print("\nDone. Let's go back to...")
                long_sleep()
                start()

    # Check if user wishes to quit or return to the main menu
    menu_choice = input('\nType "menu" or "quit" to return to the main menu'
                        ' or exit the program.\n')
    if menu_choice.lower() == "menu" or "m":
        print("\nKeep the motor running... Head out on the highway...")
        sleep()
        print("Looking for adventure, and the Menu that's coming your way!...")
        sleep()
        start()
    elif menu_choice.lower == "quit" or "exit" or "q" or "e":
        choice = input("\nHold on... Are you sure? (y/n)\n")
        if choice.lower() == "y":
            print("\nQuitting, thank you for logging your practice!"
                  "See you later alligator! ;)")
        elif choice.lower() == "n":
            return_to_main()
        else:
            print("\nSorry I didn't understand that..."
                  "Let's just go back...\n")
            sleep()
            start()


def collate_data():
    """
    Collates all of the user input variables into a single variable
    and converts ints to strings.
    """
    global data
    print("Pickin' up the pieces...")
    data = [
        str(today),
        str(session_duration),
        str(prod_score),
        user_exercises,
        user_diffs,
        user_wins]
    print(data)
    sleep()
    print("Pieces succesfully picked up :)")


def push_log_data(data):
    """
    Update log worksheet, add new row with the data provided
    by the user in the log program
    """
    print("Giving your log to Mr Postman...\n")
    log_worksheet = SHEET.worksheet("log")
    log_worksheet.append_row(data)
    sleep()
    print("Signed, sealed, delivered. Log saved! ")


# 2. Get Insights Menu
def get_insights():
    """
    Main function for option 2 to allow choice to next menu
    """
    clear_screen()
    tprint("Get Insights")
    sleep()
    print("You have chosen to get insights on your saved practice logs\n")
    sleep()
    print(
        """
        Insights Menu:
        _ _ _ _ _ _ _

        1. View Last Recorded Log
        2. View Last 3 Logs
        3. Calculate Average Practice Time
        4. View List of Exercises Practiced
        5. View List of Difficulties Encountered
        6. Return to the Main Menu
        """)
    user_choice = input("Pick a number, any number...\n")
    if user_choice == "1":
        view_last_Log()
    if user_choice == "2":
        view_3_logs()
    if user_choice == "3":
        average_time()
    if user_choice == "4":
        view_exercises()
    if user_choice == "5":
        view_difficulties()
    if user_choice == "6":
        return_to_main()
    elif user_choice != "1" or "2" or "3" or "4" or "5" or "6" or "":
        print("\nGimme, Gimme, Gimme a number between 1 and 6: Try again...")
        long_sleep()
        get_insights()


# 2. Get Insights - 1. View Last Log
def view_last_Log():
    """
    Get all log sheet data, get the last entry,
    split the list entry and seperately print to the user
    """
    clear_screen()
    print("\nYou have chosen to view the last log entry. \nLoading...\n")
    all_data = log.get_all_values()
    last_log = list.pop(all_data)
    sleep()
    clear_screen()
    tprint("Last Log")
    print("\nHere is your last recorded log:\n")
    sleep()
    print(f"\nDate: {last_log[0]}")
    print(f"\nPractice Time: {last_log[1]}")
    print(f"\nProductivity Score: {last_log[2]}")
    print(f"\nExercises Worked On: {last_log[3]}")
    print(f"\nDifficulties Encountered: {last_log[4]}")
    print(f"\nPersonal Wins: {last_log[5]}")
    input('\nHit "Enter" to continue..:')
    get_insights()


# 2. Get Insights - 2. View Last Three Logs
def view_3_logs():
    """
    Get all values from spreadsheet, find last 3 rows (logs),
    send each of the 3 rows into seperate variables,
    print the information from those variables to the user
    """
    clear_screen()
    all_data = log.get_all_values()
    most_recent = all_data[-1]
    second_recent = all_data[-2]
    third_recent = all_data[-3]

    # Printing most recent entry
    print("\nRunning to get your last 3 entries...")
    sleep()
    clear_screen()
    tprint("Logs")
    sleep()
    tprint("1")
    print("* Most Recent Log *")
    print(f"\nDate: {most_recent[0]}")
    print(f"\nYou practiced for {most_recent[1]} mins")
    print(f"\nYou scored your productivity at {most_recent[2]}")
    print(f"\nThe exercises you worked on were:\n{most_recent[3]}")
    print("\nYou expressed the difficulties you encountered as:"
          f"\n{most_recent[4]}")
    print(f"\nYou expressed your successes as:\n{most_recent[5]}")
    input('\nHit "Enter" to continue\n')

    # Printing second most recent entry
    tprint("2")
    print("* Second Most Recent Log *")
    print(f"\nDate: {second_recent[0]}")
    print(f"\nYou practiced for {second_recent[1]} mins")
    print(f"\nYou scored your productivity at {second_recent[2]}")
    print(f"\nThe exercises you worked on were:\n{second_recent[3]}")
    print("\nYou expressed the difficulties you encountered as:"
          f"\n{second_recent[4]}")
    print(f"\nYou expressed your successes as:\n{second_recent[5]}")
    input('\nHit "Enter" to continue\n')

    # Printing third most recent entry
    tprint("3")
    print("* Third Most Recent Log *")
    print(f"\nDate: {third_recent[0]}")
    print(f"\nYou practiced for {third_recent[1]} mins")
    print(f"\nYou scored your productivity at {third_recent[2]}")
    print(f"\nThe exercises you worked on were:\n{third_recent[3]}")
    print("\nYou expressed the difficulties you encountered as:"
          f"\n{third_recent[4]}")
    print(f"\nYou expressed your successes as:\n{third_recent[5]}")
    input('\nHit "Enter" to return\n')
    get_insights()


# 2. Get Insights - 3. Calculate Average Practice Time
def average_time():
    """
    Get all duration values from the column in the spreadsheet,
    Remove the column title from the list,
    Convert as numbers as strings to integers,
    Calculate average and print to the user
    """
    clear_screen()
    print("\nHold on, won't be long...")
    all_values = log.col_values(2)
    all_nums = all_values[1:]
    all_ints = [int(i) for i in all_nums]
    total_minutes = sum(all_ints)
    long_sleep()
    clear_screen()
    tprint("Average Time")
    sleep()
    print(f"\nYou have clocked a total of {total_minutes}"
          " minutes practicing...")
    num_sessions = len(all_ints)
    sleep()
    print(f"\nOver the course of {num_sessions} practice sessions...")
    result = total_minutes / num_sessions
    result_round = round(result)
    sleep()
    print("\nYour average time spent in each practice session is "
          f"{result_round} minutes!")
    sleep()
    print("\nThat's not too shabby ;)")
    sleep()
    input('\nHit "Enter" to continue:')
    get_insights()


# 2. Get Insights - 4. Get List of Exercises
def view_exercises():
    """
    Get all values from Exercises column in spreadsheet,
    Print to the user
    """
    clear_screen()
    print("\nYou have chosen to view your logged exercises.")
    sleep()
    print("\nHold on, won't be long...")
    sleep()
    all_values = log.col_values(4)
    all_exercises = all_values[1:]
    clear_screen()
    print("\nHere is a list of exercises you have logged:\n")
    for i in all_exercises:
        print(i)
    input('\nPress "Enter" to continue..:')
    get_insights()


# 2. Get Insights - 4. Get List of Difficulties
def view_difficulties():
    """
    Get all values from Difficulties column in spreadsheet,
    Print to the user
    """
    clear_screen()
    print("\nYou have chosen to view your logged difficulties")
    sleep()
    print("\n\nHold on, won't be long...\n")
    sleep()
    clear_screen()
    all_values = log.col_values(5)
    all_diffs = all_values[1:]
    print("Remember! These are useful to help you understand things you "
          "should be working on or ways to develop your practice in future"
          " sessions")
    sleep()
    print("\nHere is a list of difficulties you have logged:\n")
    for i in all_diffs:
        print(i)
    input('\nPress "Enter" to continue..:')
    get_insights()


# 3. Submit Practice Ideas
def submit_ideas():
    """
    Main function for option 3 for the user to sumbit their own
    practice ideas
    """
    clear_screen()
    tprint("Submit   Practice")
    tprint("Ideas")
    long_sleep()
    print("\nAlrighty then! You have chosen to submit some practice ideas")
    sleep()
    print("""
        \nHere I will ask you a series of questions to help me organise your
        ideas into one of 4 categories...
        """)
    long_sleep()
    clear_screen()
    print("""
        General practice topics are classed as either:

        1. Technical    - Developing technical skill through repeated
                          incremental exercises targeting specific
                          motor movements
    """)
    long_sleep()
    print("""
        2. Musicianship - Developing musically intuitive skills
                          (Aural, theory, harmony, rhythm, sight-reading
                          ensemble skills, voacbulary, etc
    """)
    long_sleep()
    print("""
        3. Creative     - Developing creative skills and intuition
                          (Improvisation, composition, interpretation,
                          phrasing, etc)
    """)
    long_sleep()
    print("""
        4. Repertoire   - Learning new or refining already-known repertoire
                          (Transciption, memorisation, repertoire reserach)
    """)
    short_sleep()
    print("""
        (Please only save one practice idea at a time)

        Press "5" to return to the Main Menu
    """)
    long_sleep()
    submit_ideas_menu()


def submit_ideas_menu():
    """
    The menu for the submit ideas menu.
    Validating user input for menu choice and directing
    the program to run the relevant function
    """
    user_choice = input("\nWhich category do you want to log your"
                        " practice idea under?:\n")
    if user_choice == "1":
        clear_screen()
        print("Technical, ok great!\n\nGood technique facilitates"
              " everything we do!")
        submit_tech()
    elif user_choice == "2":
        clear_screen()
        print("Musicianship, FAB!\n\n Good musicianship skills are essential!")
        submit_musicianship()
    elif user_choice == "3":
        clear_screen()
        print("Creative! Right on!\n\n Developing these skills help to do what"
              "we are here to do...\nMAKE MUSIC :) ")
        submit_creative()
    elif user_choice == "4":
        clear_screen()
        print("Repertoire, ROCK ON!\n\nGet ready for the gigs!")
        submit_repertoire()
    elif user_choice == "5":
        return_to_main()
    elif user_choice != "1" or "2" or "3" or "4" or "5" or "":
        print("\nGimme, Gimme, Gimme a number between 1 and 5: Try again...")
        long_sleep()
        submit_ideas_menu()


def submit_tech():
    """
    To submit a technical exercise to the spreadsheet,
    print back to the user and ask if they wish to save it to the
    spreadsheet or try again. Validate against incorrect inputs
    """
    sleep()
    clear_screen()
    global tech_data
    loop = False
    while loop is False:
        tech_idea = input("\nWhat details would you like to save?\n")
        tech_data = []
        tech_data.append(today)
        tech_data.append(tech_idea)
        print("\nOk, I've got that.\n")
        sleep()
        clear_screen()
        print("Just to confirm: Here's what you wrote:\n")
        sleep()
        print(f'\n"{tech_idea}"\n')
        user_confirm = input('\nShall I save that for you? (Hit "y" to save,'
                             ' "n" to delete and return to the menu)\n')
        if user_confirm.lower() == "y":
            loop = True
            clear_screen()
            send_tech_exs(tech_data)
        elif user_confirm.lower() == "n":
            loop = True
            print("Ok. Returning to menu...")
            submit_ideas()
        elif user_confirm.lower() != "y" or "n":
            loop = True
            confirm_loop = False
            while confirm_loop is False:
                print("\nSorry I didn't get that, please try again\n")
                confirm = input('"y" to save, "n" to delete and'
                                ' return to the menu\n')
                if confirm.lower() == "y":
                    confirm_loop = True
                    clear_screen()
                    send_tech_exs(tech_data)
                elif confirm.lower() == "n":
                    confirm_loop = True
                    print("\nTurn around...")
                    short_sleep()
                    print("Every now and then I get sent back to the menu...")
                    sleep()
                    submit_ideas()


def submit_musicianship():
    """
    To submit musicianship exercises to the spreadsheet,
    print back to the user and ask if they wish to save it to the
    spreadsheet or try again. Validate agains incorrect inputs
    """
    sleep()
    clear_screen()
    global musicianship_data
    loop = False
    while loop is False:
        musicianship_idea = input("\nWhat details would you like to save?\n")
        musicianship_data = []
        musicianship_data.append(today)
        musicianship_data.append(musicianship_idea)
        print("\nOk, I've got that.\n")
        sleep()
        clear_screen()
        print("Just to confirm: Here's what you wrote:\n")
        sleep()
        print(f'\n"{musicianship_idea}"\n')
        user_confirm = input('\nShall I save that for you? (Hit "y" to save,'
                             ' "n" to delete and return to the menu)\n')
        if user_confirm.lower() == "y":
            loop = True
            clear_screen()
            send_music_exs(musicianship_data)
        elif user_confirm.lower() == "n":
            loop = True
            print("Ok. Returning to menu...")
            submit_ideas()
        elif user_confirm.lower() != "y" or "n":
            loop = True
            confirm_loop = False
            while confirm_loop is False:
                print("\nSorry I didn't get that, please try again")
                confirm = input('"y" to save, "n" to delete and'
                                ' return to the menu')
                if confirm.lower() == "y":
                    confirm_loop = True
                    clear_screen()
                    send_music_exs(musicianship_data)
                elif confirm.lower() == "n":
                    confirm_loop = True
                    print("\nTurn around...")
                    short_sleep()
                    print("Every now and then I get sent back to the menu...")
                    sleep()
                    submit_ideas()


def submit_creative():
    """
    To submit creativity exercises to the spreadsheet,
    print back to the user and ask if they wish to save it to the
    spreadsheet or try again. Validate agains incorrect inputs
    """
    sleep()
    clear_screen()
    global creative_data
    loop = False
    while loop is False:
        creative_idea = input("\nWhat details would you like to save?\n")
        creative_data = []
        creative_data.append(today)
        creative_data.append(creative_idea)
        print("\nOk, I've got that.\n")
        sleep()
        clear_screen()
        print("Just to confirm: Here's what you wrote:\n")
        sleep()
        print(f'\n"{creative_idea}"\n')
        user_confirm = input('\nShall I save that for you? (Hit "y" to save,'
                             ' "n" to delete and return to the menu)\n')
        if user_confirm.lower() == "y":
            loop = True
            clear_screen()
            send_creative_exe(creative_data)
        elif user_confirm.lower() == "n":
            loop = True
            print("Ok. Returning to menu...")
            submit_ideas()
        elif user_confirm.lower() != "y" or "n":
            loop = True
            confirm_loop = False
            while confirm_loop is False:
                print("\nSorry I didn't get that, please try again")
                confirm = input('"y" to save, "n" to delete and'
                                ' return to the menu')
                if confirm.lower() == "y":
                    confirm_loop = True
                    clear_screen()
                    send_creative_exe(creative_data)
                elif confirm.lower() == "n":
                    confirm_loop = True
                    print("\nTurn around...")
                    short_sleep()
                    print("Every now and then I get sent back to the menu...")
                    sleep()
                    submit_ideas()


def submit_repertoire():
    """
    To submit repertoire exercises to the spreadsheet,
    print back to the user and ask if they wish to save it to the
    spreadsheet or try again. Validate agains incorrect inputs
    """
    sleep()
    clear_screen()
    global repertoire_data
    loop = False
    while loop is False:
        repertoire_idea = input("\nWhat details would you like to save?\n")
        repertoire_data = []
        repertoire_data.append(today)
        repertoire_data.append(repertoire_idea)
        print("\nOk, I've got that.\n")
        sleep()
        clear_screen()
        print("Just to confirm: Here's what you wrote:\n")
        sleep()
        print(f'\n"{repertoire_idea}"\n')
        user_confirm = input('\nShall I save that for you? (Hit "y" to save,'
                             ' "n" to delete and return to the menu)\n')
        if user_confirm.lower() == "y":
            loop = True
            clear_screen()
            send_repertoire_exe(repertoire_data)
        elif user_confirm.lower() == "n":
            loop = True
            print("Ok. Returning to menu...")
            submit_ideas()
        elif user_confirm.lower() != "y" or "n":
            loop = True
            confirm_loop = False
            while confirm_loop is False:
                print("\nSorry I didn't get that, please try again")
                confirm = input('"y" to save, "n" to delete and'
                                ' return to the menu')
                if confirm.lower() == "y":
                    confirm_loop = True
                    clear_screen()
                    send_repertoire_exe(repertoire_data)
                elif confirm.lower() == "n":
                    confirm_loop = True
                    print("\nTurn around...")
                    short_sleep()
                    print("Every now and then I get sent back to the menu...")
                    sleep()
                    submit_ideas()


# Functions to send user input data to the relevant spreadsheets
def send_tech_exs(tech_data):
    """
    Sends technique exercises to the worksheet
    """
    print("Signed, sealed...\n")
    technique_sheet.append_row(tech_data)
    sleep()
    print("Delivered! It's done. Returning to main menu...")
    sleep()
    start()


def send_music_exs(musicianship_data):
    """
    Sends musicianship exercises to the worksheet
    """
    print("Signed, sealed...\n")
    musicianship_sheet.append_row(musicianship_data)
    sleep()
    print("Delivered! It's done. Returning to main menu...")
    sleep()
    start()


def send_creative_exe(creative_data):
    """
    Sends creativity exercises to the worksheet
    """
    print("Signed, sealed...\n")
    creativity_sheet.append_row(creative_data)
    sleep()
    print("Delivered! It's done. Returning to main menu...")
    sleep()
    start()


def send_repertoire_exe(repertoire_data):
    """
    Sends repertoire exercises to the worksheet
    """
    print("Signed, sealed...\n")
    repertoire_sheet.append_row(repertoire_data)
    sleep()
    print("Delivered! It's done. Returning to main menu...")
    sleep()
    start()


# 4. Get Practice
def get_practice():
    """
    Ask user which practice topics they would like to view the logged
    exercises for, error-proof input, and display the requested data
    """
    clear_screen()
    tprint("View Exercices")
    sleep()
    print("\nYou have chosen to view your previously logged practice ideas")
    sleep()
    print("""\n
                * Menu *
                  ----\n
          1. View Technical Exercises
          2. View Musicianship Exercises
          3. View Creative Exercises
          4. View Repertoire Exercises
          5. View a Random Selection From All Categories
          6. Return to the Main Menu
    """)
    menu_loop = False
    while menu_loop is False:
        user_choice = input("\nPlease choose an option with a number (1-5):\n")
        if user_choice == "1":
            menu_loop = True
            print("\nI ammmmmm, the [option] 1 and only...")
            long_sleep()
            view_technical_exercises()
        elif user_choice == "2":
            menu_loop = True
            print("\nJust the [option] 2 of us...")
            long_sleep()
            view_musicianship_exercises()
        elif user_choice == "3":
            menu_loop = True
            print('\n3 is the magic number')
            long_sleep()
            view_creativity_exercises()
        elif user_choice == "4":
            menu_loop = True
            print("\nFaith no more, here's option 4...")
            long_sleep()
            view_repertoire_exercises()
        elif user_choice == "5":
            menu_loop = True
            print("\n[Option] 5 will make you get down now... \n")
            sleep()
            print("\nSorry......... That was the worst pun in this program")
            random_practice()
        elif user_choice == "6":
            menu_loop = True
            return_to_main()
        else:
            print("\nWhoops, you did it again... have another go\n")
            long_sleep()
            get_practice()


# 4. View Practice - 1. View Technical Exercises
def view_technical_exercises():
    """
    Retrieves all information from 'my-technical-exercises' worksheet
    and prints to user. Validates a request to return to the menu
    """
    clear_screen()
    print("Alrighty then, hold on whilst I collect your technical "
          "exercise ideas...\n")
    sleep()
    technical_exercises = technique_sheet.col_values(2)
    for exercise in technical_exercises:
        print(exercise)
        short_sleep()
    print("\nPhew! That's some GAINS material right there!")
    sleep()
    print("\nPsst! BTW, you can submit more ideas from the option 3 in the"
          " Main Menu ;)\n")
    sleep()
    user_choice = input('\nPress "v" to return to the "View Exercises" menu\n'
                        'or "m" to return to the Main Menu\n')
    if user_choice.lower() == "v":
        print("\nCoolio, returning...")
        sleep()
        get_practice()
    elif user_choice.lower() == "m":
        return_to_main()
    elif user_choice.lower() != "v" or "m":
        clear_screen()
        print("\nWhoops...")
        sleep()
        print("\nI'm sure you didn't mean...")
        sleep()
        print("\nTo not press...the buttons I said you could press...")
        sleep()
        print("\nLet's try again...")
        long_sleep()
        get_practice()


# 4. View Practice - 2. View Musicianship Exercises
def view_musicianship_exercises():
    """
    Retrieves all information from 'my-musicianship-exercises' worksheet
    and prints to user. Validates a request to return to the menu
    """
    clear_screen()
    print("Alrighty then, hold on whilst I collect your Musicianship "
          "practice ideas...\n")
    sleep()
    musicianship_exercises = musicianship_sheet.col_values(2)
    for exercise in musicianship_exercises:
        print(exercise)
        short_sleep()
    print("\nPhew! That's everything I have...\n")
    sleep()
    print("\nPsst! BTW, you can submit more ideas from the option 3 in the"
          " Main Menu ;)\n")
    sleep()
    user_choice = input('\nPress "v" to return to the "View Exercises" menu\n'
                        'or "m" to return to the Main Menu\n')
    if user_choice.lower() == "v":
        print("\nRad, returning...")
        sleep()
        get_practice()
    elif user_choice.lower() == "m":
        return_to_main()
    elif user_choice.lower() != "v" or "m":
        clear_screen()
        print("\nWhoops...\n")
        sleep()
        print("\nI'm sure you didn't mean...")
        sleep()
        print("\nTo not press...the buttons I said you could press...")
        sleep()
        print("\nMaybe I'll take you back to the santuary of the menu...")
        long_sleep()
        get_practice()


# 4. View Practice - 3. View Creativity Exercises
def view_creativity_exercises():
    """
    Retrieves all information from 'my-creativity-exercises' worksheet
    and prints to user. Validates a request to return to the menu
    """
    clear_screen()
    print("Alrighty then, hold on whilst I collect your creative "
          "practice ideas...\n")
    sleep()
    creativity_exercises = creativity_sheet.col_values(2)
    for exercise in creativity_exercises:
        print(exercise)
        short_sleep()
    print("\nPhew! Some good stuff in there!\n")
    sleep()
    print("\nPsst! BTW, you can submit more ideas from the option 3 in the"
          " Main Menu ;)\n")
    sleep()
    user_choice = input('\nPress "v" to return to the "View Exercises" menu\n'
                        'or "m" to return to the Main Menu\n')
    if user_choice.lower() == "v":
        print("\nRad, returning...")
        sleep()
        get_practice()
    elif user_choice.lower() == "m":
        return_to_main()
    elif user_choice.lower() != "v" or "m":
        clear_screen()
        print("\nWhoops...\n")
        sleep()
        print("\nI'm sure you didn't mean...")
        sleep()
        print("\nTo not press...the buttons I said you could press...")
        sleep()
        print("\nMaybe I'll take you back to the santuary of the menu...")
        long_sleep()
        get_practice()


# 4. View Practice - 4. View Repertoire Exercises
def view_repertoire_exercises():
    """
    Retrieves all information from 'my-repertoire-exercises' worksheet
    and prints to user. Validates a request to return to the menu.
    """
    clear_screen()
    print("Roger Roger, hold on whilst I collect your repertoire "
          "practice ideas...\n")
    sleep()
    repertoire_exercises = repertoire_sheet.col_values(2)
    for exercise in repertoire_exercises:
        print(exercise)
        short_sleep()
    print("\nWhat a collection of BANGERS! You have good taste!\n")
    sleep()
    print("\nPsst! BTW, you can submit more ideas from the option 3 in the"
          " Main Menu ;)\n")
    sleep()
    user_choice = input('\nPress "v" to return to the "View Exercises" menu\n'
                        'or "m" to return to the Main Menu\n')
    if user_choice.lower() == "v":
        print("\nRad, returning...")
        sleep()
        get_practice()
    elif user_choice.lower() == "m":
        return_to_main()
    elif user_choice.lower() != "v" or "m":
        print("\nWhoops...\n")
        sleep()
        print("\nYou are great at choosing tunes to play...")
        sleep()
        print("\nBut not at pressing the buttons I said you could press...")
        sleep()
        print("\nMaybe I'll take you back to the santuary of the menu...")
        long_sleep()
        get_practice()


# 4. Get Practice Ideas - 5. View Random Selection
def random_practice():
    """
    Prints information about the random practice generation and
    holds triggers the generator function
    """
    clear_screen()
    print(" * View Random Practice Ideas * ")
    sleep()
    print("\nSo, you're looking for some spontaneous practice ideas\n"
          "for your next session? I can help!\n")
    sleep()
    print("I can retrive a selection of random exercises from the\n"
          "database that holds your previous exercise idea submissions...")
    sleep()
    random_generator_loop()


def random_generator_loop():
    """
    Retrieves all practice column values from 'my-technical-exercises',
    'my-musicianship-exercises', 'my-creative-exercises,
    'my-repertoire-exercises' worksheets from main spreadsheet;
    Removes the column titles, add all values to a single list variable;
    Give user the choice to generate a random selection of 3 exercises from
    the list and validate to repeat or return to the menu
    """
    technique = technique_sheet.col_values(2)
    technique.pop(0)
    musicianship = musicianship_sheet.col_values(2)
    musicianship.pop(0)
    creativity = creativity_sheet.col_values(2)
    creativity.pop(0)
    repertoire = repertoire_sheet.col_values(2)
    repertoire.pop(0)
    all_values = []
    all_values.extend(technique)
    all_values.extend(musicianship)
    all_values.extend(creativity)
    all_values.extend(repertoire)
    clear_screen()
    user_choice = input('\nPress "g" and I will generate a list of 5 '
                        'exercises,\nType "e" to exit to the menu:\n')
    sleep()
    generate_loop = False
    while generate_loop is False:
        if user_choice.lower() == "e":
            generate_loop = True
            print("Ok! Now running up that hill, to the Menu...")
            sleep()
            get_practice()
        elif user_choice.lower() == "g":
            generate_loop = True
            clear_screen()
            print("\nSuperstar DJ, here we go!...\n")
            sleep()
            random_list_loop = False
            new_list = 0
            while random_list_loop is False:
                clear_screen()
                print("Here is your list of 3 randomly selected exercises:\n")
                while new_list < 3:
                    sleep()
                    print(random.choice(all_values))
                    new_list += 1
                sleep()
                print("\nDoes that inspire your practice??\n")
                sleep()
                user_confirm = input('\n"y" All good, lets go! or "g" Generate'
                                     ' another random list:\n')
                if user_confirm.lower() == "y":
                    random_list_loop = True
                    print("\nYou're Simply the BEST! "
                          "Have a great practice session!\n")
                    print("\nReturning to the Menu...")
                    sleep()
                    get_practice()
                elif user_confirm.lower() == "g":
                    print("\nOk, Hold on...")
                    generate_loop = False
                    new_list = 0
                    sleep()
                elif user_confirm.lower() != "y" or "g":
                    print("\nWhoops, you did it [wrong] again... Try again")
                    long_sleep()
                    random_generator_loop()
        elif user_choice.lower() != "e" or "g":
            print("\nOops, you did it [wrong] again... Try again")
            sleep()
            random_generator_loop()


# 5. Quit Program
def quit_program():
    """
    Function to allow the user to safely quit the program
    Validate for accidental quit
    """
    clear_screen()
    tprint("Quit...")
    print("\nShould you stay or should you go...?\n")
    quit_choice = input('\nStay "y", Go "n":\n')
    if quit_choice.lower() == "n":
        clear_screen()
        print("\nQuitting...\n")
        sleep()
        tprint("Bye,")
        short_sleep()
        tprint("     Bye,")
        short_sleep()
        tprint("          Bye!")
        exit()
    elif quit_choice.lower() == "y":
        return_to_main()
    else:
        print('\nYou, you, you, oughta know...\n')
        sleep()
        print("\nYou should have pressed yes or no...")
        long_sleep()
        start()


def start():
    """
    Save today's date as global variable,
    Welcome message and user choice input to proceed
    """
    clear_screen()
    get_date()
    main_title()
    long_sleep()
    print("\n ** Wecome to Nick's Practice Log! **\n")
    sleep()
    print("\nHi, my name is Nick and I'm a musician. For us musicians, "
          "our practice is essential.\n"
          "So I've built this little program to help log and manage practice"
          " session information,\n"
          "and keep track of progress.")
    sleep()
    print("\nAll data is kept on a spreadsheet and is pre-populated with"
          " a few ideas.\n")
    sleep()
    print("Without further agadoo..... Let's get busy!\n")
    input('\nPress "Enter" to continue\n')
    clear_screen()
    tprint("Main  Menu")
    print("""
        What would you like to do?

        1. Log a practice session
        2. Get insights on your practice
        3. Submit your practice ideas
        4. View your practice ideas
        5. Quit
    """)
    start_choice = input("\nMake your selection with a number:\n")
    if start_choice == "1":
        log_practice()
        log_date()
        log_duration()
        log_score()
        log_exercises()
        log_wins()
    elif start_choice == "2":
        get_insights()
    elif start_choice == "3":
        submit_ideas()
    elif start_choice == "4":
        get_practice()
    elif start_choice == "5":
        quit_program()
    else:
        print("""\n
        Oops you did it [wrong] again...

        Let's go back to the very beginning....
        """)
        long_sleep()
        start()


start()
