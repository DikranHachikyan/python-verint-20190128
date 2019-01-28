#!/home/wizard/anaconda3/bin/python3.7

def main():
    t = 11,22,33,44,55,66
    #t = (11,22,33,44,55,66)

    for value in t:
        print('v={}'.format(value))

    for idx,value in enumerate(t[2:],2):
        print('index={} value={}'.format(idx,value))

    for value in range(1,20,2):
        print('v={}'.format(value))


if __name__ == '__main__':
    main()
