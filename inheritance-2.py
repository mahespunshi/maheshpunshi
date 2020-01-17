class A:    ## this is consturctor
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):
    def __init__(self):
        super().__init__()

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

a1 = A()
b1 = B()


# notice above super() is used to call parent class first.