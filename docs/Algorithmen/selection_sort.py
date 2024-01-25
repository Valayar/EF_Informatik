from timeit import timeit
from random import shuffle
from copy import deepcopy

def bogo_sort(a):
    print(a)
    while True:
        shuffle(a)
        is_sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                is_sorted = False
                break
        if is_sorted:
            return a

to_sort = list(range(6))
shuffle(to_sort)

execution_time = timeit(lambda: bogo_sort(deepcopy(to_sort)), number=100)
print('Zeit für 100x Sortieren:', execution_time)

def selection_sort(a):
    for j in range(len(a) - 1):
        key = a[j]
        index = j
        for i in range(j + 1, len(a)):
            if a[i] < a[index]:
                index = i
        a[j] = a[index]
        a[index] = key
    return a

to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print('Unsortiert:', to_sort)
print('Sortiert:  ', selection_sort(to_sort))