# f = 3.234
# print('%2f' % f) # изучить как работают функции форматирования (3е занятие, см тетрадь)


# import random
# toy = input("Введите название лотереи (ваше лото, спортлото): ")
#
# if toy == "ваше лото":
#     human = int(input("Введите 3 первые цифры своего билета: "))
#     your_lotto = random.randint(100, 999)
#     if human == your_lotto:
#         print("Вы выиграли")
#         print(your_lotto)
#     else:
#         print("Вы проиграли")
#
# elif toy == "спортлото":                                   # можно реализовать через if (без отступов, так же)
#     human1 = int(input("Введите номер своего смс (от 10 до 999): "))
#     sport_lotto = random.randint(10, 999)
#     if human1 == sport_lotto:
#         print("Вы выиграли")
#     else:
#         print("Вы проиграли")
#         print(sport_lotto)


# date = int(input("Введите дату своего рождения: "))
# month = int(input("Введите месяц своего рождения: "))
# years = int(input("Введите год своего рождения: "))    # не готово задание второго урока, прорешать
# if month == 1:
#     if date >= 21:
#         print("Вы водолей по знаку задиака")
#     else:
#         print("Вы козерог по знаку зодиака")
# if month == 2:
#     if date >= 20:
#         print("Вы рыбы по знаку задиака")
#     else:
#         print("Вы водолей по знаку задиака")
# if month == 3:
#     if date >= 21:
#         print("Вы овен по знаку задиака")
#     else:
#         print("Вы рыбы по знаку задиака")
# if month == 4:
#     if date >= 21:
#         print("Вы телец по знаку задиака")
#     else:
#         print("Вы овен по знаку задиака")
# if month == 5:
#     if date >= 22:
#         print("Вы близнецы по знаку задиака")
#     else:
#         print("Вы телец по знаку задиака")
# if month == 6:
#     if data >= 22:
#         print("Вы рак по знаку задиака")
#     else:
#         print("Вы близнецы по знаку задиака")
# if month == 7:
#     if data >= 23:
#         print("Вы лев по знаку задиака")
#     else:
#         print("Вы рак по знаку задиака")
# if month == 8:
#     if data >= 22:
#         print("Вы дева по знаку задиака")
#     else:
#         print("Вы лев по знаку задиака")
# if month == 9:
#     if data >= 24:
#         print("Вы весы по знаку задиака")
#     else:
#         print("Вы дева по знаку задиака")
# if month == 10:
#     if date >= 24:
#         print("Вы скорпион по знаку задиака")
#     else:
#         print("Вы весы по знаку задиака")
# if month == 11:
#     if date >= 23:
#         print("Вы стрелец по знаку задиака")
#     else:
#         print("Вы скорпион по знаку задиака") # возможно скорпион, дописать 12 месяц
#
# if month > 7 or month == 7 and date <= 27:
#     print("Ваш возраст:", 2021 - years - 1)
# else:
#     print("Ваш возраст:", 2021 - years)


# a = input("Введите Ваше имя: ")
# print("Привет\t" + a)
# b = a * 3
# print(b)

# for i in range(4):
#     print(i)

# for i in range(4, 8):
#     print(i)
# for i in range(4, 8, 1):
#     print(i)
# for i in range(10, 5, -2):
#     print(i)
#
# for i in "Я учу Python":
#     print(i)

# for i in range(15, 0, -1):
#     print(i)

# a = "Я учу программирование о"
# a = a[0:5:1]
# print(a)

# a = input('Введите строку: ')
# b = input('Введите символ: ')
# c = ''
# for i in a:
#     if a != b:
#         c += i
# print('Результат: ', c)          # не работает


# a = input("Введите строку: ")
# b = input("Введите символ: ")
# c = ""
# for i in a:
#     if a != b:
#         c += i
# print("Результат: ", c)          #  " не работает


# s = input()
# s1 = input()
# print(s1.replace())              #проверить код

# s = input(1325465456)
# print(s[::2])

# s = input()
# b = s[::]
# print(b)

# a = int(input())
# b = int(input())
# c = int(input())
# for i in range(a,b,c):
#     print(i)

# arr = ['string1', 'string2', 'string3']
# l = len(arr)
# print(arr, 'Длина: ', l)

# arr = [1,7,9,10] # когда нужно перечислить элементы массива
# for i in arr:
#     print(i)

# arr = [1,7,9,10] # когда нужно перечислить элементы массива
# for i in arr:
#     print(i)
#     if i == 9:
#         break

# arr = [1,7,9,10] # когда нужно перечислять элементы массива
# for i in arr:
#     if i == 9:
#         continue
#     print(i)

# a = [10, 2, 3]
# print(a)
# a.append                               # дописать

# a = ['картошка', 'салат', 'суп']
# s = input()
# for i in a:
#     if i == s:
#         print("Я не ем", s)
#         break


# import random
# b = ''
# c = ''
# while True:
#     a = random.randint(1, 7)
#     if a == 7:
#         break
#     if a % 2 != 0:
#         # a = b
#         print(b)

 # домашнее задание
# s = 1
# for i in range(1, 100):
#     if i % 2 != 0:
#         s *= i
# print(s)

# mass = []
# for i in range(1, 501):
#     if i % 5 == 0:
#         mass.append(i)
# print(mass)

# for i in range(1, 497):
#     if i % 2 == 0:
#         print(i)

# mas_1 = [1, 5, 3, 5, 1]
# mas_2 = []
# for i in mas_1:
#     if mas_1.count(i) >= 2:
#         mas_2.append(i)
# print(mas_2)

