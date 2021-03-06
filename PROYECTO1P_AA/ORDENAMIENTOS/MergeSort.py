#Aqui va el código del MergeSort
from time import time
def mergesort(arreglo):
    alist=arreglo[:] #Realizo una copia de la lista original para que esta no sea modificada.
    mergeSort(alist)
    return alist

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

#Método que llama al ordenamiento correspondiente,
# y toma el tiempo inicial y final para calcular el tiempo de ejecución del proceso dependiendo de un número de datos.
def OrdenoMerge(arreglo):
   inicial=time()
   mergesort(arreglo)
   final=time()
   diferencia=final-inicial
   return diferencia