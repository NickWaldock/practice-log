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

data = log.get_all_values()
print(data)

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
        # Validate for correct date input format
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
    time.sleep(2)


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
    time.sleep(2)


def log_score():
    """
    Ask user for self-assesed productivity score input,
    and validate for an integer 
    """
    prod_score = int(input("\nOn a scale of 1 - 10, how productive do you feel the session was?\n"))
    if prod_score <= 3:
        print(f"\n{prod_score} is ok, you still practiced!\nIt's the consistency that counts\n")
    elif prod_score <= 5:
        print(f"\n{prod_score} is a good score! All progress is good progress!\n")
    elif prod_score <= 8:
        print(f"\n{prod_score} is fantastic! Well done!\n")
    elif prod_score <= 10:
        print(f"\n{prod_score} is awesome! You are smashing it!\n")

def start():
    """
    Welcome message and user choice input to proceed
    """
    print("1. Log a practice session")
    print("2. Get insights on your practice")
    print("3. Get practice ideas")
    print("4. Quit\n")
    print("Make your selection with a number:")
    start_choice = int(input())

    if start_choice == 1:
        print("\n You have chosen to log a new practice session.\n")
        log_practice()
        log_date()
        log_duration()
        log_score()
    elif start_choice == 2:
        print("\n You have chosen to get insights on your logged practice sessions\n")
    elif start_choice == 3:
        print("\nYou have chosen to get practice ideas")
    elif start_choice == 4:
        print("\nQuitting, thank you for logging your practice")
        exit()


print("\n ** Wecome to the Practice Log! **\n")
print("What would you like to do?\n")
# start()

