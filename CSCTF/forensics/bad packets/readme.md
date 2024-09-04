## Name: bad packets
#### Category: forensic
#### Difficulty: N/A
#### Description: Our SOC says that there seems to be some curious activities within one of our servers. They provided a pcap file but I can't find what they're talking about.

## Procedure
I have started to filter the http (get/post) request from pcapng file with wireshark, and we can see some interesting base64 strings into HTTP GET request from 146.190.239.184 to 170.64.232.14

<img width="1595" alt="Screenshot 2024-09-03 at 11 44 18 PM" src="https://github.com/user-attachments/assets/82690d76-4272-4014-8839-9eed2ddba157">
<br>
<br>

When I was trying to decode it, the strings had a kind of encryption, maybe it was using something like AES encryption.
<img width="1250" alt="Screenshot 2024-09-03 at 11 47 36 PM" src="https://github.com/user-attachments/assets/6ab111f6-fafa-4af9-afc5-187a54c86bc3">
<br>

After check for some interesting file in the pcapng, i didnt find anything, at that moment i thought, maybe this is a HTTPC2, and remember this tool [trevorc2](https://github.com/trustedsec/trevorc2), this is a command and control framework. It is a client/server model that works through a browser masquerading as a C2 tool.

Then I was checking the code looking for some similarity in headers and url, i saw the following parameters
<br>
<br>
parameter in pcapng file

```
Cookie: sessionid=KUNBTYOfDGTICbY
oldcss=IGUBqRmQ1fL9AbrJZqvHgWU3jkIt2MWxL/4TKyktAN5Yb6oDvDAv7zjqENtNi0OpE9Aq9r4PHQQUDlcpwwJiPkk/JYh9mbWLoDAdnXArr70=
GET /images?guid=QlNrbWU5eFB4cE5ZRmZPQ0xmbUFWVCsrdHoyRFZoZ2lNRGpOd0pMdVZxUFBKelhEc281YmlHbTRqWXQ3NmJKWW5Bclh0ZDkrWjFBejZaQnpraXZlMWYvT1VUaVhOcUVUc2N1ako3SGd0OVQ4RmI2YzFQQlZRU3Z1OGU4ZHhKaW1SeHVON2xuNXVLNG43RDlrMTN5YjgvMmNuWEZWNndoWm5VZVl2c0g0aHpkNFQxQStON1U3R0xJU2hzSjdiUkxlRFd4MU5IY0FWVzNpU3lCb2pvRkRWZE9wUFFnWW9NaW4xMHJHbXhjQ2w1cmlLS2I5Sm53a3N0NHJDKzBqRW4ya1BhRkVWbWU5cHdWYVlENFJ5aTVLOGJTSGV1UU5zRU9EZXhlVzZQN3RpQ2J3R1BqSG83VDNFakIzTi8zQ3lmQmt6a25BVzZKZi9oNGw4UEZ4K3k0YnpLQ1ZvNXpWMmk1ZHpIQ3JKWStsbmpzeUFWV2NPZ1kvU2hxL1BSd2RTd1VQcUk0VkxYVC8rMWpadHFkNFhCTXR5VHYwNmYvaE1jTWZZR0U1bDZpV3Z0Y2RXcmRIUHg5b09PYWF3dU9VMXdIN09JSm9yVlpiOHkwZmNjQ1Vpa1gySWdGWkJQK1FvR0xkWjBOSVY4TUd3clhoOGJlSDVYeDl6UE5rNDliRERyZ1l4VTJucHNxQnM5dnc5ZFNxN1B0bnljbXhxQVlmQ2dNOWZrc280YXlWanRsdndlUE8vYlp4MGd1ODg0NUFkZWlXTjkvbldXZCtFNVFKbTFRb09lMFZEaE0xUnhBRFhmdlR4TlVqL09uTGdBZG9pRGZLbFNHdHp0R2lmckYwSXBHWUhjbEJpR1FWelFtZWpwQnlPdHhyaFlpVnRjVmUxbTJBMk9hU3RRT25RRXY1K1FZNDhUbkV0UTYwTVlTMU95TWV1am5wOUo2bjZ6VlZaUmg0ckdXM1B4UVZDTGNnZU1rVWEvb2FZY0VMZkw2b2Y3VDVkeXNwbXhBQ0d3RTFHclhqSS9YQmpYV3B3c1U3eTd3c3EyeS9ZTGNURU9vai9RaXdFOEpJeDh2QVQxWHh3RkExTnd0aG9WK1Yvd0I3MmdOcUQ3SHFmcitIaEhVNkpVUDlqeDNjOGc9PQ== HTTP/1.1
```
parameter in trevorc2
```
COOKIE_SESSIONID_STRING = ("sessionid")
STUB = ("oldcss=")

sid = randomString()
def randomString():
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(COOKIE_SESSIONID_LENGTH))

# THIS FLAG IS WHERE THE CLIENT WILL SUBMIT VIA URL AND QUERY STRING GET PARAMETER
SITE_PATH_QUERY = ("/images")

# THIS IS THE QUERY STRING PARAMETER USED
QUERY_STRING = ("guid=")

# STUB FOR DATA - THIS IS USED TO SLIP DATA INTO THE SITE, WANT TO CHANGE THIS SO ITS NOT STATIC
STUB = ("oldcss=")

```

It reads the value of the cookie from the request. The name and length of the cookie are actually hard-coded in the variables “COOKIE_SESSIONID_STRING” and “COOKIE_SESSIONID_LENGTH” which default to “sessionid” and “15” respectively . If it’s set the instructions are read from the instruction dictionary. This dictionary is a global variable that maps every client connected to the C2 and the commands sent to it. The instructions sent by the operators are encrypted using AES and Base64 encoded. These parameters confirm that it is HTTPC2 using the trevorc2 tool.

So, I wrote the following python script to recover the plaintext data

```
import base64
import hashlib
from random import Random
from Crypto.Cipher import AES

encrypted_text = [
    "QlNrbWU5eFB4cE5ZRmZPQ0xmbUFWVCsrdHoyRFZoZ2lNRGpOd0pMdVZxUFBKelhEc281YmlHbTRqWXQ3NmJKWW5Bclh0ZDkrWjFBejZaQnpraXZlMWYvT1VUaVhOcUVUc2N1ako3SGd0OVQ4RmI2YzFQQlZRU3Z1OGU4ZHhKaW1SeHVON2xuNXVLNG43RDlrMTN5YjgvMmNuWEZWNndoWm5VZVl2c0g0aHpkNFQxQStON1U3R0xJU2hzSjdiUkxlRFd4MU5IY0FWVzNpU3lCb2pvRkRWZE9wUFFnWW9NaW4xMHJHbXhjQ2w1cmlLS2I5Sm53a3N0NHJDKzBqRW4ya1BhRkVWbWU5cHdWYVlENFJ5aTVLOGJTSGV1UU5zRU9EZXhlVzZQN3RpQ2J3R1BqSG83VDNFakIzTi8zQ3lmQmt6a25BVzZKZi9oNGw4UEZ4K3k0YnpLQ1ZvNXpWMmk1ZHpIQ3JKWStsbmpzeUFWV2NPZ1kvU2hxL1BSd2RTd1VQcUk0VkxYVC8rMWpadHFkNFhCTXR5VHYwNmYvaE1jTWZZR0U1bDZpV3Z0Y2RXcmRIUHg5b09PYWF3dU9VMXdIN09JSm9yVlpiOHkwZmNjQ1Vpa1gySWdGWkJQK1FvR0xkWjBOSVY4TUd3clhoOGJlSDVYeDl6UE5rNDliRERyZ1l4VTJucHNxQnM5dnc5ZFNxN1B0bnljbXhxQVlmQ2dNOWZrc280YXlWanRsdndlUE8vYlp4MGd1ODg0NUFkZWlXTjkvbldXZCtFNVFKbTFRb09lMFZEaE0xUnhBRFhmdlR4TlVqL09uTGdBZG9pRGZLbFNHdHp0R2lmckYwSXBHWUhjbEJpR1FWelFtZWpwQnlPdHhyaFlpVnRjVmUxbTJBMk9hU3RRT25RRXY1K1FZNDhUbkV0UTYwTVlTMU95TWV1am5wOUo2bjZ6VlZaUmg0ckdXM1B4UVZDTGNnZU1rVWEvb2FZY0VMZkw2b2Y3VDVkeXNwbXhBQ0d3RTFHclhqSS9YQmpYV3B3c1U3eTd3c3EyeS9ZTGNURU9vai9RaXdFOEpJeDh2QVQxWHh3RkExTnd0aG9WK1Yvd0I3MmdOcUQ3SHFmcitIaEhVNkpVUDlqeDNjOGc9PQ==",
    "YmtSVGxyUVFKclRKV244aUxlVDFNNm1SNW4yVUd3K0lTaEZOQUZKb09TdlJEc2p1UHJPSU80bmZRdzZoYjRDdFlCQ25EVm0ybTR2NHoxa0VaSFgyWEE9PQ==",
    "aTFWQWZOOFkxa1B2S3gyTjYvdnpibENuSVQrYS9peGxSUXFseFRrcUw5cWpMKzY3WHEwZzY4K1VTcHQrQXdOY244TEhhUDlZa0R3N0ZpNk9ySU9ZcEdla2NOQmg2U3RFM0xxTDVQaC9PNVdSSkxGcWk0K1VNYm9EZFJvYWhWM1JjRzJaVW9ZRTRodjFnazUzMFF3U1dnPT0=",
    "RmEvUTFUU05NT2JjdG9oWHJJZk5RWFlKNGExQm1LOFU1VWNoMjM3RW9NUmZjY1JjV25MT1pEbGxhWmpkZ0RGeGwrNUtsZkJTTWdJMXVTYzZBY0UxRHRmWEdTOFd4eWRBTTVZU3l3bXdEL3hudk5pSWdlQzhBaEk0RlQycVFkNE5WL3dVdzNSUzNTTm5PQjlhSktmMUVRPT0="
]

def decrypt(enc):
    key = hashlib.sha256(str_to_bytes("Tr3v0rC2R0x@nd1s@w350m3#TrevorForget")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

def str_to_bytes(data):
    u_type = type(b''.decode('utf8'))
    if isinstance(data, u_type):
        return data.encode('utf8')
    return data

def _unpad(s):
    return s[:-ord(s[len(s)-1:])]

for x in encrypted_text:
    print(decrypt(base64.b64decode(x)))
```

output

```
ubuntu-s-1vcpu-512mb-10gb-ams3-01::::b'total 1.5M\ndrwxr-xr-x 5 root    root    4.0K Aug 18 01:50 .\ndrwx------ 6 root    root    4.0K Aug 18 01:50 ..\ndrwxr-xr-x 2 root    root    4.0K Aug 18 01:47 bin\n-rw-r--r-- 1 root    root    5.9K Aug 18 01:45 c2\ndrwxr-xr-x 3 root    root    4.0K Aug 18 01:46 include\ndrwxr-xr-x 3 root    root    4.0K Aug 18 01:46 lib\nlrwxrwxrwx 1 root    root       3 Aug 18 01:46 lib64 -> lib\n-rw-r--r-- 1 tcpdump tcpdump 1.5M Aug 18 01:51 out.pcapng\n-rw-r--r-- 1 root    root     147 Aug 18 01:46 pyvenv.cfg\n-rw-r--r-- 1 root    root      37 Aug 18 01:47 requirements.txt\n'
ubuntu-s-1vcpu-512mb-10gb-ams3-01::::b'root\n'
ubuntu-s-1vcpu-512mb-10gb-ams3-01::::b'uid=0(root) gid=0(root) groups=0(root)\n'
ubuntu-s-1vcpu-512mb-10gb-ams3-01::::b'CSCTF{chang3_y0ur_variab13s_b3for3_d3pl0ying}\n'
```

flag ```CSCTF{chang3_y0ur_variab13s_b3for3_d3pl0ying}```
