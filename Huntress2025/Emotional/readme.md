## Chall description
```
Category: Web
Don't be shy, show your emotions! Get emotional if you have to! Uncover the flag.
```
<img width="1184" height="548" alt="Screenshot 2025-10-06 at 9 19 45 AM" src="https://github.com/user-attachments/assets/23c2cc6b-4558-49cc-a6e7-cf14f83b6886" />


## Procedure
Chall files
```
tree .
.
├── Dockerfile
├── flag.txt
├── package.json
├── public
│   └── scripts
│       └── client.js
├── server.js
└── views
    └── index.ejs
```
### Server.js content
```javascript
const fs = require('fs');
const ejs = require('ejs');
const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

let profile = {
    emoji: "😊"
};

app.post('/setEmoji', (req, res) => {
    const { emoji } = req.body;
    profile.emoji = emoji;
    res.json({ profileEmoji: emoji });
});

app.get('/', (req, res) => {
    fs.readFile(path.join(__dirname, 'views', 'index.ejs'), 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Internal Server Error');
        }
        
        const profilePage = data.replace(/<% profileEmoji %>/g, profile.emoji);
        const renderedHtml = ejs.render(profilePage, { profileEmoji: profile.emoji });
        res.send(renderedHtml);
    });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
**Code description**
* `POST /setEmoji` accepts emoji from the request body and stores it in `profile.emoji`, no input validation for this.
* The code does a manual string `replace()` on the template then calls `ejs.render()` with the same value after refresh.
* The code injects the raw user-supplied emoji string into the template text before calling `ejs.render`, this can allow a `SSTI` attack, we can check that using `<%= 7*7 %>`

Intercept the http request with burpsuite and use the payload `</span><%= 7*7 %><span>`, use urlencode.
<img width="1211" height="349" alt="Screenshot 2025-10-06 at 9 19 58 AM" src="https://github.com/user-attachments/assets/f683c7b8-5bb5-47ae-9a17-01aa7eb55e3a" />

After send the payload, refresh the website to inject and execute our payload, You will see `49`, this confirms the `SSTI` vulnerability.
<img width="917" height="424" alt="Screenshot 2025-10-06 at 9 44 38 AM" src="https://github.com/user-attachments/assets/d6a6e1ab-75dc-47d7-bf73-dd9e9dd382af" />

After try with diff payloads (yes i broke the chall after send some payloads 😂), finally got the flag using `</span><%=+process.mainModule.require('fs').readFileSync('flag.txt','utf8')+%><span>`

<img width="771" height="125" alt="Screenshot 2025-10-06 at 9 20 45 AM" src="https://github.com/user-attachments/assets/abf0d67a-ef7c-4eca-bcdd-3572ffc0e591" />

<img width="1211" height="500" alt="Screenshot 2025-10-06 at 9 26 40 AM" src="https://github.com/user-attachments/assets/aca46f12-2bf6-43e6-8f0c-516fb1023a86" />

Flag `flag{8c8e0e59d1292298b64c625b401e8cfa}`



