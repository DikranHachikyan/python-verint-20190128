#!/home/wizard/anaconda3/bin/python3.7


if __name__ == '__main__':
    
    a = 10
    try:
        b = int(input('value of b(int):'))

    except ValueError as e:
        print('Except 1:',e)
    except TypeError as e:
        print('Except 2:',e)
    except:
        print('Except 3')
    else:
        print(f'[else] {a} + {b} = {a + b}')
    finally:
        print('[finally]')
        

    