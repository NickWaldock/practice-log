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


# Code Reference 1
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
    print("\n\nTakin' it to the bridge...")
    long_sleep()
    start_menu()


def main_title():
    """
    Prints the program's main title using print art
    """
    tprint("                      Nick's")
    tprint("              Practice")
    tprint("                         Log")


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
    session_today = ""
    loop = True
    while loop is True:
        clear_screen()
        tprint("Date")
        session_today = input("\nWas your practice session today? (y/n)\n")
        if session_today.lower() == "y" or session_today.lower() == "yes":
            print(f"\nCoolio, Today's date is {today}. I'll log that...\n")
            session_date = today
            loop = False
            sleep()
        elif session_today.lower() == "n" or session_today.lower() == "no":
            loop = False
            request_date()
        else:
            print('\n"Please, please, please"..... either "y" or "n"...')
            sleep()


def request_date():
    """
    If user's date input is not today then this function will request a valid
    date input from the user to be stored in the session_date variable.
    Validation for correct input format
    """
    while True:
        try:
            global session_date
            clear_screen()
            tprint("Date")
            # Code Reference 2. Validate for correct date input format
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
            sleep()
    if valid_date is True:
        print("\nNice, I'll log that you practiced on "
              f"{session_date}\n")
        long_sleep()


def log_duration():
    """
    Ask user for duration of practice session and validate for an integer
    """
    global session_duration
    session_duration = 0
    while True:
        try:
            clear_screen()
            tprint("Duration")
            print("\nAssuming your practice session wasn't more than"
                  " 4 hours (240mins)...\n")
            session_duration = int(input("\nHow long was your practice session"
                                         " in minutes?\n"))
            if session_duration > 240:
                print("\nDid you really did practice more than 4 hours...?\n"
                      "\nIf so, please log them as seperate sessions")
                long_sleep()
                input('Hit "Enter" to continue... '
                      'and log part of this session.\n')
                log_duration()

        except ValueError:
            print("\n6, 3, 4, 5, 7, 8, 9... That's my number.....\n"
                  "Please enter yours...\n")
            sleep()
        else:
            print(f"\nWell done! You practiced for {session_duration} mins!")
            break
    sleep()


def check_num():
    """
    Validate for a number for the log_score function
    """
    global prod_score
    while True:
        clear_screen()
        tprint("Score")
        prod_score = input("\nOn a scale of 1 - 10, how productive do you"
                           " feel the session was?\n")
        if prod_score.isnumeric():
            prod_score = int(prod_score)
            if prod_score > 10:
                print("\nWhoa there! This one doesn't go up to 11."
                      "\nLet's stay within the bounds eh? ;)")
                sleep()
            elif prod_score == 0:
                print("\nSurly it wasn't so bad it deserves a 0...")
                sleep()
            else:
                return prod_score
        else:
            print("\nWhoops, 1-10 needs a whole number...")
            sleep()


def log_score():
    """
    Ask user for self-assesed productivity score input,
    and validate for an integer
    """
    check_num()
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
    long_sleep()


def log_difficulties():
    """
    Asks the user if they have any difficulties to log here,
    Validate for y/n input,
    If no, move on. If yes, request detail of particular problems experienced
    in the practice session.
    """
    clear_screen()
    tprint("Difficulties")
    global user_diffs
    # Ask for info on difficulties in the practice session
    user_diffs_yn = input("\nDid you experience any particular difficulties"
                          " during this practice session?\n(y/n)\n")
    short_sleep()
    if user_diffs_yn.lower() == "y" or user_diffs_yn.lower() == "yes":
        clear_screen()
        tprint("Difficulties")
        user_diffs = input("\nPlease detail them here"
                           " (seperate them with ','):\n")
        short_sleep()
        print("\nThank you. Remember that experiencing difficulties in your"
              "\npractice session is a natural part of the learning"
              " process!\n")
        long_sleep()
    elif user_diffs_yn.lower() == "n" or user_diffs_yn.lower() == "no":
        user_diffs = "None"
        print("\nGreat! Moving on up...")
        sleep()
    else:
        print('\nPlease input "y" or "n" :)')
        sleep()
        log_difficulties()


