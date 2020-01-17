class myMath:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return (self.x + self.y)

    def subract(self):
        return(self.x - self.y)

    def multiply(self):
        return (self.x * self.y)

    def divide(self):
        return (self.x /self.y)



sum = myMath(3,4)
minus = myMath(10,9)
multiply = myMath(11,12)
divide = myMath(12,4)

print(sum.add())
print(minus.subract())
print(multiply.multiply())
print(divide.divide())