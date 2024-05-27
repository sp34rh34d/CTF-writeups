## Name: Ring Cycle 2 - Rhinegold
#### Category: Reverse Engineering
#### Difficulty: easy
#### Description: Alberich, a dwarf, created an all-powerful magic ring. NOTE, the plaintext that you provide the binary should be readable English. Reverse engineer the binary to understand what it really does... patching the binary will ultimately give you the wrong answer. 

## Procedure
Running the following command ```file rhinegold``` we got the output ```rhinegold: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a787b10f294e908bd4efa1e92c2989f36df0f96c, for GNU/Linux 3.2.0, not stripped```<br>

We can use ```https://dogbolt.org``` with ```Hex-Rays``` option to recover the binary code.

## rhinegold code 
1) check function takes a string (passphrase) as an argument and verifies if it matches a specific pattern after shuffling.
2) The strcpy(nptr, "TIME") and strtol(nptr, 0LL, 10) part initializes the seed for the random number generator. However, since "TIME" is not a valid number, strtol will return 0. So, srand(0) is effectively called.
3) The for loop shuffles the input string using a fixed seed (0), ensuring a consistent shuffle each time.
4) It then compares the shuffled string to the hardcoded string "cioerosgaenessT ns k urelh oLdTie heri nfdfR".
5) If the strings match, it returns 1; otherwise, it returns 0.

```
__int64 __fastcall check(__int64 a1)
{
  int v1; // eax
  int j; // [rsp+1Ch] [rbp-64h]
  unsigned int seed; // [rsp+20h] [rbp-60h]
  char v5; // [rsp+24h] [rbp-5Ch]
  __int64 i; // [rsp+28h] [rbp-58h]
  char nptr[5]; // [rsp+3Bh] [rbp-45h] BYREF
  char v8[56]; // [rsp+40h] [rbp-40h] BYREF
  unsigned __int64 v9; // [rsp+78h] [rbp-8h]

  v9 = __readfsqword(0x28u);
  strcpy(nptr, "TIME");
  seed = strtol(nptr, 0LL, 10);
  srand(seed);
  for ( i = 45LL; i; --i )
  {
    v1 = rand();
    v5 = *(_BYTE *)(a1 + i);
    *(_BYTE *)(a1 + i) = *(_BYTE *)(a1 + v1 % 46);
    *(_BYTE *)(a1 + v1 % 46) = v5;
  }
  strcpy(v8, "cioerosgaenessT   ns k urelh oLdTie heri nfdfR");
  for ( j = 0; j <= 46; ++j )
  {
    if ( *(_BYTE *)(j + a1) != v8[j] )
      return 0LL;
  }
  return 1LL;
}

//----- (00000000000014F8) ----------------------------------------------------
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
  fgets(s, 47, stdin);
  s[46] = 0;
  if ( (unsigned __int8)check((__int64)s) )
  {
    stream = fopen("rhinegold.txt", "r");
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
<br>

I have emulated the code, I wrote the following C script, and set the input value from ```cioerosgaenessT   ns k urelh oLdTie heri nfdfR``` to ```abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST```, so we can see what char we need to change.

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check(char* input) {
    
    char nptr[] = "TIME";
    int seed = atoi(nptr);

    srand(seed);
    for (int i = 45; i > 0; --i) {
        int v1 = rand();
        int swapIndex = v1 % 46;

        char temp = input[i];
        input[i] = input[swapIndex];
        input[swapIndex] = temp;
    }

    char encrypted_phrase[] = "cioerosgaenessT   ns k urelh oLdTie heri nfdfR";

    for (int j = 0; j <= 46; ++j) {
        if (input[j] != encrypted_phrase[j]){
            printf("Mismatch: user input[%d] = %c, encrypted_phrase[%d] expected = %c\n", j, input[j], j, encrypted_phrase[j]);
            return 0;
        }else{
            printf("match %d\n", input[j]);
        }
    }

    return 1;
}

int main() {
    char staticInput[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST";
    size_t inputLength = strlen(staticInput);

    if (check(staticInput)) {
      printf("Correct!");
        
    } else {
        printf("Wrong passphrase!\n");
    }

    return 0;
}
```

Now, the code shows us the following output<br>

```
Mismatch: user input[0] = S, encrypted_phrase[0] expected = c
```

We have sent the input ```abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST```, now we know the ```S``` value need to be changes to ```c```, now we have ```????????????????????????????????????????????c?```

Run the C script again, now with input ```abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRcT```, we got the following output ``` Mismatch: user input[1] = n, encrypted_phrase[1] expected = i ```, change the ```n``` char to ```i```, and we got the string ```?????????????i??????????????????????????????c?```
<br>

Finally we got the phrase ```This sounds like a Lord of The Rings reference```
<br>

![image](https://github.com/sp34rh34d/CTF-writeups/assets/94752464/2b86f44e-3816-4162-ae12-f1b29693482e)

flag ```flag{a59b300dcc0253601d3faea254c58fdd}```




