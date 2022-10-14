class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def employe_detail(self):
        print("Employee Name is ",self.name)
        print("Age of Employee is",self.age)
        print("Salary of Employee is ",self.salary)
        print("Gander ",self.gender)


p1=Employee("sagar",22,20000,"male")
p1.employe_detail()

class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_detail(self):
        print("I am a Vechicle")
        print("Vechicle in mileage ",self.mileage)
        print("cost of vechile",self.cost)

v1=Vehicle(500,500)
v1.show_detail()

# class Car(Vehicle):
#     def show_car(self):
#         print("I am Car ")
# c1=Car(200,200)
# c1.show_detail()
# c1.show_car()

class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)

        self.tyres=tyres
        self.hp=hp
    def show_Car_details(self):
        print("number of tyres in car:",self.tyres)
        print("power of car :",self.hp)
        print("i am car ")
c1=Car(600,10000000,8,9999)
c1.show_detail()

#multipal Inheritance

class Parent1():
    def assign_string_one(self,str1):
        self.str1=str1
    def show_string_one(self):
        return self.str1

class Parent2():
    def assign_string_two(self,str2):
        self.str2=str2
    def show_string_two(self):
        return self.str2

class Child(Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3 = str3
    def show_string_three(self):
        return self.str3


my_child=Child
my_child.assign_string_one("I am string of parant")

class Derived(Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3=str3
    def show_string_three(self):
        return self.str3

d1= Derived

d1.show_string_one()
d1.show_string_two()
d1.show_string_three()

