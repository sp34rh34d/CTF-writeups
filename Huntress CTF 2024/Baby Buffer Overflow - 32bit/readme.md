Can you command this program to where it cannot go?
To get the flag, you must somehow take control of its excecution.
Is it even possible?


0x08049020  gets@plt
0x08049030  execve@plt
0x08049040  puts@plt
0x08049050  fflush@plt
0x08049060  setbuf@plt
0x08049070  __libc_start_main@plt
0x08049080  _start
0x080490d2  __x86.get_pc_thunk.bx
0x080490e0  deregister_tm_clones
0x08049120  register_tm_clones
0x08049160  __do_global_dtors_aux
0x080491b0  frame_dummy
0x080491f5  target
0x08049236  vuln
0x08049252  main


flag{4cd3b4079393e861af489ca063373f98}