# XSS Vulnerability Checker
## This is a simple tool that allows you to check if a website is vulnerable to XSS attacks. It works by injecting test payloads into input fields and script tags on the webpage, and checking if these payloads are reflected back in the HTTP response.

# Installation
- Clone this repository to your local machine
```git clone https://github.com/TheGodSkill/XSS-Checker```
- Install the required Python packages using pip install -r requirements.txt
- Run the script using python checker.py

# Usage
Enter the URL of the website you want to check in the text field
Click the "Check" button to initiate the XSS vulnerability check
If the website is vulnerable to XSS attacks, the background of the GUI will turn green and a list of vulnerable input fields and script tags will be displayed. If the website is not vulnerable, the background will turn red and a message indicating that the website is not vulnerable will be displayed.
## Contributing
Contributions are welcome! If you have any suggestions or improvements to the code, feel free to open a pull request.
