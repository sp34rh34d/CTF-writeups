## Name: Zimmer Down
#### Author: @sudo_Rem
#### Category: Forensics
#### Difficulty: N/D
#### Description: A user interacted with a suspicious file on one of our hosts.
The only thing we managed to grab was the user's registry hive.
Are they hiding any secrets?

## Procedure
The NTUSER.DAT file stores information related to:
* User activity: Recent files, searches, executed programs.
* Autostart entries: Programs that run at login.
* Typed URLs: Browsing history for Internet Explorer/Edge.
* UserAssist: Tracks GUI-based application execution.
* ShellBags: Tracks user interaction with folders.
* MRU Lists: Most recently used files and registry keys.
* Jump Lists: Recent applications and documents.
* Wireless Network Information: SSIDs of connected Wi-Fi networks.
  
The ```.DAT``` file can shows us some interesting data in shellbag or RecentsDocs, we can see the following data ```VJGSuERgCoVhl6mJg1x87faFOPIqacI3Eby4oP5MyBYKQy5paDF``` and ```d2FmZmxld2FmZmxld2FmZmxld2FmZmxl```

<img width="1279" alt="Screenshot 2025-02-10 at 7 48 11 PM" src="https://github.com/user-attachments/assets/b68ce363-d08a-41c0-9ecd-59c2b78c81db" />

the string ```d2FmZmxld2FmZmxld2FmZmxld2FmZmxl``` is a base64 encoded string and ```VJGSuERgCoVhl6mJg1x87faFOPIqacI3Eby4oP5MyBYKQy5paDF``` is a base62 encoded string

<img width="1343" alt="Screenshot 2025-02-10 at 7 51 26 PM" src="https://github.com/user-attachments/assets/dd6ae6e7-c7a6-412f-9ca1-5f5d28ab3678" />

