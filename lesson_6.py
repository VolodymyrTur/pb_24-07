########### 3.1 ################

# first_number = int(input('Enter first number: '))
# second_number = int(input('Enter second number: '))
# calculator_action = input('Enter calculator action (+ - * /): ')
#
# result: int = 0
# message: str = ''
#
# if calculator_action == '+':
#     result = first_number + second_number
# elif calculator_action == '-':
#     result = first_number - second_number
# elif calculator_action == '*':
#     result = first_number * second_number
# elif calculator_action == '^':
#     result = first_number ** second_number
# elif calculator_action == '/' and second_number != 0:
#     result = first_number / second_number
# elif calculator_action == '/' and second_number == 0:
#     message = f'Number {first_number} cannot be divided by zero'
# else:
#     message = 'You entered invalid calculator action'
#
# if message:
#     print(message)
# else:
#     print(f'{first_number} {calculator_action} {second_number} = {result}')


# pershe_chislo = input("Введіть 1-ше число: ")
# diya = input("Введіть дію: ")
# druge_chislo = input("Введіть 2-ге число: ")
#
# if int(pershe_chislo) and int(druge_chislo == "0"):
#     print('На нуль ділити не можна')
# elif diya == "+":
#     print(int(pershe_chislo) + int(druge_chislo))
# elif diya == "-":
#     print(int(pershe_chislo) - int(druge_chislo))
# elif diya == "*":
#     print(int(pershe_chislo) * int(druge_chislo))
# elif diya == ":":
#     print(int(pershe_chislo) // float(druge_chislo))


# get_number1 = input("Введіть число 1-ше число: ")
# get_action = input("Введіть дію +,-,*,/,%,//,**: ")
# get_number2 = input("Введіть число 2-ше число: ")
#
# get_number1 = int(get_number1)
# get_number2 = int(get_number2)
#
#
# if get_number2 == 0 and get_action in ("/","//","%") : # перевірка ділення на нуль
#     print("На нуль ділити не можна")
# elif get_action == "+":
#     message = f"{get_number1} + {get_number2} = {get_number1 + get_number2} "
# elif get_action == "-":
#     minus = get_number1 - get_number2
#     print(f"{get_number1} - {get_number2} = {minus} ")
# elif get_action == "*":
#     multiplication = get_number1 * get_number2
#     print(f"{get_number1} * {get_number2} = {multiplication} ")
# elif get_action == "/":
#     dil_float = get_number1 / get_number2
#     print(f"{get_number1} / {get_number2} = {dil_float} ")
# elif get_action == "//"  :
#     dilInt = get_number1 // get_number2
#     print(f"{get_number1} // {get_number2} = {dilInt} ")
# elif get_action == "%":
#     fraction = get_number1 % get_number2
#     print(f"{get_number1} % {get_number2} = {fraction} ")
# elif get_action == "**":
#     step = get_number1 ** get_number2
#     print(f"{get_number1} ** {get_number2} = {step} ")
# else:
#     print("Ви ввели не правильну дію")


####### 3.2 ########
# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst = [0]
# if len(lst) > 1:
# # if lst:
#     lst.insert(0, lst.pop())
#     print(lst)  # [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# else:
#     print("Список пустий або надто малий для переміщення елементів.")
#     print(lst)  # [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]


# my_list = [8, 12, 3, 4, 10]
# my_list = [12, 3, 4, 10]
# my_list = [1]
# my_list = []

# my_list = [10, True, "-", 18, 20]
# if len(my_list) <= 1:
#     print(my_list)
# else:
#     print("Result: " + str([my_list[-1]] + my_list[:-1]))

# mod_list = my_list[-1:] + my_list[:-1]
#
# print(f'{my_list} => {mod_list}')


######### 3.3 ###########

# my_list = [1, 2, 3, 4, 5, 6]
# my_list = [1, 2, 3, 4, 5]
# my_list = [1, 2, 3]
# my_list = [1]
# my_list = []

# length = len(my_list)
# middle = (length + 1) // 2
#
# result = [my_list[:middle], my_list[middle:]]
# print(result)

my_str = "hello World"
# my_str2 = "Привіт світ"
# byte_str = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82 \xd1\x81\xd0\xb2\xd1\x96\xd1\x82'
# print(my_str.title())
# print(my_str.capitalize())
# print(my_str.split("o"))
# print(my_str.upper())
# print(my_str.lower())

# print(my_str)
# print(my_str2)
# print(my_str.encode("utf-8"))
# print(my_str2.encode("utf-8"))
# print(byte_str.decode("utf-8"))

########## tuple ##############
# my_tuple = (
#     1,
#     2,
#     3,
#     4,
#     "5",
#     [1, 2, 3]
# )

# my_tuple2 = 1, 2, 3, 4
# my_tuple3 = ()
# my_tuple4 = (2,)

# print(id(my_tuple), my_tuple)
# print(my_tuple2)
# print(my_tuple3)
# print(my_tuple4)

# print(my_tuple[0])
# print(my_tuple[0:-1])
# print(my_tuple[0:-1:2])
# my_list = list(my_tuple)
# my_list[0] = 10
# my_list.append(11)
# my_tuple = tuple(my_list)
# my_tuple[-1].append(100)
# print(id(my_tuple), my_tuple)

############ dict ###############

# my_dict = {
#     "name": "Vova",
#     "age": 20,
#     1: "one",
#     "one": 1,
#     (1, 2): "(1, 4)",
#     6.8: "float",
#     True: "bool",
#     None: "None",
#     }

# my_dict2 = {}
# my_dict3 = dict(name="Vova", age=20)
# my_dict4 = dict([("name", "Vova"), ("age", 20)])
# my_dict5 = dict.fromkeys(["name", "age"], "Vova")

# my_dict["name"] = "Vova1"
# my_dict[0] = "null"
# my_dict.update(
#     {
#         "name": "Vova1",
#         "region": "Dnipro",
#         }
#     )

# my_dict = {}
#
# for i in range(10):
#     # my_dict.update({f"key{i}": i})
#     my_dict[f"key{i}"] = i


# my_dict = {
#     f"key{i}": i
#     for i in range(10)
#     }

# pop_val = my_dict.pop("age")
# print(pop_val)
# print(my_dict)
# print(my_dict2)
# print(my_dict3)
# print(my_dict4)
# print(my_dict5)

# for key, value in my_dict.items():
#     print(key, value)

# from collections import OrderedDict
#
# ord_dict = OrderedDict(my_dict)
# print(ord_dict)
# # print(len(ord_dict))
# # print(ord_dict.popitem(last=False))
# # ord_dict.move_to_end("name")
# ord_dict.move_to_end("age", last=False)
# print(ord_dict)

# from collections import namedtuple
#
# Point = namedtuple("Point", ["whith", "height"])
#
# p = Point(1, 2)
#
# print(p.whith, p.height)
