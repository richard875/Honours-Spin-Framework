''' BIG O
Best case - O(n log(n))
Medium case - O(n log(n))
Worst case - O(n^2)
'''

import time
import random

def partition(sort_list, esq, dir, pivot):
    while (esq <= dir):
        while (sort_list[esq] < pivot):
            esq += 1

        while (sort_list[dir] > pivot):
            dir -= 1

        if (esq <= dir):
            sort_list[esq], sort_list[dir] = sort_list[dir], sort_list[esq]  # Swap
            esq += 1
            dir -= 1

    return esq


def quick_sort_algorithm(arr, esq, dir):
    sort_list = arr
    if (esq >= dir):
        return
    pivot = sort_list[int((esq + dir) / 2)]
    index = partition(sort_list, esq, dir, pivot)
    quick_sort_algorithm(sort_list, esq, index - 1)
    quick_sort_algorithm(sort_list, index, dir)

    return sort_list


def quick_sort(arr):
    return quick_sort_algorithm(arr, 0, len(arr) - 1)

# Small: 550000, Medium: 1250000, Large: 2500000
def quick_sort_test():
    time_variable = []
    len_num = [550000, 1250000, 2500000]
    max_number = [550000, 1250000, 2500000]

    for i in range(len(len_num)):
        list = []
        for j in range(len_num[i]):
            list.append(random.randint(0, max_number[i]))

        start = time.time()
        # -------------- Function start --------------
        result = quick_sort(list)
        # -------------- Function stop --------------
        end = time.time()

        time_variable.append(str(round(end - start, 3)))

    return time_variable


if __name__ == "__main__":
    print(quick_sort([4, 2, 3, 1]))