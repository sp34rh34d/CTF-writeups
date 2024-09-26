## Name: Making Baking Pancakes
#### Category: Misc
#### Difficulty: Easy
#### Description: How many layers are on your pancakes?

## Procedure
Connect to remote server with ```nc``` command, this show us the following data:
```
Welcome to the pancake shop!
Pancakes have layers, we need you to get through them all to get our secret pancake mix formula.
This server will require you to complete 1000 challenge-responses.
A response can be created by doing the following:
1. Base64 decoding the challenge once (will output (encoded|n))
2. Decoding the challenge n more times.
3. Send (decoded|current challenge iteration)
Example response for challenge 485/1000: e9208047e544312e6eac685e4e1f7e20|485
Good luck!

Challenge: Vkcxd1lXRkZPVlZXYlhoYVZrWlZlVlJXWkV0aGF6VllWbGh3V21GdGN6QlViVEZPVFRBMVZWcDZVazVoYlUxM1ZGaHdRazFWTlVWVFZEQTl8Mw==
(0/1000) >> 
```

this challenge involves repeatedly decoding a Base64-encoded string and generate the correct response for each challenge iteration. after finishing the decoding iterations, the format should be specified as ```(decoded|current challenge iteration)```.

I have written the following python script for this
```
from pwn import *
import re,base64
context(log_level='debug')
r = remote('chal.pctf.competitivecyber.club',9001)

base64_pattern = r'[A-Za-z0-9+/=]{20,}'
md5_pattern = r'[a-f0-9]{32,32}'

for x in range(1000):
    data = r.recvuntil(b">> ").decode('utf-8')
    match = re.findall(base64_pattern,data)
    chall=""
    try:
        chall = base64.b64decode(match[1])
    except:
        chall = base64.b64decode(match[0])

    chall_data = chall.decode('utf-8').split("|")[0]
    while True:
        try:
            chall_data = base64.b64decode(chall_data)
            md5_match = re.findall(md5_pattern,chall_data.decode('utf-8'))
            if len(md5_match) > 0:
                break            
        except:
            break

    decoder = f"{chall_data.decode('utf-8')}|{x}"
    r.send(decoder)

r.interactive()
```

![2024-09-23_21-11](https://github.com/user-attachments/assets/f8db0fb7-09d9-4b84-bcb5-0ccc044dcb69)


flag ```pctf{store_bought_pancake_batter_fa82370}```
