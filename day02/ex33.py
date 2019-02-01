#!/home/wizard/anaconda3/bin/python3.7

#клас, това е типа
class Point:
   
    def __init__(self, x = 0, y = 0, *args,**kwargs):
        print('Constructor') 
        self._x = x # променливи на обекта
        self._y = y

    def moveTo(self, dx, dy):
        self._x += dx
        self._y += dy

    def show(self):
        print(f'Point ({self._x},{self._y})')

if __name__ == '__main__':
    p1  = Point() # обект, представител на класа    
    p1.show()
    
    p2 = Point(12,22)
    p2.show()
    p2.moveTo(100, -40)
    p2.show()