# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


n = int(input("Длина массива: "))
a = [int(input(f"Введите {i+1}-е число: ")) for i in range(n)]
x = int(input("Число для поиска: "))

index = 0
for i in range(1, n):
    if abs(a[i] - x) < abs(a[index] - x):
        index = i

print(f"В списке: {a}")
print(f"Для числа: {x}")
print(f"Ближайшее число: {a[index]}")
print(f"Элемент списка под номером: {index+1}")








