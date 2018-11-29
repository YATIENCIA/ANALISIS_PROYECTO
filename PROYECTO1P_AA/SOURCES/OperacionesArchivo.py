from random import randint #Libreria que permite generar números aleatorios
#Método que crear un archivo llamado datos.txt con aproximadamente 1000 datos de forma aleatoria
def CrearDoc():
    archivo=open("datos.txt","w")
    for i in range(10000):
        x=randint(0,999)
        archivo.write(str(x)+"\n")
    archivo.close()

#Método que lee un archivo que recibe como parámetro, y genera un arreglo de tamañano igual a la cantidad recibida como parámetro.
def LeerDoc(n,path):
    c=0
    arreglo=[]
    archivo=open(path,"r")
    while(c<n):
        c=c+1
        linea = archivo.readline()
        arreglo.append(int(linea))
    archivo.close()
    return arreglo

def llenarVacio(n, arreglo):
    for i in range(n):
        arreglo.append("-")

#Este método genera un archivo Resultado.txt el cual tendrá las salidas de las gráficas comparando la cantidad de datos con respecto al tiempo (milisegundos)
def GenerarArchivo(arregloX,arregloIy,arregloMy ,arregloQy ,arregloSy):
        if(arregloIy==[]):
            llenarVacio(len(arregloX),arregloIy)
        if (arregloMy == []):
            llenarVacio(len(arregloX), arregloMy)
        if (arregloQy == []):
            llenarVacio(len(arregloX), arregloQy)
        if (arregloSy == []):
            llenarVacio(len(arregloX),arregloSy)
        archivo=open("resultados.txt","w")
        archivo.write("n\t\t\tInsertionSort(mseg)\t\t\tMergeSort(mseg)\t\t\tQuickSort(mseg)\t\t\tStoogeSort(mseg)\n")
        for i in range (len(arregloX) ):
            archivo.write(str(arregloX[i])+"\t\t\t"+str(arregloIy[i])+"\t\t\t"+str(arregloMy[i])+"\t\t\t"+str(arregloQy[i])+"\t\t\t"+str(arregloSy[i])+"\n")
        archivo.close()
