## Name: Plantopia
#### Author: @HuskyHacks
#### Category: Web
#### Difficulty: N/D
#### Description: Plantopia is our brand new, cutting edge plant care management website! Built for hobbiests and professionals alike, it's your one stop shop for all plant care management.

Please perform a penetration test ahead of our site launch and let us know if you find anything.

Username: testuser
Password: testpassword

## Procedure
We have logged in the website, this does a redirect to ```/dashboard```, but the checking into the headers, we can see a simple base64 in the cookie.

![Screenshot 2024-10-25 at 11 51 11 AM](https://github.com/user-attachments/assets/126669ab-9306-4e09-a3c8-9b6ff5c228e8)

running the command ```echo "dGVzdHVzZXIuMC4xNzI5ODgyMjQ5" | base64 -d``` show the following output ```testuser.0.1729882249```, we can try to escalate privileges creating our own cookie or just try to modify our current cookie. This is our available options in dashboard page.

![Screenshot 2024-10-25 at 12 06 31 PM](https://github.com/user-attachments/assets/cc71dd08-ab70-443f-83ad-fae62737d687)


We change the value ```0``` to ```1``` in our cookie, then just create our new coockie running the command ```echo -n "testuser.1.1729882249" | base64```, output ```dGVzdHVzZXIuMS4xNzI5ODgyMjQ5```

After out modified cookie, we can see 2 new options available, ```admin``` and ```logs```.

![Screenshot 2024-10-25 at 12 06 40 PM](https://github.com/user-attachments/assets/df059202-d9d6-4ca1-8b7d-e3b57b8f5b66)

With admin privilege we can modify every item description, and Logs page shows us every action executed.
![Screenshot 2024-10-25 at 12 07 00 PM](https://github.com/user-attachments/assets/38a6a74e-a244-4de2-8d97-6200ea0740e3)
![Screenshot 2024-10-25 at 12 07 19 PM](https://github.com/user-attachments/assets/e24449c5-c8fb-4117-87d0-417c0e8f8e88)

So, we can see the command ```/usr/sbin/sendmail``` on item description, i was trying to replace the command but no luck. then i just added ```|``` to insert a second command ```/usr/sbin/sendmail -t | ls```, so when the action is executed, the ```Log``` page shows us the following

![Screenshot 2024-10-25 at 12 13 11 PM](https://github.com/user-attachments/assets/f5f9209b-72bc-4a6b-bb65-dab5029ce459)

at this point, we just need to run the command ```/usr/sbin/sendmail -t | cat flag.txt``` to get our flag

![Screenshot 2024-10-25 at 12 14 04 PM](https://github.com/user-attachments/assets/4f04ec3d-39ba-4cce-8f69-435aed4b2b36)


flag ```flag{c29c4d53fc432f7caeb573a9f6eae6c6}```
