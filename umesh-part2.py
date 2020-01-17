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

print("Choose from 1 -4, what would you like to perform?")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
z = input("Enter the number")

n1 = int(input("Enter a number"))
n2 = int(input("Enter second number"))

plus = myMath(n1,n2)
minus = myMath(n1,n2)
multiply = myMath(n1,n2)
divide = myMath(n1,n2)



if z == 1:
    print(plus.add())
elif z == 2:
    print(minus.subract())
elif z == 3:
    print(multiply.multiply())
else:
    print(divide.divide())




