## Name: Suspicious Drive
#### Category: Forensics
#### Difficulty: Hard
#### Description: An overseas branch of our company was almost hit by an attack from a well-known ransomeware group, but it seemed their final payload failed. We found a suspicious drive on premises, as well as a common string in our logs: PCTF{d)zn+d$+zqbb!t+h)!#+if+y)u+zi!l}. Can you help us figure out what this payload might have been?

## Procedure
this chall has the following files
```
suspiciousdrive/
├── config.txt
├── docs
│   ├── EULA
│   ├── full_documentation.html
│   ├── LICENSE
│   └── readme.txt
├── languages
│   └── be.json
├── loot
├── payloads
│   ├── extensions
│   │   ├── cucumber.sh
│   │   ├── debug.sh
│   │   ├── ducky_lang.sh
│   │   ├── get2_dhclient.sh
│   │   ├── get.sh
│   │   ├── mac_happy.sh
│   │   ├── requiretool.sh
│   │   ├── runpayload.sh
│   │   ├── run.sh
│   │   ├── setkb.sh
│   │   ├── waiteject.sh
│   │   ├── wait_for_notpresent.sh
│   │   ├── wait_for_present.sh
│   │   └── wait.sh
│   ├── library
│   │   └── get_payloads.html
│   ├── switch1
│   │   └── payload.txt
│   └── switch2
│       └── payload.txt
├── System Volume Information
│   ├── IndexerVolumeGuid
│   └── WPSettings.dat
├── tools
├── upgrade.html
├── version.txt
└── win7-win8-cdc-acm.inf

```

this chall talks about a suspicious drive, and the file structure look like for [Bash Bunny](https://github.com/hak5/bashbunny-payloads/tree/master), the chall says ``` but it seemed their final payload failed```, this one told me, check the payload.txt file, this file is where u write ur malicious code in order to convert it to ```.bin``` using tools like [hack5](https://payloadstudio.com/community/), example [malicious](https://www.bordergate.co.uk/getting-started-with-bash-bunny/)

checking the ```payload.txt```, the real payload was deleted ```PAYLOAD AUTOMATICALLY WIPED BY PATRIOT RANSOMWARE CORPORATION!(env) ```.
#### Attack theory
This was a close attack, the hacker loads the malicious code using US keyboard configuration, maybe with [hack5](https://payloadstudio.com/community/), but if we see into ```language``` folder, this has another keyboard layout ```be```, that didnt allow the execute of the real payload, and show the output as ```d)zn+d$+zqbb!t+h)!#+if+y)u+zi!l```.

so, we have to take the payload ```d)zn+d$+zqbb!t+h)!#+if+y)u+zi!l``` and create our bin file using US keyboard again, and then try to recover using ```be``` keyboard again. we can do this using tools like [DuckToolkit](https://github.com/kevthehermit/DuckToolkit/tree/master).

1) create the payload, create ```payload.txt``` file with ```STRING d)zn+d$+zqbb!t+h)!#+if+y)u+zi!l```
2) create the ```bin``` file using US keyboad with the commadn ```python3 ducktools.py -e payload.txt -l us injection.bin```
3) recover the flag, but this time using ```be``` Keyboard configuration with the command ```python3 ducktools.py -d injection.bin -l be flag.txt```

Flag ```PCTF{d0wn_d4_wabb1t_h013_if_y0u_wi1l}```


