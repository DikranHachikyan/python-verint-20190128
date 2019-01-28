#!/home/wizard/anaconda3/bin/python3.7


def suma(a,b, *args ):
    c = a + b
    for v in args:
        c += v    
    return c

    
def main():
    x,y = (5,6)
    res = suma(x,y)
    print('{} + {} = {}'.format(x,y,res))
    
    z = 9
    res = suma(x,y,z)
    print('{} + {} + {} = {}'.format(x,y,z,res))
    

    res = suma(x,y,1,2,3,4)
    print('1+2+...+5+6 = {}'.format(res))

    l1 = [v for v in range(1,15)]
    res = suma(x,y, *l1)

    print('+'.join( map(str, l1)) + '+ {} + {}={}'.format(x,y,res) )        
    print('+'.join(str(v) for v in l1 ) + '+ {} + {}={}'.format(x,y,res) )        

if __name__ == '__main__':
    main()


