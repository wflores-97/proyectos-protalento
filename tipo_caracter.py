def tipo_caracter(char):
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if char.islower():
        if char in vocales:
            print("La letra ingresada es una vocal")
        elif char in vocales: 
            print("La letra ingresada no es una vocal")
        return print("La letra ingresada es minuscula")
    elif char.isupper():
        if char in vocales:
            print("La letra ingresada es una vocal")
        else: 
            print("La letra ingresada no es una vocal")
        return print("La letra ingresada es mayuscula")
    
tipo_caracter(input("Ingrese una letra: "))