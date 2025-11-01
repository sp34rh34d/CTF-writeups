## Chall description
```
Category: Misc
vx-underground, widely known across social media for hosting the largest collection and library of cat pictures, has been plagued since the dawn of time by people asking: "what's the password?"
Today, we ask the same question. We believe there are secrets shared amongst the cat pictures... but perhaps these also lead to just more cats.
Uncover the flag from the file provided.
```
## Procedure
After see a lot of picture, I only thought on steg chall, I always start looking at metadata with `exiftool`, and I could see interesting user comment on every pic. and `flag.zip` file is protected by password
```bash
.
├── Cat Archive
│   ├── 000b8a1b1806920c5cec4a0ae10ec048209dad7596cfce219b9c2c3e1dc7f5f4.jpg
│   ├── 000c18880dc4af8a046aa78daeedf08e3fd575614df8e66e4cfbfd50a740ea77.jpg
│   ├── 000cb28f57ae572ba83149b2163f9076cdb9660310a8bf2547a19816cf611775.jpg
│   ├── 000cf1b3e38af81f673ca4ae37e0666137f84edd67f172c1f17d2333c3d521c0.jpg
│   ├── 00a7c5ac8139f72f15ac31130effd5c3619561635f8b13ec4a2ee626fb627ab4.jpg
│   ├── 00a91bd436455d4c73303f0d0a784660771dcc895989ad13942603d58ff798fe.jpg
│   ├── 00a9a9bb5d68ed994e4ecdc69e550dfdd38d1b673b1bac2909de9901318b4627.jpg
│   ├── 00ad6d78383d69cb4a63b0200391f1ef0b5b1265ab3b633ebeb3649a67744895.jpg
│   ├── 00ae13a062f081127bd02e9b55ce80731ab4c49a0755527d3d60c42e10960ec6.jpg
...snip...
│   ├── 0fcd21fd8b70de83c1bef8d5acb88a3cc940f4832ec64fbe8f038d9082a09dc3.jpg
│   ├── 0fd62a9214fe0808187bc29400a0047f03351356a73065d0d03e55145e41b958.JPG
│   ├── 0fdc492345a070525c40ce709a0a5aeae00cd17f6b56017d7f892d1e3435e651.jpg
│   ├── 0fdd334e775ced15f79d50813c6bd6f2281fbef8dfc324d468cdc6e35d8fd263.jpg
│   ├── 0fe89f464ad0324676483c9f14c30f31975907e3b41ca79b3c3b26a0672a2936.jpg
│   ├── 0fe8a16e59967f98ac591b28b66dad388fe9a57e3325dde6f855631f20310e33.jpg
│   ├── 0fec6482e1d3ca80d56675347e455f89149be2cd80d73d1e7a0c7e33876f8d21.jpg
│   ├── 0fed52c4cae8b2f46e75b04d39c3767bf26defe90aaef808afa6a1e0c944c0d4.jpg
│   └── 0ff8658055ea93f30482de8a990600c2f8a301a1a2632afbffda5f60cac2e1c5.jpg
├── cute-kitty-noises.txt
├── flag.zip
└── prime_mod.jpg

2 directories, 460 files
```
Recover metadata from `prime_mod.jpg`
```bash
exiftool -a prime_mod.jpg 
ExifTool Version Number         : 13.30
File Name                       : prime_mod.jpg
Directory                       : .
File Size                       : 43 kB
File Modification Date/Time     : 2025:09:21 17:31:54-06:00
File Access Date/Time           : 2025:10:17 11:41:17-06:00
File Inode Change Date/Time     : 2025:10:17 07:25:19-06:00
File Permissions                : -rw-------
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Exif Byte Order                 : Big-endian (Motorola, MM)
User Comment                    : Prime Modulus: 010000000000000000000000000000000000000000000000000000000000000129
Image Width                     : 400
Image Height                    : 400
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 400x400
Megapixels                      : 0.160
```

```bash
exiftool -a * | grep "User Comment" 
User Comment                    : 253-6ba02f81b0c38473b0442d0ebc46f4a8223edead6d164103fbcdeb10ea414e76
User Comment                    : 145-2d9ab042a4bf21369ed72897366204feff54359585275a09ab64975c43304962
User Comment                    : 415-0551477bacb1ac94a91466ffa3d96e67940afde60ff0dc79d928609a55fccfe2
User Comment                    : 363-49387f88c14c828683bdd189bcf975e384a6ae2f897e1d135814a92e539da785
User Comment                    : 35-fd90c306d0873404616dfee1bc087a4a57e7ba39983465f9f560359049344e5b
...snip...
```

