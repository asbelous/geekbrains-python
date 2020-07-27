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
