# Hikvision-Webcam-Enumeration-
Hikvision Webcam Enumeration and Brute-Forcing
Certainly! Below is the updated version of the Hikvision Webcam Enumeration and Brute-Forcing script that reads passwords from a file for brute-forcing. This script will:

Enumerate common Hikvision webcam endpoints.

Brute-force the login page using a list of usernames and passwords from a file.

Updated Python Script: Hikvision Webcam Enumeration and Brute-Forcing with Password File
How the Script Works:
Enumeration:

Checks common Hikvision webcam endpoints (e.g., /System/configurationFile, /ISAPI/Security/userCheck).

Identifies accessible endpoints and potential vulnerabilities (e.g., configuration file access).

Brute-Forcing:

Attempts to brute-force the /ISAPI/Security/userCheck endpoint using a list of usernames and passwords from a file.

Uses threading for faster brute-forcing.

Password File:

Reads passwords from a file (passwords.txt) for brute-forcing.
Prerequisites
Install Required Libraries:

Install the requests library if not already installed:

bash
Copy
pip install requests
Prepare Password File:

Create a text file (passwords.txt) containing a list of passwords to test. For example:
admin
123456
password
1234
4321
Example Usage
Save the script as hikvision_enum_brute.py.

Create a password file (passwords.txt) in the same directory as the script.

Run the script:

bash:
python hikvision_enum_brute.py
The script will:

Enumerate common Hikvision endpoints.

Brute-force the login page using the passwords from the file.

Output Example
[*] Starting enumeration and brute-forcing on 192.168.1.100:80...
[*] Enumerating Hikvision endpoints...
[+] Found endpoint: http://192.168.1.100:80/System/configurationFile
[+] Configuration file may be accessible!
[!] Authentication required: http://192.168.1.100:80/ISAPI/Security/userCheck
[*] Brute-forcing Hikvision login...
[+] Success! Username: admin, Password: 123456
[*] Enumeration and brute-forcing completed.

Disclaimer
This script is for educational purposes only. Use it responsibly and only on systems you own or have explicit permission to test. Unauthorized access to systems is illegal and unethical.



