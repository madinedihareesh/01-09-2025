from threading import *
from time import sleep

class Alpha(Thread):
    def run(self):
        for i in range(65,91):
            print(chr(i))
            sleep(0.5)
        
t=Alpha()

t.start()

for i in range(65,91):
    print(i)
    sleep(0.5)

t.join()    


