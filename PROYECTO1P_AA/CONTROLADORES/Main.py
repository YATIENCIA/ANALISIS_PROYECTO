from CONTROLADORES import OperacionesArchivo as OA, graficas as graph
import tkinter as tk # Carga módulo tk (widgets estándar)
from tkinter import ttk # Carga ttk (para widgets nuevos 8.5+)
from tkinter import messagebox
import time
import threading
# Define la ventana principal de la aplicación

#Método retorna en un arreglo el estado del checkbox utilizados para la elección del método del ordenamiento
def retornaArregloBoolean():
    io = insertion_option.get()
    mo = merge_option.get()
    qo = quick_option.get()
    so = stooge_option.get()
    arreglo = [io, mo, qo, so]
    return arreglo

#Método utilizado cuando el usuario NO INGRESA un archivo y realiza las gráficas con datos aleatorios
def DatosAleatorios():
    OA.CrearDoc()    #Creación del doc con números aleatorios aleatorios llamado datos.txt
    arreglo=retornaArregloBoolean()     #Obtengo el arreglo con los datos booleanos
    try:
        if (int(combo.get()) > 1000): #Verifico que la cantidad de datos que ingresa el usuario lo soporte el sistema
                messagebox.showerror("Error", "¡No puede escoger más de 1000 datos!")
                combo.set("250")
        else:
                espera()
                eliespera()
                graph.verificar(arreglo, int(combo.get()), "datos.txt")   #Grafico usando el archivo generado datos.txt
    except:
        messagebox.showerror("Error", "¡Datos ingresados inválidos!")
        v.set("")
        combo.set("250")


#Método utilizado cuando el usuario INGRESA un archivo con datos para realizar las gráficas
def graficar():

    arreglo = retornaArregloBoolean() #Obtengo el arreglo con los datos booleanos
    try:
        if(int(combo.get())>1000):#Verifico que la cantidad de datos que ingresa el usuario lo soporte el sistema(1000 datos)
            messagebox.showerror("Error", "¡No puede escoger más de 1000 datos!")
            combo.set("250")
        else:
            try: #Verifico que el archivo ingresado por el usuario exista dentro del proyecto
                espera()
                eliespera()
                graph.verificar(arreglo,int(combo.get()),e.get())
            except:
                messagebox.showerror("Error", "¡No existe el archivo que ingresó!") #Si no existe se presenta un mensaje de error
                v.set("")
    except:
        messagebox.showerror("Error", "¡Datos ingresados inválidos!")
        v.set("")
        combo.set("250")

#Método de feedback para el usuario
def espera():
    ve.set("Cargando...")
    raiz.update_idletasks()

def eliespera():
    ve.set("")
    raiz.update_idletasks()


#Implementación de la interfaz
raiz = tk.Tk()
raiz.geometry('800x400') # anchura x altura
raiz.configure(bg = 'beige') #Color de fondo
raiz.title('Métodos de ordenamiento')

label=ttk.Label(raiz, text="COMPARACIÓN DE ALGORITMOS DE ORDENAMIENTO")
label.pack(side=tk.TOP)
label.config(font=("Courier", 20))


label2=ttk.Label(raiz, text="Escoja los métodos de ordenamiento: ")
label2.pack(side=tk.TOP)
label2.config(font=("Courier", 12))

quick_option = tk.BooleanVar(value=True)

#Implementación de checkButtons para escoger los métodos de ordenamientos
ttk.Checkbutton(raiz, text="QuickSort", variable=quick_option).pack(side=tk.TOP)
insertion_option = tk.BooleanVar(value=True)
ttk.Checkbutton(raiz, text="InsertionSort", variable=insertion_option).pack(side=tk.TOP)
merge_option = tk.BooleanVar(value=True)
ttk.Checkbutton(raiz, text="MergeSort", variable=merge_option).pack(side=tk.TOP)
stooge_option = tk.BooleanVar(value=True)
ttk.Checkbutton(raiz, text="StoogeSort", variable=stooge_option).pack(side=tk.TOP)

label3=ttk.Label(raiz, text="Escoja la cantidad de datos: ")
label3.pack(side=tk.TOP)
label3.config(font=("Courier", 12))


#Implementación del ComboBox para escoger o escribir la cantidad de datos que desea analizar el usuario
combo=ttk.Combobox(raiz, values=("250", "500", "750", "1000"))
combo.pack(side=tk.TOP)
combo.set("250")


label4=ttk.Label(raiz, text="Ingrese el nombre de su archivo:")
label4.pack(side=tk.TOP)
label4.config(font=("Courier", 12))

#Implementación del campo para ingresar el nombre del archivo
v = tk.StringVar()
e = ttk.Entry(raiz, textvariable=v)
e.pack(side=tk.TOP)

#Implementación de cada uno de los botones dentro de la interfaz

ttk.Button(raiz, text='GRAFICAR CON ARCHIVO', command=graficar).pack(side=tk.TOP)
ttk.Button(raiz, text='GRAFICAR CON DATOS ALEATORIOS', command=DatosAleatorios).pack(side=tk.TOP)

#Label de espera para el Usuario
ve = tk.StringVar()
labele = ttk.Label(raiz, text="", textvariable=ve)
labele.pack(side=tk.TOP)
labele.config(font=("Arial", 30))

#Presentar la ventana
raiz.mainloop()

