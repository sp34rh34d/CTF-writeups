## Name: Either Or
#### Author: @Kkevsterrr
#### Category: rev
#### Difficulty: medium
#### Description: Either or, but probably not both. 

## Procedure
Using GDB, I put a breakpoint into main function with ```b *main```, then just send the char ```n``` until you se the message ```Enter the secret word```, We can see the value ```frperg_cnffjbeq``` in the stack.

```
00:0000│ rsp 0x7fffffffdd30 ◂— 'frperg_cnffjbeq'
01:0008│-0c8 0x7fffffffdd38 ◂— 0x7165626a66666e /* 'nffjbeq' */
02:0010│ rsi 0x7fffffffdd40 ◂— 0x900000
03:0018│-0b8 0x7fffffffdd48 ◂— 0x900000
04:0020│-0b0 0x7fffffffdd50 ◂— 0x800
05:0028│-0a8 0x7fffffffdd58 ◂— 0x900000
06:0030│-0a0 0x7fffffffdd60 ◂— 0x8
07:0038│-098 0x7fffffffdd68 ◂— 0x40 /* '@' */
────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────
 ► 0   0x55555555544e main+124
   1   0x7ffff7dccd68 __libc_start_call_main+120
   2   0x7ffff7dcce25 __libc_start_main+133
   3   0x555555555105 _start+37
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> 
Enter the secret word: sp34rh34d
```

It call the function ```encode_input``` and send our value ```sp34rh34d``` in the ```RDI``` as argument.

```
 ► 0x555555555464 <main+146>    call   encode_input                <encode_input>
        rdi: 0x7fffffffdd40 ◂— 'sp34rh34d'
        rsi: 0x7fffffffdd80 ◂— 0xffffffffffffffff
        rdx: 0x7fffffffdd80 ◂— 0xffffffffffffffff
        rcx: 0x0

```
The result was ```fc34eu34q```
```
 RDI  0x7fffffffdd40 ◂— 'sp34rh34d'
 RSI  0x7fffffffdd80 ◂— 'fc34eu34q'
```

Then it calls the function ```strcmp``` with the values ```fc34eu34q``` and ```frperg_cnffjbeq```.
```
 ► 0x55555555547a <main+168>    call   strcmp@plt                <strcmp@plt>
        s1: 0x7fffffffdd80 ◂— 'fc34eu34q'
        s2: 0x7fffffffdd30 ◂— 'frperg_cnffjbeq'

```
This means that our real encoded value is ```frperg_cnffjbeq```, Now i have repeated the process using that value and we can see the value ```secret_password```
```
 RDI  0x7fffffffdd40 ◂— 'frperg_cnffjbeq'
 RSI  0x7fffffffdd80 ◂— 'secret_password'
```

Now we have recovered the real password to get our flag

```
Welcome to the Encoding Challenge!
Enter the secret word: secret_password
Well done! Here's your flag: flag{f074d38932164b278a508df11b5eff89}
```

flag ```flag{f074d38932164b278a508df11b5eff89}```
