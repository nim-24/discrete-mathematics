s = int(input())

target = [45, 34, 44, 28, 7, 56, 85, 89, 23, 12, 5]
target = sorted(target)

def fff(target, s):
    left = 0
    right = len(target) - 1
    lo = 0

    while left <= right:
        mid = (left + right) // 2
        lo += 1  # посчитали проверку target[mid]

        if s == target[mid]:
            return lo
        elif s < target[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return 0  # цикл закончился, значит числа нет

print(fff(target, s))
