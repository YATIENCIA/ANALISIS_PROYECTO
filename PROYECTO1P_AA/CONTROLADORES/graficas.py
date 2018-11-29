import matplotlib.pyplot as plt #Libreria que permite graficar
from ORDENAMIENTOS import InsertionSort as IS, MergeSort as MS, QuickSort as QS, StoogeSort as SS
from CONTROLADORES import OperacionesArchivo as OA


#El tiempo de graficación de la aplicación es 18 segundos con 500 datos  para todos los algoritmos
#El tiempo de graficación de la aplicación es 70 segundos con 1000 datos  para todos los algoritmos


#Orden del arreglo=[io,mo,qo,so]
#La función graficar obtiene como parámetro los arreglos que representan las coordenadas tanto (x,y) de cada una de las ordenaciones
#Muestra la grafica utilizando la librería Matplotlib
def graficar(arregloIx,arregloIy,arregloMx,arregloMy , arregloQx ,arregloQy ,arregloSx,arregloSy):
    plt.close()
    if(arregloIy!=[]):
        plt.plot(arregloIx,arregloIy, 'bo-', label="InsertionSort", linewidth=2)
    if (arregloMy != []):
        plt.plot(arregloMx,arregloMy, 'go-', label='MergeSort', linewidth=2)
    if (arregloQy != []):
        plt.plot(arregloQx ,arregloQy, 'ro-', label='QuickSort', linewidth=2)
    if (arregloSy != []):
        plt.plot(arregloSx,arregloSy,  'yo-', label='StoogeSort', linewidth=2)
    plt.xlabel("Cantidad de datos (unidades)")  # Inserta el título del eje X
    plt.ylabel("Tiempo de ejecución (mseg)")
    plt.legend(loc="upper left")
    OA.GenerarArchivo(arregloIx,arregloIy,arregloMy ,arregloQy ,arregloSy)
    plt.show()

#Método que genera los arreglos de ejes de cada uno de los métodos de ordenamiento, que representarán los intervalos de la gráfica
def verificar(a_opc, n,path):
    arregloIx=[] #Inicializo todos los arreglos en vacío
    arregloIy = []
    arregloMx = []
    arregloMy = []
    arregloQx = []
    arregloQy = []
    arregloSx = []
    arregloSy = []
    numero=0
    div = n // 5 #Divido la cantidad de datos en 5 partes para formar el intervalo
    while(numero<=n):
        arreglo=OA.LeerDoc(numero,path) #El método LeerDoc() retorna un arreglo con la camtidad de datos enviado.
        # Proceso para el InsertionSort
        if(a_opc[0]==True): #Verifica cuales son los métodos de ordenamiento que escogió el usuario
                tiempo=IS.OrdenoInsertion(arreglo) #Se envía el arreglo que se ordenará con el método específico y retorna el tiempo de ejecución de ese proceso
                arregloIx.append(numero)
                arregloIy.append(tiempo)

        if(a_opc[1]==True): # Proceso similar para el MergeSort
                tiempo=MS.OrdenoMerge(arreglo)
                arregloMx.append(numero)
                arregloMy.append(tiempo)

        if (a_opc[2] == True): # Proceso similar para el QuickSort
                tiempo=QS.OrdenoQuick(arreglo)
                arregloQx.append(numero)
                arregloQy.append(tiempo)

        if (a_opc[3] == True): # Proceso similar para el StoogeSort
                tiempo=SS.OrdenoStooge(arreglo)
                arregloSx.append(numero)
                arregloSy.append(tiempo)

        numero=numero+div #Cambio la variable de estado, sumando el valor de la divisón de datos para cinco hasta que sea igual al número dedatos ingresados
    graficar(arregloIx,arregloIy,arregloMx, arregloMy,arregloQx, arregloQy,arregloSx, arregloSy) #Grafico las gráficas con los arreglos generados
