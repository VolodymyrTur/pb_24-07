######################### 11.1 #################
# from inspect import isgenerator
# from typing import Generator
#
#
# def prime_generator(end: int) -> Generator[int, None, None]:
#     for num in range(2, end + 1):
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             yield num
#
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')

# def prime_generator(end):
#
#     def is_prime(n):
#         if n < 2:
#             return False
#
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#
#         return True
#
#     for num in range(2, end + 1):
#         if is_prime(num):
#             yield num
#
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
#
# print('Ok')

# import sympy
# def prime_generator(end):
#
#     return sympy.primerange(2, end + 1)
#
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')

########################## 11.2 ############################
# def generate_cube_numbers(end):
#     n = 2
#     while True:
#         cube = n ** 3
#
#         if cube > end:
#             return
#
#         yield cube
#         n += 1
#
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
#
# print("OK")

# from inspect import isgenerator
# from typing import Generator
#
#
# def generate_cube_numbers(end: int) -> Generator[int, None, None]:
#     i = 2
#     while i ** 3 <= end:
#         yield i ** 3
#         i += 1
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
# print("OK")

########################## 11.3 ############################
# def is_even(number):

    # return (number & 1) == 0

# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
#
# print("OK")

# 101
# 001
#
# 001

# def is_even(number: int) -> bool:
#     ##################  Option #1  ###################
#     list_last_digit_even = [0, 2, 4, 6, 8]
#
#     last_digit_in_num = int(str(number)[-1])
#
#     return last_digit_in_num in list_last_digit_even

    #################  Option #2  ####################
    # return not number & 1


# assert is_even(2494563894038 ** 2) == True, 'Test1'
# assert is_even(1056897 ** 2) == False, 'Test2'
# assert is_even(24945638940387 ** 3) == False, 'Test3'
# print('OK')

# def is_even(number: int) -> bool:
#     # return str(number)[-1] in "02468"
#     return str(number).endswith(('0', '2', '4', '6', '8'))
#
#
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
#
# print("OK")

############################### 12.1 ########################
# import codecs
# import re
#
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as in_file:
#         cleaned_html = re.sub(r'<[^>]+>', '', in_file.read())
#         text_without_empty_line = "\n".join(
#             line.strip()
#                 for line in cleaned_html.splitlines()
#                     if line.strip()
#         )
#
#     with codecs.open(result_file, 'w', 'utf-8') as out_file:
#         out_file.write(text_without_empty_line)
#
#
# delete_html_tags('draft.html', 'my_cleaned.txt')

# import codecs
#
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#       with codecs.open(html_file, 'r', 'utf-8') as file:
#            html = file.read()
#
#       cleaned_text = ""
#       ins_tag = False
#
#       for ch in html:
#           if ch == "<":
#               ins_tag = True
#
#           elif ch == ">":
#               ins_tag = False
#               continue
#
#           cleaned_text += ch if not ins_tag else ""
#
#       with codecs.open(result_file, 'w', 'utf-8') as file:
#           file.write(cleaned_text)
#
# delete_html_tags('draft.html')

############################## 12.2 ############################
# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name} prise: {self.price}"
#
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def __str__(self):
#         info = [f"User: {self.user}"]
#
#         for key, value in self.products.items():
#             info.append(f"{key}, {value} pcs.")
#
#         return "\n".join(info)
#
#     def get_total(self):
#         total = 0
#
#         for key, value in self.products.items():
#             total += key.price * value
#
#         self.total = total
#         return self.total
#
#     def get_total(self):
#         self.total = sum(
#             item.price * cnt
#             for item, cnt in self.products.items()
#         )
#         return self.total

############## imports ###################

# from package.main import main_func
#
# main_func()

# Послідовність імпортів
# 1. Вбудовані (sys, time)
# 2. Стандартні бібліотеки (math, random)
# 3. Сторонні бібліотеки (pip, poetry, uv)
# 4. Власні модулі та пакети

# import sys
#
# print(sys.builtin_module_names)

# import random
#
# print(random.__name__)
# print(random.__doc__)
# print(random.__file__)

# import requests

######################## Polymorphism #######################

# +, -, *, /, %, **


