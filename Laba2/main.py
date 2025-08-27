from inherit import Vehicle #импортируем классы
from inherit import Car 

def main(): #создаем функцию 
    first = Vehicle('Audi', 'a5', '1997') #добавляем объект
    second = Car('Audi', 'a5', '1997', 'Дизель', 200, 1.9, 4500, 2.3) 
    first.informattion1() 
    second.informattion2()
    second.engine_power_calc()

if __name__ == '__main__': 
    main()