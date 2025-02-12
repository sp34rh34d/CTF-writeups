## Name: X-RAY
#### Author: @JohnHammond
#### Category: Malware
#### Difficulty: N/D
#### Description: The SOC detected malware on a host, but antivirus already quarantined it... can you still make sense of what it does?

NOTE: Archive password is infected

## Procedure
The chall descriptions says ```the antivirus already quarantined it```, the x-ray file is encrypted, that made us think this is Windows Defender. Windows defender uses RC4 to encrypt a malicious file when move the file to quarantine, and the key used for RC4 encryption is: ```1E87781B8DBAA844CE69702C0C78B786A3F623B738F5EDF9AF83530FB3FC54FAA21EB9CF1331FD0F0DA954F687CB9E18279697900E53FB317C9CBCE48E23D05371ECC15951B8F3649D7CA33ED68DC9047E82C9BAAD9799D0D458CB847CA9FFBE3C8A775233557DDE13A8B14087CC1BC8F10F6ECDD083A959CFF84A9D1D50755E3E191818AF23E2293558766D2C07E25712B2CA0B535ED8F6C56CE73D24BDD0291771861A54B4C285A9A3DB7ACA6D224AEACD621DB9F2A22ED1E9E11D75BED7DC0ECB0A8E68A2FF1263408DC808DFFD164B116774CD0B9B8D05411ED6262E429BA495676B8398DB2F35D3C1B9CED52636F2765E1A95CB7CA4C3DDABDDBFF38253```

Using Cyberchef we were able to recover a executable file, we know this is a exe because we can see ```This program cannot be run in DOS mode```.

<img width="1340" alt="Screenshot 2025-02-12 at 7 58 06 AM" src="https://github.com/user-attachments/assets/83468ec8-6ba7-4145-8b2b-297c3672b108" />

An ```exe``` or ```dll``` file should start with magic number ```4D 5A``` or ```MZ```, this is not the case here, so I decided to delete the bad bytes from Cyberchef output and leave it like this.

<img width="840" alt="Screenshot 2025-02-12 at 8 55 41 AM" src="https://github.com/user-attachments/assets/b5bd8fad-00a6-447a-a270-dc9c97d4c497" />

I have used [DnSpy](https://github.com/dnSpy/dnSpy) to recover the source code from exe. Here we can see the following functions.

<img width="1626" alt="Screenshot 2025-02-12 at 8 52 15 AM" src="https://github.com/user-attachments/assets/c9c8b5f2-5496-4eb8-ae5f-5cc54ed779f7" />

The function ```Main()``` calls another function ```main()``` and ```load()```, the function ```main()``` execute a ```ping``` command and then try to delete all the files into path ```/```.

<img width="1287" alt="Screenshot 2025-02-12 at 9 01 54 AM" src="https://github.com/user-attachments/assets/ca0a6910-c708-4718-94ae-bcacb91b974c" />

The ```load()``` function wait for a string parameter, this should be and hex data, then try to extract bytes from the hex parameter.

<img width="1279" alt="Screenshot 2025-02-12 at 9 05 01 AM" src="https://github.com/user-attachments/assets/971d2de2-bb7e-4dc5-bb1e-f11d0b4cffd6" />

the parameters we can see here are  ```15b279d8c0fdbd7d4a8eea255876a0fd189f4fafd4f4124dafae47cb20a447308e3f77995d3c``` and ```73de18bfbb99db4f7cbed3156d40959e7aac7d96b29071759c9b70fb18947000be5d41ab6c41``` then call another function ```otp()``` this receive those parameters, and we can see the following.
```
uint8[] otp (
	uint8[] data,
	uint8[] key
)
```

```data``` and ```key```, so maybe this is XOR encryption with ```15b279d8c0fdbd7d4a8eea255876a0fd189f4fafd4f4124dafae47cb20a447308e3f77995d3c``` and ```73de18bfbb99db4f7cbed3156d40959e7aac7d96b29071759c9b70fb18947000be5d41ab6c41```

I wrote the following python code to recover the flag.

```
from pwn import xor
data = bytes.fromhex("15b279d8c0fdbd7d4a8eea255876a0fd189f4fafd4f4124dafae47cb20a447308e3f77995d3c")
key = bytes.fromhex("73de18bfbb99db4f7cbed3156d40959e7aac7d96b29071759c9b70fb18947000be5d41ab6c41")
print(xor(data,key))
```

flag ```flag{df26090565cb329fdc8357080700b621}```



