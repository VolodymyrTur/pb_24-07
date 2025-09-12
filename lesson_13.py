#################### 10.1 ###########################
# def pow(x):
#     return x ** 2


# def some_gen(begin, end, func):
#     for _ in range(end):
#         yield begin
#         begin = func(begin)
#
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')

# def some_gen(begin, n, func):
#     count = 0
#     current = begin
#     while count < n:
#         yield current
#         current = func(current)
#         count += 1
#
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')

#################### 10.2 ###########################
# import string
#
# def first_word(text):
#     str_punc = string.punctuation.replace("'", "")
#     str_dig = string.digits
#
#     for x in text:
#         if x in str_punc or x in str_dig:
#             text = text.replace(x, " ")
#
#     text = text.strip().split()
#     return text[0]
#
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')

# def first_word(text: str) -> str:
#     """ Пошук першого слова """
#     import re
#     # return re.findall(r"[a-zA-Z']+", text)[0]
#     return re.search(r"[A-Za-z']+", text).group()
#
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')


#################### 10.3 ###########################
# def is_even(digit: int) -> bool:
#
#     return digit % 2 == 0
#
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
#
# print('OK')


# class Animal(object):
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def do_sound(self):
#         print("Doing sound")
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     def __add__(self, other):
#         return self.name + " " + other.name
#
#
# class Dog(Animal):
#     def __init__(self, name: str, age: int, breed: str):
#         super().__init__(name, age)
#         print(self.name)
#         self.breed = breed
#
#     def do_sound(self):
#         super().do_sound()
#         print("Woof")
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old, {self.breed}"
#
#
# class Cat(Animal):
#     def __init__(self, name: str, age: int, color: str):
#         super().__init__(name, age)
#         self.color = color
#
#     def do_sound(self):
#         print("Meow")
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old, {self.color}"
#
#
# d = Dog("Bob", 5, "Bulldog")
# c = Cat("Mikko", 2, "Black")
#
# print(d + c)


# class Shape:
#     def greet(self):
#         print("class shape called")
#
#
# class Shape2:
#     def greet(self):
#         print("class shape called")
#
#
# class Circle(Shape2):
#     def greet(self):
#         super().greet()
#         print("class circle called")
#
#
# class Square(Shape):
#     def greet(self):
#         super().greet()
#         print("class square called")
#
#     def some_method(self):
#         print("some method")
#
#
# class Cylinder(Square, Circle):
#     def greet(self):
#         super().greet()
#         print("class cylinder called")
#
# d = Cylinder()
# d.greet()
# print(Cylinder.mro())
# print(Cylinder.__mro__)


################# Exceptions ####################
# class MyError(Exception):
#     def __init__(self, message, num):
#         self.message = message
#         self.num = num
#
#     def __str__(self):
#         return f"{self.message} {self.num}"
#
#
# my_list = []
#
# if my_list:
#     my_list[0]
#
# try:
#     my_list[0]
#     # 1 / 0
#     # {}["name"]
#
#     if 1 != 0:
#         raise MyError("Error message", 1)
#
# except (IndexError, ZeroDivisionError) as e:
#     raise e
#
# except MyError as e:
#     print(e)
#
# else:
#     print("No errors")
#
# finally:
#     print("Finally")


# file = open("file.txt")
#
# try:
#     file.read()
#     print("File read successfully")
# except FileNotFoundError as e:
#     print(e)
#
# finally:
#     file.close()


# except ZeroDivisionError as e:
#     print(e)


# print("End")

# import time
#
# while True:
#     print("Hello")
#     time.sleep(2)

# import time
# from time import *
# from asyncio import *
# from time import sleep as time_sleep
# from asyncio import sleep as asyncio_sleep


# import math
# from math import (
#     pi,
#     e,
#     )
#
#
# # print(math.pi)
# print(pi)
# print(e)
#
# print(locals())

# from package.main import *

# from package import main_func