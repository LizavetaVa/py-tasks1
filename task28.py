# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 числo: '))

def sum(a,b):
    if b == 1:
        return a + 1
    return sum(a,b-1) + 1

print(sum(a, b))