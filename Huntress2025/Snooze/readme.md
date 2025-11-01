## Chall description
```
Category: Warmups
Don't bug me, I'm sleeping! Zzzz... zzz... zzzz....

Uncover the flag from the file presented.
```


## Procedure
I have started running `file` command. Output `snooze: compress'd data 16 bits`. 

After that I just ran `tar -xvf snooze`, and this show me the flag 👀
```
tar -xvf Downloads/snooze 
tar: Missing type keyword in mtree specification
x flag{c1c07c90efa59876a97c44c2b175903e}
```

Flag `flag{c1c07c90efa59876a97c44c2b175903e}`
