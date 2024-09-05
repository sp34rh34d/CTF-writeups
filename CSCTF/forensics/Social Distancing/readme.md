## Name: Social Distancing
#### Category: forensic
#### Difficulty: N/A
#### Description: We all remember the time of social distancing and quarantines. How about some quarantined malware? Bet you can't understand what it entails!

## Procedure
When Windows Defender detects a potentially harmful file or program, it moves it to quarantine as a precaution. Quarantined items are essentially isolated from the rest of the system to prevent them from causing any harm. They are not deleted but are kept in a secure location where they can't execute or spread.

The quarantined files are stored in a hidden and protected folder on your system. Typically, they are located in ```C:\ProgramData\Microsoft\Windows Defender\Quarantine```

Within this directory, the file structure is organized into several subdirectories, each serving a specific purpose.
The Quarantine Folder Structure typically has the followign folders:
*ResourceData: Contains the actual quarantined files. These files are encrypted, making them inaccessible and unusable in their current form.
*Resources: Often mirrors the structure of ResourceData and may contain metadata or information about the quarantined files.
*Entries: Contains metadata about the quarantined items, including information about the original location of the file, the time it was quarantined, and the threat detected.

In this chall, we can see the same file structure, so now we know this is a malware file and we need to extract the file from quarantine.
```
├── chall
│   ├── Entries
│   │   └── {80008A1B-0000-0000-7091-E5797219933B}
│   ├── ResourceData
│   │   └── 95
│   │       └── 957997B71FBF912F2A3E881A13A83E0FAB3ECB47
│   └── Resources
│       └── 95
│           └── 957997B71FBF912F2A3E881A13A83E0FAB3ECB47
```

You can extract data using this [tool](https://github.com/knez/defender-dump.git), i have modified the line ``` basedir = args.rootdir / 'ProgramData/Microsoft/Windows Defender/Quarantine'``` for ``` basedir = args.rootdir / '.'```, so this will check in the main path i send with ```-d``` paramenter, something like ```./defender-dump.py -d /path/to/quarantine/file/```

output
```
Exporting test.ps1
File 'quarantine.tar' successfully created
```

Now, checking the extracted file, we can see the file ```test.ps1```
```
#test.ps1 file contect

$hidden = @"
UEsDBAoAAAAAAOCYuCg8z1FoRAAAAEQAAAAJABwAZWljYXIuY29tVVQJAAOUYCw5y1zNZnV4CwAB
BAAAAAAEAAAAAFg1TyFQJUBBUFs0XFBaWDU0KFBeKTdDQyk3fSRFSUNBUi1TVEFOREFSRC1BTlRJ
VklSVVMtVEVTVC1GSUxFISRIK0gqUEsDBAoAAAAAAE8HG1mJ3nc0MQAAADEAAAAEABwAZmxhZ1VU
CQAD9VzNZtVczWZ1eAsAAQQAAAAABAAAAABDU0NURnt5MHVfdW4tcXU0cmFudDFuM2RfbXlfc2Ny
MVB0IV8weDkxYTNlZGZmNn0KUEsBAh4DCgAAAAAA4Ji4KDzPUWhEAAAARAAAAAkAGAAAAAAAAQAA
AKSBAAAAAGVpY2FyLmNvbVVUBQADlGAsOXV4CwABBAAAAAAEAAAAAFBLAQIeAwoAAAAAAE8HG1mJ
3nc0MQAAADEAAAAEABgAAAAAAAEAAACkgYcAAABmbGFnVVQFAAP1XM1mdXgLAAEEAAAAAAQAAAAA
UEsFBgAAAAACAAIAmQAAAPYAAAAAAA==
"@

$decodedBytes = [System.Convert]::FromBase64String($hidden)

$zipFilePath = "malicious.zip"
[System.IO.File]::WriteAllBytes($zipFilePath, $decodedBytes)

Write-Output "File saved as $zipFilePath"

```

just run the following command to get the flag

```
echo "UEsDBAoAAAAAAOCYuCg8z1FoRAAAAEQAAAAJABwAZWljYXIuY29tVVQJAAOUYCw5y1zNZnV4CwAB
BAAAAAAEAAAAAFg1TyFQJUBBUFs0XFBaWDU0KFBeKTdDQyk3fSRFSUNBUi1TVEFOREFSRC1BTlRJ
VklSVVMtVEVTVC1GSUxFISRIK0gqUEsDBAoAAAAAAE8HG1mJ3nc0MQAAADEAAAAEABwAZmxhZ1VU
CQAD9VzNZtVczWZ1eAsAAQQAAAAABAAAAABDU0NURnt5MHVfdW4tcXU0cmFudDFuM2RfbXlfc2Ny
MVB0IV8weDkxYTNlZGZmNn0KUEsBAh4DCgAAAAAA4Ji4KDzPUWhEAAAARAAAAAkAGAAAAAAAAQAA
AKSBAAAAAGVpY2FyLmNvbVVUBQADlGAsOXV4CwABBAAAAAAEAAAAAFBLAQIeAwoAAAAAAE8HG1mJ
3nc0MQAAADEAAAAEABgAAAAAAAEAAACkgYcAAABmbGFnVVQFAAP1XM1mdXgLAAEEAAAAAAQAAAAA
UEsFBgAAAAACAAIAmQAAAPYAAAAAAA==" | base64 -d
``` 

flag ```CSCTF{y0u_un-qu4rant1n3d_my_scr1Pt!_0x91a3edff6}```

