from threading import Thread
from time import sleep
from sys import exit

def f():
    print('thread begin')
    raise Exception
    print('thread end')

print('begin')
Thread(target=f).start()
while 1:
    print('running')
    sleep(1)
print('end')