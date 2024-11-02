from pwn import *
context(log_level="debug")
r = remote('challenge.ctf.games',31053)


while True:
    try:
        res = r.recvuntil(b"Your move:")
        if b"strike" in res:
            print("oponent move is strike")
            r.send(b"block")
        elif b"advance" in res:
            print("oponent move is advance")
            r.send(b"retreat")
        elif b"retreat" in res:
            print("oponent move is retreat")
            r.send(b"strike")
        elif b"block" in res:
            print("oponent move is block")
            r.send(b"advance")
        else:
            print("no move")
            break
    except:
        pass

r.interactive()