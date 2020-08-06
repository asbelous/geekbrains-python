# 1 задание

#number = int(input('Введите число: '))
#print('Ваш результат: ', number + 2)

# 2 задание

# while True:
#     number = int(input('Введите число больше 0 и меньше 10: '))
#     if(number <= 0 or number >= 10):
#         print('Число не подходит')
#         continue
#     else:
#         print('Ваш результат: ', number ** 2)
#         break

# 3 задание

# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# age = int(input('Введите возраст: '))
# weight = int(input('Введите вес: '))
#
# if(age <= 30 and weight >= 50 and weight <= 120):
#     print(name, " ", surname, ", возраст - ", age, ", вес - ", weight, " кг: в хорошем состоянии!", sep='')
# if(age > 30 and age <= 40 and weight < 50 or weight > 120):
#     print(name, " ", surname, ", возраст - ", age, "вес - ", weight, " кг: займись собой!", sep='')
# if(age > 40 and weight < 50 or weight > 120):
#     print(name, " ", surname, ", возраст - ", age, "вес - ", weight, " кг: обратись к врачу!", sep='')

# 4 Задание

# my_list_1 = [2, 5, 8, 2, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
#
# for num in my_list_2:
#     while num in my_list_1:
#         my_list_1.remove(num)
# print(my_list_1)

# my_list_1 = [2, 5, 8, 2, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# print(list(set(my_list_1)-set(my_list_2)))

# 5 Задание

# days = {
#     '01' : 'первое',
#     '02' : 'второе',
#     '03' : 'третье',
#     '04' : 'четвёртое',
#     '05' : 'пятое',
#     '06' : 'шестое',
#     '07' : 'седьмое',
#     '08' : 'восьмое',
#     '09' : 'девятое',
#     '10' : 'десятое',
#     '11' : 'одиннадцатое',
#     '12' : 'двенадцатое',
#     '13' : 'тринадцатое',
#     '14' : 'четырнадцатое',
#     '15' : 'пятнадцатое',
#     '16' : 'шестнадцатое',
#     '17' : 'семнадцатое',
#     '18' : 'восемнадцатое',
#     '19' : 'девятнадцатое',
#     '20' : 'двадцатое',
#     '21' : 'двадцать первое',
#     '22' : 'двадцать второе',
#     '23' : 'двадцать третье',
#     '24' : 'двадцать четвёртое',
#     '25' : 'двадцать пятое',
#     '26' : 'двадцать шестое',
#     '27' : 'двадцать седьмое',
#     '28' : 'двадцать восьмое',
#     '29' : 'двадцать девятое',
#     '30' : 'тридцатое',
#     '31' : 'тридцать первое'
# }
#
# months = {
#     '01' : 'января',
#     '02' : 'февраля',
#     '03' : 'марта',
#     '04' : 'апреля',
#     '05' : 'мая',
#     '06' : 'июня',
#     '07' : 'июля',
#     '08' : 'августа',
#     '09' : 'сентября',
#     '10' : 'октября',
#     '11' : 'ноября',
#     '12' : 'декабря'
# }
#
# data = input("Введите дату в формате dd.mm.yyyy : ")
#
# data = data.split('.')
# day = days[data[0]]
# month = months[data[1]]
#
# print(f'{day} {month} {data[2]} года')

# 6 Задание

# numbers = [2, 2, 5, 12, 8, 2, 12, 7]
#
# result = []
# for num in numbers:
#     if numbers.count(num) == 1:
#         result.append(num)
# print(result)

# 7 Задание Угадай число

# import random
#
# min_number = 1
# max_number = 100
# result = None
# while result != '=':
#     number = random.randint(min_number, max_number)
#     print(number)
#     result = input('= > < ')
#     if result == '>':
#         min_number = number + 1
#     elif result == '<':
#         max_number = number - 1
# print('Победа')

# 8 Задание

# def person(name, age, city):
#     return f'{name}, {age} год, проживает в городе {city}'
#
# name = input("Введите имя: ")
# age = input("Введите возраст: ")
# city = input("Введите город: ")
# print(person(name, age, city))

# 9 Задание

# def get_max(a, b, c):
#     maxi = max(a, b, c)
#     return f'Наибольшее число - {maxi}'
#
# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# c = input("Введите третье число: ")
# print(get_max(a, b ,c))

# 10 Задание

# player_name = input("Введите имя игрока: ")
# enemy_name = input("Введите имя противника: ")
#
# player = {
#     "name": player_name,
#     "health": 100,
#     "damage": 50
# }
#
# enemy = {
#     "name": enemy_name,
#     "health": 100,
#     "damage": 50
# }
#
# def attack(pers1, pers2):
#     pers2["health"] -= pers1["damage"]
#     print(f'{pers1["name"]} наносит {pers1["damage"]} урона {pers2["name"]}. Здоровья у {pers2["name"]} осталось {pers2["health"]}.')
#
# attack(player, enemy)

# 11 Задание

# player_name = input("Введите имя игрока: ")
# enemy_name = input("Введите имя противника: ")
#
# player = {
#     "name": player_name,
#     "health": 1000,
#     "damage": 50,
#     "armor": 1.2
# }
#
# enemy = {
#     "name": enemy_name,
#     "health": 1200,
#     "damage": 40,
#     "armor": 1.3
# }
#
# def get_damage(damage, armor):
#     return damage / armor
#
# def attack(pers1, pers2):
#     damage = get_damage(pers1["damage"], pers2["armor"])
#     pers2["health"] -= damage
#     print(f'{pers1["name"]} наносит {pers1["damage"]} урона {pers2["name"]}. Здоровья у {pers2["name"]} осталось {int(pers2["health"])}.')
#
# attack(player, enemy)