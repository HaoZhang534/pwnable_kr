from pwn import *
context(arch='i386',log_level='debug')
# p=process("./orw",,env={"LD_PRELOAD":"./libc_32.so.6"})
argv=['./']
p=process(argv)
def 


# e=ELF('./libc-2.23.so')
# sys_addr=libc_base+e.symbols['system']


p.interactive()