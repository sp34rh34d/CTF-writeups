## Name: GoCrackMe1
#### Author: @HuskyHacks
#### Category: Reverse Engineering 
#### Difficulty: N/D
#### Description: TENNNNNN-HUT!. Welcome to the Go Dojo, gophers in training! Go malware is on the rise. So we need you to sharpen up those Go reverse engineering skills. We've written three simple CrackMe programs in Go to turn you into Go-binary reverse engineering ninjas! First up is the easiest of the three. Go get em! Archive password: infected

## Procedure
Checking the bin file using ```file GoCrackMe1``` command, show us 
```
GoCrackMe1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, Go BuildID=XTzA9g-rxSFKyebZYVXI/BFzZeSPLsNjAFEvjiSub/nTgut0H_UB7B79xaGq7-/X7kvo6zmAQOjIJV9zPwd, with debug_info, not stripped
```
the bin is not stripped, good news!!

Now open the file using Ghidra, we can recover the follow code from main function.

```
void main.main(void *param_1,sigaction *param_2,undefined8 param_3,undefined8 param_4,
              sigaction *param_5,uint *param_6)

{
  bool bVar1;
  long extraout_RAX;
  long lVar2;
  undefined8 uVar3;
  undefined extraout_DL;
  uint uVar4;
  ulong extraout_RDX;
  undefined8 extraout_RDX_00;
  undefined8 extraout_RDX_01;
  undefined uVar6;
  undefined7 uVar7;
  undefined uVar8;
  undefined7 uVar9;
  long unaff_R14;
  undefined in_stack_ffffffffffffff78;
  undefined7 in_stack_ffffffffffffff79;
  undefined8 in_stack_ffffffffffffff80;
  undefined8 in_stack_ffffffffffffff88;
  undefined8 in_stack_ffffffffffffff90;
  undefined8 in_stack_ffffffffffffff98;
  undefined6 local_56;
  undefined2 uStack_50;
  undefined8 uStack_4e;
  undefined6 local_46;
  undefined2 uStack_40;
  undefined8 uStack_3e;
  undefined4 uStack_36;
  undefined2 uStack_32;
  undefined1 *local_30;
  undefined local_28 [16];
  undefined local_18 [16];
  ulong uVar5;
  
  uVar8 = SUB81(param_6,0);
  uVar9 = (undefined7)((ulong)param_6 >> 8);
  uVar6 = SUB81(param_5,0);
  uVar7 = (undefined7)((ulong)param_5 >> 8);
  while (&stack0xfffffffffffffff8 <= *(undefined **)(unaff_R14 + 0x10)) {
    runtime.morestack_noctxt.abi0(param_1,param_2);
  }
  local_56 = 0x342d31373a30;
  uStack_50 = 0x6334;
  uStack_4e = 0x306764336060636f;
  local_46 = 0x6e6063336363;
  uStack_40 = 0x3266;
  uStack_3e = 0x34343265306f6e63;
  uStack_36 = 0x30663533;
  uStack_32 = 0x2b6e;
  runtime.makeslice(param_1,param_2,0x34343265306f6e63,0x26,(sigaction *)CONCAT71(uVar7,uVar6),
                    (undefined1 *)CONCAT71(uVar9,uVar8),
                    CONCAT71(in_stack_ffffffffffffff79,in_stack_ffffffffffffff78),
                    in_stack_ffffffffffffff80,in_stack_ffffffffffffff88);
  uVar5 = extraout_RDX;
  for (lVar2 = 0; lVar2 < 0x26; lVar2 = lVar2 + 1) {
    uVar4 = *(byte *)((long)&local_56 + lVar2) ^ 0x56;
    uVar5 = (ulong)uVar4;
    *(char *)(extraout_RAX + lVar2) = (char)uVar4;
  }
  uVar3 = 0x26;
  local_30 = runtime.slicebytetostring
                       (param_1,param_2,uVar5,(undefined1 *)0x26,uVar6,uVar8,
                        in_stack_ffffffffffffff78,in_stack_ffffffffffffff80,
                        in_stack_ffffffffffffff88);
  bVar1 = main.checkCondition(param_1,param_2,extraout_RDX_00,uVar3,
                              (sigaction *)CONCAT71(uVar7,uVar6),(undefined1 *)CONCAT71(uVar9,uVar8)
                             );
  if (bVar1) {
    local_18._8_8_ =
         runtime.convTstring(param_1,param_2,extraout_DL,(char)uVar3,uVar6,uVar8,
                             CONCAT71(in_stack_ffffffffffffff79,in_stack_ffffffffffffff78),
                             in_stack_ffffffffffffff80);
    local_18._0_8_ = &DAT_0048b8e0;
    fmt.Fprintln((sigaction *)0x1,(sigaction *)0x1,extraout_RDX_01,local_18,
                 (sigaction *)CONCAT71(uVar7,uVar6),(uint *)CONCAT71(uVar9,uVar8),
                 CONCAT71(in_stack_ffffffffffffff79,in_stack_ffffffffffffff78),
                 in_stack_ffffffffffffff80,in_stack_ffffffffffffff88,in_stack_ffffffffffffff90,
                 in_stack_ffffffffffffff98);
  }
  else {
    local_28._8_8_ = &PTR_DAT_004badb8;
    local_28._0_8_ = &DAT_0048b8e0;
    fmt.Fprintln((sigaction *)0x1,(sigaction *)0x1,&PTR_DAT_004badb8,local_28,
                 (sigaction *)CONCAT71(uVar7,uVar6),(uint *)CONCAT71(uVar9,uVar8),
                 CONCAT71(in_stack_ffffffffffffff79,in_stack_ffffffffffffff78),
                 in_stack_ffffffffffffff80,in_stack_ffffffffffffff88,in_stack_ffffffffffffff90,
                 in_stack_ffffffffffffff98);
  }
  return;
}
```
* The function main.main takes several parameters: param_1, param_2, param_3, param_4, param_5, and param_6. Some of these parameters are pointers to structures (sigaction) and other data types (undefined8, uint).
* The for loop iterates through the local_56 data and performs an XOR operation (*(byte *)((long)&local_56 + lVar2) ^ 0x56), which is likely meant to decrypt or obfuscate the data at that position.

Now we have to decrypt our data with the following python code
```
from pwn import xor
c = bytes.fromhex("303a37312d3434636f6360603364673063633363606e6632636e6f3065323434333566306e2b")

print(xor(c,0x56))
```

![Screenshot 2025-02-10 at 1 14 41 PM](https://github.com/user-attachments/assets/56484bce-cbbd-4e2e-a922-13f920fae97a)



