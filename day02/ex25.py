#!/home/wizard/anaconda3/bin/python3.7


if __name__ == '__main__':
    
    a = 10
    try:
        b = int(input('value of b(int):'))

        print(f'{a} + {b} = {a + b}')
    except ValueError :
        print('Invalid value')

    