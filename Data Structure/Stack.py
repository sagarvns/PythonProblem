def push(a, val):
    a.append(val)
    print("Insertion Successful")


def pop(a):
    x = a.pop()
    print("pop Item=", x)
    print("pop Successfull.....")


def peek(a):
    index = len(a) - 1
    print("Peak Element ==", a[index])


def display(a):
    print("Stack Element are:")
    for i in range( len(a) - 1, -1, -1):
        print(a[i])
a=[]

while True:
    choice=int(input("1-->Push \n2--POP \n3--Peek  \n4-->Display \n5-->Exit "))

    if choice==1:
        val=int(input("Enter Number To Push"))
        push(a,val)

    elif choice==2:
        if len(a)==0:
            print("stack Underflow")
        else:
            pop(a)

    elif choice ==3:
        if len(a)==0:
            print("stack Underflow")
        else:
            peek(a)

    elif choice==4:
        if len(a)==0:
            print("stack Underflow")
        else:
            display(a)
    else:
        break

