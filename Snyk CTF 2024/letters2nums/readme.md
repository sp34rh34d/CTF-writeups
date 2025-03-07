## Name: letters2nums
#### Author: @Soups71
#### Category: rev
#### Difficulty: Medium
#### Description: This is Letters2Nums, a new data encryption format I came up with. Use the attached binary to figure out how to decrypt the encoded flag. 


## Procedure
In this chall we have the following files 
```
├── chall.txt
├── encflag.txt
└── letters2nums.elf
```

using [dogbolt](https://dogbolt.org/) site, we can recover the following code:
```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char v4[48]; // [rsp+20h] [rbp-140h] BYREF
  char v5[264]; // [rsp+50h] [rbp-110h] BYREF
  unsigned __int64 v6; // [rsp+158h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  readFlag("flag.txt", v4);
  c("This is a long and convoluded way to try and hide the flag:", v4, (__int64)v5);
  writeFlag("encflag.txt", v5);
  return 0;
}

__int64 __fastcall writeFlag(const char *a1, _BYTE *a2)
{
  __int16 v2; // ax
  int i; // [rsp+10h] [rbp-10h]
  int v5; // [rsp+14h] [rbp-Ch]
  FILE *stream; // [rsp+18h] [rbp-8h]

  stream = fopen(a1, "w");
  v5 = sl(a2, 0);
  if ( stream )
  {
    for ( i = 0; i < v5; i += 2 )
    {
      v2 = encodeChars(a2[i], a2[i + 1]);
      fprintf(stream, "%d\n", (unsigned int)v2);
    }
    fclose(stream);
  }
  else
  {
    puts("Error opening file.");
  }
  return 0LL;
}

__int64 __fastcall encodeChars(char a1, char a2)
{
  int v2; // eax

  v2 = a1 << 8;
  LOWORD(v2) = a2;
  return (a1 << 8) | (unsigned int)v2;
}

_BYTE *__fastcall c(_BYTE *a1, _BYTE *a2, __int64 a3)
{
  _BYTE *v3; // rax
  int v4; // edx
  _BYTE *v5; // rax
  int v6; // edx
  _BYTE *result; // rax
  int v11; // [rsp+24h] [rbp-4h]

  v11 = 0;
  while ( *a1 )
  {
    v3 = a1++;
    v4 = v11++;
    *(_BYTE *)(v4 + a3) = *v3;
  }
  while ( *a2 )
  {
    v5 = a2++;
    v6 = v11++;
    *(_BYTE *)(v6 + a3) = *v5;
  }
  result = (_BYTE *)(v11 + a3);
  *result = 0;
  return result;
}

```

This program reads a flag from "flag.txt", processes it using a function c(), and writes the transformed result into "encflag.txt" after encoding pairs of characters using encodeChars().

The following code loops through the array to extract every encoded data, ```char a1 = (encoded_values[i] >> 8) & 0xFF;``` Extracts the first (higher) byte and ```char a2 = encoded_values[i] & 0xFF;``` extracts the second (lower) byte. and then print the extracted characters.

```
#include <stdio.h>

int main() {
    int encoded_values[] = {
        21608, 26995, 8297, 29472, 24864, 27759, 28263, 8289, 28260, 8291, 
        28526, 30319, 27765, 25701, 25632, 30561, 31008, 29807, 8308, 29305, 
        8289, 28260, 8296, 26980, 25888, 29800, 25888, 26220, 24935, 14950, 
        27745, 26491, 13154, 12341, 12390, 13665, 14129, 13925, 13617, 25400, 
        14693, 14643, 12851, 25185, 26163, 24887, 25143, 13154, 32000
    };
    
    
    for (int i = 0; i < 50; i++) {
        char a1 = (encoded_values[i] >> 8) & 0xFF;
        char a2 = encoded_values[i] & 0xFF;
        printf("%c%c", a1, a2);
    }
    
    return 0;
}
```

<img width="1638" alt="Screenshot 2025-03-06 at 6 31 03 PM" src="https://github.com/user-attachments/assets/b8328a26-8837-4050-a4a0-34f124bce61a" />


Flag ```flag{3b050f5a716e51c89e9323baf3a7b73b}```

