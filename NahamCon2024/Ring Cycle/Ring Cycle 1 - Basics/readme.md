## Name: Ring Cycle 1 - Basics
#### Category: Reverse Engineering
#### Difficulty: easy
#### Description: Let us start with a simple one and see if you can break into this vault. NOTE, the plaintext that you provide the binary should be readable English. Reverse engineer the binary to understand what it really does... patching the binary will ultimately give you the wrong answer. 

## Procedure
Running the command ```file basisc``` we got the output ```basics: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1b62152cc3b6a13c30959ac8673ded9a80bd1140, for GNU/Linux 3.2.0, not stripped```<br>

we can use ```https://dogbolt.org``` tool with ```Hex-Rays``` option to get the binary code.

## Basic code content
1) The check function takes an input string (a1) and performs several transformations on it to compare it with a hardcoded string s2
2) s2 = ```eyrnou jngkiaccre af suryot arsto tdyea rre aouY```.

I can see a [transposition cipher](https://en.wikipedia.org/wiki/Transposition_cipher) used in s2 string

```
_BOOL8 __fastcall check(__int64 a1)
{
  char v2; // [rsp+11h] [rbp-8Fh]
  char v3; // [rsp+12h] [rbp-8Eh]
  char v4; // [rsp+13h] [rbp-8Dh]
  int i; // [rsp+14h] [rbp-8Ch]
  int j; // [rsp+18h] [rbp-88h]
  int k; // [rsp+1Ch] [rbp-84h]
  char s1[64]; // [rsp+20h] [rbp-80h] BYREF
  char s2[56]; // [rsp+60h] [rbp-40h] BYREF
  unsigned __int64 v10; // [rsp+98h] [rbp-8h]

  v10 = __readfsqword(0x28u);
  for ( i = 0; i <= 24; ++i )
  {
    v4 = *(_BYTE *)(i + a1);
    s1[i] = *(_BYTE *)(50 - i - 1LL + a1);
    s1[49 - i] = v4;
  }
  for ( j = 0; j <= 49; ++j )
  {
    v3 = s1[j];
    s1[j] = s1[j + 1];
    s1[j + 1] = v3;
  }
  s1[49] = 0;
  for ( k = 0; k <= 47; k += 2 )
  {
    v2 = s1[k];
    s1[k] = s1[k + 1];
    s1[k + 1] = v2;
  }
  strcpy(s2, "eyrnou jngkiaccre af suryot arsto  tdyea rre aouY");
  return strcmp(s1, s2) == 0;
}

//----- (0000000000001537) ----------------------------------------------------
int __fastcall main(int argc, const char **argv, const char **envp)
{
  size_t v4; // rax
  int i; // [rsp+4h] [rbp-6Ch]
  FILE *stream; // [rsp+8h] [rbp-68h]
  __int64 nmemb; // [rsp+10h] [rbp-60h]
  void *ptr; // [rsp+18h] [rbp-58h]
  char v9[16]; // [rsp+20h] [rbp-50h] BYREF
  char s[56]; // [rsp+30h] [rbp-40h] BYREF
  unsigned __int64 v11; // [rsp+68h] [rbp-8h]

  v11 = __readfsqword(0x28u);
  init();
  printf("What is the passphrase of the vault?\n> ");
  fgets(s, 50, stdin);
  if ( check((__int64)s) )
  {
    stream = fopen("basics.txt", "r");
    if ( !stream )
      return -1;
    fseek(stream, 0LL, 2);
    nmemb = ftell(stream);
    fseek(stream, 0LL, 0);
    ptr = calloc(nmemb, 1uLL);
    if ( !ptr )
      return -1;
    fread(ptr, 1uLL, nmemb, stream);
    fclose(stream);
    printf((const char *)ptr);
    v4 = strlen(s);
    MD5(s, v4, v9);
    printf("flag{");
    for ( i = 0; i <= 15; ++i )
      printf("%02x", (unsigned __int8)v9[i]);
    puts("}");
  }
  else
  {
    puts("Wrong passphrase!");
  }
  return 0;
}
```
I did it manually 💀, first apply a reverse string, and we have ```Yuoa err aeydt otsra toyrus fa erccaikgnj uonrye``` string<br>
from here we can see ```Yuoa err``` just change ```uo``` to ```ou``` and we have ```Youa err```. then we can do the same for ```'space' and a ``` and we have ```You aerr```, same for ```er``` to ```re``` and we have ```You arer```.
finally string ```You are ready to start your safe cracking journey```
<br>

<img width="697" alt="Screenshot 2024-05-26 at 22 15 31" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/b34b2926-ac70-480c-a467-d763f5212dd9">

flag ```flag{8562e979f1f754537a4e872cc20a73e8} ```





