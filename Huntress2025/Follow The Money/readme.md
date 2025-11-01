## Chall description
```
Category: Forensic
Hey Support Team,
We had a bit of an issue yesterday that I need you to look into ASAP. There's been a possible case of money fraud involving our client, Harbor Line Bank. They handle a lot of transfers for real estate down payments, but the most recent one doesn't appear to have gone through correctly.
Here's the deal, we need to figure out what happened and where the money might have gone. The titling company is looping in their incident response firm to investigate from their end. I need you to quietly review things on our end and see what you can find. Keep it discreet and be passive.
I let Evelyn over at Harbor Line know that someone from our team might reach out. Her main email is offline right now just in case it was compromised, she's using a temporary address until things get sorted out: evelyn.carter@51tjxh.onmicrosoft.com

The password to the ZIP archive below is follow_the_money
```

## Procedure

Chall files
```bash
tree .
.
├── email 1 - FTM.eml
├── email 2 - FTM.eml
├── email 3 - FTM.eml
├── email 4 - FTM.eml
└── email 5 - FTM.eml

1 directory, 5 files
```

After read and parser all the `.eml` files, I found the url `https://evergatetltle.netlify.app/`, this is a little different from original url `https://evergatetitle.netlify.app/`, so let's start analysing this site.
```bash
  
  ██████  ███▄ ▄███▓ ▄▄▄        ██████  ██░ ██ ▓█████  ██▀███  
▒██    ▒ ▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░      ░     ░   ▒   ░  ░  ░   ░  ░░ ░   ░     ░░   ░ 
      ░         ░         ░  ░      ░   ░  ░  ░   ░  ░   ░     
Coded by: sp34rh34d
twitter: @spearh34d
Welcome to Smasher v1.2 [https://github.com/sp34rh34d/Smasher]
======================================================================================================
format: eml
file: /Users/adons/Downloads/follow_the_money/email 5 - FTM.eml
timezone: America/New_York
blacklist check: True
attachment check: False
attachment metadata: False
======================================================================================================
Parsing email...
+---+---------------+----------------------------------------------------------------------------------------------------------------+
| 0 | from          | justincase@evergatetitle.com                                                                                   |
+---+---------------+----------------------------------------------------------------------------------------------------------------+
| 1 | to            | ['evelyn.carter@harborline-bank.com']                                                                          |
+---+---------------+----------------------------------------------------------------------------------------------------------------+
| 2 | subject       | Re: 200 E. Wharf Drive issue                                                                                   |
+---+---------------+----------------------------------------------------------------------------------------------------------------+
| 3 | Delivery date | 2025-10-06 14:50:42-04:00                                                                                      |
+---+---------------+----------------------------------------------------------------------------------------------------------------+
| 4 | SPF           | from CH4PR17MB7292.namprd17.prod.outlook.com (2603:10b6:610:231::5) by MN6PR17MB6971.namprd17.prod.outloo      |
|   |               | k.com with HTTPS; Mon, 6 Oct 2025 18:50:45 +0000from SA1PR17MB4545.namprd17.prod.outlook.com (2603:10          |
|   |               | b6:806:1ac::16) by CH4PR17MB7292.namprd17.prod.outlook.com (2603:10b6:610:231::5) with Microsoft SMTP Server ( |
|   |               | version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.9203.9; Mon, 6 Oct 2025 18:50:42 +0000
|   |               | [0mfrom SA1PR17MB4545.namprd17.prod.outlook.com ([fe80::ef44:377a:d20a:e3a3]) by SA1PR17MB4545.namprd17.p      |
|   |               | rod.outlook.com ([fe80::ef44:377a:d20a:e3a3%4]) with mapi id 15.20.9203.007; Mon, 6 Oct 2025 18:50:42 +0000
|   |               |                                                                                                                |
+---+---------------+----------------------------------------------------------------------------------------------------------------+

Extracting url from file /Users/demo/Downloads/follow_the_money/email 5 - FTM.eml

found: https://lh3.googleusercontent.com/sitesv/AICyYdZO75Mmm7G0vT2H8WEU0BBqFkOPQwWeUApDq9ZzJ2xSjY--1hrBzJm1X6NDSTvUsDdooQm022EVHW8mpJSk-qmvZ7qVcUz05Hk7iJm3eyiiejSi1I52kpQzQkuCWHqK4yaFzqtQ-cJacE54uSOPriZEok5tlk9sS20_WxFIZh152otT8ClserA4sQw=w1280"
found: https://evergatetltle.netlify.app/"
found: https://evergatetltle.netlify.app/">Evergate
found: https://lh3.googleusercontent.com/sitesv/AICyYdZzyHA-jJy9ss22XxxBfjOOacc3KyxIsVLZJaj9i8g3mZKDeR8YEkfnPKwODbt3GqxJlEkaxcfdUcZdU1P8NyXjS3hlN_Bsv7mMy5XpSW0M1moLT-E5k86eKiTKihRWEu8lziKk2-YTzkarqXkk3US7O-EvgU002rQZP0RxzoWXkveLR1XkaIgX=w1280"
found: https://harbor-line-bank.netlify.app/"
found: https://harbor-line-bank.netlify.app/"
found: https://lh3.googleusercontent.com/sitesv/AICyYdZO75Mmm7G0vT2H8WEU0BBqFkOPQwWeUApDq9ZzJ2xSjY--1hrBzJm1X6NDSTvUsDdooQm022EVHW8mpJSk-qmvZ7qVcUz05Hk7iJm3eyiiejSi1I52kpQzQkuCWHqK4yaFzqtQ-cJacE54uSOPriZEok5tlk9sS20_WxFIZh152otT8ClserA4sQw=w1280"
found: https://evergatetltle.netlify.app/"
found: https://evergatetltle.netlify.app/"
done
```

