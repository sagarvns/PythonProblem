class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Sagar Chauhan ", 36)
p1.myfunc()


class Person:

    def __init__(mysillyobjct, name, age):
        mysillyobjct.name = name
        mysillyobjct.age = age

    def myfunc(abc):
        print("hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()


# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()

class DemoClass:
    a=10
    def sumvalue(self):
        print(70+10)
demoobject=DemoClass()
print(demoobject.a)
demoobject.sumvalue();

class Phone:
    def makecall(self):
        print("makeing call")
    def gamecall(self):
        print("plaing game")
p1=Phone()
p1.makecall()
p1.gamecall()

class Mobail:

    # def __init__(self,cl="sdf",ct=0):
    #     self.color=cl
    #     self.cost=ct

    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def makecall(self):
        print("makeing call")
    def gamecall(self):
        print("plaing game")

p2=Mobail()
p2.set_color("red")
p2.set_cost(44)
print(p2.show_color())
print(p2.show_cost())


