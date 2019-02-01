#!/home/wizard/anaconda3/bin/python3.7

def get_squares(n):
    return [ x ** 2 for x in range(n)]
    
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

if __name__ == '__main__':
    get_squares(5)

    s = get_squares_gen(5)

    print(type(get_squares_gen))
    print(type(s))

    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))
