## Chall description
```
Category: Forensic

Ohhhh, Tab, Tab, Tab.... what has she done.
My friend Tabby just got a new laptop and she's been using it to take notes. She says she puts her whole life on there!
She was so excited to finally have a date with a boy she liked, but she completely forgot the details of where and when. She told me she remembers writing it in a note... but she doesn't think she saved it!!
She shared with us an export of her laptop files.
```

## Chall procedure
Extracting files, and running `tree` command, we can see interesting data into `TabState` folder. In Windows 11, notepad has implemented a feature to repopulate previously open notepad tabs - both saved and unsaved. those files are saved into `C:\Users\*\AppData\Local\Packages\Microsoft.WindowsNotepad_8wekyb3d8bbwe\LocalState\TabState\*.bin`
```
#C/Users/Tabby
.
├── AppData
│   ├── Local
│   │   ├── Microsoft
│   │   │   └── Windows
│   │   │       ├── Caches
│   │   │       ├── History
│   │   │       ├── INetCache
│   │   │       ├── Temporary Internet Files
│   │   │       └── UsrClass.dat
│   │   ├── Packages
│   │   │   ├── Microsoft.MicrosoftEdge_8wekyb3d8bbwe
│   │   │   │   └── LocalState
│   │   │   ├── Microsoft.Windows.Photos_8wekyb3d8bbwe
│   │   │   │   └── LocalState
│   │   │   └── Microsoft.WindowsNotepad_8wekyb3d8bbwe
│   │   │       └── LocalState
│   │   │           └── TabState
│   │   │               ├── 002d2531-9aff-42b1-b54d-b178c88063b4.bin
│   │   │               ├── 04165ca3-c82b-42ca-ab07-0c774ae66efd.bin
│   │   │               ├── 056941ef-d51d-4e57-9a55-b59d58bf3fcb.bin
│   │   │               ├── 14623d59-ad8c-43a8-b669-587f049a1516.bin
│   │   │               ├── 17de440f-3f69-4d8a-94fe-f3d4b9cf0c3f.bin
│   │   │               ├── 1aebb59c-5d51-41f1-918e-dec9e1a28ce1.bin
│   │   │               ├── 2d755c27-5840-47ad-a4ca-ed8041dd3047.bin
│   │   │               ├── 2e0dd6b6-ba93-4efc-9fd4-985dad74869a.bin
│   │   │               ├── 414e4071-60e6-4bb6-9a5a-f1e5bf6fe79c.bin
│   │   │               ├── 45dcdbe4-26b5-4e0b-ba2d-29e9e9c1e11b.bin
│   │   │               ├── 4f1c96a1-960c-4cee-9751-fe4b4f59fdd0.bin
│   │   │               ├── 5a57ac85-7e99-4bfc-9e13-f0d28a2bcc20.bin
│   │   │               ├── 66f955a8-6994-47c6-8326-0f128dafd0b9.bin
│   │   │               ├── 68d7e607-77c4-4d35-8ef2-0170a84efe5f.bin
│   │   │               ├── 68fefe2f-a7a6-4afa-b383-7fdc142aadde.bin
│   │   │               ├── 711f26f1-0eff-4a34-a78c-03562e44a36b.bin
│   │   │               ├── 7458196e-e979-4d94-982a-246fca3db028.bin
│   │   │               ├── 7ba066a2-e0cb-4c06-9339-316411a3da27.bin
│   │   │               ├── 9925cc8a-6440-4128-acae-f31541130a5e.bin
│   │   │               ├── 9bf7ca49-e491-4691-a21a-f3263bb695a2.bin
│   │   │               ├── 9e96bd4b-4155-4558-b97a-edcdf01d4584.bin
│   │   │               ├── a16d5079-b2f7-4a54-b3d5-b32256c4f238.bin
│   │   │               ├── a2048a5f-5cb5-460d-8ce6-70899de24d9c.bin
│   │   │               ├── a9da0602-fcd2-4793-9bab-70276e881006.bin
│   │   │               ├── af1fbc46-41cb-4d4b-9c34-02b874bfe9c6.bin
│   │   │               ├── b5074fe7-4f54-4728-afe9-1c063d211a82.bin
│   │   │               ├── b5154796-9d23-43ce-8a6c-c373e63f22c0.bin
│   │   │               ├── bcd5d203-1523-4b86-a572-c1c3afded478.bin
│   │   │               ├── c3cbe154-ef26-4e93-9183-c7fd323fe8c0.bin
│   │   │               ├── c4b77218-ef21-4a7f-9814-e4444f82475a.bin
│   │   │               ├── cb2f0c84-6293-4e63-8575-78dc879945e0.bin
│   │   │               ├── cd01dd8e-32f6-4f88-b9bb-4009afca3fea.bin
│   │   │               ├── dcfa4d00-41c8-439a-b1bd-2706dd8dbe0d.bin
│   │   │               ├── dea21c9d-4534-4d38-a60b-0a5c1b9b5928.bin
│   │   │               ├── e21dc9ae-2a03-42bf-8972-35ce8d524695.bin
│   │   │               ├── e6a849ab-6f02-452c-98e7-cdb03c577818.bin
│   │   │               ├── e86c9910-afca-4e83-87f6-600ed08a0570.bin
│   │   │               ├── ed9b5775-f35a-4770-a35e-e3c24b8bed47.bin
│   │   │               └── f1473e57-7637-4bd0-8158-53715ea20630.bin
│   │   └── Temp
│   ├── LocalLow
│   │   └── Microsoft
│   └── Roaming
│       └── Microsoft
│           └── Windows
│               ├── Recent
│               ├── Start Menu
│               │   └── Programs
│               └── Templates
├── Desktop
│   └── desktop.ini
├── Documents
│   └── desktop.ini
├── Downloads
│   └── desktop.ini
├── Favorites
├── Links
├── Music
│   └── desktop.ini
├── NTUSER.DAT
├── OneDrive
├── Pictures
│   └── desktop.ini
├── Saved Games
├── Searches
└── Videos
    └── desktop.ini

38 directories, 47 files
```