# __add__, __iadd__, __radd__ Складання чи конкатенація (+)
# __sub__, __isub__, __rsub__ Віднімання (-)
# __mul__, __imul__, __rmul__ Множення (*)
# __truediv__, __itruediv__, __rtruediv__ Справжнє ділення (/)
# __floordiv__, __ifloordiv__, __rfloordiv__ Ділення з округленням (%)
# __pow__, __ipow__, __rpow__ Зведення у ступінь (**)


# class Box:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __add__(self, other):
#         return Box(self.width + other.width, self.height + other.height, self.depth + other.depth)
#
#     def __str__(self):
#         return f"Box({self.width}, {self.height}, {self.depth})"
#
#
# box1 = Box(1, 2, 3)
# box2 = Box(4, 5, 6)
# box3 = box1 + box2
# print(box1)
# print(box3)
#
# box1 += box2
# box1 += 1

# print(box1)


# class Box:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.width + other.width, self.height + other.height, self.depth + other.depth)
#         raise NotImplementedError
#
#     # def __iadd__(self, other):
#     #     if isinstance(other, Box):
#     #         print("iadd")
#     #         return Box(self.width + other.width, self.height + other.height, self.depth + other.depth)
#     #     raise NotImplementedError
#
#     def __str__(self):
#         return f"Box({self.width}, {self.height}, {self.depth})"
#
#
# box1 = Box(1, 2, 3)
# box2 = Box(4, 5, 6)
# box3 = box1 + box2
# # print(box3)
#
# box1 += box2
# # box1 += 1
#
# print(box1)

# class Box:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.width + other.width, self.height + other.height, self.depth + other.depth)
#
#         if isinstance(other, (int, float)):
#             print("add")
#             return Box(self.width + other, self.height + other, self.depth + other)
#
#         raise NotImplementedError
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __str__(self):
#         return f"Box({self.width}, {self.height}, {self.depth})"
#
#
# box1 = Box(1, 2, 3)
# # box2 = box1 + 10
# # print(box2)
# #
# box3 = 10 + box1
# print(box3)

# class Box:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.width + other.width, self.height + other.height, self.depth + other.depth)
#
#         if isinstance(other, (int, float)):
#             print("add")
#             return Box(self.width + other, self.height + other, self.depth + other)
#
#         raise NotImplementedError
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __radd__(self, other):
#         # self -- Об'єкт екземпляра класу Box
#         # other -- Операнд, який стоять в лівій частині виразу
#         print("radd")
#         return Box.__add__(self, other)
#
#     def __str__(self):
#         return f"Box({self.width}, {self.height}, {self.depth})"
#
#
# box1 = Box(1, 2, 3)
# box2 = box1 + 10
# print(box1)
#
# box3 = 10 + box1
# print(box3)






# __eq__ Дорівнює ==
# __ne__ Не дорівнює !=
# __lt__ Менше <
# __le__ Менше або дорівнює <=
# __gt__ Більше >
# __ge__ Більше або дорівнює >=














# class Box:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def square(self):
#         return self.width * self.height * self.depth
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.width + other.width, self.height + other.height, self.depth + other.depth)
#
#         if isinstance(other, (int, float)):
#             print("add")
#             return Box(self.width + other, self.height + other, self.depth + other)
#
#         raise NotImplementedError
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __radd__(self, other):
#         # self -- Об'єкт екземпляра класу Box
#         # other -- Операнд, який стоять в лівій частині виразу
#         print("radd")
#         return Box.__add__(self, other)
#
#     def __str__(self):
#         return f"Box({self.width}, {self.height}, {self.depth})"
#
#     def __eq__(self, other):
#         if isinstance(other, Box):
#             return self.square() == other.square()
#         raise NotImplementedError
#
#     def __gt__(self, other):
#         if isinstance(other, Box):
#             return self.square() > other.square()
#         raise NotImplementedError
#
#     def __lt__(self, other):
#         if isinstance(other, Box):
#             return self.square() < other.square()
#         raise NotImplementedError
#
# box1 = Box(1, 2, 3)
# box2 = Box(4, 5, 6)
#
# print(box1 == box2)
# print(box1 > box2)
# print(box1 < box2)

