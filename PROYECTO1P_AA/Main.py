print("Inicio de proyecto")
from ANALISIS_PROYECTO.PROYECTO1P_AA import graficas as graph
import tkinter as tk # Carga módulo tk (widgets estándar)
from tkinter import ttk # Carga ttk (para widgets nuevos 8.5+)
def comando():
    print ("hola")
# Define la ventana principal de la aplicación

def accion():
    io=insertion_option.get()
    mo=merge_option.get()
    qo=quick_option.get()
    so=stooge_option.get()
    print("Inserción:",io)
    print("Merge:",mo)
    print("Quick:",qo)
    print("Stooge:",so)
    print("get", combo.get())

def graficar():
    print("****************************************************************")
    io = insertion_option.get()
    mo = merge_option.get()
    qo = quick_option.get()
    so = stooge_option.get()
    arreglo = [io, mo, qo, so]
    graph.verificar(arreglo,int(combo.get()))


raiz = tk.Tk()
raiz.geometry('300x400') # anchura x altura
raiz.configure(bg = 'beige')
raiz.title('Métodos de ordenamiento')
ttk.Label(raiz, text="Escoja los métodos de ordenamiento: ").pack(side=tk.TOP)
quick_option = tk.BooleanVar()
ttk.Checkbutton(raiz, text="QuickSort", variable=quick_option).pack(side=tk.TOP)
insertion_option = tk.BooleanVar()
ttk.Checkbutton(raiz, text="InsertionSort", variable=insertion_option).pack(side=tk.TOP)
merge_option = tk.BooleanVar()
ttk.Checkbutton(raiz, text="MergeSort", variable=merge_option).pack(side=tk.TOP)
stooge_option = tk.BooleanVar()
ttk.Checkbutton(raiz, text="StoogeSort", variable=stooge_option).pack(side=tk.TOP)

ttk.Label(raiz, text="Escoja la cantidad de datos: ").pack(side=tk.TOP)

combo=ttk.Combobox(raiz, values=("10", "100", "500", "1000"))
combo.pack(side=tk.TOP)
combo.set("10")

ttk.Button(raiz, text='GRAFICAR', command=graficar).pack(side=tk.TOP)
ttk.Button(raiz, text='Salir', command=quit).pack(side=tk.BOTTOM)
ttk.Button(raiz, text='print checks', command=accion).pack(side=tk.TOP)
raiz.mainloop()

