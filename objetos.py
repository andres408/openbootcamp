class Vehiculo:
    Color = 'azul'
    Ruedas = 4
    Puertas = 5


class Coche(Vehiculo):
    Velocidad = 0
    Cilindrada = 900


miCoche = Coche()
print(dir(miCoche))
