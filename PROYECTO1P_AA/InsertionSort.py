#Aqui va el código del InsertionSort
from time import time
#Metodo1
def insertionSort(alistori):
   alist = alistori[:]
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue
   return alist



def OrdenoInsertion(arreglo):
    inicial = time()
    insertionSort(arreglo)
    final=time()
    diferencia=final-inicial
    return diferencia

