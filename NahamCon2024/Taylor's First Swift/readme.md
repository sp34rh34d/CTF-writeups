## Name: Taylor's First Swift
#### Category: Reverse Engineering
#### Difficulty: easy
#### Description: OMG did you hear that they named a programming language after Taylor Swift? 

## Procedure
I have checked the bin file running ```file taylor``` command.<br>
output ```taylor: Mach-O 64-bit executable arm64```
<br>

We take a look to code, I have used ```https://dogbolt.org ``` with ```Hex-Rays``` option.
<br>

## Taylor code content
1) The input String is processed to get its UTF-8 view.
2) The UTF-8 view is passed to an array initializer, creating an array of UInt8.
3) A constant array with the characters ```swifties!``` is created using _allocateUninitializedArray.
4) The input String (in its UTF-8 form) is XOR encrypted with the constant array ```swifties!```.
5) The encrypted string is compared with a hardcoded base64 string ```FRsIAQ8PVBUVEREIVERbBkURFkUIBxVQVkAYFxJfV0FYVkIVQgo=```.

```
Swift::Bool __swiftcall flagCheck(_:)(Swift::String a1)
{
  __int64 v1; // x1
  __int64 v2; // x1
  Swift::OpaquePointer v3; // x0
  _BYTE *v4; // x1
  Swift::String v5; // kr00_16
  __int64 v6; // x1
  __int64 v7; // x0
  void *v8; // x1
  void *object; // [xsp+8h] [xbp-C8h]
  __int64 countAndFlagsBits; // [xsp+10h] [xbp-C0h]
  void *rawValue; // [xsp+18h] [xbp-B8h]
  Swift::OpaquePointer v13; // [xsp+20h] [xbp-B0h]
  __int64 v14; // [xsp+50h] [xbp-80h]
  __int64 v15; // [xsp+58h] [xbp-78h]
  __int64 v16; // [xsp+68h] [xbp-68h]
  char v17; // [xsp+74h] [xbp-5Ch]
  __int64 v18[2]; // [xsp+78h] [xbp-58h] BYREF
  Swift::String v19; // [xsp+88h] [xbp-48h]
  __int64 v20[3]; // [xsp+98h] [xbp-38h] BYREF
  __int64 v21[2]; // [xsp+B0h] [xbp-20h] BYREF
  Swift::String v22; // [xsp+C0h] [xbp-10h]

  countAndFlagsBits = a1._countAndFlagsBits;
  object = a1._object;
  v22 = a1;
  v21[0] = ((__int64 (*)(void))String.utf8.getter)();
  v21[1] = v1;
  lazy protocol witness table accessor for type String.UTF8View and conformance String.UTF8View();
  v16 = Array.init<A>(_:)(v21, &type metadata for UInt8, &type metadata for String.UTF8View);
  v20[2] = v16;
  v20[0] = String.utf8.getter(countAndFlagsBits, object);
  v20[1] = v2;
  v13._rawValue = (void *)Array.init<A>(_:)(v20, &type metadata for UInt8, &type metadata for String.UTF8View);
  v3._rawValue = (void *)_allocateUninitializedArray<A>(_:)(9LL, &type metadata for UInt8);
  *v4 = 115;   // s
  v4[1] = 119; // w
  v4[2] = 105; // i
  v4[3] = 102; // f
  v4[4] = 116; // t
  v4[5] = 105; // i
  v4[6] = 101; // e
  v4[7] = 115; // s
  v4[8] = 33;  // !
  _finalizeUninitializedArray<A>(_:)();
  rawValue = v3._rawValue;
  v5 = xorEncrypt(_:_:)(v13, v3);
  swift_bridgeObjectRelease(rawValue);
  swift_bridgeObjectRelease(v13._rawValue);
  v19 = v5;
  v18[0] = String.utf8.getter(v5._countAndFlagsBits, v5._object);
  v18[1] = v6;
  v15 = Array.init<A>(_:)(v18, &type metadata for UInt8, &type metadata for String.UTF8View);
  v7 = _allocateUninitializedArray<A>(_:)(52LL, &type metadata for UInt8);
  qmemcpy(v8, "FRsIAQ8PVBUVEREIVERbBkURFkUIBxVQVkAYFxJfV0FYVkIVQgo=", 52);
  _finalizeUninitializedArray<A>(_:)();
  v14 = v7;
  v17 = static Array<A>.== infix(_:_:)(v15);
  swift_bridgeObjectRelease(v14);
  swift_bridgeObjectRelease(v15);
  swift_bridgeObjectRelease(v5._object);
  swift_bridgeObjectRelease(v16);
  return v17 & 1;
}
```
I have created the following python code to recover the flag
<br>

```
import base64
from pwn import xor

flag_bytes=base64.b64decode("FRsIAQ8PVBUVEREIVERbBkURFkUIBxVQVkAYFxJfV0FYVkIVQgo=")

flag=xor(flag_bytes,b"swifties!")

print(flag)
```

flag ```flag{f1f4bfa202c60e2aaa9339de61513141}```



