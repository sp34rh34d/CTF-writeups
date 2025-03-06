## Name: Free Range Packets
#### Author: @Soups71
#### Category: forensics
#### Difficulty: easy
#### Description: My friend recently has decided to stop trusting WiFi, so he decided to send me information over Bluetooth. In order to prove that you can capture data from Bluetooth without being the intended recipient, I took this packet capture with a 2 dollar bluetooth adapter. 

## Procedure
Using wireshark, we can see the flag into btl2cap.payload field 1 by 1.

![Screenshot 2025-03-05 at 6 43 59 PM](https://github.com/user-attachments/assets/872862cc-0b87-43c7-8da6-502d3980c94e)

I just filter every ```btl2cap.payload``` packet using ```tshark``` with the following command.
```
tshark -r freeRangePackets.pcapng -Y "btl2cap.payload" -T fields -e btl2cap.payload | sed 's,0bef03,,g' | sed 's,9a,,g' | sed 's,09ff01065c,,g' |xxd -r -p                                                                                              
```

flag ```flag{b5be72ab7e0254c056ffb57a0db124ce}   ```
