## Chall description
```
Category: Web
Oh wow, another web app interface for command-line tools that already exist!

This one seems a little busted, though...
```

## Procedure

<img width="1387" height="747" alt="Screenshot 2025-10-05 at 5 50 23 PM" src="https://github.com/user-attachments/assets/445daa24-71f2-42d7-8172-54f9d37ec79a" />

Just watching the syntax in the website, I say, this is yaml deserialisations attack. I started using the payloads:
* `!!python`: this show an error in the backend if there is not input validation
* `!!python/object/apply:time.sleep [10]`: this is like `sleep()` function on SQLi

<img width="1376" height="490" alt="Screenshot 2025-10-05 at 9 44 52 AM" src="https://github.com/user-attachments/assets/cffdbff7-b176-4dd3-aa44-69b5b3bb1d2a" />
<img width="1377" height="489" alt="Screenshot 2025-10-05 at 9 45 05 AM" src="https://github.com/user-attachments/assets/dd06accc-68aa-40ba-a4d3-6189732d32f5" />

<br>

Now, after confirm the vulnerability, I send the command `ls -la .` using this payload `!!python/object/apply:subprocess.check_output [["ls","-la","."]]`. I was able to list all files in the current directory.

<br>

<img width="1407" height="535" alt="Screenshot 2025-10-05 at 9 42 35 AM" src="https://github.com/user-attachments/assets/9c8103ec-ec3c-4234-a489-b499c4b06814" />

<br>

Now is time to recover out flag with the payload `!!python/object/apply:subprocess.check_output [["cat","flag.txt"]]`

<img width="1383" height="506" alt="Screenshot 2025-10-05 at 9 44 26 AM" src="https://github.com/user-attachments/assets/8b37d9e0-e2fe-4b5d-b9a8-7dca55036c52" />

Flag `flag{b692115306c8e5c54a2c8908371a4c72}`
