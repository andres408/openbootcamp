'''Cualquier año divisible por 4 es un año bisiesto: por ejemplo, 1988, 1992 y 1996 son años bisiestos.
estipula que un año que es divisible por 100 (por ejemplo, 1900)
es un año bisiesto solo si también es divisible por 400.'''

def bisiesto(anio):
    es_bisiesto=False
    if anio % 4 == 0 and anio % 100 !=0:
        es_bisiesto = True
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
        es_bisiesto = True
    
    
    if es_bisiesto == True:
        return (f'El año {anio} es bisiesto')
    else: 
        return(f'El año {anio} no es bisiesto')

print(bisiesto(2044))