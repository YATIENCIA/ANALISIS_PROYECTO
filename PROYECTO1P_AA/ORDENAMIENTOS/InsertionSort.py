#Aqui va el código del InsertionSort
import time
#Metodo1
def insertionSort(alistori):
   alist = alistori[:]#Realizo una copia de la lista original para que esta no sea modificada.
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue

   return alist


#Método que llama al ordenamiento correspondiente,
# y toma el tiempo inicial y final para calcular el tiempo de ejecución del proceso dependiendo de un número de datos.
def OrdenoInsertion(arreglo):
    inicial = time.clock()
    insertionSort(arreglo)
    final=time.clock()
    diferencia=final-inicial
    return diferencia

