import random
import time

def bubble(a):
    a = a.copy()  # не меняем исходный список
    n = len(a)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]


for n in [1000, 2000, 4000]:
    data = [random.randint(0, 10000) for _ in range(n)]

    start = time.perf_counter()
    bubble(data)
    bubble_time = time.perf_counter() - start

    start = time.perf_counter()
    merge_sort(data)
    merge_time = time.perf_counter() - start

    print(f"n={n}: bubble={bubble_time:.4f} сек, merge_sort={merge_time:.4f} сек")
