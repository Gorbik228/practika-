import pandas as pd
class Summa_cash:

    def __init__(self): #инициализация
        self.file = pd.read_csv('var10.csv')


    def __pos__(self): #доопределения унарного +
        self.df = self.file.drop_duplicates() #удаляем дубликаты строк
        first_count = self.file.shape[0] #считаем кол-ыо дубликатов
        second_count = self.df.shape[0]
        dropped = first_count - second_count
        print(f'В файле удалено {dropped} дубликатов')

    def razdel(self): #разделение датафрейма на 2 разных

        self.df1 = self.df[self.df['Сумма cash-back'] > 0]    # строки, удовлетворяющие условию
        self.df2 = self.df[self.df['Сумма cash-back'] == 0]    # строки, не удовлетворяющие условию
        self.df1.to_csv('first.csv')
        self.df2.to_csv('second.csv')

    def __del__(self):
        print('Датафрейм удален')