#!/home/wizard/anaconda3/bin/python3.7

#клас, това е типа
class Point:
    x = 10 # static
    def __init__(self):
        print('Constructor') 
        self._x = 1
        self._y = 3

if __name__ == '__main__':
    p1  = Point() # обект, представител на класа    

    print(f' ( {p1._x}, {p1._y} )')
    print(type(p1))
    print(f'x = {p1.x}')
    print(f'x = {Point.x}')
    p2 = Point()
    Point.x = 111
    print(f'x = {p2.x}')
    print(f'x = {Point.x}')

    