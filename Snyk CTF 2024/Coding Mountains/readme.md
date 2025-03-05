## Name: 1200 Transmissions
#### Author: @Soups71
#### Category: scripting
#### Difficulty: easy
#### Description: I like mountains and I like coding, so I made this game. I hope you also like both of those things, or else you probably won't have a ton of fun... 



## Procedure
This chall is about test your scripting skill, we have a json file, it asks for a specific value from the json file and we have to find the right value and send it with the right format, I have to say that was not funy.

```
from pwn import *

datasss =[
    {
        "name": "Mount Everest",
        "height": "29,032",
        "first": "1953"
    },
    {
        "name": "K2",
        "height": "28,251",
        "first": "1954"
    },
    {
        "name": "Kangchenjunga",
        "height": "28,169",
        "first": "1955"
    },
...snip...

context(log_level='debug')
io = remote("challenge.ctf.games", 30577)
io.sendlineafter(b"(Y/n): ", b"Y")

continuar = True
cont = 0
while continuar:
    res = io.recvuntil(b": ").replace(b"Awesome, good luck!", b"").replace(b"What is the height and first ascent year of ", b"").replace(b"Correct!\n",b"").strip()
    cont=cont+1
    if cont>50:
        break
    if res:
        name_value = res.decode('utf-8').replace(":", "").strip()
        print(f"Received: {name_value}")
    
        for x in datasss:
            name_data = x['name']
            if name_value == name_data:
                height = x['height']
                first = x['first']
                io.send(f"{height.replace(",","")},{first}\n")
                found = True
                break
print(io.recvall())
io.interactive()
```

<img width="1210" alt="Screenshot 2025-03-05 at 8 12 14 AM" src="https://github.com/user-attachments/assets/9979a512-b819-42d0-9876-fe4827f1b2fc" />

flag ```flag{33e043f76c3ba0fe9265749dbe650940}```

