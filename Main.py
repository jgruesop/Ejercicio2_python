numero_inicial = int(input("Digite el primer número: "))
numero_final = int(input("Digite el segundo número:"))
lista = []

# Se repite el while() mientras el segundo número sea menor o igual que el primer número
while numero_final <= numero_inicial:
    numero_final = int(input("El segundo número debe ser mayor que el primero. Digite un nuevo número:"))

# Itera sobre el rango dado entre los números ingresado
for numero in range(numero_inicial, numero_final):
    if numero % 2 == 1:
        lista.append(numero)

print(f"Los números impares entre {numero_inicial} y {numero_final} son: {lista}")
