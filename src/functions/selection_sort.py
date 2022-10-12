''' BIG O
Best case - O(n^2)
Medium case - O(n^2)
Worst case - O(n^2)
'''

import time
import random

def selection_sort(sort_arr):
    arr = sort_arr
    i = 0
    n = len(arr)
    while(i<n):
        j=i+1
        min = i
        while(j<n):
            if(arr[j] < arr[min]):
                min = j 
            j+=1

        arr[i], arr[min] = arr[min], arr[i]
        i+=1
    
    return arr

def selection_sort_test():
    list = []
    for i in range(1000):
        list.append(random.randint(0, 1000))

    start = time.time()
    # -------------- Function start --------------
    result = selection_sort(list)
    # -------------- Function stop --------------
    end = time.time()

    return str(round(end - start, 3))

if __name__ == "__main__":
    print(selection_sort([4, 2, 3, 1]))