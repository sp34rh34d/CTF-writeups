
## Name: Time will tell
#### Author: @aenygma
#### Category: Misc
#### Difficulty: N/D
#### Description: A side channel timing attack.
Figure out the password in 90 seconds before connection terminates.
The password is dynamic and changes every connection session.

NOTE, the password is eight characters long and will be hexadecimal.

## Procedure
The chall gives us the following python code

```
#!/usr/bin/env python
# pylint: disable=C0200
"""
side-channel timing attack
"""

import os
import secrets
import time

# Length of password. Can be tuned if folks are solving it quickly
PASSWORD_LEN = 4
# Length of time to sleep when guess entry is correct. "simulates compute time "
SIMULATE_COMPUTE_TIME = 0.1


def generate_password() -> str:
    """
    generate a random password at start up
    """
    tmp = secrets.token_hex(PASSWORD_LEN).lower()
    # with open("dump", 'w') as fh:
    #     fh.write(tmp)
    return tmp


def read_flag() -> str:
    """
    read flag from file on disk
    """
    with open("flag", "r", encoding="ascii") as file_handle:
        data = file_handle.read()
    return data


def do_heavy_compute() -> None:
    """
    simulates some compute
    """
    time.sleep(SIMULATE_COMPUTE_TIME)


def check_guess(guess, realdeal) -> bool:
    """
    validate if the given guess matches what's known
    """
    if len(guess) != len(realdeal):
        #print(len(guess), len(realdeal))
        return False
    do_heavy_compute()
    for idx in range(len(guess)):
        if guess[idx] == realdeal[idx]:
            do_heavy_compute()
        else:
            return False
    return True


def main():
    """
    le big mac
    """
    timeout = os.getenv("CHALL_TIMEOUT")
    # Create random password
    secret_password = generate_password()
    print("Figure out the password to get the flag.")
    print("The password is dynamic and changes every connection session.")
    print(f"The connection will terminate in {timeout} seconds.")

    while True:
        guess = input(": ")
        if check_guess(guess, secret_password):
            flag = read_flag()
            print(f"Well done! Here's your flag: {flag}")
            continue
        print("Incorrect. Try again.")


if __name__ == "__main__":
    main()
```

### app.py content
1) Password of PASSWORD_LEN (4) bytes is generated using secrets.token_hex, which creates a random hexadecimal password. The password is different for each connection as it's generated dynamically.
2) read_flag This function reads a flag from a file. If the correct password is guessed, the flag is displayed to the user.
3) To simulate computation and add a delay, time.sleep(SIMULATE_COMPUTE_TIME) is used. This delay (0.1 seconds) emulates the time required for processing correct parts of the password.
4) For each character guessed correctly, an additional delay (do_heavy_compute()) is applied, leading to cumulative delays as more characters are guessed correctly in sequence.
5) If the guess is incorrect at any character, the function returns False immediately, revealing timing differences based on how many characters match from the start.
6) The main function runs the guessing loop, generating a new password for each session and prompting the user for guesses.


This code is susceptible to a timing attack: 
* Sequential Checking with Delay: check_guess iterates through each character in guess and applies do_heavy_compute() (0.1 seconds) if the guessed character matches the actual password character at that position.
* Early Exit on Mismatch: The function exits as soon as a mismatch is found. This reveals timing information, as a longer delay indicates more characters matched correctly at the start of the password.



