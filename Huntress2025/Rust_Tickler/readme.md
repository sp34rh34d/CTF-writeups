## Chall description
```
Category: Reverse Engineering
Ooooh Rust! AND tickles? Rusty tickles...?
```

## Procedure
Using IDA, let's start watching the `main` function code, this has a reference to `sub_1400011F0` function.
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char (*v4)(); // [rsp+30h] [rbp-8h] BYREF

  v4 = sub_1400011F0;
  return sub_140002250((__int64)&v4, (__int64)&unk_140007340);
}
```

**sub_1400011F0 function:**\
* Reads or processes a text buffer (probably user input or data).
* Decodes UTF-8 or wide characters.
* Filters certain characters (whitespace, special Unicode, etc.).
* Compares the resulting string with a hardcoded sequence:```7=06*gagg30d03gf2`f5g5dba3c0hhcd2c`4b,```
* Depending on whether it matches or not, it triggers one of two outcomes (success/failure).

```c
char sub_1400011F0()
{
  char v0; // bl
  unsigned __int8 *v1; // rdx
  unsigned __int8 *v2; // r9
  unsigned __int8 *v3; // r8
  char v4; // r11
  unsigned __int8 *v5; // rbx
  unsigned __int8 *v6; // rax
  unsigned int v7; // r11d
  int v8; // r9d
  int v9; // r12d
  int v10; // ebp
  unsigned int v11; // ebx
  char v12; // bl
  unsigned __int8 *v13; // r11
  unsigned int v14; // ebx
  char v15; // bp
  char v16; // r12
  int v17; // r12d
  int v18; // ebp
  unsigned int v19; // ebp
  char result; // al
  _BYTE Buf2[40]; // [rsp+20h] [rbp-F8h] BYREF
  void **v22; // [rsp+50h] [rbp-C8h] BYREF
  char (__fastcall *v23)(__int64, __int64 *); // [rsp+58h] [rbp-C0h]
  __int64 v24; // [rsp+60h] [rbp-B8h]
  char (__fastcall *v25)(__int64, __int64 *); // [rsp+68h] [rbp-B0h]
  void *v26; // [rsp+70h] [rbp-A8h] BYREF
  __int64 v27; // [rsp+78h] [rbp-A0h]
  void *v28; // [rsp+80h] [rbp-98h]
  __int64 v29; // [rsp+88h] [rbp-90h]
  unsigned __int64 v30; // [rsp+90h] [rbp-88h] BYREF
  __int64 v31; // [rsp+98h] [rbp-80h]
  __int64 v32; // [rsp+A0h] [rbp-78h]
  volatile signed __int8 *v33[2]; // [rsp+A8h] [rbp-70h] BYREF
  _QWORD v34[12]; // [rsp+B8h] [rbp-60h] BYREF

  v34[0] = &unk_1400073C8;
  v34[1] = 17;
  v34[2] = &unk_1400073D9;
  v34[3] = 17;
  v22 = (void **)v34;
  v23 = sub_140001820;
  *(_QWORD *)Buf2 = &unk_1400073F0;
  *(_QWORD *)&Buf2[8] = 2;
  *(_QWORD *)&Buf2[32] = 0;
  *(_QWORD *)&Buf2[16] = &v22;
  *(_QWORD *)&Buf2[24] = 1;
  sub_140002000(Buf2);
  v30 = 0;
  v31 = 1;
  v32 = 0;
  v33[0] = (volatile signed __int8 *)sub_140001B60();
  v0 = sub_140001BA0(v33, &v30);
  *(_QWORD *)Buf2 = &unk_140007410;
  *(_QWORD *)&Buf2[8] = 26;
  *(_QWORD *)&Buf2[16] = &unk_14000742A;
  *(_QWORD *)&Buf2[24] = 26;
  v26 = 0;
  v27 = 1;
  v28 = 0;
  v24 = 3758096416LL;
  v22 = &v26;
  v23 = (char (__fastcall *)(__int64, __int64 *))&off_140007398;
  if ( sub_140001820((__int64)Buf2, (__int64 *)&v22) || (v0 & 1) != 0 )
    BUG();
  if ( v26 )
    sub_1400017E0(v27, v26, 1);
  v1 = (unsigned __int8 *)(v31 + v32);
  if ( !v32 )
  {
    v2 = 0;
    v3 = (unsigned __int8 *)v31;
    v6 = 0;
LABEL_30:
    if ( v3 == v1 )
      goto LABEL_56;
    while ( 1 )
    {
      v13 = v1;
      v14 = (char)*(v1 - 1);
      if ( (v14 & 0x80000000) != 0 )
      {
        v15 = *(v1 - 2);
        if ( v15 >= -64 )
        {
          v1 -= 2;
          v18 = v15 & 0x1F;
        }
        else
        {
          v16 = *(v1 - 3);
          if ( v16 >= -64 )
          {
            v1 -= 3;
            v17 = v16 & 0xF;
          }
          else
          {
            v1 -= 4;
            v17 = ((*(v13 - 4) & 7) << 6) | v16 & 0x3F;
          }
          v18 = (v17 << 6) | v15 & 0x3F;
        }
        v14 = (v18 << 6) | v14 & 0x3F;
        if ( v14 - 9 < 5 )
          goto LABEL_34;
      }
      else
      {
        --v1;
        if ( v14 - 9 < 5 )
          goto LABEL_34;
      }
      if ( v14 != 32 )
      {
        if ( v14 < 0x80 )
          goto LABEL_55;
        v19 = v14 >> 8;
        if ( v14 >> 8 > 0x1F )
        {
          if ( v19 == 32 )
          {
            v12 = *((_BYTE *)off_14000A030 + (unsigned __int8)v14) >> 1;
          }
          else
          {
            if ( v19 != 48 )
            {
LABEL_55:
              v2 = &v13[v2 - v3];
              goto LABEL_56;
            }
            v12 = v14 == 12288;
          }
        }
        else if ( v19 )
        {
          if ( v19 != 22 )
            goto LABEL_55;
          v12 = v14 == 5760;
        }
        else
        {
          v12 = *((_BYTE *)off_14000A030 + (unsigned __int8)v14);
        }
        if ( (v12 & 1) == 0 )
          goto LABEL_55;
      }
LABEL_34:
      if ( v3 == v1 )
        goto LABEL_56;
    }
  }
  v2 = 0;
  v3 = (unsigned __int8 *)v31;
  do
  {
    v5 = v3;
    v6 = v2;
    v7 = *v3;
    if ( (v7 & 0x80u) != 0 )
    {
      v8 = v7 & 0x1F;
      v9 = v3[1] & 0x3F;
      if ( (unsigned __int8)v7 <= 0xDFu )
      {
        v3 += 2;
        v7 = v9 | (v8 << 6);
      }
      else
      {
        v10 = (v9 << 6) | v3[2] & 0x3F;
        if ( (unsigned __int8)v7 < 0xF0u )
        {
          v3 += 3;
          v7 = (v8 << 12) | v10;
        }
        else
        {
          v3 += 4;
          v7 = ((v7 & 7) << 18) | (v10 << 6) | v5[3] & 0x3F;
        }
      }
    }
    else
    {
      ++v3;
    }
    v2 = &v6[v3 - v5];
    if ( v7 - 9 >= 5 && v7 != 32 )
    {
      if ( v7 < 0x80 )
        goto LABEL_30;
      v11 = v7 >> 8;
      if ( v7 >> 8 > 0x1F )
      {
        if ( v11 == 32 )
        {
          v4 = *((_BYTE *)off_14000A030 + (unsigned __int8)v7) >> 1;
        }
        else
        {
          if ( v11 != 48 )
            goto LABEL_30;
          v4 = v7 == 12288;
        }
      }
      else if ( v11 )
      {
        if ( v11 != 22 )
          goto LABEL_30;
        v4 = v7 == 5760;
      }
      else
      {
        v4 = *((_BYTE *)off_14000A030 + (unsigned __int8)v7);
      }
      if ( (v4 & 1) == 0 )
        goto LABEL_30;
    }
  }
  while ( v3 != v1 );
  v6 = 0;
  v2 = 0;
LABEL_56:
  v33[0] = (volatile signed __int8 *)&v6[v31];
  v33[1] = (volatile signed __int8 *)(v2 - v6);
  qmemcpy(Buf2, "7=06*gagg30d03gf2`f5g5dba3c0hhcd2c`4b,", 38);
  if ( v2 - v6 == 38 && !memcmp(&v6[v31], Buf2, 0x26u) )
  {
    v26 = &unk_140007444;
    v27 = 21;
    v28 = &unk_140007459;
    v29 = 21;
  }
  else
  {
    v26 = &unk_1400074A0;
    v27 = 27;
    v28 = &unk_1400074BB;
    v29 = 27;
  }
  v22 = &v26;
  v23 = sub_140001820;
  v24 = (__int64)v33;
  v25 = sub_140001010;
  *(_QWORD *)Buf2 = &unk_140007470;
  *(_QWORD *)&Buf2[8] = 3;
  *(_QWORD *)&Buf2[32] = 0;
  *(_QWORD *)&Buf2[16] = &v22;
  *(_QWORD *)&Buf2[24] = 2;
  result = sub_140002000(Buf2);
  if ( v30 )
    return sub_1400017E0(v31, v30, 1);
  return result;
}
```

This mean, our flag is the encoded string ```7=06*gagg30d03gf2`f5g5dba3c0hhcd2c`4b,```
Let's use known plaintext attack using the flag format `flag{` to try to recover the key or part of the key.

```python
def xor(data: bytes, key: bytes) -> bytes:
    return bytes(d ^ key[i % len(key)] for i, d in enumerate(data))
  
  
print(xor(b'7=06*gagg30d03gf2`f5g5dba3c0hhcd2c`4b,',b'flag{'))
```
The output show us the letter `Q` used as key.
```bash
## Output:
b'QQQQQ\x01\r\x06\x00HV\x08QT\x1c\x00^\x01\x01N\x01Y\x05\x05\x1aU\x0fQ\x0f\x13\x05\x08S\x04\x1bR\x0eM'
```

```python

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(d ^ key[i % len(key)] for i, d in enumerate(data))
  
print(xor(b'7=06*gagg30d03gf2`f5g5dba3c0hhcd2c`4b,',b'Q'))
```
```bash
## Output:
b'flag{6066ba5ab67c17d6d530b2a9925c21e3}'
```


