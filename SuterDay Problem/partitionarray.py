a = [5, 5, 1, 6, 2, 4, 5, 7]
pivot = a[0]
j = 1
for i in range(1, len(a)):
    if a[i] <= pivot:
        a[i], a[j] = a[j], a[i]
        j += 1
a[0], a[j - 1] = a[j - 1], a[0]
print(a)
