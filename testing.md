
Input for Productivity Score
User should input a number between 0 and 10. If the user does this the code continues. If not the user if in a loop until a correct parameter is inputted. If the user inputs a number above 10 the loop is also restarted.

[<< Back to main ReadMe](README.md)

# Manual Application Testing

Below is reasonable test I could imagine to check every validation and all results came back as expected.

<table>
  <tr>
    <th>What is being tested</th>
    <th>How</th>
    <th>Expected Response</th>
    <th>Actual Response</th>
    <th>Outcome</th>
  </tr>
  <tr>
    <td>Start</td>
    <td>n/a</td>
    <td>Load Titles and Main Menu</td>
    <td>Program runs and loads main menu</td>
    <td>PASS</td>
  </tr>
  <tr>
    <td>Main Menu</td>
    <td>"dfg", "6", "0"</td>
    <td>An input error displays a message and reloads Titles and Main Menu</td>
    <td>As expected</td>
    <td>PASS</td>
  </tr>
  <tr>
    <td>Log Practice Option 1.</td>
    <td>"1"</td>
    <td>Clears screen, displays Log Practice info and "Enter to continue"</td>
    <td>As expected</td>
    <td>Pass</td>
    </tr>
  <tr>
    <td>Option 1 - Date Today?</td>
    <td>"dfg","45", "y", "n", "yes", "no", "YES", "NO"</td>
    <td>Requests "y/n" input, incorrect input displays message and "Enter to try again"</td>
    <td>Will except: "y", "n", "yes", "no", "YES", "NO", otherwise error handled as expected</td>
    <td>Pass</td>
  </tr><tr>
    <td>Option 1 - Date Input</td>
    <td>"sdf", "", "7654", "55/34/33"</td>
    <td>Request date input from user, if incorrect format, display error mesage and repeat request</td>
    <td>Input error handled as expected, correct format continues code</td>
    <td>Pass</td>
  <tr><tr>
    <td>Option 1 - Duration Input</td>
    <td>"sdf", "", "';", "555", "1234567890"</td>
    <td>Request input, if > 420 or not int display error and request input again</td>
    <td>Input error handled as expected, correct format continues code</td>
    <td>Pass</td>
  </tr><tr>
    <td>Option 1 - Score Input</td>
    <td>"fgh", "23","0000", "4"</td>
    <td>Request number input between 1 and 10. If number is 0, > 10, or not an number- display error and repeat request<td>
    <td>Input error handled as expected, correct input continues code</td>
    <td>Pass</td>
  </tr><tr>
    <td>Option 1 - Exercises Input</td>
    <td>"String 1234" "Strings, 1234, more strings"</td>
    <td>Input takes any sort of string input from the user, displays it back to the user and continues</td>
    <td>Input acts as intended</td>
    <td>Pass </td>
  </tr><tr>
    <td>Option 1 - Difficulties Input</td>
    <td>"fgh", "45", "", "YES", "No"</td>
    <td>Requires "y/n" input. Will accept any capitalisation of: "y", "n", "yes", "no". Other inputs display an error and repeat request. Yes and No both recieve different confirmation print statements</td>
    <td>Input validation acts as intended</td>
    <td>Pass</td>
  </tr><tr>
    <td>Option 1 - Difficulties Details Input</td>
    <td>"String 1234" "Strings, 1234, more strings"</td>
    <td>Input takes any sort of string input from the user, displays confirmation message and continues</td>
    <td>Input acts as intended</td>
    <td>Pass</td>
  </tr><tr>
    <td>Option 1 - Wins Input</td>
    <td>"fgh", "45", "", "YES", "No"</td>
    <td>Requires "y/n" input. Will accept any capitalisation of: "y", "n", "yes", "no". Other inputs display an error and repeat request. Yes and No both recieve different confirmation print statements</td>
    <td>Input validation acts as intended</td>
    <td>Pass</td>
  </tr><tr>
    <td>Option 1 - Wins Details Input</td>
    <td>"String 1234" "Strings, 1234, more strings"</td>
    <td>Input takes any sort of string input from the user, displays confirmation message and continues</td>
    <td>Input acts as intended</td>
    <td>Pass</td>
  </tr><tr>
    <td>Option 1 - Complete Log Function</td>
    <td>n/a</td>
    <td>Function returns all user inputted variable data, and triggers save_log function</td>
    <td>Function acts as intended</td>
    <td>Pass</td>
  </tr><tr>
    <td>Option 1 - Save Log Function</td>
    <td>"45", "sdfg", "YES", "No", "34f"</td>
    <td>Function asks the user whether they would like to save the log. Requires and validates for y/n input. If yes, log is saved. If no, asks if sure and validates for a second round of y/n resoponse to either save or return to the main menu. </td>
    <td>Function will recieve any capitalisation of "y"/"yes"/"n"/"no", otherwise it will display a message before requesting input again</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 1 - Collate Data Function</td>
    <td>n/a</td>
    <td>Collates all of the user inputs but converting ints to strings and collating in a sigle list variable "data"</td>
    <td>Function works as intended</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 1 - Push Log Data Function</td>
    <td>n/a</td>
    <td>Function takes the "data" variable and saves it via API in the "practice_log" spreadsheet -> "log" worksheet in a new row.</td>
    <td>Function works as intended. Data visible in spreadsheet</td>
    <td>Pass</td>
  </tr>
    <tr>
    <td>Option 2 - Get Insights Function</td>
    <td>"8", "jhjtd", "0", "Enter"</td>
    <td>Function displays the menu for the Get Insights section. Requests menu input choice via a number, validates for correct options and proceeds with relevant code if correct. If incorrect, message is displayed and the menu loads again.</td>
    <td>Function works as intended</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 2 - View Last Log Function</td>
    <td>n/a</td>
    <td>Function pulls most recent log entry from the spreadsheet and worksheet "practice_log" -> "log", and prints each string object in the list individually, finally allowing the user to return to the menu on "Enter"</td>
    <td>Function works as intended</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 2 - View Last Three Logs Function</td>
    <td>n/a</td>
    <td>Function retrieves the three most recent entries in the "practice_log" spreadsheet --> "log" worksheet, and prints the items from the log to the user in turn. When one log has been printed, request user input to continue to the next log. When all three have been printed, user input returns to the Get Insights menu.</td>
    <td>Function works as expected</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 2 - Calculate Average Practice Time Function</td>
    <td>n\a</td>
    <td>Function explains to the user the feature, requests "Enter" input to begin. Retrieves all duration values from the "practice_log" spreadsheet --> "log" worksheet, calculates the average and displays to the user. Requests "Enter" input to return to the menu</td>
    <td>Function works as intended</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 2 - View Exercises Function</td>
    <td>n/a</td>
    <td>Function iterates and prints the list of all exercises data held in the "log" workheet of the "practice_log" spreadsheet. Multiple enteries within a single string are seperated.Requests user "Enter" input to return to the menu</td>
    <td>Function works as intended</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 2 - View Difficulties Function</td>
    <td>n/a</td>
    <td>Function iterates and prints the list of all difficulties data held in the "log" workheet of the "practice_log" spreadsheet. Any "None" values are removed, multiple enteries within a single string are seperated. Requests user "Enter" input to return to the menu</td>
    <td>Function works as expects</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 3 - Submit Practice Ideas Function</td>
    <td>n/a</td>
    <td>Function displays general information and triggers submit_ideas_menu function</td>
    <td>Function works as expected</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 3 - Submit Practice Ideas Menu Function</td>
    <td>"83", "sdfg", "0", "Enter"</td>
    <td>Function recieves input from user. If not valid, displays message and repeats request. If valid, triggers relevant function.</td>
    <td>Fuction works as expected</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 3 - Submit Technical Exercises</td>
    <td>"0", "542", "gfds", "Enter"</td>
    <td>Function requests input from the user for a string. Displays it back to the user and asks whether to save or not. Validates for this choice. If yes, saves to the "practice_log" spreadsheet --> "my-technical-exercises" worksheet, if no returns to the menu</td>
    <td>Function acts and validates reponses as expected</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>Option 3 - Submit Musicicanship Exercises</td>
    <td>"YES", "245g", "Enter", "No"</td>
    <td>Function requests input from the user for a string. Displays it back to the user and asks whether to save or not. Validates for this choice. If yes, saves to the "practice_log" spreadsheet --> "my-technical-exercises" worksheet, if no returns to the menu</td>
    <td>Functions works as intended</td>
    <td>Pass</td>
  </tr>
  Changing click to different subdivisions sequentially
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>

</table>

[<< Back to ReadMe](README.md)