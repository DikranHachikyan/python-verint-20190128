#!/home/wizard/anaconda3/bin/python3.7

def main():
    # 1 + 2 + ... + 99 + 100 = 5050
    i = 1
    suma = 0

    while i <= 100:
        suma += i
        i += 1
    else:
        print('else part')

    print('1+2+...+99+100 = {}'.format(suma))

if __name__ == '__main__':
    main()
