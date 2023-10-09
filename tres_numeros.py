

def ordenar_numeros(numero):
    lista_numeros = numero.split()
    arreglo_numero = [int(numero) for numero in lista_numeros]
    numeros_ordenados = sorted(arreglo_numero)
    return print(numeros_ordenados)

ordenar_numeros(input("Ingrese numeros: "))