def log_wins():
    """
    Asks the user if they have any wins to log here. Validate for y/n input,
    If no, move on. If yes, request detail of particular problems experienced
    in the practice session.
    """
    # Ask for info on wins in the practice session
    clear_screen()
    tprint("Wins")
    global user_wins
    user_wins_yn = input("\nAny successes to brag about? (y/n)\n")
    if user_wins_yn.lower() == "y" or user_wins_yn.lower() == "yes":
        clear_screen()
        tprint("Wins")
        user_wins = input('Amazing! What were they? '
                          '(seperate your wins with ",")\n')
        sleep()
        print("\nYou are the champion my friend! "
              "You are making great progress!")
        long_sleep()
    elif user_wins_yn.lower() == "n" or user_wins_yn.lower() == "no":
        print("\nThat's ok, you practiced! Don't give up")
        long_sleep()
        user_wins = "None"
    else:
        print('\nPlease input "y" or "n" :)')
        sleep()
        log_wins()


def complete_log():
    """
    Prints the log data back to the user.
    Triggers save_log on user input
    """
    clear_screen()
    tprint("Your  Log")
    short_sleep()
    print("\nGroovy! So let me reflect your log back to you:\n")
    long_sleep()
    clear_screen()
    tprint("Your  Log")
    print(f"\nYou practiced on {session_date}...\n")
    sleep()
    print(f"\nFor {session_duration} mins...\n")
    sleep()
    print(f"\nYou scored your productivity as {prod_score} out of 10...\n")
    sleep()
    print("\nYou worked on the following exercises:")
    print(f"\n{user_exercises}\n")
    sleep()
    print("\nYou expressed the following difficulties in your session:")
    print(f"\n{user_diffs}\n")
    sleep()
    print("\nYou expressed the following WINS:")
    print(f"\n{user_wins}\n")
    sleep()
    print("\nLOG COMPLETE! You are SMASHING IT!\n")
    sleep()
    input('\nPress "Enter" to contine on down the road...')
    save_log()


def save_log():
    """
    Asks the user if they would like to save their log,
    Validate input.
    If yes, trigger the collate_data function and push_log_data
    function to save to spreadsheet. If not, ask if sure and
    validate input again, then either save and return to the main menu
    or quit program
    """
    push = ""
    while True:
        clear_screen()
        tprint("Log   Complete!")
        push = input("\nWould you like to save me, save me, SAAAAVE ME...?"
                     " (y/n)\n")
        if push.lower() == "y" or push.lower() == "yes":
            collate_data()
            push_log_data(data)
            sleep()
            input('\nReady Freddie? Lets go back to the Main Menu...'
                  ' ("Hit Enter")\n')
            return_to_main()
        elif push.lower() == "n" or push.lower() == "no":
            clear_screen()
            tprint("Log   Complete!")
            print("\nAre you sure?? You've come all this way!")
            confirm = input('\n"y" = Quit and lose all changes.'
                            ' "n" = Save and return to Main Menu.\n')
            if confirm.lower() == "y" or confirm.lower() == "yes":
                quit_program()
            elif confirm.lower() == "n" or confirm.lower() == "no":
                print("\nCaught in a trap... but you got out! Saving log...")
                long_sleep()
                collate_data()
                push_log_data(data)
                long_sleep()
                input('Hit "Enter" to return...')
                return_to_main()
            else:
                clear_screen()
                tprint("Log   Complete!")
                print("\nI can't go for that, no can do...")
                sleep()
        else:
            print('\nCan I get a "y" or "n"...?')
            sleep()
            save_log()


def collate_data():
    """
    Collates all of the user input variables into a single variable
    and converts ints to strings.
    """
    clear_screen()
    tprint("Log   Complete!")
    global data
    print("Pickin' up the pieces...")
    data = [
        str(session_date),
        str(session_duration),
        str(prod_score),
        user_exercises,
        user_diffs,
        user_wins]
    sleep()
    print("\nPieces succesfully picked up :)")


def push_log_data(data):
    """
    Update log worksheet, add new row with the data provided
    by the user in the log program
    """
    sleep()
    print("\nGiving your log to Mr Postman...\n")
    log_worksheet = SHEET.worksheet("log")
    log_worksheet.append_row(data)
    sleep()
    print("Signed, sealed, delivered. Log saved! ")


