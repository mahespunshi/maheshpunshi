class myMath:

    def add(self,x,y):
        return (x + y)

    def subract(self,x,y):
        return(x - y)

    def multiply(self,x=0,y=0):
        return (x * y)

    def divide(self,x,y):
        try:
            return (x /y)
        except ZeroDivisionError as e:
            print e
            #print('Divide by zero is not allowed')



calculator = myMath()

print(calculator.add(3,4))
print(calculator.subract(10,9))
print(calculator.multiply(3,3))
print(calculator.divide(4,2))


# we could use one object instead of 4.