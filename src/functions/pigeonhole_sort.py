import time
import random

def pigeonhole_sort(items):
    biggest = max(items)
    smallest = min(items)
    size = biggest - smallest + 1
    holes = [0] * size

    for item in items:
        holes[item - smallest] += 1

    i = 0
    for j in range(size):
        while holes[j] > 0:
            holes[j] -= 1
            items[i] = j + smallest
            i += 1
    
    return items

def pigeonhole_sort_test():
    list = []
    for i in range(1000):
        list.append(random.randint(0, 1000))

    start = time.time()
    # -------------- Function start --------------
    result = pigeonhole_sort(list)
    # -------------- Function stop --------------
    end = time.time()

    return str(round(end - start, 3))

if __name__ == "__main__":
    print(pigeonhole_sort([4, 2, 3, 1]))