#!/home/wizard/anaconda3/bin/python3.7


if __name__ == '__main__':
    squares = ( x ** 2 for x in range(10) )

    print(type(squares))

    print(next(squares))
    print(next(squares))
    print(next(squares))

    l1 = list(squares)
    print(l1)