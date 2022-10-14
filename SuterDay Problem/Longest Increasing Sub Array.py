a1 = [4, 6, 2, 1, 4, 5, 6, 7, -1, 2, 3, 4, 5, 6, 7, 8]

n = len(a1)
maxlen = 0
maxa = 0
maxb = 0
a = 0
b = 0

for i in range(n - 1):
    if (a1[i] > a1[i + 1]):
        b = i
        print("b", i)
        if (b - a + 1) > maxlen:
            maxlen = b - a + 1
            maxa = a
            maxb = b
        a = i + 1
        print(a)
b = i
print(b)
if (b - a + 1) > maxlen:
    maxlen = b - a + 1
    maxa = a
    maxb = b
print(maxa, maxb)
print(a1[maxa:maxb + 1])
