import pickle

class Vehiculo:
    color = ''
    precio = 0

    def __init__(self,color,precio) -> None:
        self.color = color
        self.precio = precio
    
    def getCaracteristicas(self):
        return self.color,self.precio



#creacion del archivo con el objeto micoche.
'''
micoche = Vehiculo('azul',43000)
f = open('datos.bin', 'wb')
pickle.dump(micoche,f)
f.close()
'''
#abrir archivo para llamar el objeto
f = open('datos.bin','rb')
carro = pickle.load(f)
f.close()

print(carro.getCaracteristicas())
