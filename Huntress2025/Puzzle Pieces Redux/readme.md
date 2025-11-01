## Chall
```
Category: Forensic
Well, I accidentally put my important data into a bunch of executables... just don't ask, okay?
It was fine... until my cat Sasha stepped on my keyboard and messed everything up! OH NOoOoO00!!!!!111
Can you help me recover my important data?
```

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

```
945363af.bin = flag_part_0.pdb
c8c5833b33584.bin = flag_part_0.pdb

5e47.bin = flag_part_1.pdb
8208.bin = flag_part_1.pdb

4fb72a1a24.bin = flag_part_2.pdb 
7b217.bin = flag_part_2.pdb

5fa.bin = flag_part_3.pdb
e1204.bin = flag_part_3.pdb

a4c71d6229e19b0.bin = flag_part_4.pdb
8c14.bin = flag_part_4.pdb

aa60783e.bin = flag_part_5.pdb
24b429c2b4f4a3c.bin = flag_part_5.pdb

53bc247952f.bin = flag_part_6.pdb
f12f.bin = flag_part_6.pdb

c54940df1ba.bin = flag_part_7.pdb
d2f7.bin = flag_part_7.pdb
```

```powershekk
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\7b217.exe
e6817
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\5fa.exe
5f93f
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\e1204.exe
d85d5
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\a4c71d6229e19b0.exe
49f8b
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\8c14.exe
48979
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\aa60783e.exe
d9c1a
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\24b429c2b4f4a3c.exe
5abfa
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\53bc247952f.exe
f18ba
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\f12f.exe
9bfc2
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\c54940df1ba.exe
02}
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux> .\d2f7.exe
23c
PS Microsoft.PowerShell.Core\FileSystem::\\vmware-host\Shared Folders\Downloads\puzzle_pieces_redux>
```

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



