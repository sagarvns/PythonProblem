a = [15, -20, 2, -8, 1, 7, 10, 23]
maxsum = a[0]
currsum = 0
c=[]
for i in range(len(a)):
    curr = a[i]
    c.append(curr)
    currsum = currsum + curr
    if currsum > maxsum:
        maxsum = currsum
    if currsum < 0:
        currsum = 0
        c.clear()
print(c)

print(maxsum)


