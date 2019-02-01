#!/home/wizard/anaconda3/bin/python3.7

from time import time,sleep

def foo():
    sleep(0.3)

def bar():
    sleep(0.5)

def mesure(func):
    t = time()
    func()
    print(func.__name__, ' time:', time() - t)

mesure(foo)
mesure(bar)

