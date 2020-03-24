class myMath:

    def add(self,x,y):
        return (x + y)

    def subtract(self,x,y):
        return(x - y)

    def multiply(self,x,y):
        return (x * y)

    def divide(self,x,y):
        return (x /y)

print("Choose from 1 -4, what would you like to perform?\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide")


calculator = myMath()

z = int(input("Enter the number"))
while z<1 or z>4:
    print("Wrong Input!")
    z = input("Enter the number")

n1 = float(input("Enter a number "))
n2 = float(input("Enter second number "))
if z == 1:
    print(calculator.add(n1, n2))
elif z == 2:
    print(calculator.subtract(n1,n2))
elif z == 3:
    print(calculator.multiply(n1,n2))
else:
    print(calculator.divide(n1,n2))




