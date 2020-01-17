# search a value from list, binary search is faster than linear search
pos = -1

def search(list, n):
    # i = 0

    # while i < len(list):
    #     if list[i] == n:
    #         globals()['pos'] = i
    #         return True;
    #     i = i + 1
    # return False;

# above example is a while loop, let's do in for loop, we don't increment in for loop

    # for i in list:
    #     if i == n:
    #         globals()['pos'] = i
    #         return True

# another method in for loop

    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True

    return False


list = [5,8,4,6,9,2]

# search any number

n = 9

if search(list,n):
    print("Found at", pos + 1)

else:
    print("Not Found")
