#!/home/wizard/anaconda3/bin/python3.7

def sum_ab():
    a = 10
    try:
        b = int(input('value of b(int):'))

    except ValueError as e:
        print('Invalid value:',e)
    else:
        print('[else]')
        return  a,b,a+b
    finally:
        print('[finally]')

if __name__ == '__main__':
    res = sum_ab()
    print('res:',res)
        

    