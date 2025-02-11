## Name: Zimmer Down
#### Author: @sudo_Rem
#### Category: Forensics
#### Difficulty: N/D
#### Description: A user interacted with a suspicious file on one of our hosts.
The only thing we managed to grab was the user's registry hive.
Are they hiding any secrets?

## Procedure
the ```.DAT``` file can shows us some interesting data with shellbag or RecentsDocs, we can see the following data ```VJGSuERgCoVhl6mJg1x87faFOPIqacI3Eby4oP5MyBYKQy5paDF``` and ```d2FmZmxld2FmZmxld2FmZmxld2FmZmxl```

<img width="1279" alt="Screenshot 2025-02-10 at 7 48 11 PM" src="https://github.com/user-attachments/assets/b68ce363-d08a-41c0-9ecd-59c2b78c81db" />

the string ```d2FmZmxld2FmZmxld2FmZmxld2FmZmxl``` is a base64 encoded string and ```VJGSuERgCoVhl6mJg1x87faFOPIqacI3Eby4oP5MyBYKQy5paDF``` is a base62 encoded string

<img width="1343" alt="Screenshot 2025-02-10 at 7 51 26 PM" src="https://github.com/user-attachments/assets/dd6ae6e7-c7a6-412f-9ca1-5f5d28ab3678" />

