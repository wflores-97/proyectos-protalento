def anio_bisiesto(anio:int, divisor:int):
    bisiesto= anio % divisor
    if bisiesto == 0:
        return print("el año", anio, "si es bisiesto")
    else:
        return print("el año", anio, "no es bisiesto")
    
anio_bisiesto(2023, 4)

