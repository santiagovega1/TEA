Lista = []
while True:
    valor = input("Introduce un numero (o 'fin' para terminar): ")
    if valor.lower() in "fin":
        break
    try:
        Lista.append(int(valor))
    except ValueError:
        print("Entrada invalida")

print("La suma de los numeros es de: {}".format(sum(Lista)))
print("La cantidad de numeros introducidos es de {}".format(len(Lista)))
print("El promedio de valores ha sido de {}".format(sum(Lista)/len(Lista)))
