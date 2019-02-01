#!/home/wizard/anaconda3/bin/python3.7

from time import time,sleep
from functools import wraps



def mesure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper"""
        t = time()
        func(*args,**kwargs)
        print(func.__name__, ' time:', time() - t)
    return wrapper


@mesure
def foo(sleep_time = 0.3):
    """foo sleeps sleep_time seconds"""
    sleep(sleep_time)

@mesure
def gen_squares(n):
    return [ x ** 2 for x in range(n)]

foo(0.3)
s = gen_squares(10)

print( foo.__doc__)
print(type(s))