def promedio(numeros):
    suma = 0
    return sum(numeros) / len(numeros)

numeros = []

num1 = int(input("Escribe un número: "))
numeros.append(num1)
num2 = int(input("Escribe un número: "))
numeros.append(num2)
num3 = int(input("Escribe un número: "))
numeros.append(num3)

print(f"El promedio es: {promedio(numeros)}")
