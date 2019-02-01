#!/home/wizard/anaconda3/bin/python3.7

def c_filter(func, *args ):
    res = []
    for v in args:
        if func(v):
            res.append(v)
    return res

def cmp( v ):
    return v > 4


if __name__ == '__main__':
    f = lambda x: x ** 2 if (x % 2) == 0 else x ** 3

    print('res1:', f(4))
    print('res2:', f(5))

    items = [ ('A' , 5 , 7) , ('D', 2, 6 ), ('B', 4, 6), ('Z',2, 5)]

    items.sort()
    print('in place sort:', items)

    items.sort(key=lambda el: (el[1]))
    print('sort 2el:', items)

    items.sort( key=lambda el:(el[1],el[2]))
    print('sort 2, 3 el:', items)

    l1 = [4,5,10,1,2]
    print(sorted(l1))
    print('l1:',l1)

    l2 = c_filter( lambda e: e > 4, *l1)
    print('l2:', l2)
    print('l1:', l1)
    
    l2 = c_filter( cmp, *l1)
    print('l2:', l2)
    print('l1:', l1)