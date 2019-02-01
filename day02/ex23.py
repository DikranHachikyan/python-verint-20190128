#!/home/wizard/anaconda3/bin/python3.7

from time import time,sleep
from functools import wraps



def mesure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper"""
        t = time()
        result = func(*args,**kwargs)
        print(func.__name__, ' time:', time() - t)
        return result
    return wrapper

def max_result(limit = 100):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > limit:
                print( f'Result is too big ({result}). Limit is {limit}')
            return result
        return wrapper
    return decorator

@mesure
@max_result(130)
def cube(n):
    return n ** 3

print(cube(2))
print(cube(5))