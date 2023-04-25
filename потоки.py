from threading import Thread
from time import sleep
def func():
    for i in range(5):
        print(f"from child thread: {i}")
        sleep(0.5)
th = Thread(target=func)
th.start()
for i in range(5):
    print(f"from main thread: {i}")
    sleep(1)
    
'''
from child thread: 0
from main thread: 0
from child thread: 1
from main thread: 1
from child thread: 2
from child thread: 3
from main thread: 2
from child thread: 4
from main thread: 3
from main thread: 4
'''

class CustomThread(Thread):
    def __init__(self, limit):
        Thread.__init__(self)
        self._limit = limit
    def run(self):
        for i in range(self._limit):
            print(f"from CustomThread: {i}")
            sleep(0.5)
cth = CustomThread(3)
cth.start()

'''
from CustomThread: 0
from CustomThread: 1
from CustomThread: 2
'''
