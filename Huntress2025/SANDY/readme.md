## Chall description
```
Category: Malware
My friend Sandy is really into cryptocurrencies! She's been trying to get me into it too, so she showed me a lot of Chrome extensions I could add to manage my wallets. Once I got everything sent up, she gave me this cool program!

She says it adds better protection so my wallets can't get messed with by hackers.

Sandy wouldn't lie to me, would she...? Sandy is the best!

Note: The password to the archive is infected.
```

## Procedure
After run `Exiftool`; I saw an interesting tag `Compiled Script: AutoIt v3 Script : 3, 2, 4, 9`, I decided to search for an `AutoIT` decopiler, and I found this [tool](https://github.com/daovantrong/myAutToExe).
```bash
exiftool -a SANDY.exe
ExifTool Version Number         : 13.30
File Name                       : SANDY.exe
Directory                       : .
File Size                       : 343 kB
File Modification Date/Time     : 2025:09:26 14:54:38-06:00
File Access Date/Time           : 2025:10:03 21:13:01-06:00
File Inode Change Date/Time     : 2025:10:03 10:30:17-06:00
File Permissions                : -rw-------
File Type                       : Win32 EXE
File Type Extension             : exe
MIME Type                       : application/octet-stream
Machine Type                    : Intel 386 or later, and compatibles
Time Stamp                      : 2007:05:25 08:27:07-06:00
Image File Characteristics      : No relocs, Executable, No line numbers, No symbols, 32-bit
PE Type                         : PE32
Linker Version                  : 7.10
Code Size                       : 200704
Initialized Data Size           : 8192
Uninitialized Data Size         : 356352
Entry Point                     : 0x88070
OS Version                      : 4.0
Image Version                   : 0.0
Subsystem Version               : 4.0
Subsystem                       : Windows GUI
File Version Number             : 3.2.4.9
Product Version Number          : 3.2.4.9
File Flags Mask                 : 0x0017
File Flags                      : (none)
File OS                         : Win32
Object File Type                : Unknown
File Subtype                    : 0
Language Code                   : English (British)
Character Set                   : Unicode
File Description                : 
File Version                    : 3, 2, 4, 9
Compiled Script                 : AutoIt v3 Script : 3, 2, 4, 9
```
Just select `SANDY.EXE`, and this save the decopiled code into `SANDY.au3` file.
<img width="625" height="687" alt="Screenshot 2025-10-03 at 11 49 51 PM" src="https://github.com/user-attachments/assets/d8ac7120-d992-4178-9a94-0fcc8602ef38" />

After read the output, I can see a lot of `base64` strings in the variable called `base64Chunks`, and yes this is vb.
<img width="1608" height="624" alt="Screenshot 2025-10-03 at 11 54 47 PM" src="https://github.com/user-attachments/assets/776e5b97-cecc-45e6-a948-5285f8384764" />

After decode the `base64` strings, we have another layer of `base64` strings 🫠
<img width="1631" height="934" alt="Screenshot 2025-10-03 at 11 56 39 PM" src="https://github.com/user-attachments/assets/3ca6b65e-ffb3-456d-9cff-49fbe456fc99" />

And finally we were able to recover the flag after decode every `base64` string here.
<img width="1353" height="774" alt="Screenshot 2025-10-03 at 11 53 49 PM" src="https://github.com/user-attachments/assets/62b500c5-a583-400c-86eb-896858fce0ab" />

Flag `flag{27768419fd176648b335aa92b8d2dab2}`
