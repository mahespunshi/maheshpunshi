# in real life parents vs child sceniors

# class inherits class


class A:    ## this is consturctor
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


a1 = A()
a2 = A()
a1.feature1()
a2.feature2()
b1 = B()
b1.feature3()
b1.feature4()

# In situation where you want class B to take every feature from class A, look below
## class B(A): in this case class B inherits all features from A
# so we call them subclass and super class

# Multilevel inheritance

class C(B):
    def feature5(self):
        print("Feature 5 working")

c1 = C()
c1.feature5()

## OR Multiple inheritance

class C2(B,A):
    def feature6(self):
        print("Feature 6 is working")


c2 = C2()
c2.feature6()

# MRO = Method resolution order, always start from left to right

