size=int(input("Enter the size Number"))
a=[]
for i in range(size):
    val = int(input("Enter Your Element in value"))
    a.append(val)
for i in range(size):
    for j in range(0,size-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t

print("Array is shorted")
print(a)