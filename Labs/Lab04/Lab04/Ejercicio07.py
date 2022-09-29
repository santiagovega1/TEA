contador = 0
suma = 0
while True:
    try:
        numero = input("Ingrese un numero: ")
        if (numero == "salir"):
            break
        else:
            contador = contador + 1
            suma = suma + int(numero)
            promedio = suma / contador
    except:
        print("Ingresar valor numerico")
        contador = contador - 1
        continue
print("Contador:", contador)
print("Sumatoria:", suma)
print("Promedio:", promedio)
