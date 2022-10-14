arr = [3, 4, 17, 10, 15, 1]
max1 = arr[0]
max2 = arr[1]
if max2 > max1:
    max1, max2 = max2, max1

for i in range(2, len(arr)):
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]
        continue
    if arr[i] > max2:
        max2 = arr[i]
print(max1, max2)
