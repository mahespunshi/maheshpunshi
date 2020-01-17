## multiple forms, like human we deal with multiple people with multiple people.
# four ways of doing polymorphism 1. duck typing 2. operator overloading 3. method overload, 4. method overriding.
# in java and C we describe variable types like init, string etc, but not in python.

#3 Method overloading: not in python: in a class two method with same name but different parameters
## this is same umesh taught about avoid error, we should define none, in case no value is given. For example, we are given two values and third is missing or vice versa



class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s = 0
        if a != None and b!= None and c!= None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a +b
        else:
            s = a
        return s


s1 = Student(58,69)
print(s1.sum())   ## no argument
print(s1.sum(1,2,3))  ## 3 arguments
print(s1.sum(3,4))    ## two arguments

# All arguments meets above requirement,if none is given we can give value.

# Method overriding: two methods with same name and same parameters/arguments: in concept of inheritance, lets say we have class A and class B
## we have same method name in two classes. This concept is very important


class A:

    def show(self):
        print("in A show")

class B(A):
    ##pass  ## not doing any thing, just keep it

    def show(self):
        print("in B show")  ## this show overrides the show of class A (even in inheritance) like anlagy given by Naveen of his phone and his father's phone, so my phone now overrides my fathers phone.

a1 = A()
a1.show()

b = B()
b.show()

