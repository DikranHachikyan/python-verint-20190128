#!/home/wizard/anaconda3/bin/python3.7

from time import time,sleep

def foo(sleep_time = 0.3):
    """foo sleeps sleep_time seconds"""
    sleep(sleep_time)


def mesure(func):
    def wrapper(*args, **kwargs):
        """Wrapper"""
        t = time()
        func(*args,**kwargs)
        print(func.__name__, ' time:', time() - t, func.__doc__)
    return wrapper

fn = mesure(foo)

fn(0.5)

print(fn.__name__ ,' doc:', fn.__doc__)



