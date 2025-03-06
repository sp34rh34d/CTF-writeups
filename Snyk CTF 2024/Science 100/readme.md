## Name: Science 100
#### Author: @HuskyHacks
#### Category: Warmups
#### Difficulty: easy
#### Description: Patrolling the Mojave almost makes you wish for a nuclear winter.


## Procedure
Connect to remote server using netcat, here it asks you for a secret word to recover the flag, but here u can see the following 
```
Welcome to Robco Industries (TM) Termlink

>SET TERMINAL/INQUIRE

RIT-V300

>SET FILE/PROTECTION=OWNER:RWED ACCOUNTS.F
>SET HALT RESTART/MAINT
0xF4F0  !^>{|{}#=]<]  0xF5F0  ^<.@<,>;]/}]
0xF4FC  #,!.(!:,]:|)  0xF5FC  ;__(:;(?%_#)
0xF508  }[]]<=--|{)&  0xF608  ^(!+}}[?})>=
0xF514  %=+&[^&<=]+(  0xF614  #/.!;+>&)-#|
0xF520  :PARTNER@&>%  0xF620  !^|(:)>?-$_}
0xF52C  [_-$]=(/_};,  0xF62C  NURSERY%@;[)
0xF538  =-/,;DISPLAY  0xF638  =@)<.>:>=}}:
0xF544  %!<-{=@-_-+[  0xF644  -(]<_$.))>&%
0xF550  ##}PASTURE#^  0xF650  ,.^##!(#)%#_
0xF55C  {&__|;#;-=#^  0xF65C  /{}<;=$^/+=|
0xF568  &[[|%&]&-.+^  0xF668  :-[?$]+.-#>[
0xF574  ,<.(&[_#.)@:  0xF674  %RECRUIT*&^+
0xF580  {;;/);^!^(=;  0xF680  $(-MAXIMUM,]
0xF58C  );?,/#/:]_%=  0xF68C  TRAGEDY$)--}
0xF598  ;@)!|JUSTIFY  0xF698  ([>_-/)<=:+<
0xF5A4  [[#&]{;^}<?/  0xF6A4  (<}][>=]#!;!
```
If you check the output, you can find the words ```PARTNER, NURSERY, DISPLAY, PASTURE, RECRUIT, MAXIMUM, TRAGEDY and JUSTIFY```, after try with that we were able to recover the flag.

```
[!] ATTEMPTS REMAINING: 4
> RECRUIT
ENTRY DENIED. LIKENESS: 0/7
[!] ATTEMPTS REMAINING: 3
> TRAGEDY
ENTRY DENIED. LIKENESS: 1/7
[!] ATTEMPTS REMAINING: 2
> JUSTIFY

[!] ACCESS GRANTED

Robco Industries Termlink (TM) Mail Protocol Initiated

User: j.hammond@robcoindustries.org

INBOX
1) h.hacks@robcoindustries.org SUBJ: new CTF game idea
2) flag.txt
3) Paella recipe


Select an option (1, 2, or 3): 2

flag.txt
flag{89e575e7272b07a1d33e41e3647b3826}
```


flag ```flag{89e575e7272b07a1d33e41e3647b3826}```
