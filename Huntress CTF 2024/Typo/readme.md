## Name: Typo
#### Author: @JohnHammond
#### Category: Misc
#### Difficulty: N/D
#### Description: Gosh darnit, I keep entering a typo in my Linux command prompt!

## Procedure
In this chall, we have to connect to remote ssh server using creds

```
Password is "userpass"
ssh -p 30179 user@challenge.ctf.games
```

After connect to remote server, show us an ascii art and then disconnect our ssh sesion, no chance to type any. 

<img width="1100" alt="Screenshot 2024-10-25 at 9 17 18 AM" src="https://github.com/user-attachments/assets/1c50b26b-c8b9-43c5-83a7-59414077894c">

ssh allows us to send linux commands as args using the syntax  ```ssh user@remoteserver 'command'```, using this we can read the flag.

<img width="534" alt="Screenshot 2024-10-25 at 9 17 36 AM" src="https://github.com/user-attachments/assets/bc97fc05-3041-4da8-b72d-11f800d59679">

<img width="614" alt="Screenshot 2024-10-25 at 9 18 03 AM" src="https://github.com/user-attachments/assets/5354cbb7-5d2d-41c5-bb27-eb4b47f90ed9">

flag ```flag{36a0354fbf59df454596660742bf09eb}```
