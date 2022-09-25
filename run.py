# Write your code to expect a terminal of 80 characters wide and 24 rows high

def log_practice():
    """
    Log a new practice session.
    Log duration and date of session and productivity score
    """
    print("\n** LOG PRACTICE **\n")
    session_today = input("\nWas your practice session today? (y/n)\n")
    
    #Ask if practice date was today
    if session_today.lower() == "n":
        session_date = input("\nPlease input the date of your practice session (DD/MM/YY):\n")
        print(f"\nYou practiced on {session_date}")
    
    elif session_today.lower() == "y":
        #Get today's date and change default format
        import datetime
        today = datetime.date.today()
        session_date = today.strftime('%d/%m/%y')
        print(f"\nToday's date is {session_date}\n")

    session_duration = int(input("How long was your practice session in minutes?\n"))
    print(f"\nWell done! You practiced for {session_duration} mins")

    prod_score = int(input("\nOn a scale of 1 - 10, how productive was it?"))
    print(prod_score)

def start():
    """
    Welcome message and user choice input to proceed
    """
    username = input("Please enter your name: ")
    print(f"\nHello {username}! What would you like to do?\n")
    print("1. Log a practice session")
    print("2. Get insights on your practice")
    print("3. Get practice ideas")
    print("4. Quit\n")
    print("Make your selection with a number")
    start_choice = int(input())

    if start_choice == 1:
        print("\n You have chosen to log a new practice session.\n")
        log_practice()
    elif start_choice == 2:
        print("\n You have chosen to get insights on your logged practice sessions\n")
    elif start_choice == 3:
        print("\nYou have chosen to get practice ideas")
    elif start_choice == 4:
        print("\nQuitting, thank you for logging your practice")
        exit()
    


print("Wecome to the Practice Log!\n")
start()

