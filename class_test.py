class Student:

    school = 'Mahesh'     ## class variable, to call it we need class method

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):       ## this is called instance method, bc self is taken from init class
        return (self.m1+self.m2+self.m3)/3

# getter = Accessor : They get the value
# setter = Mutator : Changes the value.

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1 = value


##  Above is called instance method

# Now lets talk about class method, to call class variable you need to call cls variable and to get instance variable you need to work on instance variable.

    @classmethod  ## decorator
    def def_class(cls):
        return cls.school
    @staticmethod
    def info():
        print("We don't need to pass anything in this static method.")


s1 = Student(34,47,32)
s2 = Student(1,2,3)
print(s2.avg())
setter = s1.set_m1(20)
getter = s2.get_m1()
print(getter)
print(s1.avg())

## it should wrk with object or class name, since its class variable, we should be able to work with class as well
## this is giving error, so we need to define decorator to avoid passing anything in class variable. otherwise we need to pass something as other methods.
print(Student.def_class())
Student.info()
