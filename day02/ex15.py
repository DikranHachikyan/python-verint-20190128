#!/home/wizard/anaconda3/bin/python3.7

def get_squares(n):
    return [ x ** 2 for x in range(n)]
    
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2

if __name__ == '__main__':
    get_squares(10)

    s = get_squares_gen(10)

    print(type(get_squares_gen))
    print(type(s))

    for x in s:
        print(x)
