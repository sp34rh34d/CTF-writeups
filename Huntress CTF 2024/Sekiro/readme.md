
## Name: Sekiro
#### Author: HuskyHacks
#### Category: Misc
#### Difficulty: N/D
#### Description: お前はもう死んでいる = you are dead

## Procedure
The chall give us a remote instance, after connect to it, we can see it asks us for a move, if we dont send our mov in 10 seconds it will close the connection.
<img width="1376" alt="Screenshot 2024-11-02 at 1 00 20 PM" src="https://github.com/user-attachments/assets/bd50ea2c-0826-4ea3-a8a4-b8731dfa2532">

We need map every move, in my case i did the following:
* strike = block
* advance = retreat
* block = advance
* retreat = strike

I wrote the following python code using pwntool to capture every opponent move, and send my move.
```
from pwn import *
context(log_level="debug")
r = remote('challenge.ctf.games',31053)

while True:
    try:
        res = r.recvuntil(b"Your move:")
        if b"strike" in res:
            print("oponent move is strike")
            r.send(b"block")
        elif b"advance" in res:
            print("oponent move is advance")
            r.send(b"retreat")
        elif b"retreat" in res:
            print("oponent move is retreat")
            r.send(b"strike")
        elif b"block" in res:
            print("oponent move is block")
            r.send(b"advance")
        else:
            print("no move")
            break
    except:
        pass

r.interactive()
```

after some seconds, i got the flag.
<img width="823" alt="Screenshot 2024-10-25 at 9 53 12 AM" src="https://github.com/user-attachments/assets/b983fd9e-4965-434f-8d03-a932b7443ab1">
