from timeit import timeit
from random import shuffle
from copy import deepcopy

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

N = 10000
WDH = 5

to_sort = list(range(N))
shuffle(to_sort)

execution_time = timeit(lambda: insertion_sort(deepcopy(to_sort)), number=WDH)
print('Zeit für',WDH, 'Sortieren:', execution_time/WDH)

