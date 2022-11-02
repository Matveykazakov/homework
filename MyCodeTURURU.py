import pandas as pd
from tkinter import *

root = Tk()
root.title("У вас одно сообщение, возможно вас любят и хотят вам признаться")
root.geometry("1500x800+100+100")
root.resizable(width=False, height=False)


def outText():
    label.configure(text="Здравствуйте уважаемый заказчик, мы тут немного постарались чего-то сделать, надеюсь вам понравится и вы поставите 5 звезд)))))",background="#eaf518",
    pady="100", font="12")


btn1 = Button(root, command=outText, text="Жми на меня", background="#008000", foreground="#fff", pady="2", font="12",
              width=30)
btn1.place(x=10, y=20)

label = Label(root)
label.place(x=250, y=300)

root.mainloop()

# таблица DataFrame
DataFrameTamer = pd.DataFrame(
    {
        "Год/Месяц": ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
        "2017": [65000, 61000, 63000, 0, 70580, 97365, 104755, 101820, 83655, 77910, 70365, 64200],
        "2018": [69550, 65270, 67410, 73830, 75521, 0, 112088, 108947, 89511, 83364, 75291, 68694],
        "2019": [71358, 66967, 69163, 75750, 77484, 106889, 115002, 111780, 91838, 85531, 0, 70480],
        "2020": [77781, 0, 75387, 82567, 84458, 116509, 125352, 0, 100104, 93229, 84200, 76823],
        "2021": [81670, 76644, 79157, 86695, 88681, 122335, 131620, 127932, 105109, 97890, 88410, 80664],
        "2022": [89837, 84308, 87072, 95365, 97549, 134568, 144782, 140725, 115620, 107679, 97252, 88731],
     }
)
k = 0
a = 1
i = 0
x = -11
c = 0
g = 0
shape = DataFrameTamer.shape
sr_cnach = 0
array = [None] * 12
years = 2023

while a != shape[1]:  # находим недостающее
    while i < shape[0]:
        if DataFrameTamer.iloc[i, a] == 0:
            c = DataFrameTamer.iloc[i-1, a]*(DataFrameTamer.iloc[i, a+1]/DataFrameTamer.iloc[i-1, a+1])
            DataFrameTamer.iloc[i, a] = round(c)
            i += 1
        else:
            i += 1

    i = 0
    a += 1
a -= 1

while i < shape[0]:  # находим среднее значение
    sr_cnach = sr_cnach + DataFrameTamer.iloc[i, a]
    i += 1
sr_cnach = sr_cnach / i
sr_cnach = round(sr_cnach, 2)
summ = sr_cnach * i

i = 0


while x < 1:  # узнаём элемент формулы
    b = x * DataFrameTamer.iloc[i, a]
    array[i] = b
    i += 1
    x += 1
c = sum(array)

lin_trend_b = (i*c-summ*(-66))/(i*506-4356)  # узнаём b для формулы линейного тренда
lin_trend_b = round(lin_trend_b, 6)

lin_trend = (summ-lin_trend_b*-66)/12  # узнаём элемент формулы
lin_trend = round(lin_trend)

lin_trend_a = lin_trend-lin_trend_b*12  # узнаём а для формулы линейного тренда
lin_trend_a = round(lin_trend_a, 5)

period = i+1

i = 0

while g < 2:

    DataFrameTamer.insert(a+1, years, '',)  # создаём новый год в списке

    while k < 12:
        trend = lin_trend_b*period+lin_trend_a
        trend = round(trend)  # тренд

        index = DataFrameTamer.iloc[i, 6]/sr_cnach
        index = round(index, 2)  # индекс

        prognoz = trend * index
        prognoz = round(prognoz)  # прогнозируем
        DataFrameTamer.iloc[i, a + 1] = prognoz  # присваиваем найденное значение ячейке таблицы
        i += 1
        period += 1
        k += 1

    g += 1
    k = 0
    i = 0
    years += 1
    a += 1
print(DataFrameTamer)


