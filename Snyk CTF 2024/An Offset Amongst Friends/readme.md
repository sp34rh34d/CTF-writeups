## Name: An Offset Amongst Friends
#### Author: @Kkevsterrr
#### Category: rev
#### Difficulty: easy
#### Description: What's a little offset amongst friends? 


## Procedure
Using [dogbolt](https://dogbolt.org/)
We have the following code 
```
void FUN_001011c9(long param_1)

{
  long in_FS_OFFSET;
  int local_3c;
  char local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  builtin_strncpy(local_38,"gmbh|d65426593642d22b87bfbb939f54918d~",0x27);
  for (local_3c = 0; local_38[local_3c] != '\0'; local_3c = local_3c + 1) {
    *(char *)(param_1 + local_3c) = local_38[local_3c] + -1;
  }
  *(undefined *)(param_1 + local_3c) = 0;
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    // WARNING: Subroutine does not return
    __stack_chk_fail();
  }
  return;
}
```
This function FUN_001011c9:
* defines local variables, including a stack canary for security.
* copy the string ```gmbh|d65426593642d22b87bfbb939f54918d~``` into local_38 using builtin_strncpy, ensuring it does not exceed 0x27 (39) bytes.
* iterates over local_38, decrementing each character by 1

I have written the following python script 
```
flag = "gmbh|d65426593642d22b87bfbb939f54918d~"
out = ""
for x in flag:
	out += chr(ord(x)-1)
print(out)
```

flag ```flag{c54315482531c11a76aeaa828e43807c}```
