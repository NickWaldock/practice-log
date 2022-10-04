
print(
        """
         ___     __    __
        |    \  |  |  |  |    /          
        |  |  \ |  |  |  |   /              
        |  |\  \|  |  |  |  |            
        |  | \  |  |  |  |   \              
        |__|  \____|  |__|    \          

        """
    )



def log_topics():
    """
    Explain to the user the next steps. Define the four main pratice topics.
    Ask the user whether they practiced any exercises within a topic 
    if they respond YES specifics are requested. Data is saved to variables 
    and later sent to the spreadsheet.
    """
    print("\nNext I will ask you about what exercises you worked on...")
    sleep()
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
    global user_exercises
    user_topics = []

    user_exercises = {
        "Technical": "",
        "Musicianship": "",
        "Creative": "",
        "Repertoire": ""
    }

    # Repeated acknoledgement responses
    logged = "\nGreat, I've made a note of that.\n"
    no_log = "\nOk, no problem.\n"

    # Ask about Technique practice
    technique = input("Did you work on anything Technical? (y/n)\n")
    if technique.lower() == "y":
        user_exercises["Technical"] = input('\nPlease list the exercises you worked on seperated by ","\n')
        print(logged)
        sleep()
    elif technique.lower() == "n":
        user_exercises["Technical"] = "None"
        print(no_log)
        sleep()

    # Ask about Musicianship practice
    musicianship = input("Did you work on anything relating to Musicianship? (y/n)\n")
    if musicianship.lower() == "y":
        user_exercises["Musicianship"] = input('\nPlease list the exercises you worked on seperated by ","\n')
        print(logged)
        sleep()
    elif musicianship.lower() == "n":
        user_exercises["Musicianship"] = "None"
        print(no_log)
        sleep()

    # Ask about Creative practice
    creative = input("Did you work on anything relating to Creativity? (y/n)\n")
    if creative.lower() == "y":
        user_exercises["Creative"] = input('\nPlease list the exercises you worked on seperated by ","\n')
        print(logged)
        sleep()
    elif creative.lower() == "n":
        user_exercises["Creative"] = "None"
        print(no_log)
        sleep()

    # Ask about Repertoire practice
    repertoire = input("Did you work on anything relating to Repertoire? (y/n)\n")
    if repertoire.lower() == "y":
        user_exercises["Repertoire"] = input('\nPlease list the exercises you worked on seperated by ","\n')
        print(logged)
        sleep()
    elif repertoire.lower() == "n":
        user_exercises["Repertoire"] = "None"
        print(no_log)
        sleep()
    sleep()
    print("\nYou have logged the following this practice session:\n")
    print(user_exercises)
    sleep()
    print("\nLet's move on to the final part of the log...\n")
    sleep()
