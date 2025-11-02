## Chall
```
Category: Forensic
Well, I accidentally put my important data into a bunch of executables... just don't ask, okay?
It was fine... until my cat Sasha stepped on my keyboard and messed everything up! OH NOoOoO00!!!!!111
Can you help me recover my important data?
```
## Procedure
Running strings and filtering `flag` using grep, we can see `pdb` files with references for flag order. 
```bash
strings * | grep "flag"
flag_part_5.pdb
   flag_part_2.pdb 
flag_part_6.pdb
flag_part_1.pdb
flag_part_3.pdb
flag_part_2.pdb
flag_part_1.pdb
flag_part_4.pdb
flag_part_0.pdb
flag_part_4.pdb
flag_part_5.pdb
flag_part_7.pdb
flag{
flag_part_0.pdb
flag_part_7.pdb
flag_part_3.pdb
flag_part_6.pdb
```
Every file is a windows binary, we just need to run every file and recover the output, then using the `pdb` we can know the flag order.
```
945363af.bin = flag_part_0.pdb = f9f73
c8c5833b33584.bin = flag_part_0.pdb = flag{

5e47.bin = flag_part_1.pdb = 88a2d
8208.bin = flag_part_1.pdb = be7a1

4fb72a1a24.bin = flag_part_2.pdb 
7b217.bin = flag_part_2.pdb = e6817

5fa.bin = flag_part_3.pdb = 5f93f
e1204.bin = flag_part_3.pdb = d85d5

a4c71d6229e19b0.bin = flag_part_4.pdb = 49f8b
8c14.bin = flag_part_4.pdb = 48979

aa60783e.bin = flag_part_5.pdb = d9c1a
24b429c2b4f4a3c.bin = flag_part_5.pdb = 5abfa

53bc247952f.bin = flag_part_6.pdb = f18ba
f12f.bin = flag_part_6.pdb = 9bfc2

c54940df1ba.bin = flag_part_7.pdb = 02}
d2f7.bin = flag_part_7.pdb = 23c
```

The problem now is about duplicated flag parts, the chall description give us a hint `my cat Sasha`, what if we check the `sha256 or sha512` for every file?
```bash
sha256 *
SHA256 (24b429c2b4f4a3c.exe) = 58798dd344f3d335f7248b8ed5ecd7e3f438146475adb7a7c38c22dde9000000
SHA256 (4fb72a1a24.exe) = 519579a8035f417f9712ff5de008cfffc30bd9048a76759eeeccbad578669919
SHA256 (53bc247952f.exe) = c6077559a3a6dfefbfbb08aad3e4c055e0fefa8d7755f24c74253f9f50000000
SHA256 (5e47.exe) = 6a85a5142db362292eaf5381be0e404916eda7cb7b0a10d662d48e51c0a23222
SHA256 (5fa.exe) = c000308df0e0b23ae25bea530f1a55653d96e8781ada596d86e2ab090170dd69
SHA256 (7b217.exe) = cda1612776677eaec749332d505c5071fbd92f207c69e5796ae80a6f076ac000
SHA256 (8208.exe) = 3607f4fbc21247e2910c3ab6d86bf9fecd7a5cf493e52850ccc21cf4f3114c00
SHA256 (8c14.exe) = 21559486f1e3ce05d970091c5a516aa86fef86664f14b978fe24b770a840f3f5
SHA256 (945363af.exe) = 425364d90285b957cb8ff1a151b5d3dc011b26c19ff8a8e6078f07503415deba
SHA256 (a4c71d6229e19b0.exe) = db730b200c6290f7691c9ed6316ef2e23695ff989f1e036d5d8b9693a6d00000
SHA256 (aa60783e.exe) = e2cf9b23f225400c99735683216627975b8b3e19d4a8f59fad5d0e77afdcafcc
SHA256 (c54940df1ba.exe) = f304c626549d4a79f9feff97721b8a5f3eae7c7006464ce255948a8400000000
SHA256 (c8c5833b33584.exe) = af3dc02b97619ac833faf01811ebb868c900318d37dc074feb4052dd58a02cd0
SHA256 (d2f7.exe) = a7b57a5bc6bf84d2585e8561da4efe2542411d09e6bebe9dde52bfd1caffab34
SHA256 (e1204.exe) = fd57949e3211fce15429cb98c337bc87d81b8d55ca1dca10ec4b4e641afd0000
SHA256 (f12f.exe) = 45503b2f02879ea036cb1f4a77b48279610d141dcda79c92cecd53c837d4f178
```
Some binary sha256 ended with `0`, maybe this is a reference for `OH NOoOoO00!!!!!111`, let's sort file output with a python script
```python
#!/usr/bin/env python3
import json,subprocess

flag_parts ={
    "24b429c2b4f4a3c.exe":"5abfa",
    "4fb72a1a24.exe":"",
    "53bc247952f.exe":"f18ba",
    "5e47.exe":"88a2d",
    "5fa.exe":"5f93f",
    "7b217.exe":"e6817",
    "8208.exe":"be7a1",
    "8c14.exe":"48979",
    "945363af.exe":"f9f73",
    "a4c71d6229e19b0.exe":"49f8b",
    "aa60783e.exe":"d9c1a",
    "c54940df1ba.exe":"02}",
    "c8c5833b33584.exe":"flag{",
    "d2f7.exe":"23c",
    "e1204.exe":"d85d5",
    "f12f.exe":"9bfc2"
}

file_metadata = json.loads(subprocess.check_output("exiftool *.exe -j", shell=True))
file_metadata_sorted = sorted(file_metadata, key=lambda x: x.get("PDBFileName",""))
flag =""

for x in file_metadata_sorted:
    pdb = x.get('PDBFileName')
    filename = x.get('FileName')
    sha256 = subprocess.check_output("sha256sum "+ filename + " | awk '{print $1}'",shell=True).decode().replace('\n','')
    num = sha256[63:]
    if pdb and num == '0':
        flag += flag_parts[filename]
        print(pdb, sha256,num, flag_parts[filename] ,filename)

print(flag)
```

```bash
### output
   16 image files read
flag_part_0.pdb af3dc02b97619ac833faf01811ebb868c900318d37dc074feb4052dd58a02cd0 0 flag{ c8c5833b33584.exe
flag_part_1.pdb 3607f4fbc21247e2910c3ab6d86bf9fecd7a5cf493e52850ccc21cf4f3114c00 0 be7a1 8208.exe
flag_part_2.pdb cda1612776677eaec749332d505c5071fbd92f207c69e5796ae80a6f076ac000 0 e6817 7b217.exe
flag_part_3.pdb fd57949e3211fce15429cb98c337bc87d81b8d55ca1dca10ec4b4e641afd0000 0 d85d5 e1204.exe
flag_part_4.pdb db730b200c6290f7691c9ed6316ef2e23695ff989f1e036d5d8b9693a6d00000 0 49f8b a4c71d6229e19b0.exe
flag_part_5.pdb 58798dd344f3d335f7248b8ed5ecd7e3f438146475adb7a7c38c22dde9000000 0 5abfa 24b429c2b4f4a3c.exe
flag_part_6.pdb c6077559a3a6dfefbfbb08aad3e4c055e0fefa8d7755f24c74253f9f50000000 0 f18ba 53bc247952f.exe
flag_part_7.pdb f304c626549d4a79f9feff97721b8a5f3eae7c7006464ce255948a8400000000 0 02} c54940df1ba.exe
flag{be7a1e6817d85d549f8b5abfaf18ba02}
```


Flag: `flag{be7a1e6817d85d549f8b5abfaf18ba02}`
