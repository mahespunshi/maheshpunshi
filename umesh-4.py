# 1. Write a program that runs for 10 seconds and generates a random number in range 0 to 10.
# Before termination of program, it should display number of times each number generated.
#
# 2. Modify the program above to display the output in descending order such that the number
# that has most number of occurences is shown first and the number that has least number of occurences is shown last.


import multiprocessing
import time
from random import random
from random import seed
from random import randint

counter = []

for i in range(10):
    n = randint(0,10)
    time.sleep(1)
    counter.append(n)
    print(counter)





# t1.sleep(10)
# t1.terminate()
# t1.join()
#
# # Your foo function
# def foo(n):
#     for i in range(10000 * n):
#         print "Tick"
#         time.sleep(1)
#
# t1 = foo()
# t1.sleep(10)
# t1.terminate()
# t1.join()
#
# # if __name__ == '__main__':
# #     # Start foo as a process
# #     p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
# #     p.start()
# #
# #     # Wait 10 seconds for foo
# #     time.sleep(10)
# #
# #     # Terminate foo
# #     p.terminate()
# #
# #     # Cleanup
# #     p.join()