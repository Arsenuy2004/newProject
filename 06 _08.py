# elements = [1, 3, 'a', 6, 'b']
# print(elements)
#
# elements = list()
# print(elements)
#
# import random
# # объявим список с и заполним его 10-ю элементами от 0 до 100:
# c = [random.randint(0, 100) for i in range(10)]
# print(c)
#
# print(c[0])
# print(c[-1])
# print(c[5])
# print([-4])


# elements = []          #для добавления в список новых элементов
# elements.append("a")
# elements.append(1)
# print(elements)

# elements = [1, 3, 'a', 6, 'b']
# elements.insert(1, 2)     # для добавления элемента на позицию
# print(elements)

# elements = [1, 3, 'a', 6, "b"]  # для замещения одного элемента другим
# elements[1] = 2
# print(elements)

# elements = [1, 3, "a", 6, "b"]  # для удаления элемента по индексу
# del elements[1]
# print(elements)
#
# elements = [1, 3, "a", 6, "a", "b"]  # для удаления элемента по значению
# elements.remove("a")
# print(elements)

# my_list = ['hello', 'world']
# elements = [1, 3, my_list, 6, "a", "b"]
# del elements[2][1]
# print(elements)

# elements = [1, 3, 6, "a", "b", "abc", 123, 435]                        #
# del elements[4:]   # удаляет все элементы после 4го включительно
# print(elements)
# del elements[:2] # удаляет всё до 2-го элемента
# print(elements)
# del elements[1:3]  # удаляет от 1го до 3го элемента
# print(elements)

                       # ВОПРОСЫ ПО УДАЛЕНИЮ - 2М ПОСЛЕДНИМ ДЕЛ...


# elements = [1, 3, 6, "a", "b", "abc", 123, 453]
# if "abc" in elements:        # для поиска какого-либо элемента в списке
#     print("Yes.")

# a = [1, 3, 5]
# b = [1, 5, 8, 9]
# print(a + b)
#
# d = ["h", "e", "l", "l", "e"]
# e = ["w", "e", "r", "l", "d"]
# d.extend(e) # не создаёт новый список, а дополняет тек-й список
# print(d)

# a = [1, 2, 3, 4]
# b = a   # переменной b присваивается не значение списка а, а его адрес
# a.append(5)
# print(a)
# b.append(6)
# print(b)
# print("a", a, "b", b)


# a = ["кот", "слон", "змея"]
# b = a.copy()
# print(a, b)
#
# d = list(a)       # работает через встроеную функцию лист
# print(a, d)
#
# import copy
# e = copy.copy(a)    # функция копи из пакета копи
# print(a, e)
# f = copy.deepcopy(a)
# print(a, f)
# c = a[:]            # через срез (устаревший способ)
# print(a, c)


# a = ["кот", "слон", "змея"]
# b = a[2:]      # со втрого элемента включительно и до конца
# print(b)
# c = a[:2]     # до второго элемента
# print(c)
# d = a[1:2]     # c первого элемента (включительно) до 2го
# print(d)
#
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# e = a[0:8:2]
# print(e)

# elements = [1, 2, 3, "meow"]
# for i in elements:           # для перебора списка - функция for
#     print(i)
#
# elements = [1, 2, 3, "meow"]
# elements_len = len(elements)
# i = 0
# while i < elements_len:   # для перебора списка
#     print(elements[i])
#     i += 1

# МЕТОДЫ СПИСКОВ
# a = [1, 2, 3]
# a.clear()
# print(a)
#
# a = [1, 2, 3]
# b = a.copy()
# print(id(a), id(b), a, b)
#
# elements = ["one", "two", "three", "one", "two", "one"]
# b = elements.count("one")
# print(b)
#
# elements = ["one", "two", "three", "one", "two", "one"]
# print(elements.index("three"))



# elements = [1, "meow", 3, "meow"]
# elements.pop(1)
# print(elements)
#
# elements.pop()    # удаляет первый элемент списка
# print(elements)
#
# elements.pop(-1)  # удаляет последний элемент списка
# print(elements)
#
# a = [1, 2, 3]
# a.reverse()
# print(a)            # СМ РАБОТУ РОР(-1)


# elements = [3, 19, 0, 3, 102, 3, 1]
# elements.sort()
# print(elements) # по возростанию
#
# elements = [3, 19, 0, 3, 102, 3, 1]
# elements.sort(reverse=True)
# print(elements) # по убыванию


# elements = [["яблоки", 50], ["апельсины", 190], ["груши", 100]]
# print(elements[0])
# print(elements[1][0])
#
# elements = [["яблоки", 50], ["апельсины", 190], ["груши", 100]]
# print(elements[0])
# print(elements[1][0])

# elements = [0.1, 0.2, 1, 2, 3, 4, 0.3, 0.4]
# int_elements = elements[2:6]    # с 2го элемента по 6й включительно
# print(id(elements), id(int_elements))
# print(elements)
# print(int_elements) # срезы не изменяют исходный список
# cм примеры со срезами

# ЗАДАЧИ

# elements = [1, 2, 3, 4, 5]
# elements.sort(reverse=True)
# a = list(elements)
# print(id(a), id(elements), a, elements)


# elements = [1, 2, 3, 20, 10, 600, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# l = elements.index(20)
# print(l)
# elements[l] = 200
# print(elements)


# ДОМАШНЯЯ ЗАДАЧА

