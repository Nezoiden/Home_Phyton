# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
a = int(input('Введите число: '))


def Fibonacci(a):
    b = []
    fib1 = 1
    fib2 = 1
    for i in range(a):
        b.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2
    fib1 = 0
    fib2 = 1
    for i in range(a+1):
        b.insert(0, fib1)
        fib1, fib2 = fib2, fib1 - fib2
    print(b)


Fibonacci(a)
