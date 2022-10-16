# Nick's Practice Log
<img src="readme-imgs/titles.png" width="50%">
<br/>

[View the live site here](https://nicks-practice-log.herokuapp.com/)
<br/>
<br/>

# Table of Contents
1. [Introduction](#introduction)
    i. [Aims](#aims)
2. [User Experience](#user-experience-ux)
3. [Main Features](#main-features)
    1. [Inspiration & Design](#inspiration--design)
    4. [Flow Chart](#)
    5. [Features](#features)
    7. [Future Developments](#future-developments)
4. [Technologies](#technologies)
5. [Testing](#testing)
    1. [Manual Testing](#manual-testing)
    2. [Code Validation](#code-validation)
    4. [Tools](#tools)
6. [Deployment](#deployment)
    1. [GitHub](#github)
    2. [Forking](#forking)
    3. [Cloning](#cloning)
7. [References & Acknowledgements](#references--acknowledgements)
   3. [References](#references)
   4. [Acknoledgements](#acknoledgements)
<br />
<br />

# Introduction & Aims

<br>
<br>


## Aims
- 
<br />
<br />


# Main Features
## Inspiration & Design

<br />
<br />


## Wireframes
[Balsamiq](https://balsamiq.cloud/) has been used to develop wireframes to demonstrate the basic design of the site.
<br />
<br />

<img src="" width="33%">

<br />
<br />

## Features
<img src="" width="40%">

<br />
<br />


## User Stories
<br />
<br />

<br />
<br />
In intend to

I do not intend to

## Future Developments
This project has a great deal of developmental potential in features that could eventually add increased functionality and a deeper user experiece. 
The following are a few examples:
- Get logs with certain scores
- After viewing lists of exercises, immediatly have the option to add more
<br />
<br />

# Technologies
Languages used in this site are [Python]

Additional technologies include: 

- [GitHub](https://github.com/)
  - Site repository
- [Gitpod](https://gitpod.io/)
  - Online IDE for all coding work and site file management, terminal was used to add, commit, and push to Github
<br />
<br />

# 3rd party Modules
art



# Testing
## Pep8
This program is free of any Pep8 errors. There are however a number of suggestions and warnings against my use of global variables and their naming style. My global variables do not act as constants which the Pep8 validator believes they are. This project represents a learning curve for me with Python and its good practice conventions, I believe the use of global variables was a logical step within the scope of this project and in my learning the language. I understood too late to the deadline of this project that this isn't considered 'good practice'. Therefore, for future developments I will adapt this program to take this into account.
<br />
<br />

## Manual Testing 
Each function and validation has been manually tested. All testing logs can her viewed here:
[>> Testing](testing.md)
<br />
<br />


## Tools
Tools used in the development of this project include:
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Heroku](https://heroku.com/)
- [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
- [Lucid Chart](https://www.lucidchart.com/)
- [Google Drive](https://www.google.co.uk/intl/en-GB/drive/)
- [Google Sheets](https://www.google.co.uk/sheets/about/)
<br />
<br />

# Deployment
The live site can be accessed [here](https://nicks-practice-log.herokuapp.com/)
<br />
<br />

## Heroku
This project was deloyed to [Heroku](https://heroku.com/) with the following steps:
1. Log in to Heroku (create an account if necessary)
2. Navigate to your dashboard, click "New" and select "Create new app"
3. Input an appropriate name for your project and choose a region
4. Click the "Settings" tab
5. Click "Reveal Config Vars"
6. Input PORT and 8000 as one config var and click add
7. Input CREDS and the information from your Google Sheet API creds file as another config var and click add
8. Click "Add buildpack"
9. Add "nodejs" and "python" from the list or search if required, click save.
10. Ensure python is the first build pack. YOu can drag to change the order
11. Select "Deploy" from the heading tabs
12. Select "GitHub - Connect to GitHub" next to the Deployment Methods
13. Click "Connect to GitHub"
14. Search for the repository ("practice-log") and click to connect
15. Click either 'Enable Automatic Deploys' or 'Deploy Branch' to deploy manually. If you select Deploy Branch please note you will need to manually deploy each time you update the repository.
16. Finally, click 'View' to visit the deployed site. It may take a moment to become visible
<br />
<br />

## Forking
To fork this repository on [Github](https://github.com/NickWaldock/practice-log) proceed with the following steps:
1. Log it to GitHub (create an account if necessary)
2. Locate the [GitHub Respository](https://github.com/NickWaldock/practice-log)
3. On the repository page, find the 'Fork' menu in the top right, click on the small down arrow
4. Select '+ Create a new fork'
5. Remane repository as required
6. Click 'Create Fork'
7. You now have your forked version of this repository
<br />
<br />

## Cloning
To clone the repository procees with the following steps:
1. Log in to GitHub (create an account if necessary)
2. Locate the [GitHub Respository](https://github.com/NickWaldock/practice-log)
3. On the repository page, find and click on the 'Code' menu in the mid-top right of the page
4. Choose to either download or open in GitHub Desktop,
  - or;
    5. Choose the HTTPS option and copy the URL to your clipboard
    6. - To clone the repository using HTTPS, under "HTTPS", copy the url
       - To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then copy the url
       - To clone a repository using GitHub CLI, click GitHub CLI, then copy url
    7. Open Terminal and change the current directory to where you want the cloned directory
    8. Type git clone, and paste the url, press Enter to create your local clone
<br />
<br />

# References & Acknoledgements


## References

The following sites were used for syntax checking, problem solving, and general coding concept referencing:
- 

<br />
<br />

## Acknoledgements























References
General
https://www.programiz.com/python-programming/methods/string/lower
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
https://www.edureka.co/blog/python-list-length/
https://docs.gspread.org/en/latest/user-guide.html

Clear screen
https://www.geeksforgeeks.org/clear-screen-python/

Datetime formatting
https://pynative.com/python-datetime-format-strftime/

Checking string format
https://www.adamsmith.haus/python/answers/how-to-check-if-a-string-matches-a-pattern-in-python

Checking for integer
https://bobbyhadz.com/blog/python-check-if-input-is-integer#:~:text=isdigit()%20%23-,Use%20the%20str.,point%20numbers%20or%20negative%20numbers.
https://pythonguides.com/python-check-if-the-variable-is-an-integer/

Code checker
https://www.pythonchecker.com/

The slow print
https://replit.com/talk/learn/The-Slow-Print/44741

pretty printer
https://docs.python.org/3/library/pprint.html

Console Art
https://github.com/sepandhaghighi/art


https://kodify.net/python/math/round-integers/

Random
https://pynative.com/python-random-choice/

Conditionals
https://www.openbookproject.net/books/bpp4awd/ch04.html

Strip
https://www.w3schools.com/python/ref_string_strip.asp

BUGS
Data not pushing to spreadsheet - due to attemping to send dictionary objects across. Topics dicts function removed and replaced with a log_exercises function