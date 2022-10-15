
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
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr><tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

[<< Back to ReadMe](README.md)