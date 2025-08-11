# usr/bin/env python3
# -*- coding: utf-8 -*-

# while, for

# while True:
#     pass

# if True:
#     pass
# else:
#     pass

# print(list(range(2, 11, 2)))
# for i, value in enumerate(range(2, 11)):
#     print(i, value)

# my_list2 = []
#
# for i in range(2, 11):
#     if i % 2 == 0:
#         my_list2.append(i)
#     else:
#         my_list2.append(None)
#
# my_list = [
#     i
#     # if i % 2 == 0 else None
#     for i in range(2, 11)
#     if i % 2 == 0
#     ]
#
# print(my_list)

# user_input = int(input("Введіть 4-значне число: "))
#
# thousands = user_input // 1000
# hundreds = user_input // 100 % 10
# tenthes = user_input // 10 % 10
# ones = user_input % 10
#
# print(thousands)
# print(hundreds)
# print(tenthes)
# print(ones)

# n = int(input('Введіть додатне 5-значне ціле число: '))
#
# a = n // 10000
# b = (n % 10000) // 1000
# c = (n % 1000) // 100
# d = (n % 100) // 10
# e = n % 10
#
# result = e * 10000 + d * 1000 + c * 100 + b * 10 + a

# print(result)

###### string #######

# my_string = "Hello"
# my_string2 = "Hello"
#
# print(my_string == my_string2)
# print(my_string is my_string2)

# my_list = [1, 2, 3]
# my_list2 = [1, 2, 3]
#
# print(my_list == my_list2)
# print(my_list is my_list2)

# name = "Vova Turvav"
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.swapcase())
# print(name.count("v"))
# print(name.find("v"))
# print(name.rfind("v"))
# print(name)
# print(name.strip("_"))
# print(name.rstrip("_"))
# print(name.lstrip("_"))
# print(name.replace("v", "a"))

# some_string = "H e l l o"
# path = "C:\\Users\\user\\Desktop\\some_string.txt"
# new_list = path.split(".")
# new_list[-1] = "pdf"
# path = ".".join(new_list)
# print(path.split("."))
# print(path)
# print(some_string.split())
# print(" / ".join(some_string.split()))

# serial_number = "0000000013"
# serial_number2 = "12w"
# print(serial_number2.zfill(10))
# print(some_string.startswith("o"))
# txt = "Hello, welcome to my world."
#
# x = txt.startswith("Hello", 1, 9)
# x2 = txt.endswith("world.")
#
# print(x2)
# is_string = True
# print(serial_number2.isdigit())
# print(serial_number2.isalpha())

# %, format(), f-string

# name = "Vova"
# age = "20"
# my_float = 3.141592653589793

# print("%s  %s  %.3f" % (name, age, my_float))
# print("%s  %s  %s" % (name, age, my_float))

# print("{1}  {0}  {1}".format(name, age, my_float))
# print("{1}  {0}  {2:.2f}".format(name, age, my_float))
# print("{}  {}  {:.2f}".format(name, age, my_float))
# print("{1}  {0}  {1}".format(name, age))

# print(f"name={name}  age={age}  my_float={my_float}")
# print(f"{name=}  {age=}  {my_float=:.4f}")


############# ASCII vs UTF-8  ######################

# print(ord("a"))
# print(ord("A"))
# print(chr(4672))
# print(chr(65))
#
# alphbet = []
#
# from string import ascii_lowercase, ascii_uppercase
#
# print(ascii_lowercase)
# print(ascii_uppercase)

# for letter in range(ord("A"), ord("Z") + 1):
#     alphbet.append(chr(letter))
#
#
# print("".join(alphbet))

# import this
