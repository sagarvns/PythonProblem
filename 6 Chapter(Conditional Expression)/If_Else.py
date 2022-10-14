age=int(input("Enter Your Age"))
if age>18:
    print("Yes")
else:
    print("No")
#Max in 4 number   
num1=int(input("Enter Number 1:"))  
num2=int(input("Enter Number 2:"))  
num3=int(input("Enter Number 3:"))  
num4=int(input("Enter Number 4:"))  
if(num1>num4):
    f1= num1
else:
    f1=num4
    
if(num2>num3):
    f2= num2
else:
    f2=num3
if(f1>f2):
    print(str(f1) + "Greatest")   
else:
    print(str(f2) + "Greatest") 
    
    

