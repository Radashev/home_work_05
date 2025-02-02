import re
from typing import Callable

def generator_numbers(text: str):
    """
    Функція, що аналізує текст і повертає генератор дійсних чисел.
    """
    # Шукаємо всі дійсні числа у тексті за допомогою регулярного виразу
    pattern = r"\b\d+\.\d+\b"
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    """
    Функція, що обчислює загальний прибуток з використанням генератора чисел.
    """
    # Використовуємо генератор чисел з функції generator_numbers
    numbers_generator = func(text)
    total_profit = sum(numbers_generator)
    return total_profit

text = "Загальний дохід працівника складається з декількох частин: 1000.01\
    як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")