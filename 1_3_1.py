"""
    Реалізувати програмно мовою Python завдання з наведеного нижче списку. Для
кожної з задач алгоритм реалізувати з використанням рекурсії і ітерації. Аргументувати
письмово доцільність вибору в кожному випадку рекурсії або ітерації (використовувати
в якості критеріїв - час розробки та виконання програм, обсяг займаної пам'яті,
читабельність програми).

1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.

Васильченко Даниїл 122 А
"""
from time import time  # для підрахунку часу виконання треба використовувати великі значення


# РЕКУРСІЯ
def factorial_recursion(n):
    if n == 0:
        return 1
    return n * factorial_recursion(n - 1)


# ІТЕРАЦІЯ
def factorial_iteration(n):
    kek = 1
    for i in range(1, n + 1):
        kek *= i
    return kek


x = int((input('F = ')))
tic1 = time()
print("Результат виконання рекурсією: \n", factorial_recursion(x))
toc1 = time()
recursion_time = toc1 - tic1
tic2 = time()
print("Результат виконання ітерацією: \n", factorial_iteration(x))
toc2 = time()
iteration_time = toc2 - tic2
print()
print("Час розробки: обидва способи прості у реалізації і потребують майже однакову к-ть коду\n"
      f"Час виконання: ітерація = {iteration_time}\n"
      f"               рекурсія = {recursion_time}\nІтерація виконується швидше\n"
      "Обсяг пам'яті: рекурсія забирає більше пам'яті через зберігання значень у стеку"
      "Обидва методи читабельні, але рекурсивний метод може бути інтуїтивно зрозуміліший")
