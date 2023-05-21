# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10


s = int(input('Количество сделанных журавликов: '))

petya = s // 6
katya = s // 6 * 4
sergey = s // 6
print(f'Из {s} журавликов {petya} сделал Петя, {katya} - Катя, {sergey} и - Сережа.')


# или
# s = int(input('Количество сделанных журавликов: '))

# if s % 6 == 0:
#     petya = s // 6
#     katya = s // 6 * 4
#     sergey = s // 6
#     print(f'Из {s} журавликов {petya} сделал Петя, {katya} - Катя, {sergey} и - Сережа.')
# else:
#     print('Из данных нельзя изъять верные значения.')