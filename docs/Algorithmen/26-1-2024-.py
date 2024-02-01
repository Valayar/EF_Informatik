from timeit import timeit
from random import shuffle
from copy import deepcopy

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

N = 10000
WDH = 5

to_sort = list(range(N))
shuffle(to_sort)

execution_time = timeit(lambda:selection_sort(deepcopy(to_sort)), number=WDH)
print('Zeit für',WDH, 'Sortieren:', execution_time/WDH)


