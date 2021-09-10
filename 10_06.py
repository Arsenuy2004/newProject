# number = input("Введите семизначное число: ")
# even = 0
# odd = 0
# sum = 0
# s = []
# if len(number) == 7:
#     for i in number:
#         if int(i) % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     if even > odd:
#         for i in number:
#             sum += int(i)
#             #print(sum)
#     elif odd > even:
#         s = int(number[0]) * int(number[2]) * int(number[5])
#         print(s)
# print(sum)


# a = input("Введите текст: ")
# b = "ауоыиэяюёе"
# sg = 0
# gl = 0
# s = []
# for i in a.lower():
#     if i in b:
#         sg += 1
#         s.append(i)
#     else:
#         gl += 1
# print(f'Согласные: {sg}', f'Гласные: {gl}')
# if sg == gl:
#     print(s)



# a = input("Введите семизначное число: ")
# ch = 0
# n_ch = 0
# summ = 0
# s = []
# if len(a) == 7:
#     for i in a:
#         i = int(i)
#         if i % 2 == 0:
#             ch += 1
#         else:
#             n_ch += 1
#     if ch > n_ch:
#         summ += i
#         print(f'Сумма: {summ}')
#     elif n_ch > ch:
#         s = int(a[0]) * int(a[2]) * int(a[5])
#         print(s)


# a = input("Введите строку: ")
# vowels = "ауоыиэяюёе"
# vowels_list = 0
# consonants_list = 0
# char = []
# for i in a:
#     if i.lower() in vowels:
#         vowels_list += 1
#         char.append(i)
#     elif i.isalpha():
#         consonants_list += 1
# print(vowels_list, consonants_list)
# if vowels_list == consonants_list:
#     print(char)


# a = input("Введите строку: ")
# gl = 'ауоыиэяюёе'
# gl_n = 0
# sogl_n = 0
# s = []
# for i in a:
#     if i.isalpha():
#         if i.lower() in gl:
#             gl_n += 1
#             s.append(i.lower())
#         else:
#             sogl_n += 1
# print(gl_n, sogl_n)
# if gl_n == sogl_n:
#     print(s)


# import random
# a = int(input("Введите первое число (от 1 до 20): "))
# b = int(input("Введите воторое число (от 1 до 20): "))
# human = 0
# comp = 0
#
# c = random.randint(1, 20)
# d = random.randint(1, 20)
#
# for i in range(6):
#     if a + b > c + d:
#         human += 1
#         i == 4
#     elif a + b < c + d:
#         comp += 1
#     if human == comp:
#         print(i)
# print(human, comp)       # решить до конца






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
# a = int(input("Введите  число: "))
# b = input("Введите искомую цифру: ")
# s = 0
# for i in range(a):
#     k = random.randint(1, 50)
#     k = str(k)
#     if b in k:
#         s += 1
# print(s)





#
# my_list = input("Введите строку: ")
# for i in my_list:
#     if i.isdigit():
#         print(i, end=" ")






# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
# веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
# также сколько всего букв в слове, сколько гласных и согласных.
#

a = input("Введите строку: ")
gl = 0
sogl = 0
low = ''
up = ''
p_l = 0 # пары нижнего регистра
p_h = 0 # пары верхнего регистра
for i in a:
    if a.isalpha():
        if i in "AEOIUaeoiu":
            gl += 1
        else:
            sogl += 1
    if i.islower():
        low += i
        if len(low) % 2 == 0:
            p_l += 1
    # elif low != '':
    #     low = ''
    if i.isupper():
        up += i
        if len(up) % 2 == 0:
            p_h += 1
    # elif up != '':
    #     up = ''
print('Согласные', sogl, 'Гласные', gl)
print(f"Пары нижнего регистра: {p_l}, Пары верхнего регистра: {p_h}")
print('Длина строки', len(a))







# vowels = "ауоыиэяюёе"
# line = input("Введите слово с разным регистром: ")
# pare = 0
# pare1 = 0
# vowels_count = 0
# consonants_count = 0
# for char in range(len(line) - 1):
#     if line[char].islower() and line[char + 1].isupper():
#         pare = 1
#     elif line[char].isupper() and line[char + 1].islower():              # см Артур - не считает пары
#         pare1 += 1
#     # if line[char].lower() in vovels:
#     #     vowels_count += 1
#     # elif line[char].isalpha():
#     #     consonants_count += 1
# print(pare, pare1)






# my_list = input("Введите слово с разным регистром: ")
#  i = ""
# # s = 0
# # prev = my_list[0]
# while i
# for i in my_list[1:]:
#     if i.islower():
#         key = i.islower(sorted(prev + i)
#         s += 1
#     print(i)
#
# s = 'abbsbsbsbsassbsbasabsbasss'
# prev = s[0]
# d = {}
# for i in s[1:]:
#     key = ''.join(sorted(prev + i))  # это равнозначно key = a.join(sorted(prev + i))
#     d[key] = d.get(key, 0) + 1        # c введением пепеменной a
#     prev = i
# print(d)



# for i in range(1, 10):
#     i -= 5
# print(i)

# i = 0
# while i < 10:
#     i += 1
#     print(i)
# i -= 10
# print(i)

# 'a'+'x'
# if '123'.isdigit():
# else:
# 'y'+'b'                # ???








