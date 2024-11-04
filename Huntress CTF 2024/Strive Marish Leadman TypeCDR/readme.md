## Name: Strive Marish Leadman TypeCDR
#### Author: @aenygma
#### Category: Cryptography 
#### Difficulty: N/D
#### Description: Looks like primo hex garbage. Maybe something went wrong? Can you make sense of it?

## Procedure
In this chall we have to connect to remote server and it sends us a encrypted text with RSA, but it sends us the value for ```e,N,p,q and d```, this is enough to decrypt our flag, every single value is in hex data, so we have to convert them to big integer. I wrote the following python code

```
d = int("cf7ce214f3a0728caf436cfe9074de74913d206bcfb634837a4f053eefb181da956931cc75016e84a5acc2f84a15a3a1b04239817f8471e40aca1cf2e758bd9a31766152706923463cf12fabda5fb9ef7f14798375321db837e9a3d7af4c3ae915001540bfba697865daf97124f4e587db7ee96bb23ca570b09a5936b483581", 16)
n = int("9cce147502fdd8753c814fbbfa4b8581bf27a208a4d8e76ba3aafaf0a9fdb0af65470f1576b0605f47c0129fdf8b90b1d77c706c9d350bd54ac378874956d3f266c0d180948358fde364c324e52a1c1ef743c84fe1854d18a826308092fa635454fd23d8922ec81f1c0da647ede54b492ff305e347063b2c5d6051547fbb4efd", 16)
c = int("3100a2f47b79dc0649c261d40221868bd742934dba4a6d11b5d64806d7f5da488afe33a21f3383e0efda268f32ba4d96ff305fc958d9ffd365bfc3eead332646cf3d19b2cac4ea409b2ebcc6ae7e4ce8eefd3a8d6de216c4afc81c10364277f1402d72e16a18b2282cf91414f3135f0847937d73d32c1282f1469cc59cd51ee3",16)
e = 0x1001
pt = pow(c,d,n)
print(bytes.fromhex(hex(pt).replace("0x","")))
```

flag ```flag{cf614b15ac1dd461a2e48afdfe21b8e8}```
