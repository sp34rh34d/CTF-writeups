## Name: System Code
#### Author: Truman Kain
#### Category: Misc
#### Difficulty: N/D
#### Description: Follow the white rabbit.
NOTE: Bruteforce is permitted for this challenge instance if you feel it is necessary.

## Procedure
the chall asks for a password or something like that, it sends a GET request to ```challenge.ctf.games:30984/enter=test``` it returns the msg ```Incorrect. You will receive the flag with the correct input.```.

I was trying with ```rockyou.txt``` file and sending some sqli payloads,etc but no luck, since we dont have the source code i was checking the website code with inpect option from the browser.

The website has a the following url in the source code ```https://github.com/Rezmason/matrix```, this is a github project with the matrix theme. but it also has some interesting files path.

I was using that files path as reference to check in the challenges website, i was stuck  :|

After a hint, i downloaded the github project with ```git clone https://github.com/Rezmason/matrix.git``` and then enumerate every single file with the command ```find . -name "*" 2>/dev/null | sed -e 's,\./,,g' | grep ".js" > files.txt```.

Now i wrote the following python code to do a cmp with the chall website and see if there is a diff file in the website.
```
import requests

files = open("matrix/files.txt","r").read()

chall_url="http://challenge.ctf.games:30984/"
github_url="https://raw.githubusercontent.com/Rezmason/matrix/refs/heads/master/"

for x in files.split("\n"):
    if x:
        res1 = requests.get(chall_url + x)
        res2 = requests.get(github_url + x)

        if len(res1.text) != len(res2.text):
            print(f"file: {x} [{len(res1.text)}] [{len(res2.text)}]")
```

![image](https://github.com/user-attachments/assets/7ce9d760-d952-4ad5-a667-e02a46ac53e8)

We have detected the file ``` js/config.js```, the chall says ```Follow the white rabbit.```, ```twr```, if you looking for ```twr``` in ```js/config.js``` u will see  ``` backupGlyphsTwr: ["a", "b", "c", "d", "e", "f"], ```

from here u can use ```abcdef``` to create ur wordlist and do a bruteforce with burpsuite or maybe doing ur own script. here is my python script.

```
import requests
from itertools import product
from concurrent.futures import ThreadPoolExecutor, as_completed

characters = "abcdef"
wordlist = [''.join(p) for length in range(6, 7) for p in product(characters, repeat=length)]
chall_url = "http://challenge.ctf.games:30984/enter="

def test_password(password):
    try:
        res = requests.get(chall_url + password)
        print(f"testing pass:{password}",end="\r")
        if "flag{" in res.text:
            print(f"\nPassword: {password}\n{res.text}")
            return True
    except:
        pass
    return False

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(test_password, word) for word in wordlist]
    for future in as_completed(futures):
        if future.result():
            break
```
![image](https://github.com/user-attachments/assets/38911616-9cf3-4d6a-9d98-527f660c2db4)


flag ```flag{dc9edf4624504202eec5d3fab10bbccd}```

