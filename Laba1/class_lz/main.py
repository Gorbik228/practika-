from kod import Octagon #импортируем класс

def main(): #создаем функцию 
    first = Octagon(10) #добавляем объект
    first.inscribed_circle() #используем все методы
    first.circumscribed_circle()
    first.perimeter()
    first.square()
    first.picture()

if __name__ == '__main__': #проверяем на прямой запуск
    main() #запускаем функцию