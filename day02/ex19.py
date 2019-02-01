#!/home/wizard/anaconda3/bin/python3.7

from time import time,sleep

def foo():
    sleep(0.3)

def bar():
    sleep(0.5)

t = time()
foo()
print('foo:', time() - t)

t = time()
bar()
print('bar:', time() - t)


