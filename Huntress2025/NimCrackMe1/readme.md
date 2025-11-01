## Chall description
```
Category: Reverse Engineering
I just really like Nim, okay, I think it's neat.
(Could very well be used by threat actors too, so it's worth getting a feel for some Nimlang reverse engineering!)
```
## Procedure
Opening the `exe` with `gdb`, run `info functions`, we can see the following function `buildEncodedFlag__crackme_u18`.
```bash
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from nimcrackme1.exe...
(gdb) info functions

Non-debugging symbols:
...snip..
0x0000000140010650  mnewString
0x0000000140011540  nimErrorFlag
0x0000000140011e78  buildEncodedFlag__crackme_u18
0x0000000140012883  xorStrings__crackme_u3
0x0000000140012b5f  nimErrorFlag
0x0000000140012b84  main.crackme_u20
0x0000000140012dd3  PreMainInner
0x0000000140012df1  PreMain
0x0000000140012e14  NimMainInner
0x0000000140012e28  NimMain
0x0000000140012e41  main
0x0000000140012e8d  NimMainModule
...snip...
(gdb)
```

This code, load an encoded value into `v10` array.

```C
_QWORD *__fastcall buildEncodedFlag__crackme_u18(_QWORD *a1)
{
  _BYTE *v1; // rdx
  __int64 v3[2]; // [rsp+20h] [rbp-50h] BYREF
  char v4[8]; // [rsp+30h] [rbp-40h] BYREF
  const char *v5; // [rsp+38h] [rbp-38h]
  __int64 v6; // [rsp+40h] [rbp-30h]
  const char *v7; // [rsp+48h] [rbp-28h]
  __int16 v8; // [rsp+50h] [rbp-20h]
  __int64 v9; // [rsp+60h] [rbp-10h] BYREF
  _BYTE *v10; // [rsp+68h] [rbp-8h]

  v5 = "buildEncodedFlag";
  v7 = "C:\\CTF\\nimcrackme1\\crackme.nim";
  v6 = 0i64;
  v8 = 0;
  nimFrame_8(v4);
  v6 = 13i64;
  v7 = "C:\\CTF\\nimcrackme1\\crackme.nim";
  mnewString(v3, 38i64);
  v9 = v3[0];
  v10 = (_BYTE *)v3[1];
  v6 = 14i64;
  if ( v3[0] > 0 )
  {
    nimPrepareStrMutationV2(&v9);
    v10[8] = 40;
    v6 = 15i64;
    if ( v9 > 1 )
    {
      nimPrepareStrMutationV2(&v9);
      v10[9] = 5;
      v6 = 16i64;
      if ( v9 > 2 )
      {
        nimPrepareStrMutationV2(&v9);
        v10[10] = 12;
        v6 = 17i64;
        if ( v9 > 3 )
        {
          nimPrepareStrMutationV2(&v9);
          v10[11] = 71;
          v6 = 18i64;
          if ( v9 > 4 )
          {
            nimPrepareStrMutationV2(&v9);
            v10[12] = 18;
            v6 = 19i64;
            if ( v9 > 5 )
            {
              nimPrepareStrMutationV2(&v9);
              v10[13] = 75;
              v6 = 20i64;
              if ( v9 > 6 )
              {
                nimPrepareStrMutationV2(&v9);
                v10[14] = 21;
                v6 = 21i64;
                if ( v9 > 7 )
                {
                  nimPrepareStrMutationV2(&v9);
                  v10[15] = 92;
                  v6 = 22i64;
                  if ( v9 > 8 )
                  {
                    nimPrepareStrMutationV2(&v9);
                    v10[16] = 9;
                    v6 = 23i64;
                    if ( v9 > 9 )
                    {
                      nimPrepareStrMutationV2(&v9);
                      v10[17] = 18;
                      v6 = 24i64;
                      if ( v9 > 10 )
                      {
                        nimPrepareStrMutationV2(&v9);
                        v10[18] = 23;
                        v6 = 25i64;
                        if ( v9 > 11 )
                        {
                          nimPrepareStrMutationV2(&v9);
                          v10[19] = 85;
                          v6 = 26i64;
                          if ( v9 > 12 )
                          {
                            nimPrepareStrMutationV2(&v9);
                            v10[20] = 9;
                            v6 = 27i64;
                            if ( v9 > 13 )
                            {
                              nimPrepareStrMutationV2(&v9);
                              v10[21] = 75;
                              v6 = 28i64;
                              if ( v9 > 14 )
                              {
                                nimPrepareStrMutationV2(&v9);
                                v10[22] = 66;
                                v6 = 29i64;
                                if ( v9 > 15 )
                                {
                                  nimPrepareStrMutationV2(&v9);
                                  v10[23] = 8;
                                  v6 = 30i64;
                                  if ( v9 > 16 )
                                  {
                                    nimPrepareStrMutationV2(&v9);
                                    v10[24] = 85;
                                    v6 = 31i64;
                                    if ( v9 > 17 )
                                    {
                                      nimPrepareStrMutationV2(&v9);
                                      v10[25] = 90;
                                      v6 = 32i64;
                                      if ( v9 > 18 )
                                      {
                                        nimPrepareStrMutationV2(&v9);
                                        v10[26] = 69;
                                        v6 = 33i64;
                                        if ( v9 > 19 )
                                        {
                                          nimPrepareStrMutationV2(&v9);
                                          v10[27] = 88;
                                          v6 = 34i64;
                                          if ( v9 > 20 )
                                          {
                                            nimPrepareStrMutationV2(&v9);
                                            v10[28] = 68;
                                            v6 = 35i64;
                                            if ( v9 > 21 )
                                            {
                                              nimPrepareStrMutationV2(&v9);
                                              v10[29] = 87;
                                              v6 = 36i64;
                                              if ( v9 > 22 )
                                              {
                                                nimPrepareStrMutationV2(&v9);
                                                v10[30] = 69;
                                                v6 = 37i64;
                                                if ( v9 > 23 )
                                                {
                                                  nimPrepareStrMutationV2(&v9);
                                                  v10[31] = 119;
                                                  v6 = 38i64;
                                                  if ( v9 > 24 )
                                                  {
                                                    nimPrepareStrMutationV2(&v9);
                                                    v10[32] = 93;
                                                    v6 = 39i64;
                                                    if ( v9 > 25 )
                                                    {
                                                      nimPrepareStrMutationV2(&v9);
                                                      v10[33] = 84;
                                                      v6 = 40i64;
                                                      if ( v9 > 26 )
                                                      {
                                                        nimPrepareStrMutationV2(&v9);
                                                        v10[34] = 68;
                                                        v6 = 41i64;
                                                        if ( v9 > 27 )
                                                        {
                                                          nimPrepareStrMutationV2(&v9);
                                                          v10[35] = 92;
                                                          v6 = 42i64;
                                                          if ( v9 > 28 )
                                                          {
                                                            nimPrepareStrMutationV2(&v9);
                                                            v10[36] = 69;
                                                            v6 = 43i64;
                                                            if ( v9 > 29 )
                                                            {
                                                              nimPrepareStrMutationV2(&v9);
                                                              v10[37] = 19;
                                                              v6 = 44i64;
                                                              if ( v9 > 30 )
                                                              {
                                                                nimPrepareStrMutationV2(&v9);
                                                                v10[38] = 89;
                                                                v6 = 45i64;
                                                                if ( v9 > 31 )
                                                                {
                                                                  nimPrepareStrMutationV2(&v9);
                                                                  v10[39] = 91;
                                                                  v6 = 46i64;
                                                                  if ( v9 > 32 )
                                                                  {
                                                                    nimPrepareStrMutationV2(&v9);
                                                                    v10[40] = 71;
                                                                    v6 = 47i64;
                                                                    if ( v9 > 33 )
                                                                    {
                                                                      nimPrepareStrMutationV2(&v9);
                                                                      v10[41] = 66;
                                                                      v6 = 48i64;
                                                                      if ( v9 > 34 )
                                                                      {
                                                                        nimPrepareStrMutationV2(&v9);
                                                                        v10[42] = 94;
                                                                        v6 = 49i64;
                                                                        if ( v9 > 35 )
                                                                        {
                                                                          nimPrepareStrMutationV2(&v9);
                                                                          v10[43] = 89;
                                                                          v6 = 50i64;
                                                                          if ( v9 > 36 )
                                                                          {
                                                                            nimPrepareStrMutationV2(&v9);
                                                                            v10[44] = 22;
                                                                            v6 = 51i64;
                                                                            if ( v9 > 37 )
                                                                            {
                                                                              nimPrepareStrMutationV2(&v9);
                                                                              v10[45] = 93;
                                                                            }
...snip...
```

