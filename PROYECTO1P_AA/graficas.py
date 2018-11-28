import matplotlib.pyplot as plt
from random import randint
from ANALISIS_PROYECTO.PROYECTO1P_AA import InsertionSort as IS, MergeSort as MS, QuickSort as QS, StoogeSort as SS

#arreglo=[io,mo,qo,so]
def graficar(x,y):
    plt.plot(x, y, 'go-', label='line 1', linewidth=2)
    plt.show()

def verificar(a_opc, n):
    arregloIx=[]
    arregloIy = []
    arregloMx = []
    arregloMy = []
    arregloQx = []
    arregloQy = []
    arregloSx = []
    arregloSy = []
    cantidad=n
    while(cantidad>=0):
        arreglo=LeerDoc(cantidad)
        if(a_opc[0]==True):
            tiempo=IS.OrdenoInsertion(arreglo)
            arregloIx.append(cantidad)
            arregloIy.append(tiempo)
        if(a_opc[1]==True):
            tiempo=MS.OrdenoMerge(arreglo)
            arregloMx.append(cantidad)
            arregloMy.append(tiempo)
        if (a_opc[2] == True):
            tiempo=QS.OrdenoQuick(arreglo)
            arregloQx.append(cantidad)
            arregloQy.append(tiempo)
        if (a_opc[3] == True):
            tiempo=SS.OrdenoStooge(arreglo)
            arregloSx.append(cantidad)
            arregloSy.append(tiempo)
        cantidad=cantidad/2
    graficar(arregloIx,arregloIy)
def CrearDoc():
    archivo=open("datos.txt","w")
    for i in range(1000):
        x=randint(0,999)
        archivo.write(str(x)+"\n")
    archivo.close()

def LeerDoc(n):
    c=0
    arreglo=[]
    archivo=open("datos.txt","r")
    while(c<n):
        c=c+1
        linea = archivo.readline()
        arreglo.append(int(linea))
    archivo.close()
    return arreglo


