## Chall description
```
Category: Forensic

So.... bad news.
We got hit with ransomware.
And... worse news... we paid the ransom.
After the breach we FINALLY set up some sort of backup solution... it's not that good, but, it might save our bacon... because my VM crashed while I was trying to decrypt everything.
And perhaps the worst news... I forgot the decryption key.
Gosh, I have such bad memory!!

The archive password is i_forgot.
```

## Procedure
File content
```bash
tree .
.
├── flag.enc
└── memdump.dmp

1 directory, 2 files
```

Doing a filescan with volatility, we can see an intereting file `BackupHelper.exe` on `Desktop`. After try to recover that file, I got some errors.
```bash
./vol.py -f ~/Downloads/i_forgot/memdump.dmp windows.filescan | grep "Users"

### output
0xdf07c3ac7520.0\Users\User\AppData\Local\Microsoft\Windows\Explorer\iconcache_16.db	216
0xdf07c3c4b520	\Users\User\AppData\Local\Microsoft\Windows\Explorer\iconcache_idx.db	216
0xdf07c439bd00	\Users\User\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\LocalState\EBWebView\Default\Sync Data\LevelDB\000004.log	216
0xdf07c439c660	\Users\User\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\LocalState\EBWebView\Default\SharedStorage	216
...snip...
0xdf07c759e5b0	\Users\User\Desktop\BackupHelper.exe	216

### dump file
./vol.py -f ~/Downloads/i_forgot/memdump.dmp windows.dumpfile --virtaddr 0xdf07c759e5b0
Volatility 3 Framework 2.7.0
Progress:  100.00		PDB scanning finished                        
Cache	FileObject	FileName	Result

ImageSectionObject	0xdf07c759e5b0	BackupHelper.exe	Error dumping file
```

I just extracted all strings from dmp file to search for `BackupHelper`
```bash
strings memdump.dmp > allstrings.txt
```

Then use sublime to filter `BackupHelper`, we have a reference to a zip file called `DECRYPT_PRIVATE_KEY.zip`
```bash
### using sublime with Ctr + shift + F with "BackupHelper" filter
Searching 1 file for "BackupHelper" (regex)

~/Downloads/i_forgot/allstrings.txt:
 45317  2/Z/
 45318  96\[
 45319: BackupHelper started: 2025-09-28T04:41:52.5463814Z
 45320  ZipPath: C:\Users
 45321  \Desktop\DECRYPT_PRIVATE_KEY.zip
```

Filter `DECRYPT_PRIVATE_KEY` we can see a string talking about a password for the zip file, and it shows us a hash `SHA256`, the `\Desktop\DECRYPT_PRIVATE_KEY.zip`, is not on users desktop, this mean the file could be deleted.
```bash
### using sublime with Ctr + shift + F with "DECRYPT_PRIVATE_KEY" filter
Searching 1 file for "DECRYPT_PRIVATE_KEY" (regex)

~/Downloads/i_forgot/allstrings.txt:
 45319  BackupHelper started: 2025-09-28T04:41:52.5463814Z
 45320  ZipPath: C:\Users
 45321: \Desktop\DECRYPT_PRIVATE_KEY.zip
 45322  ZIP read: 1938
 45323  SHA256: d1f9bd7084f5234400f878971fa7ccba835564845f0b10479efd5c38bd184f09

...snip...

## and another interesting thing, a password maybe for the zip file
 3308794  AND FILE RECOVERY INSTRUCTIONS 
 3308795: The private key to decrypt is stored in 'DECRYPT_PRIVATE_KEY.zip'.
 3308796: ZIP password: ePDaACdOCwaMiYDG
 3308797  On a machine with OpenSSL installed (Linux / Windows(
 3308798  ), the steps
```

