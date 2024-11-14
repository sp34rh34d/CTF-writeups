## Name: Base-p-
#### Author: Izzy Spering
#### Category: Misc
#### Difficulty: N/D
#### Description: That looks like a weird encoding, I wonder what it's based on.

## Procedure
Base -p-, if you have used nmap you know that -p- means scan all the ports ```65535```, so maybe this is talking about ```base65536``` encoding, you can use the site [base65536](https://www.better-converter.com/Encoders-Decoders/Base65536-Decode) and then we recovered the following base64 string 
```
H4sIAG0OA2cA/+2QvUt6URjHj0XmC5ribzBLCwKdorJoSiu9qRfCl4jeILSICh1MapCINHEJpaLJVIqwTRC8DQ5BBQ0pKtXUpTej4C4lBckvsCHP6U9oadDhfL7P85zzPTx81416LYclYgEAOLgOGwKgxgnrJKMK8j4kIaAwF3TjiwCwBejQQDAshK82cKx/2BnO3xzhmEmoMWn/qdU+ntTUIO8gmOw438bbCwRv3Y8vE2ens9y5sejat497l51sTRO18E8j2aSAAkixqhrKFl8E6fZfotmMlw7Z3NKFmvp92s8+HMg+zTwaycvVQlnSn7FYW2LFYY0+X18JpB9LCYliSm6LO9QXvfaIbJAqvNsL3lTP6vJ596GyKIaXBnNdRJahnqYLnlQ4d+LfbQ91vpH0Y4NSYwhk8tmv/5vFZFnHWrH8qWUkTfgfUPXKcFVi+5Vlx7V90OjLjZqtqMMH9FhMZfGUALnotancBQAA
```

Now run the command 
```
echo "H4sIAG0OA2cA/+2QvUt6URjHj0XmC5ribzBLCwKdorJoSiu9qRfCl4jeILSICh1MapCINHEJpaLJVIqwTRC8DQ5BBQ0pKtXUpTej4C4lBckvsCHP6U9oadDhfL7P85zzPTx81416LYclYgEAOLgOGwKgxgnrJKMK8j4kIaAwF3TjiwCwBejQQDAshK82cKx/2BnO3xzhmEmoMWn/qdU+ntTUIO8gmOw438bbCwRv3Y8vE2ens9y5sejat497l51sTRO18E8j2aSAAkixqhrKFl8E6fZfotmMlw7Z3NKFmvp92s8+HMg+zTwaycvVQlnSn7FYW2LFYY0+X18JpB9LCYliSm6LO9QXvfaIbJAqvNsL3lTP6vJ596GyKIaXBnNdRJahnqYLnlQ4d+LfbQ91vpH0Y4NSYwhk8tmv/5vFZFnHWrH8qWUkTfgfUPXKcFVi+5Vlx7V90OjLjZqtqMMH9FhMZfGUALnotancBQAA" | base64 -d > decoded.bin
```
then run the command ```file decoded.bin``` we can see a ```compressed``` data
```
decoded.bin: gzip compressed data, last modified: Sun Oct  6 22:25:49 2024, original size modulo 2^32 1500
```

Now, just extract the content with ```7z e decoded.zip``` and then run ```file decoded```, now we can see a PNG file
```
decoded: PNG image data, 1400 x 200, 8-bit/color RGB, non-interlaced
```
![decoded](https://github.com/user-attachments/assets/c822b2e2-e5e8-46ff-a1c0-3d94711509e8)

i have used the site [ImageColorPicker](https://imagecolorpicker.com/) to extract RGB data in hex

![2024-11-13_23-43](https://github.com/user-attachments/assets/2d409a5a-9967-4afa-aa9c-128a95699578)

hex data ```666c61677b35383663663863383439633937333065613762323131326666663339666636617d20```
flag ```flag{586cf8c849c9730ea7b2112fff39ff6a} ```




