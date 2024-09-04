## Name: Geometry Dash 2.1
#### Category: forensic
#### Difficulty: N/A
#### Description: I would give you the flag but I can't let go (haha get it). use GDBrowser for the last step btw.

## Procedure
The CCLocalLevels.dat file is used by the game Geometry Dash to store user-created levels and other information related to downloaded levels. This file is stored in the game's data folder and is encrypted to protect the information it contains.

![Screenshot 2024-09-03 at 8 24 29 PM](https://github.com/user-attachments/assets/5d3f726b-8667-4274-b5c7-a2f9c8edfc3a)

After search about the file, i found a site called [GDColon](https://gdcolon.com/gdsave/) that allow us to read our CCLocalLevels.dat file. We can see the string ```flag is in the level somewhere```.

![Screenshot 2024-09-03 at 8 29 18 PM](https://github.com/user-attachments/assets/184c550c-6cab-4d86-829b-59c74c058270)

Select download button, and check for the json file, and we got interesting data like ```author```

![Screenshot 2024-09-03 at 8 32 43 PM](https://github.com/user-attachments/assets/1547de0d-5d4c-4319-ab49-3ca7ea8e6552)
![Screenshot 2024-09-03 at 8 34 45 PM](https://github.com/user-attachments/assets/306d7495-76c5-4f5d-ab45-b3312cbb457b)

the challenge description talks about use [GDBrowser](https://gdbrowser.com/) for the last step, so we are going to search ```CSCTFa52de5``` user

![Screenshot 2024-09-03 at 8 41 17 PM](https://github.com/user-attachments/assets/3703c50d-95b5-4440-b5af-ed806c8ae015)

I checked into comments section, and boom, the flag was there :)
![Screenshot 2024-09-03 at 8 41 48 PM](https://github.com/user-attachments/assets/540bdf6b-0cd7-4c0e-81b1-9173955fab57)

flag ```CSCTF{geometry_dash_d0895c120d671b}```
