# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials 
from datetime import datetime
import datetime
import re
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("practice_log")

log = SHEET.worksheet("log")

# data = log.get_all_values()
# print(data)

def log_practice():
    """
    Log a new practice session.
    Log duration and date of session and productivity score
    """
    print("\n** LOG PRACTICE **\n")


def log_date():
    """
    Ask user if their practice date was today,
    if yes - store today's date,
    if no - ask for date input and validate for correct format
    """
    session_today = input("\nWas your practice session today? (y/n)\n")

    if session_today.lower() == "y":
        # Get today's date and change default format
        today = datetime.date.today()
        session_date = today.strftime('%d/%m/%y')
        print(f"\nToday's date is {session_date}\n")

    elif session_today.lower() == "n":
        # Validate for correct date input format (Code Ref.1)
        while True:
            try:
                session_date = input("\nPlease input the date of your practice session (DD/MM/YY):\n")
                is_valid = re.match(r"^[0-3][0-9]['/'][0-1][0-9]['/'][2][2-3]$", session_date)
                valid_date = bool(is_valid)
                if valid_date is False:
                    raise ValueError("Please enter a valid date in the correct format (DD/MM/YY):")
                else:
                    break

            except ValueError as e:
                print(f"Invalid Date Format: {e}")

        if valid_date is True:
            print(f"\nYou practiced on {session_date}\n")
    time.sleep(1.5)


def log_duration():
    """
    Ask user for duration of practice session and validate for an integer
    """
    session_duration = 0
    while True:
        try:
            session_duration = int(input("How long was your practice session in minutes?\n"))
        except ValueError:
            print("\nPlease enter a number\n")
        else:
            print(f"\nWell done! You practiced for {session_duration} mins!")
            break
    time.sleep(1.5)


def log_score():
    """
    Ask user for self-assesed productivity score input,
    and validate for an integer 
    """
    prod_score = int(input("\nOn a scale of 1 - 10, how productive do you feel the session was?\n"))
    if prod_score <= 3:
        print(f"\n{prod_score} is ok, you still practiced!\nIt's the consistency that counts\n")
        time.sleep(1.5)
    elif prod_score <= 5:
        print(f"\n{prod_score} is a good score! All progress is good progress!\n")
        time.sleep(1.5)
    elif prod_score <= 8:
        print(f"\n{prod_score} is fantastic! Well done!\n")
        time.sleep(1.5)
    elif prod_score <= 10:
        print(f"\n{prod_score} is awesome! You are smashing it!\n")
        time.sleep(1.5)


def log_topics():
    """
    Explain to the user the next steps. Define the four main pratice topics.
    Ask the user whether they practiced any exercises within a topic 
    if they respond YES specifics are requested. Data is saved to variables 
    and later sent to the spreadsheet.
    """
    print("\nNext I will ask you about what exercises you worked on.")
    time.sleep(1.5)
    topics_options = '''
        In this model, general practice topics are classed as either:

        1. Technical    - Developing technical skill through repeated 
                          incremental exercises targeting specific 
                          motor movements

        2. Musicianship - Developing musically intuitive skills 
                          (Aural, theory, harmony, rhythm, sight-reading
                          ensemble skills, voacbulary, etc)

        3. Creative     - Developing creative skills and intuition
                          (Improvisation, composition, interpretation,
                          phrasing, etc)

        4. Repertoire   - Learning new or refining already-known repertoire
                          (Transciption, memorisation, repertoire reserach)
        '''
    print(topics_options)

    # Define the dictionary for user input
    user_exercises = {
        "Technical": "",
        "Musicianship": "",
        "Creative": "",
        "Repertoire": ""
    }

    # Repeated acknoledgement responses
    logged = "\nGreat, I've made a note of that.\n"
    no_log = "\nOk, no problem.\n"

    # Define variables for user inputs as global
    global user_technique_exercises
    global user_musicianship_exercises
    global user_creative_exercises

    # Ask about Technique practice
    technique = input("Did you work on anything Technical? (y/n)\n")
    if technique.lower() == "y":
        user_exercises["Technical"] = input('\nPlease list the exercises you worked on seperated by ","\n')
        print(logged)
        time.sleep(1)
    elif technique.lower() == "n":
        print(no_log)
        time.sleep(1)

    # Ask about Musicianship practice
    musicianship = input("Did you work on anything relating to Musicianship? (y/n)\n")
    if musicianship.lower() == "y":
        user_musicianship_exercises = input('\nPlease list the exercises you worked on seperated by ","\n')
        print(logged)
        time.sleep(1)
    elif musicianship.lower() == "n":
        print(no_log)
        time.sleep(1)

    # Ask about Creative practice
    creative = input("Did you work on anything relating to Musicianship? (y/n)\n")
    if creative.lower() == "y":
        user_creative_exercises = input('\nPlease list the exercises you worked on seperated by ","\n')
        print(logged)
        time.sleep(1)
    elif creative.lower() == "n":
        print(no_log)
        time.sleep(1)

    # Ask about Repertoire practice
    repertoire = input("Did you work on anything relating to Musicianship? (y/n)\n")
    if repertoire.lower() == "y":
        user_repertoire_exercises = input('\nPlease list the exercises you worked on seperated by ","\n')
        print(logged)
        time.sleep(1)
    elif repertoire.lower() == "n":
        print(no_log)
        time.sleep(1)
    time.sleep(1.5)
    print("\nOk, you have logged the following this practice session:\n")
    print()


    print("Let's move on to the final part of the log...")





def quit_program():
    """
    Function to allow the user to safely quit the program
    """
    print("\nYou have chosen to quit Nick's Practice Log\n")
    quit_choice = ""
    quit_choice = input("\nAre you sure? (y/n)\n")
    if quit_choice.lower() == "y":
        print("\nQuitting, thank you for logging your practice! See you next time!")
        exit()
    elif quit_choice.lower() == "n":
        print("\nGreat! Returning to main menu...")
        time.sleep(1.5)
        start()
    else:
        print("\nSorry, I didn't understand your input\n")
        print("\nReturning to main menu...\n")
        time.sleep(1.5)
        start()

def start():
    """
    Welcome message and user choice input to proceed
    """
    print("1. Log a practice session")
    print("2. Get insights on your practice")
    print("3. Get practice ideas")
    print("4. Quit\n")
    print("\nMake your selection with a number:")
    start_choice = int(input())

    if start_choice == 1:
        print("\n You have chosen to log a new practice session.\n")
        log_practice()
        log_date()
        log_duration()
        log_score()
        log_topics()
    elif start_choice == 2:
        print("\n You have chosen to get insights on your logged practice sessions\n")
    elif start_choice == 3:
        print("\nYou have chosen to get practice ideas")
    elif start_choice == 4:
        quit_program()
        

        

print("\n ** Wecome to Nick's Practice Log! **\n")
print("What would you like to do?\n")
start()

