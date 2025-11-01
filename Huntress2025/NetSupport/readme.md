## Chall description
```
Category: Malware
An unexpected Remote Monitoring and Management (RMM) tool was identified on this laptop. We identified a suspicious PowerShell script written to disk at a similar time. Can you find the link between the two?
The password to the ZIP archive is netsupport
```

## Procedure
After open the file, we can see this was a powershell script, but there is a large numeric bytes array, let start checking this. Copy the numeric array and save it into `payload.txt` file, now let's convert those numbers to char, and print only the first 100 chars.
```python
payload = open("payload.txt",'r').read()

out = []
for x in payload.split(','):
    out.append(chr(int(x)))

print(''.join(out)[:100].encode())
```
```bash
# Output
b'PK\x03\x04\x14\x00\x00\x00\x00\x00H\xc2\xbeG[\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00download/PK\x03\x04\x14\x00\x00\x00\x08\x00&\xc2\x99\xc3\xadZ\xc2\xb3\xc2\xac\x05\x1a\xc3\xa9\xc2\xa5\x00\x00H]\x01\x00\x19\x00\x00\x00download/AudioCapture.dll\xc3\xac]k\\T\xc3\x87'
```
The `PK` tell us, this is a zip file, now modify our python script to save the zip file.
```python
with open("payload.txt", "r") as f:
    payload = f.read().strip()

nums = [int(x) for x in payload.split(',') if x.strip()]
data = bytes(nums)

with open("file.zip", "wb") as f:
    f.write(data)

```
```bash
unzip file.zip 
Archive:  file.zip
   creating: download
  inflating: download/AudioCapture.dll  
  inflating: download/client32.exe   
  inflating: download/CLIENT32.ini   
  inflating: download/HTCTL32.DLL    
  inflating: download/kfla.exe       
  inflating: download/msvcr100.dll   
  inflating: download/nskbfltr.inf   
  inflating: download/NSM.ini        
  inflating: download/NSM.LIC        
 extracting: download/nsm_vpro.ini   
  inflating: download/pcicapi.dll    
  inflating: download/PCICHEK.DLL    
  inflating: download/PCICL32.DLL    
  inflating: download/remcmdstub.exe  
  inflating: download/TCCTL32.DLL
```

Here, we can see a lot of `DLL` files, but some files are `ini`, checking that, we can see a base64 string into `CLIENT32.ini`

```ini
0x435302e0

[Client]
_present=1
DisableChat=1
DisableClientConnect=1
DisableDisconnect=1
DisableLocalInventory=1
DisableMessage=1
DisableReplayMenu=1
DisableRequestHelp=1
HideWhenIdle=1
Protocols=3
RADIUSSecret=dgAAAPpMkI7ke494fKEQRUoablcA
Shared=1
silent=1
SKMode=1
SOS_Alt=0
SOS_LShift=0
SOS_RShift=0
SysTray=0
Usernames=*
ValidAddresses.TCP=*

[_Info]
Filename=C:\Users\Administrator\Desktop\Svservices\client32.ini

[_License]
quiet=1

[Audio]
DisableAudioFilter=1

[Bridge]
PasswordFile=C:\Program Files\NetSupport\NetSupport Manager\bridgegevvwe21.psw
Flag=ZmxhZ3tiNmU1NGQwYTBhNWYyMjkyNTg5YzM4NTJmMTkzMDg5MX0NCg==

[General]
BeepUsingSpeaker=0

[HTTP]
GatewayAddress=polygonben.github.io
gsk=FN;J?ACCHJ<O?CBEGB;MEC:B
gskmode=0
GSK=FN;J?ACCHJ<O?CBEGB;MEC:B
GSKX=FP;L?CCEHL=A?EBGGD;O:ABA;D@C
Port=443
SecondaryGateway=@polygonben
SecondaryPort=443
```

```bash
echo ZmxhZ3tiNmU1NGQwYTBhNWYyMjkyNTg5YzM4NTJmMTkzMDg5MX0NCg== | base64 -d
flag{b6e54d0a0a5f2292589c3852f1930891}
```
