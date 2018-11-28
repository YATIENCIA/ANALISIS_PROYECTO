print("Inicio de proyecto")
import tkinter as tk # Carga módulo tk (widgets estándar)
from tkinter import ttk # Carga ttk (para widgets nuevos 8.5+)
def comando():
    print ("hola")
# Define la ventana principal de la aplicación

def accion():
    print(insertion_option.get())


raiz = tk.Tk()

# Define las dimensiones de la ventana, que se ubicará en
# el centro de la pantalla. Si se omite esta línea la
# ventana se adaptará a los widgets que se coloquen en
# ella.

raiz.geometry('300x200') # anchura x altura

# Asigna un color de fondo a la ventana. Si se omite
# esta línea el fondo será gris

raiz.configure(bg = 'beige')

# Asigna un título a la ventana

raiz.title('Métodos de ordenamiento')

# Define un botón en la parte inferior de la ventana
# que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'raiz'
# donde se ubicará el botón
ttk.Label(raiz, text="Escoja los métodos de ordenamiento: ").pack(side=tk.TOP)
ttk.Button(raiz, text='Salir', command=quit).pack(side=tk.BOTTOM)
ttk.Button(raiz, text='print check', command=accion).pack(side=tk.BOTTOM)
#Creeacion de checkbox
quick_option = tk.BooleanVar()
ttk.Checkbutton(raiz, text="QuickSort", variable=quick_option).pack(side=tk.TOP)

insertion_option = tk.BooleanVar()
ttk.Checkbutton(raiz, text="InsertionSort", variable=insertion_option).pack(side=tk.TOP)


merge_option = tk.BooleanVar()
ttk.Checkbutton(raiz, text="MergeSort", variable=merge_option).pack(side=tk.TOP)
tk.TOP
stooge_option = tk.BooleanVar()
ttk.Checkbutton(raiz, text="StoogeSort", variable=stooge_option).pack(side=tk.TOP)









# Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de
# que alguna persona interactúe con ella.

# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.

raiz.mainloop()