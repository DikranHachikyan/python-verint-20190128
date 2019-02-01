#!/home/wizard/anaconda3/bin/python3.7

def show(a = [], b = {}):
    z = 2
    print(a)
    print(b)
    print('-' * 12, z * 2)
    a.append(len(a))
    b[len(a)] = len(a)
    
if __name__ == '__main__':
    show()    
    show([1,2,3], {'B':100})    
    show()    
