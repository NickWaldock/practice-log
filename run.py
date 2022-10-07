# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from datetime import date
import re
import time
from art import *
from os import system, name

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
tech_sheet = SHEET.worksheet("my-technical-exercises")
mus_sheet = SHEET.worksheet("my-musicianship-exercises")
create_sheet = SHEET.worksheet("my-creative-exercises")
rep_sheet = SHEET.worksheet("my-repertoire-exercises")


# Display Titles
def main_title():
    tprint("Nick's")
    tprint("Practice")
    tprint("Log")


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

def clear_screen():
    """
    Clear the user terminal
    """
    system('clear')


def get_date():
    """
    Get the current date to reference the users inputs in the spreadsheet
    """
    global today
    date_today = date.today()
    today = date_today.strftime('%d/%m/%y')


# 1. Log Practice
def log_practice():
    """
    Log a new practice session.
    Log duration and date of session and productivity score
    """
    clear_screen()
    print("\n** LOG PRACTICE **\n")


def log_date():
    """
    Ask user if their practice date was today,
    if yes - store today's date,
    if no - ask for date input and validate for correct format
    """
    global session_date
    session_date = ""
    session_today = input("\nWas your practice session today? (y/n)\n")

    if session_today.lower() == "y":
        print(f"\nToday's date is {today}\n")

    elif session_today.lower() == "n":
        # Validate for correct date input format (Code Ref.1)
        while True:
            try:
                session_date = input("\nPlease input the date of your practice"
                                     " session (DD/MM/YY):\n")
                valid = re.match(
                    r"^[0-3][0-9]['/'][0-1][0-9]['/'][2][2-3]$",
                    session_date)
                valid_date = bool(valid)
                if valid_date is False:
                    raise ValueError("Please enter a valid date in the correct"
                                     " format (DD/MM/YY):")
                else:
                    break

            except ValueError as e:
                print(f"Invalid Date Format: {e}")

        if valid_date is True:
            print(f"\nOk, I'll log that you practiced on {session_date}\n")
    sleep()


