
import time as t

def pa_la_casa():
    hora_actual = t.localtime()
    #print(hora_actual)
    hora_fin_trabajo = t.struct_time(hora_actual[:3] + (19, 0, 0) + hora_actual[6:])
    tiempo_restante = t.mktime(hora_fin_trabajo) - t.mktime(hora_actual)
    if tiempo_restante < 0:
        return 'Es hora de ir a casa'
    else:
        return f'Debes trabajar por {int(tiempo_restante//3600)} horas {int(tiempo_restante//60)%60} minutos mas'

if __name__ =='__main__':
    print(pa_la_casa())