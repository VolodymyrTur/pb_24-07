########## 5.1 ##############
# import string
# import keyword
#
# name = input("Введіть ім'я змінної: ")
#
# allowed_chars = set(string.ascii_lowercase + string.digits + "_")
# result = True
#
# # 1. Не починається з цифри
# if name[0].isdigit():
#     result = False
#
# # 2. Не містить великих літер
# elif any(ch.isupper() for ch in name):
#     result = False
#
# # 3. Не містить пробілів і знаків пунктуації, крім "_"
# elif any(ch not in allowed_chars for ch in name):
#     result = False
#
# # 4. Не більше одного підкреслення в усьому імені
# elif name.count("_") > 1:
#     result = False
#
# # 5. Не входить до списку зареєстрованих слів
# elif name in keyword.kwlist:
#     result = False
#
# print(result)

# variable_name = input('Enter a variable name: ')
#
# is_single_underscore = variable_name == '_'
# is_identifier = variable_name.isidentifier()
# is_lower = variable_name.islower()
#
# is_valid_variable = is_single_underscore or all((is_lower, is_identifier))
#
# print(is_valid_variable)

############ 5.2 ##################
# working_calc = 'y'
# while working_calc in ('y', 'yes'):
#
#     first_number = int(input('Enter first number: '))
#     second_number = int(input('Enter second number: '))
#     calculator_action = input('Enter calculator action (+ - * /): ')
#
#     result = 0
#     message = ''
#
#     if calculator_action == '+':
#         result = first_number + second_number
#
#     elif calculator_action == '-':
#         result = first_number - second_number
#
#     elif calculator_action == '*':
#         result = first_number * second_number
#
#     elif calculator_action == '^':
#         result = first_number ** second_number
#
#     elif calculator_action == '/' and second_number != 0:
#         result = first_number / second_number
#
#     elif calculator_action == '/' and second_number == 0:
#         message = f'Number {first_number} cannot be divided by zero'
#
#     else:
#         message = 'You entered invalid calculator action'
#
#     if message:
#         print(message)
#     else:
#         print(f'{first_number} {calculator_action} {second_number} = {result}')
#
#     working_calc = input('You need a calculator? (yes/no): ')

############### 5.3 ##################
# import string
#
# text = input("Введіть рядок: ")
#
# # Видаляю знаки пунктуації та пробіли
# for char in string.punctuation:
#     text = text.replace(char, "")
#
# text = text.title()
#
# # Розбираю текст на слова
# words = text.split()
#
# # Об'єдную слова та додаю #
# hashtag = "#" + "".join(words)
#
# # Завдання виконав :)
# print(hashtag[:140])

# import string
#
# user_string = 'Should, I. subscribe? Yes!'
#
# mod_string = ''.join(
#     item
#     for item in user_string
#     if item not in string.punctuation
#     ).title().replace(' ', '')

# hashtag_string = '#' + mod_string[:139]
#
# print(f'{user_string} -> {hashtag_string}')
#
#
# import string
#
# text_by_hashtag = input("Введіть текст для формування хештегу: ")
#
# # Прибираємо пунктуацію, залишаємо тільки букви/пробіли
# for char in string.punctuation:
#     text_by_hashtag = text_by_hashtag.replace(char, "")
#
# # Додаємо решітку попереду та робимо кожне слово з великої літери
# hashtag = '#' + text_by_hashtag.title().replace(" ", "")
#
# # Виводимо максимум 140 символів
# print(hashtag[:140])

# def multiply(a: str, b: int) -> float:
#     """
#     Multiply two numbers.
#
#     Args:
#         a (int): First number.
#         b (int): Second number.
#
#     Returns:
#         int: Result of the multiplication.
#     """
#     if isinstance(b, str):
#         return 10 * a * b
#
#     else:
#         return 100 * a * float(b)
#
#
# print(multiply(10, 2))

# import operator
#
#
# def calculator(a: int, b: int, operation: str) -> int | float | str:
#     operations = {
#         "+": operator.add,
#         "-": operator.sub,
#         "*": operator.mul,
#         "/": operator.truediv,
#         }
#
#     result = "Invalid operation"
#     func = operations.get(operation)
#
#     if func:
#         result = func(a, b)
#
#
#     # if operation == "+":
#     #     result = operator.add(a, b)
#     #
#     # elif operation == "-":
#     #     result = operator.sub(a, b)
#     #
#     # elif operation == "*":
#     #     result = operator.mul(a, b)
#     #
#     # elif operation == "/":
#     #     result = operator.truediv(a, b)
#
#     return result
#
#
# print(calculator(10, 2, "l"))
# print(operator.add(10, 2))

###### LEGB - locals, enclosing, globals, builtins ######

# var = "global"
#
# def outer():
#     var = "locals"
#     print(locals())
#
#     def inner():
#         var = "enclosing"
#         print(var)
#
#     inner()
#
# print(var)
# outer()

# def func(arg_1, arg_2, arg_3, *args):
#     for i in args:
#         print(str(i ** 8))
#
#     print(arg_1, arg_2, arg_3, args, sep='\n')
#
# vars = [1, 2, 3, 4, 5, 6]
# func(*vars)


# def func(*args, **kwargs):
# def func(arg_1, arg_2, *, arg_3, arg_4, arg_5=True, arg_6): # всі елементи після * передаються як ключьові
# def func(arg_1, arg_2, *, arg_3):
#     if arg_3:
#     print("DO something")
    # print(args)
    # print(kwargs)

    # for i in kwargs.items():
    #     print(str(i))
    #
    # print(arg_1, arg_2, arg_3, kwargs, sep='\n')

# vars = {
#     # 'arg_1': 1,
#     # 'arg_2': 2,
#     'arg_3': 3,
#     'arg_4': 4,
#     'arg_5': 5,
#     'arg_6': 6
# }

# func(1, 2, **vars)
# func(1, 2, arg_3=3, arg_4=4, arg_6=6)

# print(*list("7890"), sep='\n')

# drukuy = print
# drukuy("Hello", "World", sep="!")