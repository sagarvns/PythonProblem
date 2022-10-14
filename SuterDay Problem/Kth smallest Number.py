a = [53, 8, 6, -7, 2]
pos = int(input("Enter pos\n"))
pos = pos - 1

left = 0
right = len(a) - 1
if pos < left or pos > right:
    print("Galat Hy ")
else:

    while True:
        a[pos], a[left] = a[left], a[pos]
        fp = left
        pivot = a[left]

        for i in range(left + 1, right + 1):
            if a[i] >= pivot:
                continue
            fp += 1
            a[i], a[fp] = a[fp], a[i]
        a[left], a[fp] = a[fp], a[left]
        if fp == pos:
            print("Ans=", pivot)
            print(a)
            break
        if pos < fp:
            right = fp - 1
        else:
            left = fp + 1
