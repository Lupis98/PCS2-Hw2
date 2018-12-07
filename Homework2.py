from timeit import Timer
import random
import time
import timeit
import matplotlib.pyplot as plt
setup = """
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def mergeSort(lst):
    if len(lst)>1:
        mid = len(lst) // 2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k]=lefthalf[i]
                i=i+1
            else:
                lst[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            lst[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            lst[k]=righthalf[j]
            j=j+1
            k=k+1
    return lst
    
import random
lst1 = list(range(10))
random.shuffle(lst1)
lst2 = list(range(100))
random.shuffle(lst2)
lst3 = list(range(1000))
random.shuffle(lst3)
lst4 = list(range(10000))
random.shuffle(lst4)
"""
quick = []
merge = []
for i in range(1,5):
    a = str(i)
    s = 'quickSort (lst'+a+', 0 , len(lst'+a+')-1)'
    t1 = Timer(s, setup)
    time1 = t1.timeit(1)
    e = 'mergeSort (lst'+a+')'
    t2 = Timer(e, setup)
    time2 = t2.timeit(1)
    quick.append(time1)
    merge.append(time2)
    print('quickSort:', time1, 'mergesort;', time2, 'percent:', time1/time2)

plt.plot(quick , label = 'QuickSort')
plt.plot(merge , label = 'MergeSort')
plt.legend()
plt.xlabel('Dimension of the list')
plt.ylabel('Process Time')
plt.show()