# print(box1 >= box2)





















# class Box:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def square(self):
#         return self.width * self.height * self.depth
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.width + other.width, self.height + other.height, self.depth + other.depth)
#
#         if isinstance(other, (int, float)):
#             print("add")
#             return Box(self.width + other, self.height + other, self.depth + other)
#
#         raise NotImplementedError
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __radd__(self, other):
#         # self -- Об'єкт екземпляра класу Box
#         # other -- Операнд, який стоять в лівій частині виразу
#         print("radd")
#         return Box.__add__(self, other)
#
#     def __str__(self):
#         return f"Box({self.width}, {self.height}, {self.depth})"
#
#     def __eq__(self, other):
#         if isinstance(other, Box):
#             return self.square() == other.square()
#         raise NotImplementedError
#
#     def __gt__(self, other):
#         if isinstance(other, Box):
#             return self.square() > other.square()
#         raise NotImplementedError
#
#     def __lt__(self, other):
#         if isinstance(other, Box):
#             return self.square() < other.square()
#         raise NotImplementedError
#
#     def __ge__(self, other):
#         if isinstance(other, Box):
#             return self.square() >= other.square()
#         raise NotImplementedError
#
#     def __le__(self, other):
#         if isinstance(other, Box):
#             return self.square() <= other.square()
#         raise NotImplementedError
#
#     def __ne__(self, other):
#         if isinstance(other, Box):
#             return self.square() != other.square()
#         raise NotImplementedError
#
#
# box1 = Box(1, 2, 3)
# box2 = Box(4, 5, 6)
#
# print(f"{box1.square()} == {box2.square()}", box1 == box2)
# print(f"{box1.square()} > {box2.square()}", box1 > box2)
# print(f"{box1.square()} < {box2.square()}", box1 < box2)
# print(f"{box1.square()} >= {box2.square()}", box1 >= box2)
# print(f"{box1.square()} <= {box2.square()}", box1 <= box2)
# print(f"{box1.square()} != {box2.square()}", box1 != box2)


























###################### Incapsulation #######################

# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.__color = color
#
#     @staticmethod
#     def do_sound():
#         print("Meow")
#
#     def __str__(self):
#         return f"Cat(name={self.name}, age={self.age}, color={self.__color})"
#
#
# cat = Cat("Vasyl", 2, "Black")
# print(cat)
# print(cat.do_sound())
# # print(cat.__color)
# cat._Cat__color = "White"
# print(cat._Cat__color)










# __dict__
# __slots__



# class Cat:
#     __slots__ = ("name", "age", "color")
#
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     @staticmethod
#     def do_sound():
#         print("Meow")
#
#     def __str__(self):
#         return f"Cat(name={self.name}, age={self.age}, color={self.color})"
#
#
# cat = Cat("Vasyl", 2, "Black")
# # cat.bread = "Siamese"
# print(cat)
# cat.age = 3
# print(cat)



# __getattribute__ - викликається автоматично при спробі набути значення певного або невизначеного (відсутнього) поля класу.
# __getattr__ - викликається автоматично при спробі отримати значення невизначеного поля класу.
# __setattr__ - викликається при спробі надати значення будь-якому полю класу (певного та невизначеного)
# __delattr__ – викликається при видаленні поля.





# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     @staticmethod
#     def do_sound():
#         print("Meow")
#
#     def __str__(self):
#         return f"Cat(name={self.name}, age={self.age}, color={self.color})"
#
#
#     # def __getattribute__(self, item):
#     #     print(f"__getattribute__({item})")
#     #     try:
#     #         return super().__getattribute__(item)
#     #     except AttributeError:
#     #         pass
#
#     def __getattribute__(self, item):
#         print(f"__getattribute__({item})")
#         return super().__getattribute__(item)
#
#     def __getattr__(self, item):
#         print(f"__getattr__({item})")
#         return None
#
#
# cat = Cat("Vasyl", 2, "Black")
# # print(cat.name)
# # print(cat.name1)
#
# # print(getattr(cat, "name"))
# # print(hasattr(cat, "name"))
#
# setattr(cat, "age4", 4)
# print(cat.age4)
