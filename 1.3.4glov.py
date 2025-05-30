
# Реализуйте рекурсивный алгоритм возведения числа в степень. Оцените сложность алгоритма.

# Возведение числа в степень — это математическая операция, при которой число умножается само на себя определённое количество раз.
# Рекурсивный подход заключается в том, что для вычисления power(a, b) мы умножаем a на результат power(a, b-1).
# Пример:
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)

# Пример использования:
if __name__ == "__main__":
    a = 2
    b = 3
    result = power(a, b)
    print(f"{a} в степени {b} равно {result}")

# Посянение работы кода:
# Базовый случай: если b = 0, то возвращаем 1, так как любое число в нулевой степени равняется 1.
# Рекурсивный случай: если b > 0, то возвращаем a * power(a, b-1).
# Во время использования: задаём основание a и показатель степени b, вызваем функцию power(a, b) и выводим результат.

# Оценка сложности: O(b), так как функция делает ровно b рекурсивных вызовов (общее кол-во операций линейно растёт с увеличением b).