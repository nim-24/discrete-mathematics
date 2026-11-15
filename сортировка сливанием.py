def merge_sort(a):
    if len(a) <= 1:             # один элемент уже отсортирован
        return a

    middle = len(a) // 2
    left = merge_sort(a[:middle])     # сортируем левую половину
    right = merge_sort(a[middle:])    # сортируем правую половину

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]          # добавляем остаток, если он есть
    result += right[j:]
    return result


a = [45, 34, 44, 28, 7, 56, 85, 89, 23, 12, 5]
print(merge_sort(a))   # [5, 7, 12, 23, 28, 34, 44, 45, 56, 85, 89]
