## Name: A Dire Situation
#### Category: Forensics
#### Difficulty: Easy
#### Description: I really need help with my budget. Let's see if there's anything you can do with my current situation!

## Procedure
I have ran the command ```file budget.wim```, this show me the following output ```budget.wim: Windows imaging (WIM) image v1.13, reparse point fixup```.

Windows Imaging Format (WIM) is a file-based disk image format developed used to deploy operating system images. It's used primarily to capture, manage, and deploy Windows operating system images, allowing for flexible and efficient management of images in environments like installation, recovery, and deployment.

I have extrated the files running the command ```wimextract budget.wim 1 --dest-dir=./data```, this show me the following output

```
data/
└── budget
```

checking the ```data/budget``` file, this is ```data/budget: ASCII text```, so i ran ```cat``` command to check the content.

```
Can someone please help me budget? My family is dying. 

Rent: $750
Insurance: $100
Streaming: $5000
Food: $200
```

Ok, this was not what i expected!, i have checked the ```.wim``` file again using ```xxd``` and ```binwalk``` commands.

```
xxd output

000003f0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000400: 0000 3230 3234 3a30 393a 3230 2031 343a  ..2024:09:20 14:
00000410: 3138 3a34 3600 3230 3234 3a30 393a 3230  18:46.2024:09:20
00000420: 2031 343a 3138 3a34 3600 0000 6100 7200   14:18:46...a.r.
00000430: 6300 7400 6900 6300 7800 0000 ffe1 041a  c.t.i.c.x.......
00000440: 6874 7470 3a2f 2f6e 732e 6164 6f62 652e  http://ns.adobe.
00000450: 636f 6d2f 7861 702f 312e 302f 003c 3f78  com/xap/1.0/.<?x
00000460: 7061 636b 6574 2062 6567 696e 3d27 efbb  packet begin='..
00000470: bf27 2069 643d 2757 354d 304d 7043 6568  .' id='W5M0MpCeh
00000480: 6948 7a72 6553 7a4e 5463 7a6b 6339 6427  iHzreSzNTczkc9d'
00000490: 3f3e 0d0a 3c78 3a78 6d70 6d65 7461 2078  ?>..<x:xmpmeta x
000004a0: 6d6c 6e73 3a78 3d22 6164 6f62 653a 6e73  mlns:x="adobe:ns
000004b0: 3a6d 6574 612f 223e 3c72 6466 3a52 4446  :meta/"><rdf:RDF
000004c0: 2078 6d6c 6e73 3a72 6466 3d22 6874 7470   xmlns:rdf="http
000004d0: 3a2f 2f77 7777 2e77 332e 6f72 672f 3139  ://www.w3.org/19
000004e0: 3939 2f30 322f 3232 2d72 6466 2d73 796e  99/02/22-rdf-syn
000004f0: 7461 782d 6e73 2322 3e3c 7264 663a 4465  tax-ns#"><rdf:De
00000500: 7363 7269 7074 696f 6e20 7264 663a 6162  scription rdf:ab
00000510: 6f75 743d 2275 7569 643a 6661 6635 6264  out="uuid:faf5bd
00000520: 6435 2d62 6133 642d 3131 6461 2d61 6433  d5-ba3d-11da-ad3
00000530: 312d 6433 3364 3735 3138 3266 3162 2220  1-d33d75182f1b" 
00000540: 786d 6c6e 733a 6463 3d22 6874 7470 3a2f  xmlns:dc="http:/
00000550: 2f70 7572 6c2e 6f72 672f 6463 2f65 6c65  /purl.org/dc/ele
00000560: 6d65 6e74 732f 312e 312f 222f 3e3c 7264  ments/1.1/"/><rd
```

```
binwalk output
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
354           0x162           TIFF image data, big-endian, offset of first image directory: 8
```
Both output tells me that there is an hidden image into ```wim``` file, i was trying to extract data using ```binwalk -e budget.wim```, but not work.

I did a manual carve using ```dd``` command, ```dd if=budget.wim of=flag.tiff bs=1 skip=354```, but the image was currupted.

![2024-09-24_21-45](https://github.com/user-attachments/assets/72a63097-87d4-4106-a266-f2b57da48204)

Checking the hex data, run the command ```cat flag.tiff | hex > flag.hex``` we can see it start with ```4d4d002a``` this is TIFF format (Motorola - big endian, I have changed to ```49492a00``` using the [magic number](https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5) but still corrupted, so i decide change the magic number to JPEG format ```ffd8ffe0```.

![2024-09-24_21-55](https://github.com/user-attachments/assets/dacd62ea-0a70-4d10-96b8-d6ec1d8260ed)

create the jpg file, ```cat flag.hex  | xxd -p -r > flag.jpg ```, after that, we can recover the image correctly

![flag](https://github.com/user-attachments/assets/ed12ce91-c169-4475-b877-c883382760ef)







