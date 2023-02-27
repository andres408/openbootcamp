'''En este segundo ejercicio, tendréis que crear una
interfaz sencilla la cual debe de contener
una lista de elementos seleccionables, también debe de
tener un label con el texto que queráis.'''

import tkinter as tk

window =tk.Tk()
window.title("Ejercicio2")
window.geometry('400x100')
label=tk.Label(window, text='Escoge una opción').place(x=200, y=30)
lista = ['Cali','Bogota','Medellin','Bucaramanga','Cucuta','Florencia','Orito']
lista_items = tk.StringVar(value=lista)
listbox = tk.Listbox(window,height=30, listvariable=lista_items)
listbox.grid(column=0,row=0,sticky=tk.W)

window.mainloop()