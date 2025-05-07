def promedio(numeros):
    suma = 0
    return sum(numeros) / len(numeros)

numeros = []

for n in range(3) :
    num = int(input("Escribe un número: "))
    numeros.append(num)

print(f"El promedio es: {promedio([numeros)}")
