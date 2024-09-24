## Name: Simple Exfiltration
#### Category: Forensics
#### Difficulty: Easy
#### Description: We've got some reports about information being sent out of our network. Can you figure out what message was sent out.

## Procedure
We can start opening the pcapng file with Wireshark, and it shows some interesting http requests, we can filter using ```http``` query or using tshark with the following command ``` tshark -r exfiltration_activity_pctf_challenge.pcapng -Y "http" -T fields -e "http.file_data"```

And we can see that every http request has the following data.

```
<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
</ul>
<hr>
</body>
</html>
```

this look like a rabbot hole, you can see some echo ping requests, we can filter the icmp packets using ```icmp.type==0``` for icmp echo reply and ```icmp.type==8``` for icmp echo request, using both filters, you can see that every ttl value change for icmp echo request, use the following command to extract ttl data ``` tshark -r exfiltration_activity_pctf_challenge.pcapng -Y "icmp.type==8" -T fields -e "ip.ttl"```
output
```
112,99,116,102,123,116,105,109,101,95,116,111,95,108,105,118,101,95,101,120,102,105,108,116,114,97,116,105,111,110,125
```

The attacker is using the ttl value to hide every char using ord numbers, example: for letter ```a```  its ord number is ```97```, u can check that using the command ```python3 -c "print(ord('a'))"```, for letter ```p``` the ord number is ```112```, this is an attack knowns as Drop by Drop attack using icmp.

U can recover the flag with the following script.
```
ttl=[112,99,116,102,123,116,105,109,101,95,116,111,95,108,105,118,101,95,101,120,102,105,108,116,114,97,116,105,111,110,125]
out=""
for x in ttl:
    out+=chr(x)

print(out)
```

output 
```
pctf{time_to_live_exfiltration}
```



