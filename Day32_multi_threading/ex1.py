from threading import *
from time import *

def display(str):
    l.acquire()
    for i in str:
        
        print(i)
        sleep(0.5)
    l.release()


t=Thread(target=display,args=('hello world',))
t1=Thread(target=display,args=('python is easy',))
t2=Thread(target=display,args=('123456789',))

l=Semaphore(2)

t.start()
t1.start()
t2.start()

t.join()
t1.join()
t2.join()