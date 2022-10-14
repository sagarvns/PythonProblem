a = "a1b2c5d8"
ord0 = ord('0')
ord9 = ord('9')
total = 0
for ch in a:
    if ord(ch) >= ord0 and ord(ch) <= ord9:
        total += int(ch)
print(total)
