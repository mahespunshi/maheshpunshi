# compile time error --> Syntactical errors --> eg. missing (:), wrong spelling. easiest error.

# logical error e.g wrong output 2+2 = 5, like bugs, QA guys do this.

# run time error: everything is fine but user might give you a wrong input, e.g number divide by zero. mistake is done by user

a = 5
b = 2

try:
    print("Resource opened here")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, you can't divide a number by Zero", e)

except ValueError as e:
    print("Invalid input")

except Exception as e:  ## exception is something that doesn't fall under value or ZeroDivisonError.
    print("Something went wrong", e)

finally:    ## finally is used to close the open door, so that we can close the resource.
    print("resource close")
