# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# -> 4
# -> 1 2 3 4
# 9

# bush, berry = 4, [1, 2, 3, 4]

bush = int(input("Введите количество кустов: "))
berry = [
    int(input(f"Введите кол-во ягод на {i+1} кусте: ")) for i in range(bush)]
sum_berry = [berry[i]+berry[(i+1) % bush]+berry[(i+2) % bush]
             for i in range(bush)]
print(f"Максимальное кол-во ягод с трех соседних кустов: {max(sum_berry)}")