Carve on dmp file using magic bytes `PK\x03\x04` for zip file, we can see a lot of reference about zip files in our `dmp`.
```bash
### checking for zip files on memdump.dmp
grep -aobUa "PK\x03\x04" memdump.dmp
31536692:PK
84237035:PK
108859138:PK
131557760:PK
182798065:PK
191087984:PK
206328718:PK
206329105:PK
212399426:PK
226135711:PK
239510596:PK
253260133:PK
264404377:PK
281895822:PK
281896209:PK
289506295:PK
308010396:PK
319646527:PK
324545668:PK
336307458:PK
336307507:PK
349085033:PK
386447552:PK
399758692:PK
406218318:PK
441870113:PK
462798284:PK
463221069:PK
511644888:PK
554895381:PK
678578558:PK
684268874:PK
698573718:PK
721258878:PK
722903923:PK
738147865:PK
739902467:PK
739905024:PK
793384411:PK
807758565:PK
807821373:PK
807822208:PK
807822402:PK
807822442:PK
843075806:PK
898137155:PK
910887572:PK
919256501:PK
919256604:PK
919256708:PK
925264963:PK
951177608:PK
955469824:PK
955471233:PK
967440142:PK
973172388:PK
979304840:PK
989193854:PK
1027883291:PK
1027885678:PK
```
I asked to GPT a script to recover that zip file using as reference the sha256 to get the right file
```python
## extract.py
import re, hashlib

data = open("memdump.dmp", "rb").read()
starts = [m.start() for m in re.finditer(b'PK\x03\x04', data)]
ends = [m.start() for m in re.finditer(b'PK\x05\x06', data)]

for s in starts:
    e = next((x for x in ends if x > s), None)
    if not e: continue
    chunk = data[s:e+22]
    h = hashlib.sha256(chunk).hexdigest()
    if h == "d1f9bd7084f5234400f878971fa7ccba835564845f0b10479efd5c38bd184f09":
        open("DECRYPT_PRIVATE_KEY.zip", "wb").write(chunk)
        print(f"✅ Found at offset {s} - saved DECRYPT_PRIVATE_KEY.zip")
        break
```
I was able to recover the `DECRYPT_PRIVATE_KEY.zip`
```bash
## output
✅ Found at offset 955469824 - saved DECRYPT_PRIVATE_KEY.zip

zipinfo DECRYPT_PRIVATE_KEY.zip 
Archive:  DECRYPT_PRIVATE_KEY.zip
Zip file size: 1938 bytes, number of entries: 2
-rw-------  3.0 unx     1708 TX defN 25-Sep-27 22:35 private.pem
-rw-rw-r--  3.0 unx      256 BX stor 25-Sep-27 22:35 key.enc
2 files, 1964 bytes uncompressed, 1568 bytes compressed:  20.2%
```
The zip file has 2 new files `key.enc` and `private.pem`, but my question was, if we only need to decrypt the `flag.enc` file, why we have `key.enc`, what is this file?
```bash
tree .
.
├── DECRYPT_PRIVATE_KEY.zip
├── flag.enc
├── key.enc
├── memdump.dmp
├── private.pem
└── extract.py
```

I was trying to decrypt the `flag.enc` using only the `private.pem file`, but got some errors
```bash
openssl pkeyutl -decrypt -in flag.enc -inkey private.pem -out ff.txt -pkeyopt rsa_padding_mode:oaep
Public Key operation error
00005147F87F0000:error:02000079:rsa routines:RSA_padding_check_PKCS1_OAEP_mgf1:oaep decoding error:crypto/rsa/rsa_oaep.c:332:
```

Then I decided to decrypt the key.enc using the `private.pem file`, this works, but now I have no idea what was that 💀. first line has `32` bytes `64 chars`, and second line has `16` bytes `32 chars`.
```bash
openssl pkeyutl -decrypt -in key.enc -inkey private.pem -out key.bin -pkeyopt rsa_padding_mode:oaep

xxd -p key.bin
289ea58a38549d5faf7a97a6dd19cdf2ddc0496a8a64f99a77c643529c94
b8042c6a55b0a89141056517687a977305d6
```

Reading about and checking the GPT suggestion, I was trying with AES using Cyberchef, to decrypt using AES256, you need KEY and IV, the key size can be `16` bytes = `AES-128`, `24` bytes = `AES-192`, `32` bytes = `AES-256`, and the IV expect `16` bytes.

<img width="1348" height="664" alt="Screenshot 2025-10-13 at 5 23 00 PM" src="https://github.com/user-attachments/assets/96033898-5512-490b-ad22-44bf939d9c6a" />

Flag `flag{fa838fa9823e5d612b25001740faca31}`





