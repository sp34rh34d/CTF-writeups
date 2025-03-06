## Name: Math For Me
#### Author: @Kkevsterrr
#### Category: rev
#### Difficulty: medium
#### Description: Just gotta do some math! This flag is a non-standard format. It will be wrapped in flag{ prefix and } suffix but inside the curly braces will be any printable characters, not be just hexadecimal characters. 


## Procedure
We can see the following C code from ```math4me``` binary:

```
undefined8 main(void)

{
  int iVar1;
  long in_FS_OFFSET;
  undefined4 local_50;
  int local_4c;
  undefined local_48;
  undefined local_47;
  undefined local_46;
  undefined local_45;
  undefined local_44;
  undefined local_23;
  undefined local_22;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  puts("Welcome to the Math Challenge!");
  printf("Find the special number: ");
  __isoc99_scanf(&DAT_00102049,&local_50);
  local_48 = 0x66;
  local_47 = 0x6c;
  local_46 = 0x61;
  local_45 = 0x67;
  local_44 = 0x7b;
  iVar1 = check_number(local_50);
  if (iVar1 == 0) {
    puts("That\'s not the special number. Try again!");
  }
  else {
    for (local_4c = 5; local_4c < 0x25; local_4c = local_4c + 1) {
      compute_flag_char(&local_48,local_4c,local_50);
    }
    local_23 = 0x7d;
    local_22 = 0;
    printf("Congratulations! Here\'s your flag: %s\n",&local_48);
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    // WARNING: Subroutine does not return
    __stack_chk_fail();
  }
  return 0;
}
```
It asks for a magic number, then call the ```check_number``` function and then it does a math operation, the result should be ```0x34``` or ```52```

```
bool check_number(int param_1)

{
  return (param_1 * 5 + 4) / 2 == 0x34;
}
```

From here we can try to create our python script and repeat the math operation to find the magic number

```
for x in range(50):
  res = (x * 5 + 4)/2
  if res == 52:
    print(x)
```

the result is ```20```, so this is our magic number to recover the flag.

```
└─$ ./math4me      
Welcome to the Math Challenge!
Find the special number: 20
5: 2
6: -3
7: 1
8: 4
9: -2
10: 1
11: 3
12: -2
13: 4
14: -1
15: 2
16: -3
17: 1
18: 4
19: -2
20: 1
21: 3
22: -2
23: 4
24: -1
25: 2
26: -3
27: 1
28: 4
29: -2
30: 1
31: 3
32: -2
33: 4
34: -1
35: 2
36: -3
Congratulations! Here's your flag: flag{h556cdd`=ag.c53664:45569368391gc}

```


flag ```flag{h556cdd`=ag.c53664:45569368391gc}```
