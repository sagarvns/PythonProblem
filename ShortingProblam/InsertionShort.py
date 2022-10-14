size=int(input("Enter your Size"))
a=[]
for i in range(size):
    val=int(input("Enter Your Size"))
    a.append(val)
for i in range(1,size):
    t=a[i]
    j=i-1
    while j>=0 and t<a[j]:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=t
print("shorted list",a)

