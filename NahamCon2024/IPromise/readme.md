## Name: IPromise
#### Category: Reverse Engineering
#### Difficulty: easy
#### Description: Instead of making the next IPhone, I made this challenge. I do make a truthful promise though... 

## Procedure
Run ```file IPromise``` command <br>
Output ```IPromise: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=89878e2c4353d02a9ae4a40d8c831124197d2e30, for GNU/Linux 3.2.0, not stripped```
<br>

I have ran the binary file to check the behavior, and i see the following output
<br>

<img width="892" alt="Screenshot 2024-05-25 at 23 20 38" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/39003baa-031a-4469-9144-9d4bcdbb681a">
<br>

Open the bin file with ```gdb ./IPromise```, and list the functions with command ```info functions```, We can see ```decryptIPromise``` function.
<br>

<img width="503" alt="Screenshot 2024-05-25 at 23 25 27" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/21492609-a4e4-4a0a-9bc7-3244b4689fb6">
<br>

now run ```disassemble main``` command to check the main function code, then add a breakpoint with ```b *main+0``` command
<br>

<img width="628" alt="Screenshot 2024-05-25 at 23 29 25" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/c1fbfd6f-38d4-414f-abfc-c0909205334c">
<br>

then run ```disassemble decryptIPromise```, here we want to know what is the decryptIPromise address, and we can see ```0x0000000000401065```
<br>

<img width="727" alt="Screenshot 2024-05-25 at 23 35 21" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/0d3498d5-131f-4af3-bfa9-b65f168498ac">
<br>

now we can try to jump to ```decryptIPromise``` function, run the bin file with ```r``` command, and gdb will take a break on ```main+0```, from here we can try to jump to ```decryptIPromise``` function, just editing the ```rip``` (instruction pointer) value to ```0x0000000000401065``` then press ```n``` command.
<br>

<img width="801" alt="Screenshot 2024-05-25 at 23 40 38" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/f0a33f5e-415e-49e0-b275-12b8b7202783">
<br>

press enter until you see the flag in rsi value.
<br>

<img width="664" alt="Screenshot 2024-05-25 at 23 42 55" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/ce341ef5-51c8-4369-b9f8-18d30a934e0f">
<br>

flag ```flag{d41d8cd98f00b204e9800998ecf8427e}```


