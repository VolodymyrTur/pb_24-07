#################### 6.1 ###############
# import string
#
# # Отримуємо вхідні дані
# start, end = input("Введіть діапазон (наприклад, a-c): ").split("-")
#
# # Знаходимо позиції початкової та кінцевої літери
# start_index = string.ascii_letters.index(start)
# end_index = string.ascii_letters.index(end)
#
# # Беремо зріз і друкуємо
# print(string.ascii_letters[start_index:end_index+1])

# import string
#
# user_letters = input('Please enter two letters separated by a hyphen (Example: a-A): ')
#
# start_letter, end_letter = user_letters.split('-')
#
# index_start_letter = string.ascii_letters.index(start_letter)
# index_end_letter = string.ascii_letters.index(end_letter)
#
# if index_start_letter > index_end_letter:
#     mod_string_letters = string.ascii_letters[index_start_letter:] + string.ascii_letters[:index_end_letter + 1]
# else:
#     mod_string_letters = string.ascii_letters[index_start_letter:index_end_letter + 1]
#
# print(f'"{user_letters}" -> {mod_string_letters}')

######################## 6.2 ##########################

# seconds = int(input("Введіть число секунд (0 <= n < 8640000): "))
# days, remainder = divmod(seconds, 86400)
# hours, remainder = divmod(remainder, 3600)
# minutes, seconds = divmod(remainder, 60)
#
# if days % 10 == 1 and days % 100 != 11:
#     day_word = "день"
# elif days % 10 in (2, 3, 4) and not (12 <= days % 100 <= 14):
#     day_word = "дні"
# else:
#     day_word = "днів"
#
# time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
# print(f"{days} {day_word}, {time_str}")
# print(f'{days} {day_word}, {hours:02}:{minutes:02}:{seconds:06}')

######################## 6.3 ##########################

# number = int(input("Введіть число: "))
#
# while number > 9:
#     product = 1
#     for digit in str(number):
#         product *= int(digit)
#     number = product
#
# print(number)

# import math
#
# number = int(input('Введіть будь-яке число: '))
# if int(number) > 9:
#     while number > 9:
#         list_number = [int(ch) for ch in str(number)]  # отримуємо список із цифр
#         list_number2 = list(map(int, list(str(number))))  # отримуємо список із цифр
#         number = math.prod(list_number) # перемножуємо елементи списку
#     print('Результат множення: ', number)
# else:
#     print("Результат множення дорівнює введеному числу: ", number)


# def square(x: int):
#     return x ** 2
#
#
# def cube(x: int):
#     return x ** 3
#
#
# def apply(func, data: list[int]):
#     result = []
#     for item in data:
#         result.append(func(item))
#
#     return result
#
# # square(2)
# # print(square(2))
# # print(cube(2))
# my_list = [1, 2, 3, 4, 5]
# my_apply = apply(square, my_list)
#
# print(my_apply)
# print("__" * 100)
# print(apply(cube, my_list))


# def calculate_area(radius):
#     """
#     Calculate the area of a circle.
#
#     :param radius: The radius of the circle.
#     :return: The area of the circle.
#     """
#     area = 3.14 * radius ** 2
#     return area
#
#
# # Виведення документації функції
# print(help(calculate_area))
#
#
# def calc(number_1: int, number_2: int, operation: str = "") -> tuple[int, bool]:
#     """
#     Calculates numbers based on the given operation.
#
#     Args:
#         number_1: The first number.
#         number_2: The second number.
#         operation: The operation to perform.
#
#     Returns:
#         tuple: A tuple containing the result and a boolean indicating whether the result is zero.
#     """
# print(calc(2, 3,  ""))


# def factorial(number: int):
#     if number == 0 or number == 1:
#         return 1
#
#     else:
#         print(number)
#         return number * factorial(number - 1)
#
#
# print(factorial(5))


# def cube(x: int):
#     return x ** 3
#
# my_func = lambda x: x ** 3
#
# print([cube(i) for i in range(10)])
# print([(my_func)(x) for x in range(10)])
# print([(my_func)(x) for x in range(20)])
# print([(my_func)(x) for x in range(30)])


### map, filter, zip


# def square(x: int):
#     # print(x)
#     return x ** 2
#
# my_func = lambda x, y: x ** y
#
# print(my_func(2, 3))
# print(my_func(2, 6))
# print(my_func(2, 3))
# print(my_func(3, 3))
# print(my_func(2, 3))
# print(my_func(2, 3))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(map(lambda x: x ** 2, numbers)))
# print(list(map(square, numbers)))
# print([square(x) for x in numbers])

# for x in map(square, numbers):
#     print(x)


# def my_filter(x):
#     return x % 2 == 0
#
#
# print(list(filter(lambda x: x % 2 == 0, numbers)))
# print(list(filter(my_filter, numbers)))
# print([x for x in numbers if x % 2 == 0])

# fruit = ["apple", "banana", "cherry", "kiwi", "mango"]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# names = ["John", "Peter", "Sam", "Max", "Alex"]
#
# print(list(zip(numbers, fruit, names)))