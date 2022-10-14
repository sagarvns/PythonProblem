a = [53, 8, 6, -7, 2]
fp = 0
left = 0
right = len(a) - 1
pivot = a[left]
print(left, fp, right, pivot)
for i in range(left + 1, right + 1):
    if a[i] >= pivot:
        continue
    fp += 1
    a[i], a[fp] = a[fp], a[i]
    print(a)
a[left],a[fp]=a[fp],a[left]
print(fp)
print(a)
