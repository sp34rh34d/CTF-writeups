from pwn import *
import re,base64
context(log_level='debug')
r = remote('chal.pctf.competitivecyber.club',9001)



base64_pattern = r'[A-Za-z0-9+/=]{20,}'
md5_pattern = r'[a-f0-9]{32,32}'

for x in range(1000):
    data = r.recvuntil(b">> ").decode('utf-8')
    match = re.findall(base64_pattern,data)
    chall=""
    try:
        chall = base64.b64decode(match[1])
    except:
        chall = base64.b64decode(match[0])
    chall_data = chall.decode('utf-8').split("|")[0]
    while True:
        try:
            chall_data = base64.b64decode(chall_data)
            md5_match = re.findall(md5_pattern,chall_data.decode('utf-8'))
            if len(md5_match) > 0:
                break
            
        except:
            break
        
        
    decoder = f"{chall_data.decode('utf-8')}|{x}"
    r.send(decoder)

r.interactive()