# my_list = [15, 48, "hello", 6, 19, "world"]
# for i in my_list:
#     if type(i) == int:
#         if i % 2 == 0:
#             c = i % 10 + i // 10
#             print(f"Число {i} чётное, сумма цифр числа:", c)
#         else:
#             my_list[my_list.index(i)] = 1
#     elif type(i) == str:
#         vowels = 0
#         consonants = 0
#         for a in i:
#             if a in "aeiouy":
#                 vowels += 1
#             else:
#                 consonants += 1
#         print(vowels, consonants)
# print(my_list)




#
# my_list = [15, 48, "hello", 6, 19, "world"]
# for i in my_list:
#     if type(i) == int:
#         if i % 2 == 0:
#             print(f"Число {i} чётное, сумма цифр числа:", i % 10 + i // 10)
#         else:
#             my_list[my_list.index(i)] = 1
#     elif type(i) == str:
#         vowels = 0
#         consonants = 0
#         for a in "aeiouy":
#             if a in i:
#                 s = i.count(a)
#                 vowels += s
#         for a in 'bcdfghjklmnpqrstvwxyz':
#             if a in i:
#                 s = i.count(a)
#                 consonants += s
#
#         print(f'Количество гласных: {vowels}; Количество согласных: {consonants}')
# print(my_list)









# Введите семизначное число
# Если чётных в нём больше чем нечётных, то найти сумму всех его чисел
# Если наоборот то произведение - 1го, 3го, 4го.


number = input("Введите семизначное число: ")
# number = [1,2,3,4, 5, 6, 7]
even = 0
odd = 0
sum = 0
s = []
if len(number) == 7:
    for i in number:
        #if type(i) == int:        # почему не работает для стороки
        if int(i) % 2 == 0:
            even += 1
    print(even)
    #     else:
    #         odd += 1
    # if even > odd:
    #     for i in number:
    #         sum += int(i)
    #         #print(sum)
    # elif odd > even:
    #     s = int(number[0]) * int(number[2]) * int(number[3])
    # print(s)
    # print(sum)

# введите строку, посчитать кол-в гласных и согласных,
# если гласных  и согласных одинаковое количество вывести на экран все гласные буквы


# a = input("Введите строку: ")
# vowels = "ауоыиэяюёе"
# vowels_list = 0
# consonants_list = 0
# char = []
# char2 = []
# for i in a:
#     if i.lower() in vowels:
#         vowels_list += 1
#         char.append(i)
#     else:
#         consonants_list += 1
#         char2.append(i)
#
# print(vowels_list, consonants_list)
# if vowels_list == consonants_list:
#     print(char, char2)


# import random
# number1 = int(input("Введите первое число от 1 до 20: "))
# number2 = int(input("Введите второе число от 1 до 20: "))
# user = 0
# rand = 0
# remember1 = 0
# remember2 = 0
# for i in range(8):
#     rand_number1 = random.randint(1, 20)
#     rand_number2 = random.randint(1, 20)
#     if i == 4:
#         remember1 = rand_number1
#         remember2 = rand_number2
#     if number1 + number2 > rand_number1 + rand_number2:
#         user += 1
#     elif number1 + number2 < rand_number1 + rand_number2:
#         rand += 1
#
# print(f"Пользователь: {user}", f"Комп: {rand}")
# if user == rand:
#     print(remember1, remember2)
# else:
#     print("Не равны")

# import random
# count_item = int(input("Введите число в котором будем искать: "))
# number = input("Введите цифру которую будем искать: ")
# answer = 0
# for i in range(count_item):
#     rand = random.randint(1, 100)
#     answer += str(rand).count(number)
# print(answer)





# a = input('5 dkfj78df 9 8 dkfj8')
# num_list = []
# num = ''
# for char in a:
#     if char.isdigit():
#         num = num + char
#         print(num)
#     else:
#         if num != '':
#             num_list.append(int(num))
#             num = ''
# # if num != '':
# #     num_list.append(int(num))       # ОБРАЗЕЦ ИЗ ИНТЕРНЕТА НЕ РАБОТАЕТ
# print(num_list)

# s = int(input('5 dkfj78df 9 8 dkfj8'))
# l = len(s)
# # print(l)
# integ = []
# i = 0
# while i < l:
#     s_int = ''
#     a = s[i]
#     # print(s_int)
# while '0' <= a <= '9':
#     s_int += a
#     i += 1
#     if i < l:
#         a = s[i]
#     else:
#         break
# i += 1
# if s_int != '':
#     integ.append(int(s_int))        # # ОБРАЗЕЦ ИЗ ИНТЕРНЕТА НЕ РАБОТАЕТ
#
# print(integ)



# list = [15, 48, 'hello', 6, 19, 'world']
# #
# def sum_of_digits(x):
#     x = str(x)
#     y = 0
#     for i in x:
#         y += int(i)
#     return y
# #
# def foo(x):
#     y = 0
#     z = 0
#     for i in x:
#         if i == 'i' or i == 'o' or i == 'u' or i == 'y' or i == 'a' or i == 'e':
#             y += 1
#         else:
#             z += 1
#     return [str(y), str(z)]
#
# # for i in list:
#     if type(i) is int:
#         if i % 2 == 0:
#             print(sum_of_digits(i))
#         else:
#             list[list.index(i)] = list[0]
#
# for i in list:
#     if type(i) is str:
#         g = i.lower()
#         print('Гласных {0[0]},Согласных {0[1]}'.format(foo(g)))
# print(list)
