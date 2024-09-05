## Name: key
#### Category: rev
#### Difficulty: N/A
#### Description: GDB is cool! Ghidra or IDA is helpful

## Procedure
Running the file command into key binary we got the following output: 
```
key: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e88e8f1f53ccc08981b7ee01fb4975fe508d7c45, for GNU/Linux 3.2.0, not stripped
```
I have used the site [dogbolt](https://dogbolt.org) with ```Hex-Rays``` option to analysis the binary.

## main function Content
1) The program prompts the user to input a key with ```printf("Enter the key: ");``` and reads the input using ```__isoc99_scanf("%32s", s);```
2) It checks whether the length of the key is exactly 32 characters ```if ( (unsigned int)strlen(s) == 32 )```
3) For each character in the key, it performs a check where it XORs the character's position ```(i)``` with the corresponding character from the input ```(s[i])``` and multiplies it by ```(i % 2 + 1)``` to generate a value stored in ```v5[i]```
4) It compares ```v5[i]``` with a corresponding pre-determined value stored in the array ```v6```.

```
//----- (00000000000011A9) ----------------------------------------------------
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+8h] [rbp-138h]
  int v5[32]; // [rsp+10h] [rbp-130h]
  int v6[32]; // [rsp+90h] [rbp-B0h]
  char s[40]; // [rsp+110h] [rbp-30h] BYREF
  unsigned __int64 v8; // [rsp+138h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  v6[0] = 67;
  v6[1] = 164;
  v6[2] = 65;
  v6[3] = 174;
  v6[4] = 66;
  v6[5] = 252;
  v6[6] = 115;
  v6[7] = 176;
  v6[8] = 111;
  v6[9] = 114;
  v6[10] = 94;
  v6[11] = 168;
  v6[12] = 101;
  v6[13] = 242;
  v6[14] = 81;
  v6[15] = 206;
  v6[16] = 32;
  v6[17] = 188;
  v6[18] = 96;
  v6[19] = 164;
  v6[20] = 109;
  v6[21] = 70;
  v6[22] = 33;
  v6[23] = 64;
  v6[24] = 32;
  v6[25] = 90;
  v6[26] = 44;
  v6[27] = 82;
  v6[28] = 45;
  v6[29] = 94;
  v6[30] = 45;
  v6[31] = 196;
  printf("Enter the key: ");
  __isoc99_scanf("%32s", s);
  if ( (unsigned int)strlen(s) == 32 )
  {
    for ( i = 0; i < 32; ++i )
    {
      v5[i] = (i % 2 + 1) * (i ^ s[i]);
      if ( v5[i] != v6[i] )
        break;
      if ( i == 31 )
        printf("Success!");
    }
  }
  else
  {
    printf("Denied Access");
  }
  return 0;
}
```

So, we know the encrypted key is ```[67,164,65,174,66,252,115,176,111,114,94,168,101,242,81,206,32,188,96,164,109,70,33,64,32,90,44,82,45,94,45,196]```, from here I wrote the following code to recover the plaintext key

```
flag = [67,164,65,174,66,252,115,176,111,114,94,168,101,242,81,206,32,188,96,164,109,70,33,64,32,90,44,82,45,94,45,196]
out=""
for x in range(32):
    if x % 2 == 0:
        out+=chr( ( x ^ flag[x] ) )
    else:
        out+=chr( ( x ^ flag[x] // 2 ) )

print(out)
```

flag ```CSCTF{u_g0T_it_h0OrAy6778462123}```

### Bonus
Another way to solve this chall is doing a bruteforce, since we know what is the encrypted value, and what is the operation used, we can try to encrypt each char and see if it matches with the encrypted value.

```
flag = [67,164,65,174,66,252,115,176,111,114,94,168,101,242,81,206,32,188,96,164,109,70,33,64,32,90,44,82,45,94,45,196]
chars="CSTF}{0123456789._abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ"
key=""
for i in range(32):
    for char in chars: #try with every value from chars
        var1 = (i % 2 + 1) * (i ^ ord(char)) # encrypt every char with the same operation, (char simulate user input)
        if var1 == flag[i]:  # check if the encrypted value is the same for every value into flag
            key+=char
            break 

print(key)
```
