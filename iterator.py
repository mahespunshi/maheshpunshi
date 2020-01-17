#nums = [7,8,9,45]

# 1st way
## for i in nums:
##    print(i)

# For loop behind the scene is also iterator,

# 2nd way

# it = iter(nums)
## next is not working ..
# print(it.__next__())

## print(next(it))
# print(next(it))
#print(next(it))
#print(next(it))

## Above commented is just an example that you can have your own iterator by creating own object and class. In above example next is the iterator etc.


class TopTen:
    def __init__(self):
        self.num = 1  ## just create a counter variable that will start from 1.

# To create your own iterator, we need two important methods. 1) iter() will give you object of iter 2) next() will give next value/object.

    def __iter__(self):
        return self

    def next(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


value = TopTen()
print(next(value))  ## notice in output it doesn't show value twice for i, is beauty of iterator, it shows only once.

for i in value:
    print(i)