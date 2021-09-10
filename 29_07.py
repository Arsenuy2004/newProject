# a = int(input())
# b = int(input())
# c = int(input())
# if a > 0 and b < 0:
#     print("and")
# if a > 0 or b < 0:
#     print("or")
# if not (c > 0) == True:
#     print("not")

# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a > c:
#     print("a")
# elif a < b > c:
#     print("b")
# else:
#     print("c")

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if a > b and a > c:
#     print("a")
# elif b > a and b > c:
#     print("b")
# else:
#     print("c")

# import random
# random_numb = random.randint(1, 3)
# print(if "1" == "камень" or elif "2" == "ножницы" or elif "3" == "бумага")      # не работает


import random
random_numb = random.randint(1, 3)
human = int(input('Введите команду ("камень - 1", "ножницы - 2", "бумага - 3"): '))

if random_numb == 1:
    print("комп - камень")
elif random_numb == 2:
    print("комп - ножницы")
else:
    print("комп - бумага")

if human == 1:
    print("твой выбор - камень")
elif human == 2:
    print("твой выбор - ножницы")
else:
    print("твой выбор - бумага")

if human == 1 and random_numb == 3:
    print("комп выиграл")
elif human == 3 and random_numb == 1:
    print("ты выиграл")
elif human < random_numb:
    print("ты выиграл")
elif human > random_numb:
    print("комп выиграл")
else:
    print("ничья")

# import random
# while True:
#     random_numba = random.randint(1, 9)
#     human = int(input("Введите число от дного до 9: "))
#     if human == random_numba:
#         print("Вы угадали число", random_numba)
#         break
#     else:
#         print("Увы, вы проиграли",  random_numba)


# import random
# while True:
#     random_numba = random.choice('195678234')
#     human = input("Введите число от дного до 9: ")
#     if human == random_numba:
#         print("Вы угадали число", random_numba)
#         break
#     else:
#         print("Увы, вы проиграли",  random_numba)




