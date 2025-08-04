#Вариант 15

#импортируем библиотеки
from math import pow, sqrt
from time import perf_counter
from itertools import filterfalse
# Импортируем наш собственный модуль
import mymodule

#декоратор
def c_decorator(functions):
    def decorator(v_list):
        start_time = perf_counter()

        res = functions(v_list)

        end_time = perf_counter()
        elapsed_time = end_time - start_time

        # при помощи этой функции мы находим максимально значение
        max_value = lambda vals: max([num for num in vals if isinstance(num, int)], default=None)
        max_val = max_value(v_list)

        # Возведение в степень и вычисление квадратного корня
        if max_val is not None:
            power_result = pow(max_val, 2)  # Возведем в квадрат
            square_root_result = sqrt(abs(max_val))  # Найдем квадратный корень
        else:
            power_result = None
            square_root_result = None

         #объединение всех элементов
        # all_values = ''.join(value for value in v_list if isinstance(value, str))

        #нахожу последнюю введенную букву и произвожу подсчет их количества
        # number_of_repetitions = all_values[-1] if len(all_values)  > 1 else ' '
        # count_repetitions = all_values.count(number_of_repetitions)

        #вывод результатов операций
        print(f"Квадрат числа {max_val}: {power_result}")
        print(f"Квадратный корень из |{max_val}|: {square_root_result}")
        # print(f"Количество повторений последней буквы '{number_of_repetitions}' во всей строке:", count_repetitions)
        print(f"Время выполнения функции 'вычислитель': {elapsed_time:.6f} секунд")

        return res

    return decorator


@c_decorator
#Функция вычислитель
def calculator(values):
    # При помощи анонимной функции нахожу максимальное значение
    get_max_value = lambda vals: max([num for num in vals if isinstance(num, int)], default=None)
    max_value = get_max_value(values)

    # Объединение всех элементов (именно букв)
    # all_values = ''.join(value for value in values if isinstance(value, str))

    # Нахожу ближайшую к концу алфавита букву
    # closest_letter = max(all_values) if all_values else None

    # Вывод результатов вычислений
    print("Максимальное значение:", max_value)
    # print("Ближайшая к концу алфавита буква:", closest_letter)

    return max_value
# , closest_letter

# Функция обработчик ввода

def input_values(value):
    # Проверка на ввод
    if not value:
        print('Значение не было введено!')
        return None
    # Сначала проверяем, является ли значение числом
    try:
        # Пробуем преобразовать значение в число
        int_value = int(value)
        if int_value < 0:
            return int_value
        else:
            print("Ввод положительных чисел запрещен!")
            return None
    except ValueError:
        pass  # Если не получилось преобразовать в число, продолжаем обработку строки

    # Теперь обрабатываем строку
    if isinstance(value, str):
        letters = 'ЁУЕЭОАЫЯИЮ'  # Допустимые заглавные гласные
        filtered_letters = list(filterfalse(lambda x: x in letters, value))
        if filtered_letters:
            print("Неподходящие символы введены!")
            return None
        else:
            return value
    else:
        print("Ошибка: введено значение, не соответствующее требованиям.")
        return None

# Генерация двух наборов числовых значений
first_set = [mymodule.generate_random_int(-72, -33) for _ in range(5)]
second_set = [mymodule.generate_complex_random(-64, -22, 8) for _ in range(7)]

# Вывод сгенерированных наборов
print("Первый набор чисел:", first_set)
print("Второй набор чисел:", second_set)


# Функция для ввода данных
def p_input():
    # Массив для значений
    v_list = []

    for value in first_set + second_set:
        p_value = input_values(str(value))
        if p_value is not None:
            v_list.append(p_value)

    print("\nПосле обработки числовые значения:", v_list)

    return v_list



# #функция для ввода данных
# def p_input():
#     #массив для значений
#     v_list = []
#     while True:
#         value = input('Введите значение или end для завершения:')
#         if value.lower() == 'end':
#             break
#         p_value = input_values(value)
#         if p_value is not None:
#             v_list.append(p_value)#добавляем в массив значение
#     return v_list #возвращаем массив
#

def main():
    v_list = p_input()
    if v_list:
        res = calculator(v_list)
        print("Все успешно")
    else:
        print("Программа завершена")

    # Используем функции из нашего модуля
    print(f"Генерация случайного целого числа в диапазоне от -72 до -33 включительно:", mymodule.generate_random_int(-72, -33))
    print(f"Генерация сложного целого числа в диапазоне от -64 до -22 включительно с шагом 8:", mymodule.generate_complex_random(-64, -22, 8))

if __name__ == "__main__":
    main()
