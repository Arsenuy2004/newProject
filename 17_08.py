# a = (1, 2, 3, 4, 5, 6)
# b = (1,)
# print(a, b)

# a = (1, 2, 3, 4, 5, 6)
# b = [1, 2, 3, 4, 5, 6]
# print(a.__sizeof__())
# print(b.__sizeof__())

# a = (1, 2, 3, 4, 5, 6)
# print(a[0:3])
# print(a[:3])
# print(a[1:])
# print(a[2::2])
# print(a[::2])

# a = (10, 2.13, "square", 89, 'C')
# b = [1, 2, 3]
# c = list(a)
# d = tuple(b)

# nested = (1, "do", ["param", 10, 20])
# nested[2][1] = 15
# print(nested)

# x = (1, 2, 3, 4)
# y = (5, 6, 7, 8)
# z = x + y
# print(z)

# x = (1, 2, 3, 4)
# z = x * 2
# print(z)

# a = (1, 2, 3, 4, 5, 5)
# print(a.count(5), len(a))

# a = (1, 2, 3, 4, 5, 5)
# print('max', max(a), 'min', min(a))   #со списками то же работает

# arr = ('asd', 'asdfb', 'bcd', 'a')
# print(min(arr, key=len))
# print(max(arr, key=len))


# arr = (12, 123, 124, 15, 78, 456, 23, 45, 467, 45)
# print('max', max(arr), 'min', min(arr))

# import random
# b = int(input("Введите диапазон от 1 до 1000: "))
# s = []
# for i in range(10):
#     a = random.randint(1, b)
#     s.append(a)
# s = tuple(s)
# print(s)
# print('max', max(s), 'min', min(s))

# import random
# a = [random.randint(1, 100) for i in range(10)]
# s = tuple(a)
# print(a)
# print('max', max(s), 'min', min(s))

# import random
# a = [random.randint(0, 5) for i in range(10)]
# b = [random.randint(-5, 0) for i in range(10)]
# s = tuple(a)
# c = tuple(b)
# z = c + s
# print(f"Кол-во нулей: {z.count(0)}, Числа: {z}")5158309


# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
# i = 1
# k = 0
# s = 0
# while k <= 4000000:
#
#     k += i
#     i += k
#     if k < 4000000:
#         print(k)
#     if i < 4000000:
#         print(i)
#     if i < 4000000:
#         if i % 2 == 0:
#             s += i
#     if k < 4000000:
#         if k % 2 == 0:
#             s += k
#
# print("Сумма:", s)

# i = 1
# k = 0
# s = 0
#
# while k < 4000000 and i < 4000000:
#
#     k += i
#     i += k
#     if k < 4000000:
#
#         # print(k)
#         # print(i)
#
#         if k % 2 == 0:
#             s += k
#         if i % 2 == 0:
#             s += i
#
# print(f'Сумма: {s}')


# d ={}
#
# d = {'dict': 1, 'diktionary': 2}
#
# print(d)

# d = dict(short='dict', long='dictionary')
# d_2 = dict([(1, 1), (2, 4)])

# d = dict.fromkeys(["a", 'b'])
# d_2 = dict.fromkeys(["a", "b"], 100)
#
# print(d, "\n", d_2).

# Months = {1:"Jan", 2:"Feb", 3:'Mar', 4:'Apr',
# #           5:'May', 6:'Jun', 7:'Jul', 8:'Aug',
# #           9:'Sep', 10:'oc', 11:'Nov', 12:'Dec'}
# # count = len(Months)
# # print(count)
# #
# n = dict(zip([1, 2, 3], ['one', 't', 'th', 'for']))
# print(n)

# p = {'name': "Arseni", 'age': 17, 'sity': "Smolevichi"}
# print(p['age'])

# p = {'BMV': ['1', '2', '3'], "Tesla": ['4', '5', '6']}
# print(p['BMV'][0], p['BMV'][2], p["Tesla"][0], p["Tesla"][2])
#
# p = {'BMV': '1' '2' '3', "Tesla": '4' '5' '6'}
# print(p['BMV'][0] a, p['BMV'][2], p['Tesla'][0], p['Tesla'][2])

d1 = {'a':}