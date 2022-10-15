
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