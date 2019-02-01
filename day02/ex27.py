#!/home/wizard/anaconda3/bin/python3.7


if __name__ == '__main__':
    
    a = 10
    try:
        b = int(input('value of b(int):'))

    except ValueError as e:
        print('Invalid value:',e)
    else:
        print(f'[else] {a} + {b} = {a + b}')
    finally:
        print('[finally]')
        

    