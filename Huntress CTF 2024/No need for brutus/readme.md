## Name: No need for Brutus
#### Author: @aenygma
#### Category: Cryptography
#### Difficulty: N/D
#### Description: A simple message for you to decipher:

squiqhyiiycfbudeduutvehrhkjki

Submit the original plaintext hashed with MD5, wrapped between the usual flag format: flag{}

Ex: If the deciphered text is "hello world", the MD5 hash would be 5eb63bbbe01eeed093cb22bb8f5acdc3, and the flag would be flag{5eb63bbbe01eeed093cb22bb8f5acdc3}.

## Procedure
The cipher text is ```squiqhyiiycfbudeduutvehrhkjki```, watching this made me think on transportation or substitution cipher, yes a classic cipher was used here, just copy the text and use Cyberchef, I have started with ```rot13 bruteforce``` module, that was enough to get the plaintext.

<img width="1340" alt="Screenshot 2025-02-12 at 7 42 09 AM" src="https://github.com/user-attachments/assets/1b0431a4-f380-45dc-aed8-477b18c865f9" />

The just run ``` echo -n "caesarissimplenoneedforbrutus" | md5 ``` to recover the flag.

flag ```flag{c945bb2173e7da5a292527bbbc825d3f}```
