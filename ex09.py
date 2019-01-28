#!/home/wizard/anaconda3/bin/python3.7


def suma(a,b, d = None ):
    if not d:
        c = a +b
    else:
        c = a + b + d
        
    return c

    
def main():
    x,y = (5,6)
    res = suma(x,y)
    print('{} + {} = {}'.format(x,y,res))
    
    z = 9
    res = suma(x,y,z)
    print('{} + {} + {} = {}'.format(x,y,z,res))
        

if __name__ == '__main__':
    main()


