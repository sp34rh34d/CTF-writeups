## Name: Hidden Streams
#### Author: Adam Rice - @adam.huntress
#### Category: Forensics
#### Difficulty: N/D
#### Description: Beneath the surface, secrets glide, A gentle flow where whispers hide. Unseen currents, silent dreams, Carrying tales in hidden streams. Can you find the secrets in these Sysmon logs?

## Procedure
Hidden Streams means Alternate Data Streams - ADS and this is used into NTFS as an evasion technique, the command is very simple. 

```type malicious_file.exe > test.txt:malicious_file.exe```

Sysmon event ID for ```File stream created``` is ```15```, dump the evtx data with command ```evtx_dump.py Sysmon.evtx > outout.data``` and then seek for event id 15 using the following filter ```<EventID Qualifiers="">15</EventID>```

We got the following code

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event"><System><Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}"></Provider>
<EventID Qualifiers="">15</EventID>
<Version>2</Version>
<Level>4</Level>
<Task>15</Task>
<Opcode>0</Opcode>
<Keywords>0x8000000000000000</Keywords>
<TimeCreated SystemTime="2024-08-28 00:19:14.033585"></TimeCreated>
<EventRecordID>15107</EventRecordID>
<Correlation ActivityID="" RelatedActivityID=""></Correlation>
<Execution ProcessID="6968" ThreadID="6552"></Execution>
<Channel>Microsoft-Windows-Sysmon/Operational</Channel>
<Computer>WIN-UL3TI0T0LM6.test.local</Computer>
<Security UserID="S-1-5-18"></Security>
</System>
<EventData><Data Name="RuleName">-</Data>
<Data Name="UtcTime">2024-08-28 00:19:11.899</Data>
<Data Name="ProcessGuid">{b56ae52f-6533-66ce-be00-000000000900}</Data>
<Data Name="ProcessId">2460</Data>
<Data Name="Image">C:\Windows\system32\WindowsPowerShell\v1.0\PowerShell.exe</Data>
<Data Name="TargetFilename">C:\Temp:$5GMLW</Data>
<Data Name="CreationUtcTime">2024-08-28 00:00:22.726</Data>
<Data Name="Hash">SHA1=B1C3068058ADDF418D3E1418CD28414325B7A757,MD5=E754797031C6B367D0B6209092F34B3B,SHA256=F414CBA3A5D8C6EF18B1BE31F09C848447DDB37A5712E36EB7825E4E1EFAE868,IMPHASH=00000000000000000000000000000000</Data>
<Data Name="Contents">ZmxhZ3tiZmVmYjg5MTE4MzAzMmY0NGZhOTNkMGM3YmQ0MGRhOX0=  </Data>
<Data Name="User">WIN-UL3TI0T0LM6\Administrator</Data>
</EventData>
</Event>
```

Now just run ```echo ZmxhZ3tiZmVmYjg5MTE4MzAzMmY0NGZhOTNkMGM3YmQ0MGRhOX0== | base64 -d```

flag ```flag{bfefb891183032f44fa93d0c7bd40da9}```




