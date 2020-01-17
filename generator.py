## iterator is good to give you list of items, like printing all values.
# but you had to write methods on your own, but you don't want to do it instead Python can do it for you.

# we have to define a function here not a class

# we are making following function as generator with keyword yield.

# def topten():
#
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#



# values = topten()
# print(values)
# print(values.next())
# print(values.next())
# print(values.next())
# print(values.next())
# for i in values:
#     print(i)


## Example 2

def topten2():

    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1

## return will terminate the function but yield will not **

values2 = topten2()

for i in values2:
    print(i)
