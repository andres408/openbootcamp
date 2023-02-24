'''Script que le pide al usuario una lista de países
(separados por comas). Éstos se deben almacenar en una lista.
No debería haber países repetidos (haz uso de set). Finalmente,
muestra por consola
la lista de países ordenados alfabéticamente y separados por comas.'''

def no_repetidos(lista):
    return list(set(lista))


if __name__=='__main__':
    paises = list(input('Favor ingresar nombre de los paises separados por comas:\n').strip().split(','))
    print(no_repetidos(paises))



