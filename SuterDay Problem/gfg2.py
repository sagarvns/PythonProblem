a = [3, 9, 1, 7, 6, 11, -191]
max1 = a[0]
min1 = a[0]
for i in a:
    if i > max1:
        max1 = i
    if i < min1:
        min1 = i
print(max1)
print(min1)
