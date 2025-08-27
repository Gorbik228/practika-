
class Vehicle:

    def __init__(self,brand,model,year):    
        self.brand = brand
        self.model = model
        self.year = year
    
    def informattion1(self):
        print ("Автомобиль")
        print (f"Бренд: {self.brand}")
        print (f"Модель: {self.model}")
        print (f"Год выпуска: {self.year}")


class Car(Vehicle):

    def __init__(self,brand,model,year,fuel_type, max_speed, engine_capacity, rotation_speed, pe):
        super().__init__(brand,model,year)
        self.fuel = fuel_type
        self.capacity = engine_capacity
        self.max_speed = max_speed
        self.rotation_speed = rotation_speed
        self.pe = pe
    
    def engine_power_calc(self):
        self.engine_power = self.capacity * self.pe * self.pe *1000 / 120 / 0.735
        print (f"Мощность ДВС равна: {self.engine_power} лс")

    def informattion2(self):
        print (f"Вид топлива: { self.fuel}")
        print (f"Максимальная скорость: {self.max_speed} км/ч")
        print (f"Обьем двигателя: {self.capacity} TDI")
        print (f"Количетсво оборотов в минуту: {self.rotation_speed} об/мин")
        print (f"Среднее давление масла : {self.pe} кПа")
        
    