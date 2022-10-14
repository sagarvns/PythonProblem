def enqueue(a,val):
    a.append(val)
    print("Value of Insertion Successful")
def dequeue(a):
    a.pop(0)
    print("Value Of Dequeue Successful")

def peak(a):
    print("Peak Element Is successful",a[0])


def display(a):
    for i in a:
        print(i)




a=[]
while True:
    choice=int(input("1--Enqueue \n2--Dequeue \n3--peak \n4--Display  \n5--Exit \nEnter Your Choice== "))
    if choice==1:
        val=int(input("Enter Your Push Number"))
        enqueue(a,val)
    elif choice==2:
        if len(a)==0:
            print("Queue Is Underflow")
        else:
            dequeue(a)
    elif choice==3:
        if len(a)==0:
            print("Queue Is Underflow")
        else:
            peak(a)
    elif choice==4:
        if len(a)==0:
            print("Queue Is Underdflow")

        else:
            display(a)
    else:
        break