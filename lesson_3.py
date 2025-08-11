# не змінний
# int
# complex
# float
# str
# bool
# tuple

# Змінний
# list
# dict
# set

# MY_CONST = 10
####### оператори порівняння #### >, <, >=, <=, !=, ==, is, in, not

# some_value = 4
# some_value2 = 4
#
# print(some_value <= some_value2)

# some_string = "Hello"
# some_string2 = "Hello"
#
# print(some_string == some_string2)

# some_value = 4
# some_value2 = 4.0
# some_value3 = "4"
#
# print(some_value is some_value2)
# print(some_value == some_value2)
# print(id(some_value), id(some_value2))

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# lst3 = lst1
#
# print(id(lst1), id(lst2), id(lst3))
# print(lst1 is not lst2)
# print(lst1 is lst3)


# and, or

# some_int = 30
# some_int2 = 20
#
# if some_int != some_int2:
#     print(f"{some_int} меньший за {some_int2}")
#
# # elif some_int < some_int2 and some_int == some_int2:
# elif some_int < some_int2 and some_int == some_int2:
#     print(f"{some_int} дорівнює {some_int2}")
#
# else:
#     print(f"{some_int} більший за {some_int2}")

# if 9 > 10 and 10 < 11:
# # if 9 > 10 < 11:
#     print("yes")
# else:
#     print("no")

# print("end")

# some_value = 10 if some_int < some_int2 else 20
#
# if some_int < some_int2:
#     some_value = 10
# else:
#     some_value = 20

from copy import deepcopy
# print(0 or 20)
#      0  1    2     3        4       5
# lst = [2, 3.4, True, "hello", [1, 4], 6]
# my_list = [1, 2, 3]
# lst.append([11, 12])
# lst += [11]
# print(lst[:3]) # всі елементи з початку до 3-го(виключно)
# print(lst[-1]) # останній елемент
# print(lst[3:]) # все з 3-го елементу і до останнього
# print(lst[3:]) # все з 3-го елементу і до останнього
# print(lst[10:28])

# my_list[2] = 10
# del my_list[2]
# print(my_list)
# new_list = deepcopy(lst) + my_list
# lst[4][1] = 5
# print(new_list)
# print(lst)
# print(my_list)
# print("hello" in lst)
# print(len(lst))
# print(len("lst"))