Let's try to order this and dump it into data.txt
```
exiftool -a * | grep "User Comment" | awk '{print $4}' | sort -t- -k1,1n > data.txt
head data.txt 
1-d278c2aad8f1c0de7023b4ec81df35fd9515a4330d5db48fda746c0548c200f5
2-60cf3885dabd878c2f24cd503b02db29c7c2dfdad310a8ec9c0d826b8d84ff2f
3-f84c72ebf84336085a6f1013ccff8cd987a0baa1c6d5c0fb650b14b4daf6ca2f
4-b2ebc1f2cc12460fbafb34975e12ecb4e0d5c6fde61ed64ae8c6c99a97c11cb3
5-51e10e577e79c3bb548d4fa0abc2809926c22c1d39a068d4804ed5f78db5aa05
6-9ed77e10474f730060a401af72bbffc311e7b6fb0dada2596dbe825fac7cb0d3
7-2df0e88c067f0337018463a171c80966669f5b1338cf8b701d450cf75bd10828
8-0d29bad043e5506debddfb41419839332e6d55c6586622dbf636d69dc12a824d
9-5a022d51d3afa18b614a4c2bdcecb159fb7930b1b6fbcecf737a08034a065980
10-e7f254644a03a550110e2be89160ad50f0561f7387cf8a7d181a7619decb12ca

## delete numbers
exiftool -a * | grep "User Comment" | awk '{print $4}' | sort -t- -k1,1n | sed 's/-/ /g' | awk '{print $2}' > data.txt
head data.txt 
d278c2aad8f1c0de7023b4ec81df35fd9515a4330d5db48fda746c0548c200f5
60cf3885dabd878c2f24cd503b02db29c7c2dfdad310a8ec9c0d826b8d84ff2f
f84c72ebf84336085a6f1013ccff8cd987a0baa1c6d5c0fb650b14b4daf6ca2f
b2ebc1f2cc12460fbafb34975e12ecb4e0d5c6fde61ed64ae8c6c99a97c11cb3
51e10e577e79c3bb548d4fa0abc2809926c22c1d39a068d4804ed5f78db5aa05
9ed77e10474f730060a401af72bbffc311e7b6fb0dada2596dbe825fac7cb0d3
2df0e88c067f0337018463a171c80966669f5b1338cf8b701d450cf75bd10828
0d29bad043e5506debddfb41419839332e6d55c6586622dbf636d69dc12a824d
5a022d51d3afa18b614a4c2bdcecb159fb7930b1b6fbcecf737a08034a065980
e7f254644a03a550110e2be89160ad50f0561f7387cf8a7d181a7619decb12ca
```

Now with `Prime Modulus` and after extract those user comment, this look like a crypto challenge, something like [Shamir's Secret](https://www.lost-cluster.org/shattered_secrets/).
After read about this python script adaptation can help us to decrypt the secret message
```python
from functools import reduce

shares = {i+1:int(l,16) for i,l in enumerate(open("data.txt")) if l.strip()}
p = int("010000000000000000000000000000000000000000000000000000000000000129",16)
modinv = lambda a,p: pow(a,-1,p)

secret = sum(y * reduce(lambda x,j:x*-j%p,(j for j in shares if j!=i),1) * modinv(reduce(lambda x,j:x*(i-j)%p,(j for j in shares if j!=i),1),p) for i,y in shares.items()) % p
print(hex(secret), secret.to_bytes((secret.bit_length()+7)//8,"big"))

```

This show us the password for zip file, but look like another encoded message `Meow lang`
```bash
### output
python3 solve.py
0x2a5a49502070617373776f72643a20464170656b4a21794a363959616a5773 b'*ZIP password: FApekJ!yJ69YajWs'

head cute-kitty-noises.txt 
MeowMeow;MeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowMeowM
..snip...
```
Python script to decode meow lang
```python
from pathlib import Path

decoded = ''.join(
    chr(s.count('Meow'))
    for s in Path('cute-kitty-noises.txt').read_text().replace(';;',';').split(';')
    if 32 <= s.count('Meow') <= 126
)

print(decoded)
```

```bash
### output
python3 meow.py
malware is illegal and for nerdscats are cool and badassflag{35dcba13033459ca799ae2d990d33dd3}
```

Flag  `flag{35dcba13033459ca799ae2d990d33dd3}`
