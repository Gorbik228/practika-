
#импорт библиотек
import math
import matplotlib.patches
import matplotlib.pyplot as mathplt


#создаем класс
class Octagon: #
    def __init__(self,side):
        self.side = side
        self.k = (1+math.sqrt(2))
        self.corner = 135


    def inscribed_circle(self): #находим радиус и площадь описаннной окружности
        self.rad1 = self.side*math.sqrt(self.k/(self.k-1))
        self.s1 = self.rad1**2*3.14
        print(f'Радиус опис оркужности{self.rad1}')
        print(f'Площадь опис окружности{self.s1}')

    def circumscribed_circle(self): #радиус и площадь вписанной окружности
        self.rad2 = math.sqrt(2)/2*self.side
        self.s2 = self.rad2**2*3.14
        print(f'Радиус впис окружности{self.rad2}')
        print(f'Площадь впис окружности{self.s2}')
    

    def perimeter(self): #находим периметр октагона
        self.per = 8*self.side
        print(f'Периметр октагона{self.per}')


    def square(self): #находим площадь октагона
        self.sq = 2*self.side**2*self.corner
        print(f'Площадь октагона{self.sq}')


    def picture(self): #вывод графика
        self.sq = 2*self.k*self.side**2
        self.rad2= math.sqrt(self.sq/8/(math.sqrt(2)-1))
        self.rad1 = math.sqrt(self.sq/2/math.sqrt(2))

        mathplt.xlim(-25, 25)
        mathplt.ylim(-25, 25)
        mathplt.grid()
        axes = mathplt.gca()

        polygon_1 = matplotlib.patches.Polygon([(self.rad2, self.side/2),  #делаем октагон
                                                (self.rad2, -self.side/2),
                                                (self.side/2, -self.rad2),
                                                (-self.side/2, -self.rad2),
                                                (-self.rad2, -self.side/2),
                                                (-self.rad2, self.side/2), 
                                                (-self.side/2, self.rad2), 
                                                (self.side/2, self.rad2)], 
                                                fill = False, color = 'red')

        a = matplotlib.patches.Circle((0, 0), radius=self.rad1, fill = False, color = 'yellow') 
        b = matplotlib.patches.Circle((0, 0), radius=self.rad2, fill = False, color = 'green')
        axes.add_patch(a)
        axes.add_patch(b)
        axes.add_patch(polygon_1)
        mathplt.show()


    def __del__(self):
        print('Класс удален')
    