## Name: Stack It
#### Author: @sudo_Rem
#### Category: Reverse Engineering
#### Difficulty: N/D
#### Description: Our team of security analysts recently worked through a peculiar Lumma sample.
The dentists helping us advised we floss at least twice a day to help out.
He also gave us this weird file. Maybe you can help us out.

## Procedure
the binary is stripped, so if u try to list the functions with gdb, u cant recover any function, i decided to use radare2, it shows us the entry point ```0x08049000```, we can use this addr to set a breakpoint in gdb and do dynamic analysis.

![image](https://github.com/user-attachments/assets/c9f1ad9e-e2a5-4284-bc4f-1fbe9a0d4d18)

Set the breakpoint with command ```b *0x08049000``` and then just run the binary and push ```n``` and u will see the flag at EDX register after finish the XOR operation.

![image](https://github.com/user-attachments/assets/230e73b2-8c50-46d1-9be6-f9c2a5ca2430)

![image](https://github.com/user-attachments/assets/85abe6c9-e636-466c-888c-7ded0f74ece8)


flag  ```flag{b4234f4bba4685dc84d6ee9a48e9c106}```


