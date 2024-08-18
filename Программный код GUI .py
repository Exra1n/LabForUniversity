import tkinter
import tkinter.messagebox
import math



class MyGui:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Контрольная работа by Хныкин')
        self.main_window.geometry('1000x800')
        self.main_window.configure(background='pink')

        #Рамки
        self.Frame_tasks = tkinter.Frame(self.main_window)
        self.Frame_usl = tkinter.Frame(self.main_window)
        self.Frame_otv = tkinter.Frame(self.main_window)

        #Кнопки
        self.but1 = tkinter.Button(self.Frame_tasks,text='Задание 1.5',padx='100',pady='25',command= self.one)
        self.but2 = tkinter.Button(self.Frame_tasks, text='Задание 2.18',padx='100',pady='25',command=self.two)
        self.but3 = tkinter.Button(self.Frame_tasks, text='Задание 3.18',padx='100',pady='25',command=self.three)
        self.but4 = tkinter.Button(self.Frame_tasks, text='Задание 4.18',padx='100',pady='25',command=self.four)
        self.but5 = tkinter.Button(self.Frame_tasks, text='Задание 5.18',padx='100',pady='25',command=self.five)
        self.but6 = tkinter.Button(self.Frame_tasks, text='Задание 6.18',padx='100',pady='25',command=self.six)
        self.but7 = tkinter.Button(self.Frame_tasks, text='Задание 7.18',padx='100',pady='25',command=self.seven)
        self.but8 = tkinter.Button(self.Frame_tasks, text='Задание 8.18',padx='100',pady='25',command=self.eight)
        self.but9 = tkinter.Button(self.Frame_tasks, text='Задание 9.18',padx='100',pady='25',command=self.nine)
        self.but10 = tkinter.Button(self.Frame_tasks, text='Задание 10.18',padx='100',pady='25',command=self.ten)
        self.but11 = tkinter.Button(self.Frame_tasks, text='Задание 11.18',padx='100',pady='25',command=self.eleven)
        # упаковываем
        self.but1.pack()
        self.but2.pack()
        self.but3.pack()
        self.but4.pack()
        self.but5.pack()
        self.but6.pack()
        self.but7.pack()
        self.but8.pack()
        self.but9.pack()
        self.but10.pack()
        self.but11.pack()

        self.usl = tkinter.Label(self.Frame_usl,text= 'Условие')
        self.text_usl = tkinter.Text(self.Frame_usl,width= 80,height=20)

        self.usl.pack()
        self.text_usl.pack()

        self.otv = tkinter.Label(self.Frame_otv, text='Ответ')
        self.text_otv = tkinter.Text(self.Frame_otv, width=80, height=20)

        self.otv.pack()
        self.text_otv.pack()


        self.Frame_tasks.pack(side='right')
        self.Frame_usl.pack(side= 'top')
        self.Frame_otv.pack(side='bottom')

        tkinter.mainloop()

    def delete(self):
        self.text_otv.delete(1.0,tkinter.END)
        self.text_usl.delete(1.0, tkinter.END)
    def one(self):
        def solution_one(one):
            self.text_otv.delete(1.0, tkinter.END)
            ch1 = int(self.ent1.get())
            ch2 = int(self.ent2.get())
            sr = (ch1 + ch2) / 2
            self.text_otv.insert(1.0,f'Среднее арифметическое чисел {ch1} и {ch2} равно {sr}')
        self.delete()
        self.text_usl.insert(1.0,'Два целых числа вводятся с клавиатуры. Написать программу, находящую их среднее арифметическое.')
        self.run = tkinter.Toplevel()
        self.run.title('Решение')
        self.run.geometry('300x150')
        self.lab3 = tkinter.Label(self.run,text= 'Введите данные: ')
        self.Frame_1 = tkinter.Frame(self.run)
        self.Frame_2 = tkinter.Frame(self.run)
        self.lab_sk1 = tkinter.Label(self.Frame_1,text= 'Введите 1 число: ')
        self.ent1 = tkinter.Entry(self.Frame_1)
        self.lab_sk2 = tkinter.Label(self.Frame_1,text= 'Введите 2 число: ')
        self.ent2 = tkinter.Entry(self.Frame_1)
        self.but12 = tkinter.Button(self.Frame_2,text= 'Решить')
        self.but12.bind('<Button-1>',solution_one)

        self.lab3.pack()
        self.but12.pack()
        self.lab_sk1.pack(side='top')
        self.ent1.pack(side= 'top')
        self.lab_sk2.pack(side='top')
        self.ent2.pack(side='top')
        self.Frame_1.pack(side='top')
        self.Frame_2.pack(side='bottom')

    def two(self):
        def solution_two(two):
            self.text_otv.delete(1.0, tkinter.END)
            k = int(self.ent1.get())

            hours = k // 3600
            minutes = (k % 3600) // 60
            seconds = k % 60

            self.text_otv.insert(1.0,f'Полных часов:{hours}\n')
            self.text_otv.insert(2.0,f'Полных минут: {minutes}\n')
            self.text_otv.insert(3.0,f'Полных секунд:{seconds}\n')

        self.delete()
        self.text_usl.insert(1.0,'Идет k-я секунда суток. Написать программу для вычисления целого числа полных часов, минут, секунд.')
        self.run = tkinter.Toplevel()
        self.run.title('Решение')
        self.run.geometry('300x150')
        self.lab3 = tkinter.Label(self.run, text='Введите данные: ')
        self.Frame_1 = tkinter.Frame(self.run)
        self.Frame_2 = tkinter.Frame(self.run)
        self.lab_sk1 = tkinter.Label(self.Frame_1, text='Введите кол-во секунд: ')
        self.ent1 = tkinter.Entry(self.Frame_1)
        self.but12 = tkinter.Button(self.Frame_2, text='Решить')
        self.but12.bind('<Button-1>', solution_two)

        self.lab3.pack()
        self.but12.pack()
        self.lab_sk1.pack()
        self.ent1.pack()
        self.Frame_1.pack(side='top')
        self.Frame_2.pack(side='bottom')

    def three(self):
        def solution_three(three):
            self.text_otv.delete(1.0, tkinter.END)
            birthday_str = (self.ent1.get())
            birthday_day, birthday_month, birthday_year = map(int, birthday_str.split("."))

            current_date_str = (self.ent2.get())
            current_day, current_month, current_year = map(int, current_date_str.split("."))

            age_years = current_year - birthday_year
            age_months = current_month - birthday_month

            if age_years > 18 or (age_years == 18 and age_months >= 5):
                self.text_otv.insert(1.0,"Студенту исполнилось 18 лет и 5 месяцев.")
            else:
                self.text_otv.insert(1.0,"Студенту еще не исполнилось 18 лет и 5 месяцев.")

        self.delete()
        self.text_usl.insert(1.0,'Вводятся две даты: дата рождения студента и текущая дата. Написать программу, проверяющую, исполнилось ли студенту 18 лет и 5 месяцев.')
        self.run = tkinter.Toplevel()
        self.run.title('Решение')
        self.run.geometry('300x150')
        self.lab3 = tkinter.Label(self.run, text='Введите данные: ')
        self.Frame_1 = tkinter.Frame(self.run)
        self.Frame_2 = tkinter.Frame(self.run)
        self.lab_sk1 = tkinter.Label(self.Frame_1, text="Введите дату рождения студента в формате ДД.ММ.ГГГГ: ")
        self.ent1 = tkinter.Entry(self.Frame_1)
        self.lab_sk2 = tkinter.Label(self.Frame_1, text="Введите текущую дату в формате ДД.ММ.ГГГГ: ")
        self.ent2 = tkinter.Entry(self.Frame_1)
        self.but12 = tkinter.Button(self.Frame_2, text='Решить')
        self.but12.bind('<Button-1>', solution_three)

        self.lab3.pack()
        self.but12.pack()
        self.lab_sk1.pack(side='top')
        self.ent1.pack(side='top')
        self.lab_sk2.pack(side='top')
        self.ent2.pack(side='top')
        self.Frame_1.pack(side='top')
        self.Frame_2.pack(side='bottom')
    def four(self):
        global k
        k = 0
        def solution_four(four):
            global k
            def calculate_final_amount(principal, rate, time, compounding_frequency):
                final_amount = principal * (1 + rate / compounding_frequency) ** (compounding_frequency * time)
                return final_amount

            principal = float(self.ent2.get())
            rate = float(self.ent3.get())
            time = float(self.ent4.get())
            compounding_frequency = int(self.ent5.get())

            final_amount = calculate_final_amount(principal, rate, time, compounding_frequency)
            k += 1

            self.text_otv.insert(tkinter.END,f"На конец срока вклад бизнесмена № {k} будет равен {final_amount:.2f}\n")

        self.delete()
        self.text_usl.insert(1.0,'Известно, какую сумму денег, на какой срок (в годах) и под какой годовой процент положил каждый из n бизнесменов в банк. Определить величину вклада каждого бизнесмена на конец срока.')
        self.run = tkinter.Toplevel()
        self.run.title('Решение')
        self.run.geometry('400x250')
        self.lab3 = tkinter.Label(self.run, text='Введите данные: ')

        self.Frame_1 = tkinter.Frame(self.run)
        self.Frame_2 = tkinter.Frame(self.run)

        self.lab_sk2 = tkinter.Label(self.Frame_1, text=f"Введите величину вклада бизнесмена: ")
        self.ent2 = tkinter.Entry(self.Frame_1)
        self.lab_sk3 = tkinter.Label(self.Frame_1, text=f"Введите годовой процент бизнесмена (в долях): ")
        self.ent3 = tkinter.Entry(self.Frame_1)
        self.lab_sk4 = tkinter.Label(self.Frame_1, text=f"Введите срок вклада в годах для бизнесмена : ")
        self.ent4 = tkinter.Entry(self.Frame_1)
        self.lab_sk5 = tkinter.Label(self.Frame_1, text=f"Введите количество раз начисления процентов в год для бизнесмена ")
        self.ent5 = tkinter.Entry(self.Frame_1)
        self.but12 = tkinter.Button(self.Frame_2, text='Решить')
        self.but12.bind('<Button-1>', solution_four)
        self.lab3.pack()
        self.but12.pack()
        self.lab_sk2.pack(side='top')
        self.ent2.pack(side='top')
        self.lab_sk3.pack(side='top')
        self.ent3.pack(side='top')
        self.lab_sk4.pack(side='top')
        self.ent4.pack(side='top')
        self.lab_sk5.pack(side='top')
        self.ent5.pack(side='top')

        self.Frame_1.pack(side='top')
        self.Frame_2.pack(side='bottom')


    def five(self):
        def solution_five():
            self.text_otv.delete(1.0, tkinter.END)

            def find_completion():
                base_number = 523000
                for i in range(1000):
                    candidate = base_number + i
                    if candidate % 7 == 0 and candidate % 8 == 0 and candidate % 9 == 0:
                        return candidate

            result = find_completion()
            self.text_otv.insert(1.0,f"Подходящее дополнение: {result}")

        self.delete()
        self.text_usl.insert(1.0,'Дополнить число 523*** цифрами справа так, чтобы полученное шестизначное число делилось на 7, 8 и 9 одновременно.')
        solution_five()

    def six(self):
        def solution_six():
            self.text_otv.delete(1.0, tkinter.END)

            def analyze_temperature_data(temperatures):
                average_temperature = sum(temperatures) / len(temperatures)
                max_temperature = max(temperatures)
                min_temperature = min(temperatures)
                days_below_zero = sum(1 for temp in temperatures if temp < 0)

                coldest_decade_start = 0
                coldest_decade_min_temperature = float('inf')

                for i in range(0, len(temperatures) - 9):
                    current_decade_temperature = sum(temperatures[i:i + 10])
                    if current_decade_temperature < coldest_decade_min_temperature:
                        coldest_decade_min_temperature = current_decade_temperature
                        coldest_decade_start = i

                return {
                    "average_temperature": average_temperature,
                    "max_temperature": max_temperature,
                    "min_temperature": min_temperature,
                    "days_below_zero": days_below_zero,
                    "coldest_decade_start": coldest_decade_start,
                    "coldest_decade_min_temperature": coldest_decade_min_temperature / 10
                }

            temperatures = [2, -4, 1, -5, 0, 3, -2, -7, 6, 1, 0, -3, 5, -1, 4, 2, -6, 1, -4, 3, -8, -2, 0, -1, 2]
            result = analyze_temperature_data(temperatures)

            self.text_otv.insert(1.0,f'Среднемесячная температура: {result["average_temperature"]}\n')
            self.text_otv.insert(2.0,f'Максимальная температура: {result["max_temperature"]}\n')
            self.text_otv.insert(3.0,f'Минимальная температура:{result["min_temperature"]}\n')
            self.text_otv.insert(4.0,f'Количество дней с температурой ниже нуля: {result["days_below_zero"]}\n')
            self.text_otv.insert(5.0,f'Самая холодная декада начинается с дня: {result["coldest_decade_start"]}\n')
            self.text_otv.insert(6.0,f'Минимальная температура за самую холодную декаду: {result["coldest_decade_min_temperature"]}\n')

        self.delete()
        self.text_usl.insert(1.0,'В массиве хранятся данные о температуре окружающего воздуха за месяц. Найти:\n')
        self.text_usl.insert(2.0, '– среднемесячную температуру;\n')
        self.text_usl.insert(3.0, '- максимальную и минимальную температуру\n')
        self.text_usl.insert(4.0, '– количество дней с температурой ниже нуля\n')
        self.text_usl.insert(5.0, '– самую холодную декаду месяца.\n')
        solution_six()

    def seven(self):
        def solution_seven():
            self.text_otv.delete(1.0, tkinter.END)

            def find_min_prices(matrix):
                n = len(matrix)
                m = len(matrix[0])
                min_prices = [float('inf')] * m
                for j in range(m):
                    for i in range(n):
                        min_prices[j] = min(min_prices[j], matrix[i][j])
                return min_prices

            matrix = [
            [3, 5, 2, 8],
            [4, 1, 7, 3],
            [6, 2, 9, 4]
            ]

            min_prices = find_min_prices(matrix)

            for j, min_price in enumerate(min_prices, start=1):
                self.text_otv.insert(tkinter.END,f"Минимальная цена для изделия {j}: {min_price}\n")

        self.delete()
        self.text_usl.insert(1.0,'В таблице, состоящей из n строк и m столбцов, на пересечении i-й строки и j-го столбца указывается цена, по которой i-й завод продает j-e изделие. Необходимо купить все m изделий минимальной цене.')
        solution_seven()

    def eight(self):
        def solution_eight():
            self.text_otv.delete(1.0, tkinter.END)

            def words_to_array(text):
                words = text.split()
                return words

            english_text = "Hello, this is an example text."
            word_array = words_to_array(english_text)

            self.text_otv.insert(1.0,f"Массив слов: {word_array}")

        self.delete()
        self.text_usl.insert(1.0,f'Все слова заданного английского текста переписать «пословно» в массив.')
        solution_eight()

    def nine(self):
        def solution_nine(nine):
            self.text_otv.delete(1.0, tkinter.END)

            def find_index(arr, target):
                for i, element in enumerate(arr):
                    if element == target:
                        return i
                return -1

            my_array = [1, 3, 5, 7, 9, 11, 13, 15]
            target_element = int(self.ent1.get())

            result = find_index(my_array, target_element)

            if result != -1:
                self.text_otv.insert(1.0,f"Индекс элемента {target_element} в массиве: {result}")
            else:
                self.text_otv.insert(2.0,f"Элемент {target_element} не найден в массиве.")

        self.delete()
        self.text_usl.insert(1.0,'Разработать функцию, отыскивающую индекс заданного элемента в одномерном массиве \n')
        self.text_usl.insert(2.0, 'Массив: [1, 3, 5, 7, 9, 11, 13, 15]')

        self.run = tkinter.Toplevel()
        self.run.title('Решение')
        self.run.geometry('300x150')
        self.lab3 = tkinter.Label(self.run, text='Введите данные: ')
        self.Frame_1 = tkinter.Frame(self.run)
        self.Frame_2 = tkinter.Frame(self.run)
        self.lab_sk1 = tkinter.Label(self.Frame_1, text='Введите элемент массива: ')
        self.ent1 = tkinter.Entry(self.Frame_1)
        self.but12 = tkinter.Button(self.Frame_2, text='Решить')
        self.but12.bind('<Button-1>', solution_nine)

        self.lab3.pack()
        self.but12.pack()
        self.lab_sk1.pack()
        self.ent1.pack()
        self.Frame_1.pack(side='top')
        self.Frame_2.pack(side='bottom')

    def ten(self):
        def solution_ten():
            self.text_otv.delete(1.0, tkinter.END)

            table1 = ["Иванов", "Петров", "Сидоров", "Смирнов", "Козлов"]
            table2 = ["Иванов", "Смирнов"]
            table3 = ["Козлов"]
            table4 = ["Козлов"]

            all_employees = set(table1 + table2 + table3 + table4)

            non_foreign_language_employees = all_employees - set(table2 + table3 + table4)

            self.text_otv.insert(tkinter.END,"Сотрудники, не владеющие иностранными языками:\n")
            self.text_otv.insert(tkinter.END, "\n")
            for employee in non_foreign_language_employees:
                self.text_otv.insert(tkinter.END,f'{employee}\n')

        self.delete()
        self.text_usl.insert(1.0,f'В табл. 1 хранится список сотрудников фирмы, в табл. 2 – список сотрудников, владеющих английским языком, в табл. 3 – список сотрудников, владеющих французским языком, в табл. 4 – список сотрудников, владеющих немецким языком. Написать программу, выводящую фамилии сотрудников фирмы, не владеющих иностранными языками.')
        solution_ten()
    def eleven(self):
        def solution_eleven():
            self.text_otv.delete(1.0, tkinter.END)

            def calculate_function(x):
                return x ** 2 + math.log(5 * x - 4)

            interval_start = 1
            interval_end = 10
            num_points = 20
            step = (interval_end - interval_start) / (num_points - 1)

            points = []
            for i in range(num_points):
                x = interval_start + i * step
                y = calculate_function(x)
                points.append((x, y))

            with open("function_values.txt", "w") as file:
                for x, y in points:
                    file.write(f"{x}\t{y}\n")

            self.text_otv.insert(tkinter.END,"Результаты записаны в файл function_values.txt")

        self.delete()
        self.text_usl.insert(1.0,f'Вычислить значение функции y = x 2+ln(5x-4) в 20 равноотстоящих точках интервала [1; 10]. Результаты (x и y) записать в текстовый файл.')
        solution_eleven()


my_gui = MyGui()
