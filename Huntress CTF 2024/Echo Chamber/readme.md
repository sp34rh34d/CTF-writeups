## Name: Echo Chamber
#### Author: @JohnHammond#6971
#### Category: Scripting
#### Difficulty: N/D
#### Description: Is anyone there? Is anyone there? I'm sending myself the flag! I'm sending myself the flag!

## Procedure
This technique is knowns as  ```drop by drop```, the pcapng file is sending our flag into icmp requests, we can recover the flag using the follow python code.
```
import pyshark

cap = pyshark.FileCapture('echo_chamber.pcap', display_filter="frame.number >=31773 && frame.number <= 31847 and icmp.type ==8")

out=""
for pkt in cap:
    if hasattr(pkt.icmp, 'data'):
        out+= pkt.icmp.data[16:18]

print(bytes.fromhex(out))
```

<img width="950" alt="Screenshot 2025-02-10 at 11 10 06 AM" src="https://github.com/user-attachments/assets/c189a188-83a7-4eb2-bd19-b474e0076b7a" />
