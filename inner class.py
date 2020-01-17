class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() ## we call object in ouside class for laptop (inner class)

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student("Mahesh", 23)
s2 = Student("Rakesh", 25)
s1.show()

lap1 = s1.lap
print(lap1.brand)

# you can create object of inner class inside the outer class
# you can create object of inner class outside the outer class provided you use outer class name to call it.

s1.lap.show()
s1.show()