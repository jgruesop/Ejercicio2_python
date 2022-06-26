numero_inicial = 2
numero_final = 8
lista = []

for numero in range(numero_inicial,numero_final):
    if numero % 2 == 1:
        lista.append(numero)

print(lista) #[3,5,7]
