# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i = i + 1    # счётчик записывается в конце

# i = 1
# result = 0
# while i <= 50:
#     result += i
#     i += 1
# print(result)


# i = 1           # записать квадраты всех целых чисел от 1 до 10
# while i < 11:
#     print(i**2)
#     i = i + 1    # похоже на шаг (если поставить 2 будет считать через одну, начиная с первой)

# s = 1
# for i in range(1, 125):
#     if i % 2 == 0:
#         s *= i
# print(s)

# i = 1
# s = 1
# while i <= 125:
#     if i % 2 == 0:
#         s *= i
#     i += 1
# print(s)




# a = []
# i = 1
# while i < 16:
#     a.append(i)
#     i = i + 1
# print(a[::-1])

# a = []
# b = []
# i = 1
# while i < 16:
#     a.append(i)
#     i = i + 1
# print(a)
# b = a
# print(b)
# b.reverse()
# print(b)



# i = 15
# while i >= 1:
#     print(i)
#     i -= 1

# for i in range(3):
#     print(i)
# else:
#     print("Готово")

# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print('Готово')

# mas = []
# i = 7
# while i < 103:
#     mas = i
#     i += 7
#     print(mas, end = ' ')
    # print(len(mas))    # это не список (массив) поэтому команда не работакт

# mas = []
# i = 7
# while i < 100:
#     mas.append(i)
#     i += 7
# print(mas)
# print(len(mas))          # 2й вариант предыдущего задания

# i = 0
# for i in range(7, 99, 7):
#     print(i)
# else:
#     print("Готово")
#
# a = int(input("Введите отрицательное число: "))
# b = int(input("Введите положительное число: "))
# for i in range(a, b):
#     if i < 0:
#         print(i)


# a = int(input("Введите отрицательное число: "))
# b = int(input("Введите отрицательное число: "))
# i = -1
# s = ''
# while a <= i < b and b < 0:
#     #if i < 0:
#     i += 1
#     s += str(i)
# print(s)              # неправильно задано условие while
#


# i = int(input("Введите отрицательное число: "))
# j = int(input("Введите целое число: "))
# s = ''
# while i < j and i < -1:
#     i += 1
#     s += str(i)
#     s += " "
# print(s)

# ДОМАШНЕЕ ЗАДАНИЕ

# import random
# human = int(input("Введите число от 1 до 10: "))
# human1 = input("Выберите цвет ('красный', 'чёрный'): ")
# a = random.randint(1, 10)
# b = random.randint(1, 2)
#
# if b == 1 and human1 == 'красный':
#     print(a)
#     print("красный")
# elif b == 2 and human1 == 'чёрный':
#     print(a)
#     print("чёрный")
#
# if human == a and human1 == b:
#     print("Вы победили")
# else:
#     print("Вы проиграли:", a, b)    # не закончена рулетка
s = []
c = []
import random
human = str(input("Введите число от 1 до 10 и выберете цвет ('красный', 'чёрный'): "))
human.split()
s = human.split()
print(s)

a, b = random.randint(1, 10), random.randint(1, 2)
a = str(a)
b = str(b)
c.append(a)
c.append(b)
print(c)

# if b == 1 and 1 == 'красный':
# elif b == 2 and 2 == 'чёрный':
#     print(a)
#     print("чёрный")

# if human == a and human1 == b:
#     print("Вы победили")
# else:
#     print("Вы проиграли:", a, b)    # не закончена рулетка



# calculator = int(input("Для продолжения программы введите 1, для выхода введите 0: "))
# if calculator == 0:
#     print("Завершение программы")
# elif calculator == 1:
#
#     number = input('Введите первое число: ')
#     number1 = input('Введите второе число: ')
#     sing = input('Введите знак (+, -, \, *): ')
#     if not number.isalpha() or not number1.isalpha():
#         number = float(number)
#         number1 = float(number1)
#         if sing == '+':
#             print(number + number1)
#         elif sing == '-':
#             print(number - number1)
#         elif sing == '/':
#             if number1 == 0:
#                 print("На ноль делить нельзя")
#             else:
#                 print(number / number1)
#         elif sing == '*':
#             print(number * number1)
#         else:
#             print("Введён не верный знак")
