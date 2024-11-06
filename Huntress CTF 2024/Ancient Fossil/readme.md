## Name: Ancient Fossil
#### Author: @JohnHammond
#### Category: Forensics
#### Difficulty: N/D
#### Description: All things are lost to time...

## Procedure
The command ```file ancient.fossil ``` tells us this is a sqlite database.

```
ancient.fossil: SQLite 3.x database (Fossil repository), last written using SQLite version 3046000, file counter 415, database pages 154, cookie 0x28, schema 4, UTF-8, version-valid-for 415
```

From here we just need to open the file using tools like sql3 or fossil, but i just take another way. I just extract the content using the command ```binwalk -e ancient.fossil``` and then just do ```strings * | grep "flag{"```  to extract the flag.

![image](https://github.com/user-attachments/assets/df94f9e6-198a-45a6-b9e1-0a8fe998f7b4)

flag ```flag{2ed33f365669ea9f10b1a4ea4566fe8c}```
