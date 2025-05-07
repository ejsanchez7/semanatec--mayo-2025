def promedio(numeros):
    suma = 0
    return sum(numeros) / len(numeros)

num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe un número: "))
num3 = int(input("Escribe un número: "))

print(f"El promedio es: {promedio([num1, num2, num3])}")
