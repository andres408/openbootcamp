'''Crear una lista de RadioButton
que muestre la opción que se ha seleccionado y que contenga un botón de
reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.'''

import tkinter as tk

def seleccion():
    print('Opcion seleccionada:', s1.get())

def reinicio():
    s1.set(None)

window = tk.Tk()
window.geometry("400x300")
window.title('Ejercicio1')
s1 = tk.IntVar()
lbl1 = tk.Label(window,text= 'Ejercicio para llegar a ser desarrollador').place(x=100,y=70)
rb1 = tk.Radiobutton(window,text='Opcion1',value=1,variable=s1,command=seleccion).place(x=100,y=100)
rb2 = tk.Radiobutton(window,text='Opcion2',value=2,variable=s1,command=seleccion).place(x=100,y=120)
rb3 = tk.Radiobutton(window,text='Opcion3',value=3,variable=s1,command=seleccion).place(x=100,y=140)
rb4 = tk.Radiobutton(window,text='Reinicio',value=4,variable=s1,command=reinicio).place(x=100,y=160)
window.mainloop()