Let's extract those encoded values, and convert to char.

```python
flag = [40,5,12,71,18,75,21,92,9,18,23,85,9,75,66,8,85,90,69,88,68,87,69,119,93,84,68,92,69,19,89,91,71,66,94,89,22,93]
out = []

for x in flag:
  out.append(chr(x))

print(''.join(out))
```
```bash
## Output:

(GK\	U	KBUZEXDWEw]TD\EY[GB^Y]
```

We know the flag format is `flag{`, we can try a known plaintext attack using this, the output show us an interesting output `Nim i` for `flag{` as key, this reveals part of the key.

```python
flag = [40,5,12,71,18,75,21,92,9,18,23,85,9,75,66,8,85,90,69,88,68,87,69,119,93,84,68,92,69,19,89,91,71,66,94,89,22,93]

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(d ^ key[i % len(key)] for i, d in enumerate(data))
  
out = []

for x in flag:
  out.append(chr(x))
  
print(xor(''.join(out).encode(),b'flag{'))
```
```bash
## Output:
b'Nim i-y=niq9h,9n9;"#";$\x10&2(="h?7&%%?z<'
```

Let's start with strings on `exe`, let's grep `Nim i`, this show us `Nim is not for malware!`.
```bash
strings nimcrackme1.exe | grep "Nim i"
@Nim is not for malware!
```
Modify the python code to decrypt the flag using the key `Nim is not for malware!`
```python
flag = [40, 5,12,71,18,75,21,92,9,18,23,85,9,75,66,8,85,90,69,88,68,87,69,119,93,84,68,92,69,19,89,91,71,66,94,89,22,93]

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(d ^ key[i % len(key)] for i, d in enumerate(data))
  
out = []

for x in flag:
  out.append(chr(x))
  
print(xor(''.join(out).encode(),b'Nim is not for malware!'))
```
```bash
## Output
b'flag{852ff73f9be462962d949d563743b86d}'
```

