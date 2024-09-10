## Name: Covert
#### Category: Forensics
#### Difficulty: N/D
#### Description: It appears there's been some shady communication going on in our network...

## Procedure
Checking the chall's files, we have the network capture ```chall.pcapng``` file, and tls keys ```keys.log```, from here we need to load the ```key.log``` file to be able to decrypt the traffic in pcapng file.
```
├── chall.pcapng
└── keys.log
```

I did it using tshark and start filtering the http requests with the command
```
tshark -r chall.pcapng -o tls.keylog_file:keys.log -Y "http" -T fields -e http.file_data
```

We recovered the follow interesting data
```
<html>
   <body>
   # ez covert transfer...
   from scapy.all import IP, TCP, send
   key = ??
   dst_ip = &#34;X.X.X.X&#34;
   dst_port = ?????
   src_ip = &#34;X.X.X.X&#34;
   src_port = ?????

   def encode_message(message):
       for letter in message:
           ip = IP(dst=dst_ip, src=src_ip, id=ord(letter)*key)
           tcp = TCP(sport=src_port, dport=dst_port)
           send(ip/tcp)

   encode_message(&#34;????????????&#34;)
   </body>
</html>
```
### py content
1) ```from scapy.all import IP, TCP, send``` This imports the necessary functions from Scapy to create and send IP and TCP packets.
2) ```key = ??``` It will be multiplied with the ASCII value of each character in the message you want to send.
3) ```dst_ip = "X.X.X.X"``` The destination IP address where the covert message will be sent.
4) ```dst_port = ?????``` The destination port number.
5) ```src_ip = "X.X.X.X"``` The source IP address from which the packets will be sent.
6) ```src_port = ?????``` The source port number.
7) ```def encode_message(message):``` This function encodes the message by manipulating the IP header.
8) ```ip = IP(dst=dst_ip, src=src_ip, id=ord(letter)*key)``` An IP packet is created where the id field of the packet is set to the ASCII value of the character (ord(letter)) multiplied by the key.
9) ```tcp = TCP(sport=src_port, dport=dst_port)``` A TCP segment is created with the specified source and destination ports.
10) ```send(ip/tcp)``` The IP packet containing the TCP segment is sent to the destination.

After analyzing the source code we have recovered from http request, we know that our flag was sent into the ID TCP header, so we need to dump each ID TCP from pcapng file, to do it we need to run the following command
```
tshark -r chall.pcapng -o tls.keylog_file:keys.log -T fields -e ip.id > ip_ids.txt
```

we have saved the ```IP IDs``` in the file ```ip_ids.txt``` file, each ID is in hex format, so we need to convert it to base16, and then we have to do an XOR operation de retrieve our flag, but we dont know the key used to encrypt the flag.
<br>
Reading the code again, we have ```key = ??```, this tells me, maybe the key is using only two digits, so we can try to do a bruteforce attack. I wrote the following python script.

```
for key in range(1,99):
	out=""
	for x in open('ip_ids.txt','r').read().split('\n'):
	    try:
	        t = int(int(x,base=16) / key)
	        out+=chr(t)

	    except:
	        pass
	if "csawctf" in out:
		print("key:",key,"message:",out)
```
output
```
key: 55 message: șdǬкʽǔΧĥ«ǀÙɜǞѨǅȈɋŘʳ΃csawctf{licen$e_t0_tr@nsmit_c0vertTCP$$$}
```

flag ```csawctf{licen$e_t0_tr@nsmit_c0vertTCP$$$}```

    