Move to `TabState folder`, we need to identify where is the Tabby note, we can use `grep`
```bash
grep -rw "f.*l.*a.*g.*{" *

# output
Binary file 2e0dd6b6-ba93-4efc-9fd4-985dad74869a.bin matches`
```

Then just dump the `2e0dd6b6-ba93-4efc-9fd4-985dad74869a.bin` content with `xxd`

```bash
00000000: 4e50 0000 0100 0001 0000 0301 0101 0000  NP..............
00000010: 8120 48e2 0000 ba03 3dd8 96dc 3dd8 96dc  . H.....=...=...
00000020: 2000 4400 6100 7400 6500 2000 7700 6900   .D.a.t.e. .w.i.
00000030: 7400 6800 2000 4500 7200 6900 6300 2100  t.h. .E.r.i.c.!.
00000040: 2100 2100 2000 3dd8 96dc 3dd8 96dc 0d00  !.!. .=...=.....
00000050: 0d00 6f00 6d00 6700 6700 6700 6700 6700  ..o.m.g.g.g.g.g.
00000060: 2000 6900 2700 6d00 2000 7300 6f00 6f00   .i.'.m. .s.o.o.
00000070: 6f00 2000 6500 7800 6300 6900 7400 6500  o. .e.x.c.i.t.e.
00000080: 6400 2000 3dd8 0dde 0d00 6800 6500 2000  d. .=.....h.e. .
00000090: 6100 6300 7400 7500 6100 6c00 6c00 7900  a.c.t.u.a.l.l.y.
000000a0: 2000 6100 7300 6b00 6500 6400 2000 6d00   .a.s.k.e.d. .m.
000000b0: 6500 2000 6f00 7500 7400 2100 2100 2100  e. .o.u.t.!.!.!.
000000c0: 2000 6900 2000 6300 6100 6e00 2700 7400   .i. .c.a.n.'.t.
000000d0: 2000 6200 6500 6c00 6900 6500 7600 6500   .b.e.l.i.e.v.e.
000000e0: 2000 6900 7400 0d00 0d00 4400 6500 7400   .i.t.....D.e.t.
000000f0: 6100 6900 6c00 7300 2000 7300 6f00 2000  a.i.l.s. .s.o. .
00000100: 6900 2000 6400 6f00 6e00 1920 7400 2000  i. .d.o.n.. t. .
00000110: 6600 6f00 7200 6700 6500 7400 3a00 0d00  f.o.r.g.e.t.:...
00000120: 2d00 2000 7700 6800 6500 6e00 3a00 2000  -. .w.h.e.n.:. .
00000130: 7300 6100 7400 7500 7200 6400 6100 7900  s.a.t.u.r.d.a.y.
00000140: 2c00 2000 7300 6500 7000 7400 2000 3100  ,. .s.e.p.t. .1.
00000150: 3400 7400 6800 2c00 2000 3700 3a00 3000  4.t.h.,. .7.:.0.
00000160: 3000 7000 6d00 0d00 2d00 2000 7700 6800  0.p.m...-. .w.h.
00000170: 6500 7200 6500 3a00 2000 5300 7400 6100  e.r.e.:. .S.t.a.
00000180: 7200 6200 7500 6300 6b00 7300 2000 6f00  r.b.u.c.k.s. .o.
00000190: 6e00 2000 4d00 6100 6900 6e00 2000 5300  n. .M.a.i.n. .S.
000001a0: 7400 7200 6500 6500 7400 2000 1526 0d00  t.r.e.e.t. ..&..
000001b0: 2d00 2000 6100 6600 7400 6500 7200 2000  -. .a.f.t.e.r. .
000001c0: 6d00 6100 7900 6200 6500 2000 6d00 6f00  m.a.y.b.e. .m.o.
000001d0: 7600 6900 6500 2000 6100 7400 2000 7400  v.i.e. .a.t. .t.
000001e0: 6800 6500 2000 7000 6c00 6100 7a00 6100  h.e. .p.l.a.z.a.
000001f0: 2000 3cd8 acdf 0d00 0d00 6200 7400 7700   .<.......b.t.w.
00000200: 2000 7400 6800 6500 2000 7700 6900 6600   .t.h.e. .w.i.f.
00000210: 6900 2000 6100 7400 2000 7400 6800 6100  i. .a.t. .t.h.a.
00000220: 7400 2000 7300 7400 6100 7200 6200 7500  t. .s.t.a.r.b.u.
00000230: 6300 6b00 7300 2000 6900 7300 2000 7300  c.k.s. .i.s. .s.
00000240: 6f00 6f00 6f00 6f00 2000 7700 6500 6900  o.o.o.o. .w.e.i.
00000250: 7200 6400 2c00 0d00 7400 6800 6500 7900  r.d.,...t.h.e.y.
00000260: 2000 7400 6f00 6c00 6400 2000 6d00 6500   .t.o.l.d. .m.e.
00000270: 2000 7400 6800 6500 2000 7000 6100 7300   .t.h.e. .p.a.s.
00000280: 7300 7700 6f00 7200 6400 2000 6900 7300  s.w.o.r.d. .i.s.
00000290: 3a00 2000 6600 6c00 6100 6700 7b00 3100  :. .f.l.a.g.{.1.
000002a0: 3600 3500 6400 3100 3900 6200 3600 3100  6.5.d.1.9.b.6.1.
000002b0: 3000 6300 3000 3200 6200 3200 3800 3300  0.c.0.2.b.2.8.3.
000002c0: 6600 6300 3100 6100 3600 6200 3400 6100  f.c.1.a.6.b.4.a.
000002d0: 3500 3400 6300 3400 6100 3500 3800 7d00  5.4.c.4.a.5.8.}.
000002e0: 0d00 0d00 6800 6500 1920 7300 2000 7300  ....h.e.. s. .s.
000002f0: 6f00 6f00 6f00 2000 6300 7500 7400 6500  o.o.o. .c.u.t.e.
00000300: 2100 2100 2100 2000 6900 2000 7700 7200  !.!.!. .i. .w.r.
00000310: 6f00 7400 6500 2000 6900 7400 2000 6100  o.t.e. .i.t. .a.
00000320: 6c00 6c00 2000 6400 6f00 7700 6e00 2000  l.l. .d.o.w.n. .
00000330: 6a00 7500 7300 7400 2000 6900 6e00 2000  j.u.s.t. .i.n. .
00000340: 6300 6100 7300 6500 2000 6900 2000 6600  c.a.s.e. .i. .f.
00000350: 6f00 7200 6700 6500 7400 2000 6c00 6f00  o.r.g.e.t. .l.o.
00000360: 6c00 0d00 6300 6100 6e00 1920 7400 2000  l...c.a.n.. t. .
00000370: 7700 6100 6900 7400 2100 2100 2000 3dd8  w.a.i.t.!.!. .=.
00000380: 95dc 3dd8 95dc 3dd8 95dc 0d00 c357 03ed  ..=...=......W..
```

Flag `flag{165d19b610c02b283fc1a6b4a54c4a58}`
