## Name: Finder Fee
#### Author: @JohnHammond
#### Category: Warmups
#### Difficulty: N/D
#### Description: You gotta make sure the people who find stuff for you are rewarded well! Escalate your privileges and uncover the flag.txt in the finder user's home directory.

## Procedure
We have a remote intance, and the chall gives us the creds for ssh 
```
Connect with:

# Password is "userpass"
ssh -p 30919 user@challenge.ctf.games
```
the flag.txt file is storage at ```/home/finder/flag.txt```, we need to find the way to escalate privileges and read the flag. I have started to enumerate the machine looking for an interesting binary file that allows us to do the privalege escalation. use the command ```find / -perm /4000 -type f 2>/dev/null```

![image](https://github.com/user-attachments/assets/cbd82819-629d-4116-863e-4604802421a1)

After check every single bin in the list, no luck :(

I have checked the file ```/etc/group``` and i saw the group ```finder```.

![image](https://github.com/user-attachments/assets/05eb2b47-62e1-4e37-9dd2-1f79f12025f0)

I did enumeration again but looking for any finder binary with command ```find / -group finder 2>/dev/null```

![image](https://github.com/user-attachments/assets/e8937dfa-0b21-42c2-aa99-3498301de356)

interesting binary file ```/usr/bin/find``` and the flag is under finder user, so this is our binary, find binary allows us to run any command as arg, so we can try to read the flag content using ```/usr/bin/find```, run the following command ```find /home/finder -name flag.txt -exec cat {} \; 2>/dev/null```

![image](https://github.com/user-attachments/assets/1e32e387-f5f9-4aa3-8477-d71bdb1c808d)

flag ```flag{63a10f0440218364424b20f9ddf6ad39}```
