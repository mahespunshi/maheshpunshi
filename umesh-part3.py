class myMath:

    def add(self,x,y):
        return (x+y)

    def subract(self,x,y):
        return(x-y)

    def multiply(self,x,y):
        return (x*y)

    def divide(self,x,y):
        return (x/y)

calculator = myMath()
while True:
    print("Choose from 1 -5, what would you like to perform?")
    print("1.Add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.close")
    z = int(input("Choose any option"))
    if z==5:
        quit();
    while z<1 or z>4:
        print ("Wrong Input")
        z = int(input("choose any action"))

    n1 = int(input("Enter first number"))
    n2 = int(input("Enter second number"))
    if z == 1:
        print(calculator.add(n1,n2))
    elif z == 2:
        print(calculator.subract(n1,n2))
    elif z == 3:
        print(calculator.multiply(n1,n2))
    elif z == 4:
        try:
            print(calculator.divide(n1,n2))
        except ZeroDivisionError as e:
            print e