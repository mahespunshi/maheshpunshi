f = open('/Users/maheshkumar/Desktop/rsi.txt', 'r')
# print(f.readlines(2))
# print(f.readline())
#
#
# f1 = open('abc', 'a')
# f1.write("\nsomething\n")
# f1.write("Laptop\n")

# following example is reading lines one by one.
# for data in f:
#     print(data)

# What if we want to write something line by line to another file.

# f1 = open('abcd', 'w')
# for data in f:
#     f1.write(data)

# to open a pic like jpg file, use 'rb' which is read binary.

# f = open('image.jpg','rb')
#
# for i in f:
#     print(i)

## what if we want to write image to another file 'wb' write binary.

f1 = open('Mypic.jpg','wb')

for i in f:
    f1.write(i)
