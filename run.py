# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("Wecome to the Practice Log!\n")

def start():
    username = input("Please enter your name: ")
    print(f"\nHello {username}! What would you like to do?\n")
    print("1. Log a practice session")
    print("2. Get insights on your practice")
    print("3. Get practice ideas")
    print("4. Quit\n")
    print("Make your selection with a number. ie: 1")
    start_choice = int(input())

    if start_choice == 1:
        print("\n You have chosen to log a new practice session.\n")
    elif start_choice == 2:
        print("\n You have chosen to get insights on your logged practice sessions.\n")
    elif start_choice == 3:
        print("\nYou have chosen to get practice ideas")
    elif start_choice == 4:
        print("\nQuitting, thank you for logging your practice")
        exit()
    

start()

