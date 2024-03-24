def caching_fibonacci():
    cache = {}  # Створюємо порожній словник для зберігання результатів обчислень

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Перевіряємо, чи вже є результат в кеші
            return cache[n]
        else:
            # Обчислюємо числа Фібоначчі рекурсивно та зберігаємо їх в кеші
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15)) 