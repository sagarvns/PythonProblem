print("half porymid of stor ")
for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()

print("Swap Two veriable program ")

x=20
y=10
x,y=y,x
print("value of x:",x)
print("value of y:",y)


# print(" ****  Fibonaci Series **** ")

# n=int(input("Enter The value Of N :"))
# a=0
# b=1
# sum=0
# count=1
# print(" Fibonaci Series:",end=" ")
# while(count<=n):
#     print(sum,end=" ")
#     count +=1
#     a=b
#     b=sum
#     sum=a+b
    
print("Python program to Generate a Rondom number")

import random
print(random.randint(0,9))



# print("Python Programe to calculate area of terangal")
# s1=5
# s2=2
# s3=7
# s=(a+b+c)/2
# area=(s*(s-s1)*s*(s-s2)*s*(s-s1))
# print("area of traingal is ")


print("Ascii value ")
c='p'
print("the Ascii value = ",ord(c))

print("Display a Calander ")
import calendar
yy=2001
mm=11
print(calendar.month(yy,mm))



print(" Add Two Matrix ")
x=[[12, 7, 3],[4, 5, 6],[7, 8, 9]]
y=[[5, 8, 1],[6, 7, 3],[4, 5, 9]]

result=[[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(len(x)):
    for j in range(len(y)):
        result[i][j]=x[i][j] + y[i][j]
for r in result:
    print(r)

print("python simple calculater ")
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("selector Option")
print("1.add")
print("2.sub")
print("3.mul")
print("4,div")

while True:
    choice=input("Enter your Choise")
    if(choice in ('1', '2')):
