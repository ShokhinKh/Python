"""
Модуль mymodule содержит функции для генерации случайных чисел.

Функции:
- generate_random_int(): генерирует случайное целое число в диапазоне от -72 до -33 включительно.
- generate_complex_random(): генерирует сложное случайное число, основанное на выражении floor(random()*randrange(-64, -22, 8)).
"""

from random import randint, random, randrange
from math import floor

def generate_random_int(a, b):
    """
    Генерирует случайное целое число в диапазоне от -72 до -33 включительно.
    """
    return randint(a, b)

def generate_complex_random(a, b, c):
    """
    Генерирует сложное случайное число, основанное на выражении floor(random()*randrange(-64, -22, 8)).
    """
    return floor(random() * randrange(a, b, c))

