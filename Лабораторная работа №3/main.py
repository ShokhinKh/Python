#Вариант 15

#импортируем библиотеку
import math

#декоратор
def c_decorator(functions):
    def decorator(v_list):
        res = functions(v_list)

        # при помощи этой функции мы находим максимально значение
        max_value = lambda vals: max([num for num in vals if isinstance(num, int)], default=None)
        max_val = max_value(v_list)

        #тут я нахожу квадратный корень модуля максимального из введенных чисел
        if max_val is not None:
            abs_sqrt_of_max_value = math.sqrt(abs(max_val))
        else:
            abs_sqrt_of_max_value = None

         #объединение всех элементов
        all_values = ''.join(value for value in v_list if isinstance(value, str))

        #нахожу последнюю введенную букву и произвожу подсчет их количества
        number_of_repetitions = all_values[-1] if len(all_values)  > 1 else ' '
        count_repetitions = all_values.count(number_of_repetitions)

        #просто вывожу все буквы на экран, чтобы проверить правильность
        print("Все введенные буквы:", all_values)

        #вывод результатов операций
        print("Квадратный корень модуля максимального из введенных чисел:", abs_sqrt_of_max_value)
        print("Количество повторений последней буквы во всей строке:", count_repetitions)

        return res

    return decorator


@c_decorator
#Функция вычислитель
def calculator(values):
    # При помощи анонимной функции нахожу максимальное значение
    get_max_value = lambda vals: max([num for num in vals if isinstance(num, int)], default=None)
    max_value = get_max_value(values)

    # Объединение всех элементов (именно букв)
    all_values = ''.join(value for value in values if isinstance(value, str))

    # Нахожу ближайшую к концу алфавита букву
    closest_letter = max(all_values) if all_values else None

    # Вывод результатов вычислений
    print("Максимальное значение:", max_value)
    print("Ближайшая к концу алфавита буква:", closest_letter)

    return max_value, closest_letter

#функция обработчик ввода
def input_values(value):
    # Проверка на ввод
    if not value:
        print('Значение не было введено!')
        return None
    elif isinstance(value, int):  # Проверка на ввод только отрицательных чисел
        if value < 0:
            return value
        else:
            print('Разрешен ввод только отрицательных чисел!')
    elif isinstance(value, str):
        letters = 'ЁУЕЭОАЫЯИЮ'  # Допустимые заглавные гласные
        if any(char.islower() for char in value):  # Проверка на наличие маленьких букв
            print("Ошибка: вводить нужно только заглавные буквы!")
            return None
        if all(char in letters for char in value):  # Проверка на допустимые гласные
            return value
        else:
            try:
                int_value = int(value)
                if int_value < 0:
                    return int_value
                else:
                    print("Ввод положительных чисел запрещен!")
            except ValueError:
                print("Ошибка: введено не соответствующее требованиям значение.")
                return None
    else:
        print("Ошибка: введено значение, не соответствующее требованиям.")
        return None




#функция для ввода данных
def p_input():
    #массив для значений
    v_list = []
    while True:
        value = input('Введите значение или end для завершения:')
        if value.lower() == 'end':
            break
        p_value = input_values(value)
        if p_value is not None:
            v_list.append(p_value)#добавляем в массив значение
    return v_list #возвращаем массив


def main():
    v_list = p_input()
    if v_list:
        res = calculator(v_list)
        print("Все успешно")
    else:
        print("Программа завершена")


if __name__ == "__main__":
    main()
