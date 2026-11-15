a = [45, 34, 44, 28, 7, 56, 85, 89, 23, 12, 5]

def bubble(a):
    for f in range(len(a) -1):
        for i in range(len(a)-1-f):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a [i+1], a[i]
    print(a)
print(bubble(a))