After visit the website, we can see a transfer button, trying with fake data this show us a base64 string `aHR0cHM6Ly9uMHRydXN0eC1ibG9nLm5ldGxpZnkuYXBwLw==`, the encoded value was `https://n0trustx-blog.netlify.app/`, and show us the username `N0TrustX`.
<img width="1212" height="396" alt="Screenshot 2025-10-22 at 10 06 39 PM" src="https://github.com/user-attachments/assets/1ee05936-366b-414c-aac3-bee2b890a2f4" />

**What is the username of the hacker?**\
`N0TrustX`

Checking the blog, we can see a link for `Github`, this has 1 repository with some interesting files.
<img width="1430" height="583" alt="Screenshot 2025-10-22 at 10 11 01 PM" src="https://github.com/user-attachments/assets/8d57e8d5-b91b-43da-9a11-c2839bcbcaa1" />

Reading the `spectre.html` file, we can see another base64 string with our second flag.
```html
<!-- Payload Modal -->
    <div id="payloadModal" class="fixed inset-0 w-full h-full flex items-center justify-center modal-overlay hidden z-50">
        <div class="terminal-window bg-black rounded-lg p-8 w-full max-w-2xl m-7 text-center">
            <h2 class="text-3xl font-bold text-glow mb-4">Payload Retrieved</h2>
            <p class="text-lg mb-6">Object Data:</p>
            <!-- This div will hold the DECODED object -->
            <div id="decodedPayloadContainer" class="bg-gray-900 p-9 rounded-lg text-2xl font-bold text-yellow-400">
                <!-- The decoded object will appear here -->
            </div>
            <!-- The Base64 encoded object is stored here, hidden from view -->
            <div id="encodedPayload" class="hidden">ZmxhZ3trbDF6a2xqaTJkeWNxZWRqNmVmNnltbHJzZjE4MGQwZn0=</div>
            <button id="closePayloadBtn" class="mt-8 action-button font-bold py-2 px-6 rounded-lg">Close</button>
        </div>
    </div>
```

```bash
echo "ZmxhZ3trbDF6a2xqaTJkeWNxZWRqNmVmNnltbHJzZjE4MGQwZn0=" | base64 -d
flag{kl1zklji2dycqedj6ef6ymlrsf180d0f}%
```


Flag `flag{kl1zklji2dycqedj6ef6ymlrsf180d0f}`

