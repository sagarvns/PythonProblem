
class GeekforGeeks:

	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = GeekforGeeks()
obj.print_Geek()

#parameterized constructor :


class Student:
    a=0
    b=0
    add=0
    def __init__(self,aa,bb):
        self.a=aa
        self.b=bb
    def display(self):
        print("First number"+ str(self.a))
        print("Second number"+ str(self.b))
        print("Add Number"+ str(self.ans))
    def calculate(self):
        self.ans=self.a + self.b

obj=Student(100,200)
obj.calculate()
obj.display()


