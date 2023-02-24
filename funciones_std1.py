'''crear una aplicación que obtendrá los elementos impares de una lista
pasada por parámetro con filter y realizará una suma de todos estos
elementos obtenidos mediante reduce.'''

from functools import reduce
def filtros(elemento):
    if elemento % 2 != 0:
        return True
    return False


if __name__ =='__main__':
    lista = [i for i in range(10000000)]
    resultado = (filter(filtros,lista))
    resultado = reduce(lambda a,b : a + b, resultado)
    print(resultado)