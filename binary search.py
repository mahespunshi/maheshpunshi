# make lower bound and upper bound, if search value is smaller then change upper bound and Mid becomes new upper bound.
# if search value is bigger then change lower bound and mid becomes new lower bound.

# to make binary efficient, we need to sort out values first, that way we will skip many values to search comparison.

pos = -1

def search(list, n):
    l = 0  # define lower bound
    u = len(list) -1 # define upper bound, -1 because values in list start from 0.
    while l <= u:
        mid = (l+u)//2  ## double slash will give you integer value, we don't want normal division(like float)

        if list[mid] == n:
            globals()['pos'] = mid
            return True   # to break the loop
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

list = [1,2,3,4,45]
n = 32

if search(list,n):
    print("Found at", pos+1)

else:
    print("Not Found")

