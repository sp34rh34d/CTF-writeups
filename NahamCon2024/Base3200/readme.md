## Name: Base3200
#### Category: Scripting
#### Difficulty: easy
#### Description: You know what to do. 

## Procedure
run ```file``` command on theflag file
output ```theflag: ASCII text, with very long lines (65536), with no line terminators```
<br>
<br>
Running ```cat``` command on theflag file, shows me a base64 string, after ran the command ```cat theflag | base64 -d | base64 -d``` still returns a base64 string. so, the flag could be encoded by running base64 for 10 or more times.
<br>
<br>
I have created the following python code to get the flag
<br>
```
import base64

flag=""
with open('theflag','r') as base64_encode_file:
    flag=base64_encode_file.read()

while True:
    flag=base64.b64decode(flag)
    if b'flag' in flag:
        print(flag)
        break
```

output ```flag{340ff1bee05244546c91dea53fba7642}```
