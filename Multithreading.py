
from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep (1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep (1)

t1 = Hello()
t2 = Hi()

t1.start() # start will call run internally but it will run on two simulteneous thread
sleep(0.2) # to avoid collision between two threads, to understand remove this line and see output.
t2.start()

t1.join()
t2.join() ## You are asking main thread to wait for t1 and t2 to complete

print("Bye") ## this is done by main thread

# Main thread creates two threads one at a time with start keyword and join will wait for sometime.