def log_duration():
    """
    Ask user for duration of practice session and validate for an integer
    """
    global session_duration
    session_duration = 0
    clear_screen()
    while True:
        try:
            session_duration = int(input("How long was your practice session"
                                         " in minutes?\n"))
        except ValueError:
            print("\nPlease enter a number\n")
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
    global prod_score
    prod_score = int(input("\nOn a scale of 1 - 10, how productive do you"
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


def log_exercises():
    """
    Asks the user to provide details of the specific exercises they worked on
    in the practice session, saved in a variable
    """
    clear_screen()
    global user_exercises
    user_exercises = input('\nWhat exercises did you work on in this practice'
                           ' session?\n(Seperate exercises with ",")\n')
    sleep()
    print("\nGreat work!\n")
    print(f"\nI have made a note of the following:\n {user_exercises}")
    sleep()


def log_wins():
    """
    Asks the user to detail particular problems experienced in the
    practice session, then asks for details on what positive
    outcomes they achieved.
    """
    clear_screen()
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
        print("\nGreat! Moving on...")
    sleep()

    # Ask for info on wins in the practice session
    clear_screen()
    user_wins_yn = input("\nAny successes to brag about? (y/n)\n")
    if user_wins_yn.lower() == "y":
        user_wins = input('Amazing! What were they? '
                          '(seperate your wins with ",")\n')
        sleep()
        print("\nWell done! You are making great progress!")
    elif user_wins_yn.lower() == "n":
        print("\nThat's ok, you practiced! That's what counts!")
        user_wins = "None"

    sleep()
    clear_screen()
    print("\nYou logged the following difficulties and wins:\n")
    sleep()
    print(f"Difficulties -\n {user_diffs}\n")
    sleep()
    print(f"Wins         -\n {user_wins}\n")
    sleep()
    print("\nThis completes your log. Thank you and great work!\n")
    sleep()
    clear_screen()

    # Commit log to spreadsheet
    push = ""
    # Check for a valid input
    while push != 'y' or push != 'n':
        push = input("\nWould you like to save this log? (y/n)\n")
        if push.lower() == "y":
            collate_data()
            sleep()
            print("\nSaving log...")
            push_log_data(data)
            sleep()
            print("\nReturning to main menu...")
            sleep()
            start()
        elif push.lower() == "n":
            print("\nAre you sure you do not want to save this log?")
            confirm = input('\n"y" = quit and lose all changes.'
                            ' "n" = save and return to main menu.\n')
            if confirm.lower() == "y":
                quit_program()
            elif confirm.lower() == "n":
                collate_data()
                print("\nSaving log...")
                sleep()
                push_log_data(data)
                print("\nReturning to main menu...")
                sleep()
                clear_screen()
                start()

    # Check if user wishes to quit or return to the main menu
    menu_choice = input('\nType "menu" or "quit" to return to the main menu'
                        ' or exit the program.\n')
    if menu_choice.lower() == "menu":
        print("\nReturning to main menu...\n")
        sleep()
        clear_screen()
        start()
    elif menu_choice.lower == "quit" or "exit":
        choice = input("\nAre you sure you want to quit? (y/n)\n")
        if choice.lower() == "y":
            print("\nQuitting, thank you for logging your practice!"
                  "See you next time!")
        elif choice.lower() == "n":
            print("Returning to main menu...")
            sleep()
            clear_screen()
            start()
        else:
            print("\nSorry I didn't understand that." 
                  "Returning to main menu...\n")
            sleep()
            clear_screen()
            start()


def collate_data():
    """
    Collates all of the user input variables into a single variable
    and converts ints to strings.
    """
    global data
    print("Collating data...")
    data = [
        str(today),
        str(session_duration),
        str(prod_score),
        user_exercises,
        user_diffs,
        user_wins]
    print(data)
    print("Data successfully collated")


def push_log_data(data):
    """
    Update log worksheet, add new row with the data provided
    by the user in the log program
    """
    print("Updating log worksheet...\n")
    log_worksheet = SHEET.worksheet("log")
    log_worksheet.append_row(data)
    print("Logged sucessfully updated")


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

        1. View Last Recorded Log
        2. View Last 3 Logs
        3. Calculate Average Practice Time
        4. View List of Exercises Practiced
        5. View List of Difficulties Encounterd
        """)
    user_choice = input("What would you like to do? (Enter a number)\n")
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
    print("\nHere is you last recorded log:\n")
    sleep()
    print(f"\nDate: {last_log[0]}")
    print(f"\nPractice Time: {last_log[1]}")
    print(f"\nProductivity Score: {last_log[2]}")
    print(f"\nExercises Worked On: {last_log[3]}")
    print(f"\nDifficulties Encountered: {last_log[4]}")
    print(f"\nPersonal Wins: {last_log[5]}")


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

    # Printing most latest entry
    print("\nGetting last 3 entries...")
    sleep()
    clear_screen()
    print("\nMost Recent Log:")
    print(f"\nDate: {most_recent[0]}")
    print(f"\nYou practiced for {most_recent[1]} mins")
    print(f"\nYou scored your productivity at {most_recent[2]}")
    print(f"\nThe exercises you worked on were:\n{most_recent[3]}")
    print("\nYou expressed the difficulties you encountered as:"
          f"\n{most_recent[4]}")
    print(f"\nYou expressed your successes as:\n{most_recent[5]}")
    
    # Printing second most recent entry
    sleep()
    print("\nSecond Most Recent Log:")
    print(f"\nDate: {second_recent[0]}")
    print(f"\nYou practiced for {second_recent[1]} mins")
    print(f"\nYou scored your productivity at {second_recent[2]}")
    print(f"\nThe exercises you worked on were:\n{second_recent[3]}")
    print("\nYou expressed the difficulties you encountered as:"
          f"\n{second_recent[4]}")
    print(f"\nYou expressed your successes as:\n{second_recent[5]}")

    # Printing third most recent entry
    sleep()
    print("\nThird Most Recent Log:")
    print(f"\nDate: {third_recent[0]}")
    print(f"\nYou practiced for {third_recent[1]} mins")
    print(f"\nYou scored your productivity at {third_recent[2]}")
    print(f"\nThe exercises you worked on were:\n{third_recent[3]}")
    print("\nYou expressed the difficulties you encountered as:"
          f"\n{third_recent[4]}")
    print(f"\nYou expressed your successes as:\n{third_recent[5]}")


# 2. Get Insights - 3. Calculate Average Practice Time
def average_time():
    """
    Get all duration values from the column in the spreadsheet,
    Remove the column title from the list,
    Convert as numbers as strings to integers,
    Calculate average and print to the user
    """
    clear_screen()
    print("\nGetting practice data...")
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
    sleep()
    print(f"\nYour average time spent in each practice session is {result}"
          " minutes!")
    sleep()
    print("\nThat's not too shabby ;)")


# 2. Get Insights - 4. Get List of Exercises
def view_exercises():
    """
    Get all values from Exercises column in spreadsheet,
    Print to the user
    """
    clear_screen()
    print("\nYou have chosen to view your logged exercises.")
    sleep()
    print("\nRetrieving data...")
    sleep()
    all_values = log.col_values(4)
    all_exercises = all_values[1:]
    print("\nHere is a list of exercises you have logged:\n")
    for i in all_exercises:
        print(i)


# 2. Get Insights - 4. Get List of Difficulties
def view_difficulties():
    """
    Get all values from Difficulties column in spreadsheet,
    Print to the user
    """
    clear_screen()
    print("\nYou have chosen to view your logged difficulties")
    sleep()
    print("\nRetrieving data...\n")
    sleep()
    clear_screen()
    all_values = log.col_values(5)
    all_diffs = all_values[1:]
    for i in all_diffs:
        print(i)


# 3. Submit Practice Ideas
def submit_ideas():
    """
    Main function for option 3 for the user to sumbit their own
    practice ideas
    """
    clear_screen()
    tprint("Submit Practice Ideas!")
    long_sleep()
    print("\nYou have chosen to submit some practice ideas")
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
    long_sleep()
    user_choice = input("\nWhich category do you want to log your"
                        " practice idea under?\n")
    if user_choice == "1":
        print("\nTechnical, ok great! Good technique facilitates"
              " everything we do!")
        global tech_data
        tech_idea = input("\nWhat details would you like to save?\n")
        tech_data = []
        tech_data.append(today)
        tech_data.append(tech_idea)
        sleep()
        print("\nOk, I've got that. This is what I will save under the topic"
              " 'Technical':\n")
        sleep()
        print(tech_idea)
        user_confirm = input('\nShall I save that for you? (Hit "y" to save,'
                             ' "n" to edit, "d" to delete)\n')
        if user_confirm.lower() == "y":
            send_tech_exs(tech_data)


def send_tech_exs(tech_data):
    print("Saving...\n")
    tech_sheet.append_row(tech_data)


# 5. Quit Program
def quit_program():
    """
    Function to allow the user to safely quit the program
    """
    clear_screen()
    print("\nYou have chosen to quit Nick's Practice Log\n")
    quit_choice = input("\nAre you sure? (y/n)\n")
    if quit_choice.lower() == "y":
        print("\nQuitting...\n")
        tprint("See you next time!")
        exit()
    elif quit_choice.lower() == "n":
        print("\nGreat! Returning to main menu...")
        sleep()
        clear_screen()
        start()
    else:
        print("\nSorry, I didn't understand your input\n")
        sleep()
        print("\nReturning to main menu...\n")
        sleep()
        clear_screen()
        start()


def start():
    """
    Save today's date as global variable,
    Welcome message and user choice input to proceed
    """
    get_date()
    main_title()
    long_sleep()
    print("\n ** Wecome to Nick's Practice Log! **\n")
    long_sleep()
    clear_screen()
    print("What would you like to do?\n")
    print("\n1. Log a practice session")
    print("2. Get insights on your practice")
    print("3. Submit practice ideas")
    print("4. Get practice ideas")
    print("5. Quit\n")
    print("\nMake your selection with a number:")
    start_choice = int(input())

    if start_choice == 1:
        clear_screen()
        print("\n You have chosen to log a new practice session.\n")
        log_practice()
        log_date()
        log_duration()
        log_score()
        log_exercises()
        log_wins()
    elif start_choice == 2:
        clear_screen()
        get_insights()
    elif start_choice == 3:
        clear_screen()
        submit_ideas()
    elif start_choice == 5:
        clear_screen()
        quit_program()


start()