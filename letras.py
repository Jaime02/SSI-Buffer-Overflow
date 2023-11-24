import sys
n = int(sys.argv[1])
l = int(sys.argv[2])
abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
resultado = ""


for letra in abecedario[:n]:
	resultado += letra*l

print(resultado)
