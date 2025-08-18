#################### 4.1 ###############

# my_list = [0, 1, 0, 12, 3, 7, 0, 4, 0, 6, 0]
# zeros = my_list.count(0)
#
# while 0 in my_list:
#     my_list.remove(0)
#
# my_list.extend([0] * zeros)
#
# print(my_list)

# my_list = [0, 1, 0, 12, 3, 66, 0, 4]
# zeros = my_list.count(0)
#
# for _ in range(zeros):
#     my_list.remove(0)
#
# # my_list.extend([0] * zeros)
# my_list += [0] * zeros
#
# print(my_list)
#
# val1, _ = divmod(8, 2)
#
# print(val1)

# my_list =[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# print(f'{my_list} -> ', end='')
#
# for item in my_list:
#     if item == 0:
#         my_list.remove(item)
#         my_list.insert(len(my_list), item)
#
# print(my_list)

############ 4.2 ###############
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list = []
#
# result = sum(my_list[::2]) * my_list[-1] if my_list else 0
#
# print(result)

############ 4.3 ###############
# import random
#
# my_list = []
# new_list = [
#     random.randint(3,10)
#     for el in range(random.randint(3, 10))
#     ]
#
# print(my_list)
# print([my_list[0], my_list[2], my_list[-2]])
#
# import random
#
# my_list = [random.randint(1, 9) for i in range(random.randint(3, 10))]
#
# mod_list = [my_list[0], my_list[2], my_list[-2]]
#
# print(f'{my_list} == {mod_list}')

# my_dict = {
#     "name": "Vova",
#     "age": 20,
# }

# print(my_dict.get("country", "Ukraine"))
# print(my_dict["country"])
# my_dict["country"] = "Ukraine"
# my_dict["city"] = "Dnipro"
# my_dict["age"] = "20 years old"
#
# my_dict.update(
#     {
#         "country": "Ukraine",
#         "city": "Dnipro",
#         "age": "20 years old",
#         }
#     )

# my_dict = dict.fromkeys(
#     ["name", "age"],
#     []
#     )
#
# my_dict["name"].append("Vova")
#
# print(my_dict)
#
# from collections import defaultdict
#
# my_dict = defaultdict(list)
# my_dict["name"].append("Vova")
# my_dict["age"].append("24")
#
# print(my_dict)

# from collections import namedtuple
#
# Person = namedtuple("Person", ["name", "age", "city"])
#
# p = Person("Vova", 24, "Dnipro")
# print(p.name, p.age, p.city)


############# set ################

# my_set = {1, 2, 3, "one", "two", "three",}
# my_set2 = {78, 93, 13, 2, "three",}
# my_set.update(my_set2)
# my_set.add(10)

# print(my_set.union(my_set2))

# my_set3 = my_set.intersection(my_set2)
# my_set4 = my_set.difference(my_set2)
# my_set5 = my_set2.difference(my_set)
#
# print(my_set3)
# print(my_set4)
# print(my_set5)

# my_frozenset = frozenset([1, 2, 3, 4, 5])
# print(my_frozenset)

############ Functions ################

# def calc(number_1: int, number_2: int, operation: str) -> tuple[int, bool]:
#     """
#     Calculates numbers based on the given operation.
#
#     Args:
#         number_1 (int): The first number.
#         number_2 (int): The second number.
#         operation (str): The operation to perform.
#
#     Returns:
#         tuple[int, bool]: A tuple containing the result and a boolean indicating whether the result is zero.
#     """
#     response: int = 0
#
#     if operation == "+":
#         response = number_1 + number_2
#     elif operation == "-":
#         response = number_1 - number_2
#     elif operation == "*":
#         response = number_1 * number_2
#     elif operation == "/":
#         response = number_1 / number_2
#
#     return response, response == 0

# def some_function(param=[]):
#     param.append(1)
#     return param

# print(calc(1, 2, operation="*"))
# print(calc(10, 2, "-"))
# print(calc(1, 2, "+"))
# print(calc(1, 3, "+"))
# print(help(calc))
# print(some_function())
# print(some_function())
# print(some_function())
