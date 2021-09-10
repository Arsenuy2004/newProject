# рулетка

# import random
# print("Играем в русскую рулетку")
# e = random.randint(1, 2)
# p = random.randint(1, 2)
# x = 0
# while x < 5:
#     x += 1
#     print('Попытка №', x)
#     d = int(input("Делайте Вашу ставку от 1 до 10: "))
#     print(f"Ваша ставка принята. Номер: {d}")
#     h = int(input("Выберите цвет (1-красный, 2-чёрный): "))
#     if h == 1:
#         print("Вы выбрали красный")
#     else:
#         print("Вы выбрали чёрный")
#     if d == e and h == p:
#         print("Вы угадали число и цвет")
#         break
#     elif d == e and h != p:
#         print("Вы угадали число")
#         # print(e, p)
#     elif d != e and h == p:
#         print("Вы угадали цвет")
#     else:
#         print("Не угадали ничего")

# Посчитать сколько раз встречается определённая цифра в числах.
# Количество введённых чисел и искомая цифра задаются с клавиатуры
# Числа выбираются рандомно.

# import random
# number = int(input("Введите количество необходимых чисел до 100: "))
# number_1 = input("Введите искомую цифру: ")
# c = 0
# s = []
# for i in range(number):
#     i = random.randint(1, 100)
#     s.append(i)
# print(s)
# s = str(s)
# b = s.count(number_1)
# print(b)


# a = [2, 3, 4, 3, 44, 5]
# a = str(a)
# b = a.count('4')
# print(b)



# Необходимо, чтоб программа выводила на экран вот такую последовательность(не использовать готовый массив):
# 7 14 21 28 35 42 49 56 63 70 77 84 91 98
# Добавить в массив и найти его длинну.



# Дан список list = [15,48,'hello',6,19,'world'].
# Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр.
# Если число нечётное, то заменить его на 1 в списке.
# Все слова: посчитать количкство гласных и согласных.
# Вывести всё на экран.


# list = [15, 48, 'hello', 6, 19, 'world']
# p = 0
# h = 0
# d = 0
# for i in list:
#     if type(i) is int:
#         if i % 2 == 0:
#             i = str(i)
#             for k in i:
#                 k = int(k)
#                 print('k: ' + str(k))
#                 p = k + p
#             print(i, "Сумма цифр: ", p, "\n")
#             p = 0
#         else:
#             index = list.index(i)
#             print(index)
#             list[index] = 1
#             print(index, list)
#     elif type(i) is str:
#         for r in i:
#             if r in "aeoiu":
#                 h += 1
#             else:
#                 d += 1
#         print(i, "\nКоличество глассных: ", h)
#         print("Количество согласных: ", d, "\n")
#         h = 0
#         d = 0
# print(list)

# list = [15, 48, 'hello', 6, 19, 'world']
# s = []
# a = 0
# b = 0
# e = 0
# c = 0
# schetchik = 0
# for i in list:
#     if type(i) is int:
#
#         # print(i)
#         if i % 2 == 0:
#             # schetchik += 1
#             s.append(i)
#             # print(schetchik)
# # print(s)
# # a += 1
# for i in s:
#     i = str(i)
#     for k in i:
#         k = int(k)
#         b += k
#     print(f"Сумма чётного числа: {b}")
#     b = 0
#
# for i in list:
#     if type(i) is int:
#
#         if i % 2 != 0:
#             index = list.index(i)
#             list[index] = 1
#             # schetchik += 1
#             # list[schetchik - 1] = 1
#             # print(list)
# print(list)
#
# for i in list:
#     if type(i) is str:
#         for k in i:
#             if k in "aeoiu":
#                 e += 1
#             else:
#                 c += 1
#
#         e = 0
#         c = 0


# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра
# находятся в введённом с клавиатуры слове,
# а также сколько букв в слове и сколько гласных и согласных.

# a = input("Введите текст с верхним и нижним регистром: ")
# gl = 0
# sogl = 0
# up_v = 0
# low_n = 0
# low = ''
# up = ''
#
# for i in a:
#     if i in "OAEIUaeoiu":
#         gl += 1
#     else:
#         sogl += 1
#     if i.islower():
#         low += i
#         if len(low) % 2 == 0:
#             low_n += 1
#     # elif low != '':              # обнуляем строку
#     #     low = ''
#     if i.isupper():
#         up += i
#         if len(up) % 2 == 0:
#             up_v += 1
#     # elif up != '':
#     #     up = ''
# print(f'Гласные: {gl}, Согласные: {sogl}')
# print(f'Верхний регистр: {up_v}, Нижний регистр: {low_n}')



# first = 'Python is the language of the future.'
# print(first.index('lang', 10))

# ????????????????? print('$100 $200 $300'.count('$'))
# print('$100 $200 $300'.count('$''100' '$''200'))
# # print('$100 $200 $300'.count('$', 5))


# i = 1
# s = []
# while i <= 10:
#     i += 1
#     if i % 2 == 0:
#         s.append(i**2)
# print(s)

# a = int(input("Введите отрицательное число: "))
# b = int(input("Введите второе число: "))
# s = ''
# while a < b and a < -1:
#     a += 1
#     s += str(a)
#     # s += ''
# print(s)

# arr = ('asd', 'asdfb', 'dcd', 'a')
# print(min(arr, key=len))
# print(max(arr, key=len))

# import random
# a = [random.randint(0, 100) for i in range(10)]
# b = tuple(a)
# print(b)
# print('max', max(a), 'min', min(a))


# ёsp1 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
# sp2 = []
# index1 = 0
# index2 = 0
# sum1 = 0
# sum2 = 0
# rezult = 0
#
# for i in range(len(sp1)):
#
#     znachenie = sp1[i].index(max(sp1[i][0:]))
#     print(sp1[i][znachenie])
#

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# print(a[4::-2])

# a[:] is a
# print(a[:] is a)

# t = ('foo', 'bar', 'baz')
# t[1] = 'qux'
# e = tuple("sdtfgsr")
# print(e)
# d = {'foo': 100, 'bar': 200, 'baz': 300}
# print(d['bar':'baz'])

a = {"1" : "2"}
a = a.keys()
print(a)