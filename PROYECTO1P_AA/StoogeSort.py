#Aqui va el código del StoogeSort
from time import time
def stoogeSort(alist):
    arreglo=alist[:]
    stoogesort(arreglo,0,len(alist)-1)
    return arreglo

def stoogesort(arr, l, h):
    if l >= h:
        return

    # If first element is smaller
    # than last,swap them
    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    # If there are more than 2 elements in
    # the array
    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)

        # Recursively sort first 2/3 elements
        stoogesort(arr, l, (h - t))

        # Recursively sort last 2/3 elements
        stoogesort(arr, l + t, (h))

        # Recursively sort first 2/3 elements
        # again to confirm
        stoogesort(arr, l, (h - t))



def OrdenoStooge(arreglo):
    inicial = time()
    stoogeSort(arreglo)
    final=time()
    diferencia=final-inicial
    return diferencia