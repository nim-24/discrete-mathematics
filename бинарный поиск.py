s = int(input()) #то, что буду искать
target = [45, 34, 44, 28, 7, 56, 85, 89, 23, 12, 5] #список откуда буду искать
target = sorted(target) #метод сортировки

def fff(target, s):
    left = 0
    right = len(target) -1 #выбирать из длины спискп
    mid = (left + right) // 2
    lo = 0
    while s != target[mid]:
        
        lo +=1
        if s < target[mid]:
            right = mid - 1

        else:
            left = mid + 1 
        
        mid // 2 #это середина
    return lo   

print(fff(target, s))
