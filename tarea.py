def indice(peso,estatura):
    return round(peso/(estatura**2),2)


peso = int(input('Ingresa tu peso en kilos:'))
estatura =  float(input('Ingresa tu estatura en metros:'))
print(f'Tu indice de masa corporal es:{indice(peso,estatura)}')