# 2. Get Insights Menu
def get_insights():
    """
    Main function for option 2 to allow choice to next menu
    """
    while True:
        clear_screen()
        tprint("Get   Insights")
        sleep()
        print("You have chosen to get insights on your saved practice logs\n")
        sleep()
        print(
            """
            * Insights Menu *
              - - - - - - -

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
        elif user_choice == "2":
            view_3_logs()
        elif user_choice == "3":
            average_time()
        elif user_choice == "4":
            view_exercises()
        elif user_choice == "5":
            view_difficulties()
        elif user_choice == "6":
            return_to_main()
        else:
            print("\nGimme, Gimme, Gimme a number between 1 and 6:"
                  " Try again...")
            long_sleep()


# 2. Get Insights - 1. View Last Log
def view_last_Log():
    """
    Get all log sheet data, get the last entry,
    split the list entry and seperately print to the user
    """
    clear_screen()
    tprint("Last Log")
    print("\nYou have chosen to view the last log entry. \nLoading...\n")
    all_data = log.get_all_values()
    last_log = list.pop(all_data)
    sleep()
    clear_screen()
    tprint("Last Log")
    print("\nOk, I've found your last recorded log:\n")
    sleep()
    print(f"\nDate: {last_log[0]}")
    short_sleep()
    print(f"\nPractice Time: {last_log[1]}")
    short_sleep()
    print(f"\nProductivity Score: {last_log[2]}")
    short_sleep()
    print(f"\nExercises Worked On:\n\n{last_log[3]}\n")
    short_sleep()
    print(f"\nDifficulties Encountered:\n\n{last_log[4]}\n")
    short_sleep()
    print(f"\nPersonal Wins:\n\n{last_log[5]}\n")
    short_sleep()
    input('\nHit "Enter" to take it back...\n')
    get_insights()


# 2. Get Insights - 2. View Last Three Logs
def view_3_logs():
    """
    Get all values from spreadsheet, find last 3 rows (logs),
    send each of the 3 rows into seperate variables,
    print the information from those variables to the user
    """
    clear_screen()
    tprint("Logs")
    print("\nRunning up that hill to get your last 3 entries...")
    all_data = log.get_all_values()
    most_recent = all_data[-1]
    second_recent = all_data[-2]
    third_recent = all_data[-3]
    long_sleep()
    clear_screen()
    tprint("Log   1")
    sleep()
    print("* Most Recent Log *")
    sleep()
    print(f"\nDate: {most_recent[0]}\n")
    sleep()
    print(f"\nYou practiced for {most_recent[1]} mins\n")
    sleep()
    print(f"\nYou scored your productivity at {most_recent[2]}\n")
    sleep()
    print(f"\nThe exercises you worked on were:\n\n{most_recent[3]}\n")
    sleep()
    print("\nYou expressed the difficulties you encountered as:"
          f"\n\n{most_recent[4]}\n")
    sleep()
    print(f"\nYou expressed your successes as:\n\n{most_recent[5]}\n")
    sleep()
    input('\nHit me with your rhythm ("Enter") stick...\n')

    # Printing second most recent entry
    clear_screen()
    tprint("Log   2")
    sleep()
    print("* Second Most Recent Log *")
    sleep()
    print(f"\nDate: {second_recent[0]}\n")
    sleep()
    print(f"\nYou practiced for {second_recent[1]} mins\n")
    sleep()
    print(f"\nYou scored your productivity at {second_recent[2]}\n")
    sleep()
    print(f"\nThe exercises you worked on were:\n\n{second_recent[3]}\n")
    sleep()
    print("\nYou expressed the difficulties you encountered as:"
          f"\n\n{second_recent[4]}\n")
    sleep()
    print(f"\nYou expressed your successes as:\n\n{second_recent[5]}\n")
    sleep()
    input('\nHit me... (Press "Enter")\n')

    # Printing third most recent entry
    clear_screen()
    tprint("Log   3")
    sleep()
    print("* Third Most Recent Log *")
    sleep()
    print(f"\nDate: {third_recent[0]}\n")
    sleep()
    print(f"\nYou practiced for {third_recent[1]} mins\n")
    sleep()
    print(f"\nYou scored your productivity at {third_recent[2]}\n")
    sleep()
    print(f"\nThe exercises you worked on were:\n\n{third_recent[3]}\n")
    sleep()
    print("\nYou expressed the difficulties you encountered as:"
          f"\n\n{third_recent[4]}\n")
    sleep()
    print(f"\nYou expressed your successes as:\n\n{third_recent[5]}\n")
    sleep()
    input('\nHIT... ME! ...(Press "Enter" to return to the Menu...)\n')
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
    tprint("Average Time")
    print("\nHold on, won't be long...")
    long_sleep()
    clear_screen()
    tprint("Average Time")
    sleep()
    print("Here I can calculate your average time spent per practice session\n"
          "from looking at the total time spent in each individual session\n"
          "in your logs\n")
    sleep()
    input('Ready Freddie? (Press "Enter")\n')
    clear_screen()
    tprint("Average Time")
    all_values = log.col_values(2)
    all_nums = all_values[1:]
    all_ints = [int(i) for i in all_nums]
    total_minutes = sum(all_ints)
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
    input('\nHit "Enter" to return to the Menu...\n')
    get_insights()


# 2. Get Insights - 4. Get List of Exercises
def view_exercises():
    """
    Get all values from Exercises column in spreadsheet,
    Print to the user
    """
    clear_screen()
    tprint("Exercises")
    print("\nLet's look at your logged exercises")
    sleep()
    print("\nHold on, won't be long...")
    long_sleep()
    clear_screen()
    tprint("Exercises")
    all_values = log.col_values(4)
    all_exercises = all_values[1:]
    print("\nHere is a list of exercises you have logged:\n")
    sleep()
    # Code Reference 3
    for i in all_exercises:
        if "," in i:
            i = i.split(",")
            for x in i:
                print(x.strip())
                short_sleep()
        else:
            print(i)
            short_sleep()
    print("\nQuite a list eh?!")
    sleep()
    input('\nHit "Enter" to return to the Menu...\n')
    get_insights()


# 2. Get Insights - 4. Get List of Difficulties
def view_difficulties():
    """
    Get all values from Difficulties column in spreadsheet,
    Removes any "None" values. Prints to the user
    """
    clear_screen()
    tprint("Difficulties")
    print("\nLet's look at your logged difficulties")
    sleep()
    print("\n\nHold on, won't be long...\n")
    long_sleep()
    clear_screen()
    tprint("Difficulties")
    print("Remember! These are useful to help you understand things you "
          "should be working on\nor ways to develop your practice in future"
          " sessions\n")
    sleep()
    all_values = log.col_values(5)
    all_diffs = all_values[1:]
    none = "None"
    new_diffs_list = [i for i in all_diffs if none not in i]
    print("\nHere is a list of difficulties you have logged:\n")
    for i in new_diffs_list:
        if "," in i:
            i = i.split(",")
            for x in i:
                print(x.strip())
                short_sleep()
        else:
            print(i)
            short_sleep()
    input('\nHit "Enter" to return to the Menu...\n')
    get_insights()


# 3. Submit Practice Ideas
def submit_ideas():
    """
    Main function for option 3 for the user to sumbit their own
    practice ideas
    """
    clear_screen()
    tprint("Submit   Ideas")
    long_sleep()
    print("\nAlrighty then! Let me show you how to submit some practice ideas")
    long_sleep()
    print("\nHere I will ask you a series of questions to help me organise\n"
          "your ideas into one of 4 categories...")
    input('Hit "Enter" to continue...')
    clear_screen()
    tprint("Topics")
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
    long_sleep()
    print("""
        (Please only save one practice idea at a time)
    """)
    long_sleep()
    input('\nHit "Enter" to continue...\n')
    submit_ideas_menu()


def submit_ideas_menu():
    """
    The menu for the submit ideas menu.
    Validating user input for menu choice and directing
    the program to run the relevant function
    """
    clear_screen()
    tprint("Topics")
    print("""
                * Menu *
                  ----\n
            1. Technical
            2. Musicianship
            3. Creative
            4. Repertoire
            5. Return to Menu
    """)
    user_choice = input("\nWhich category do you want to log your"
                        " practice idea under?\n")
    while True:
        if user_choice == "1":
            clear_screen()
            tprint("Technique")
            print("Technical, ok great!\n\nGood technique facilitates"
                  " everything we do!")
            submit_tech()
        elif user_choice == "2":
            clear_screen()
            tprint("Musicianship")
            print("Musicianship, FAB!\n\n Good musicianship"
                  " skills are essential!")
            submit_musicianship()
        elif user_choice == "3":
            clear_screen()
            tprint("Creative")
            print("Creative! Right on!\n\n Developing these skills help to "
                  "do what we are here to do...\nMAKE MUSIC :) ")
            submit_creative()
        elif user_choice == "4":
            clear_screen()
            tprint("Repertoire")
            print("Repertoire, ROCK ON!\n\nGet ready for the gigs!")
            submit_repertoire()
        elif user_choice == "5":
            return_to_main()
        elif user_choice != "1" or "2" or "3" or "4" or "5" or "":
            print("\nGimme, Gimme, Gimme a number between 1 and 5:"
                  " Try again...")
            long_sleep()
            submit_ideas_menu()


def submit_tech():
    """
    Prepares to submit technical exercises to the spreadsheet,
    print back to the user and ask if they wish to save it to the
    spreadsheet or try again. Add today's date to the data.
    Validate agains incorrect inputs
    """
    sleep()
    clear_screen()
    global tech_data
    tprint("Technique")
    tech_idea = input("\nWhat details would you like to save?\n")
    tech_data = []
    tech_data.append(today)
    tech_data.append(tech_idea)
    print("\nOk, I've got that.\n")
    sleep()
    while True:
        clear_screen()
        tprint("Technique")
        print("Just to confirm, Here's what you wrote:\n")
        print(f'\n"{tech_idea}"\n')
        user_confirm = input('\nShall I save that for you?\n(Hit "y" to save,'
                             ' "n" to delete and return to the menu)\n')
        if user_confirm.lower() == "y" or user_confirm.lower() == "yes":
            clear_screen()
            send_tech_exs(tech_data)
        elif user_confirm.lower() == "n" or user_confirm.lower() == "no":
            print("\nCool and the gang. Returning to menu...")
            sleep()
            submit_ideas_menu()
        else:
            print("\nOops you did it again....Please try again...")
            sleep()


def submit_musicianship():
    """
    Prepares to submit musicianship exercises to the spreadsheet,
    print back to the user and ask if they wish to save it to the
    spreadsheet or try again. Add today's date to the data.
    Validate agains incorrect inputs
    """
    sleep()
    clear_screen()
    tprint("Musicianship")
    global musicianship_data
    musicianship_idea = input("\nWhat details would you like to save?\n")
    musicianship_data = []
    musicianship_data.append(today)
    musicianship_data.append(musicianship_idea)
    print("\nOk, I've got that.\n")
    sleep()
    while True:
        clear_screen()
        tprint("Musicianship")
        print("Just to confirm: Here's what you wrote:\n")
        print(f'\n"{musicianship_idea}"\n')
        user_confirm = input('\nShall I save that for you?\n(Hit "y" to save,'
                             ' "n" to delete and return to the menu)\n')
        if user_confirm.lower() == "y" or user_confirm.lower() == "yes":
            clear_screen()
            send_music_exs(musicianship_data)
        elif user_confirm.lower() == "n" or user_confirm.lower() == "no":
            print("Coolio. Returning to menu...")
            sleep()
            submit_ideas_menu()
        else:
            print("\nOops you did it again....Please try again...")
            sleep()


def submit_creative():
    """
    Prepares to submit creative exercises to the spreadsheet,
    print back to the user and ask if they wish to save it to the
    spreadsheet or try again. Add today's date to the data.
    Validate agains incorrect inputs
    """
    sleep()
    clear_screen()
    tprint("Creative")
    global creative_data
    creative_idea = input("\nWhat details would you like to save?\n")
    creative_data = []
    creative_data.append(today)
    creative_data.append(creative_idea)
    print("\nOk, I've got that.\n")
    sleep()
    while True:
        clear_screen()
        tprint("Creative")
        print("Just to confirm: Here's what you wrote:\n")
        print(f'\n"{creative_idea}"\n')
        user_confirm = input('\nShall I save that for you?\n(Hit "y" to save,'
                             ' "n" to delete and return to the menu)\n')
        if user_confirm.lower() == "y" or user_confirm.lower() == "yes":
            clear_screen()
            send_creative_exe(creative_data)
        elif user_confirm.lower() == "n" or user_confirm.lower() == "no":
            print("Coolio. Returning to menu...")
            submit_ideas_menu()
        else:
            print("\nOops you did it again....Please try again...")
            sleep()


def submit_repertoire():
    """
    Prepares to submit repertoire exercises to the spreadsheet,
    print back to the user and ask if they wish to save it to the
    spreadsheet or try again. Add today's date to the data.
    Validate agains incorrect inputs
    """
    sleep()
    clear_screen()
    tprint("Repertoire")
    global repertoire_data
    repertoire_idea = input("\nWhat details would you like to save?\n")
    repertoire_data = []
    repertoire_data.append(today)
    repertoire_data.append(repertoire_idea)
    print("\nOk, I've got that.\n")
    sleep()
    while True:
        clear_screen()
        tprint("Repertoire")
        print("Just to confirm: Here's what you wrote:\n")
        print(f'\n"{repertoire_idea}"\n')
        user_confirm = input('\nShall I save that for you?\n(Hit "y" to save,'
                             ' "n" to delete and return to the menu)\n')
        if user_confirm.lower() == "y" or user_confirm.lower() == "yes":
            clear_screen()
            send_repertoire_exe(repertoire_data)
        elif user_confirm.lower() == "n" or user_confirm.lower() == "no":
            print("Cool and the gang. Returning to menu...")
            sleep()
            submit_ideas_menu()
        else:
            print("\nOops you did it again....Please try again...")
            sleep()


# Functions to send user input data to the relevant spreadsheets
def send_tech_exs(tech_data):
    """
    Sends technique exercises to the worksheet
    """
    tprint("Saving...")
    print("Signed, sealed...\n")
    technique_sheet.append_row(tech_data)
    sleep()
    print("Delivered! It's done. Returning to Menu...")
    sleep()
    submit_ideas_menu()


def send_music_exs(musicianship_data):
    """
    Sends musicianship exercises to the worksheet
    """
    tprint("Saving...")
    print("Signed, sealed...\n")
    musicianship_sheet.append_row(musicianship_data)
    sleep()
    print("Delivered! It's done. Returning to Menu...")
    sleep()
    submit_ideas_menu()


def send_creative_exe(creative_data):
    """
    Sends creativity exercises to the worksheet
    """
    tprint("Saving...")
    print("Signed, sealed...\n")
    creativity_sheet.append_row(creative_data)
    sleep()
    print("Delivered! It's done. Returning to Menu...")
    sleep()
    submit_ideas_menu()


def send_repertoire_exe(repertoire_data):
    """
    Sends repertoire exercises to the worksheet
    """
    tprint("Saving...")
    print("Signed, sealed...\n")
    repertoire_sheet.append_row(repertoire_data)
    sleep()
    print("Delivered! It's done. Returning to Menu...")
    sleep()
    submit_ideas_menu()


# 4. Get Practice
def get_practice():
    """
    Ask user which practice topics they would like to view the logged
    exercises for, error-proof input, and display the requested data
    """
    while True:
        clear_screen()
        tprint("View Exercices")
        print("Here I can show you your previously logged practice ideas")
        print("\nBo Selecta! from the following:")
        print("""\n
                      * Menu *
                        ----\n
            1. View Technical Exercises
            2. View Musicianship Exercises
            3. View Creative Exercises
            4. View Repertoire Exercises
            5. Random Exercise Generator
            6. Return to the Main Menu
        """)
        user_choice = input("\nPlease choose an option with a number (1-6):\n")
        if user_choice == "1":
            clear_screen()
            tprint("Technical")
            print("\nI ammmmmm, the [option] 1 and only...")
            long_sleep()
            view_technical_exercises()
        elif user_choice == "2":
            clear_screen()
            tprint("Musicianship")
            print("\nJust the [option] 2 of us...")
            long_sleep()
            view_musicianship_exercises()
        elif user_choice == "3":
            clear_screen()
            tprint("Creative")
            print('\n3 is the magic number...')
            long_sleep()
            view_creativity_exercises()
        elif user_choice == "4":
            clear_screen()
            tprint("Repertoire")
            print("\nFaith no more, here's option 4...")
            long_sleep()
            view_repertoire_exercises()
        elif user_choice == "5":
            clear_screen()
            tprint("Generator!")
            print("\n[Option] 5 will make you get down now... \n")
            long_sleep()
            random_practice()
        elif user_choice == "6":
            return_to_main()
        else:
            print("\nWhoops, you did it again... have another go\n")
            sleep()


def view_error():
    """
    Reusable error message for the Get Practice functions,
    Returns the user to the Get Practice Menu
    """
    clear_screen()
    tprint("Whoops...")
    sleep()
    print("\nI'm sure you didn't mean...")
    sleep()
    print("\nTo not press...the buttons I said you could press...")
    sleep()
    print("\nDon't worry...\n")
    sleep()
    print("                I'll lift us up where we belong...")
    long_sleep()
    get_practice()


# 4. View Practice - 1. View Technical Exercises
def view_technical_exercises():
    """
    Retrieves all information from 'my-technical-exercises' worksheet
    and prints to user. Removes the column title and prints,
    Validates a request to return to the menu
    """
    clear_screen()
    tprint("Technical")
    print("Hold on whilst I collect your Technical "
          "practice ideas...\n\n")
    technical_exercises = technique_sheet.col_values(2)
    technical_exercises.remove("Technical Exercises")
    for exercise in technical_exercises:
        print(exercise)
        short_sleep()
    sleep()
    print("\n\nPhew! That's some GAINS material right there!")
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
    else:
        view_error()


# 4. View Practice - 2. View Musicianship Exercises
def view_musicianship_exercises():
    """
    Retrieves all information from 'my-musicianship-exercises' worksheet
    and prints to user. Removes the column title and prints,
    Validates a request to return to the menu
    """
    clear_screen()
    tprint("Musicianship")
    print("Hold on whilst I collect your Musicianship "
          "practice ideas...\n\n")
    sleep()
    musicianship_exercises = musicianship_sheet.col_values(2)
    musicianship_exercises.remove("Musicianship Exercises")
    for exercise in musicianship_exercises:
        print(exercise)
        short_sleep()
    print("\n\nPhew! That's everything I have...\n")
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
    else:
        view_error()


# 4. View Practice - 3. View Creativity Exercises
def view_creativity_exercises():
    """
    Retrieves all information from 'my-creativity-exercises' worksheet
    and prints to user. Validates a request to return to the menu
    """
    clear_screen()
    tprint("Creative")
    print("Hold on whilst I collect your creative "
          "practice ideas...\n\n")
    sleep()
    creativity_exercises = creativity_sheet.col_values(2)
    creativity_exercises.remove("Creative Practice")
    for exercise in creativity_exercises:
        print(exercise)
        short_sleep()
    print("\n\nOutta SIGHT! Some good stuff in there!\n")
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
    else:
        view_error()


# 4. View Practice - 4. View Repertoire Exercises
def view_repertoire_exercises():
    """
    Retrieves all information from 'my-repertoire-exercises' worksheet
    and prints to user. Validates a request to return to the menu.
    """
    clear_screen()
    tprint("Repertoire")
    print("Hold on whilst I collect your repertoire "
          "practice ideas...\n\n")
    sleep()
    repertoire_exercises = repertoire_sheet.col_values(2)
    repertoire_exercises.remove("Repertoire Practice")
    for exercise in repertoire_exercises:
        print(exercise)
        short_sleep()
    print("\n\nWhat a collection of BANGERS! You have good taste!\n")
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
    else:
        view_error()


# 4. Get Practice Ideas - 5. View Random Selection
def random_practice():
    """
    Prints information about the random practice generation and
    holds triggers the generator function
    """
    clear_screen()
    tprint("Generator!")
    print(" * Random Exercise Generator * ")
    sleep()
    print("\nSo... you're looking for some spontaneous practice ideas\n"
          "for your next session? I can help!\n")
    sleep()
    print("I can retrive a selection of random exercises from the\n"
          "database that holds your previous exercise idea submissions...")
    sleep()
    input('\nReady Freddie? Hit "Enter" to begin...\n')
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
    print("\nLoading....")
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
    while True:
        clear_screen()
        tprint("Generator!")
        user_choice = input('\nPress "g" and I will generate a list of 5 '
                            'exercises\n\nType "e" to exit to the menu:\n')
        if user_choice.lower() == "e":
            print("\nOk! Now running up that hill, to the Menu...")
            long_sleep()
            get_practice()
        elif user_choice.lower() == "g":
            clear_screen()
            tprint("Generator!")
            print("Superstar DJ, here we go!...\n")
            long_sleep()
            while True:
                clear_screen()
                tprint("Generator!")
                print("Here is your list of 3 randomly selected "
                      "exercises for your next session:\n\n")
                new_list = 0
                # Code Reference 4
                while new_list < 3:
                    sleep()
                    print(random.choice(all_values))
                    new_list += 1
                sleep()
                print("\n\nDoes that inspire your practice??")
                short_sleep()
                user_confirm = input('\n"y" All good, lets go! or "g" Generate'
                                     ' another random list:\n')
                if user_confirm.lower() == "y":
                    print("\nYou're Simply the BEST! "
                          "Have a great practice session!\n")
                    long_sleep()
                    print("\nReturning to the Menu...")
                    sleep()
                    get_practice()
                elif user_confirm.lower() == "g":
                    print("\nOk, Hold on...")
                    new_list = 0
                    sleep()
                else:
                    print("\nHmmm...I'm just going to pretend you wanted"
                          " to start again... ")
                    long_sleep()
                    random_generator_loop()
        else:
            print("\nOoops up side your head...")
            sleep()
            print("\nLets try that again...")
            sleep()


# 5. Quit Program
def quit_program():
    """
    Function to allow the user to safely quit the program
    Validate for accidental quit
    """
    while True:
        clear_screen()
        tprint("Quit...?")
        print("\nShould you stay or should you go...?\n")
        quit_choice = input('\nStay "y", Go "n":\n')
        if quit_choice.lower() == "n" or quit_choice.lower() == "no":
            clear_screen()
            print("\nQuitting...\n")
            sleep()
            tprint("Bye,")
            short_sleep()
            tprint("                  Bye,")
            short_sleep()
            tprint("                                Bye!")
            exit()
        elif quit_choice.lower() == "y" or quit_choice.lower() == "yes":
            return_to_main()
        else:
            clear_screen()
            tprint("Quit...?")
            print('\nYou, you, you, oughta know...\n')
            sleep()
            print("\nYou should have pressed yes or no...")
            long_sleep()


def start():
    """
    Save today's date as global variable,
    Welcome message and user choice input to proceed
    """
    clear_screen()
    get_date()
    main_title()
    long_sleep()
    print("\n ** Welcome to Nick's Practice Log! **")
    sleep()
    print("\nHi, my name is Nick and I'm a musician. For us musicians, "
          "practice\nis essential.")
    sleep()
    print("\nSo I've built this little program to help log and"
          " manage basic practice session\ninformation.")
    sleep()
    print("\nI also enjoy silly pop music references, "
          "see how many you can spot!")
    sleep()
    print("\nFYI, all data is kept on a spreadsheet and is pre-populated with"
          " a few ideas\nfor your convenience.\n")
    sleep()
    print("Without further agadoo... ;) Let's get busy!\n")
    input('\nPress "Enter" to continue\n')
    start_menu()


def start_menu():
    """
    Creates the Main Menu and validates user choice,
    Triggers relevant function
    """
    while True:
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
            log_difficulties()
            log_wins()
            complete_log()
            save_log()
        elif start_choice == "2":
            get_insights()
        elif start_choice == "3":
            submit_ideas()
        elif start_choice == "4":
            get_practice()
        elif start_choice == "5":
            quit_program()
        else:
            print("\nOops you did it [wrong] again...\n"
                  "\nLet's go back to the very beginning....")
            long_sleep()


start()
