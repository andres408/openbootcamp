class Alumno:

    def __init__(self,nombre,nota) -> None:
        self.nombre=nombre
        self.nota=nota

    def aprobado(self):
        if self.nota >= 6:
            print(f'{self.nombre} ha aprobado con una nota de {self.nota}')
        else:
            print(f'{self.nombre} ha desaprobado con una nota de {self.nota}')

alumno1= Alumno('Alfredo',8)
alumno1.aprobado()