################## 7.1 ####################
# def say_hi(name: str, age: int) -> str:
#     return f"Hi. My name is {name} and I'm {age} years old"
#
#
# assert say_hi(name="Alex", age=32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi(name="Frank", age=68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')
import sys

################# 7.2 ######################

# def correct_sentence(text):
#     text = text[0].upper() + text[1:]
#
#     if not text.endswith("."):
#         text += "."
#
#     return text
#
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')

# def correct_sentence(text: str) -> str:
#     mod_string = text[0].upper() + text[1:] + ('.' if text[-1] != '.' else '')
#
#     return mod_string
#
# correct_sentence("Greetings, friends.")
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')


################# 7.3 ######################
# def second_index(text, some_str):
#     first_index = text.find(some_str)
#     result = None
#
#     if first_index != -1:
#         sec_ind = text.find(some_str, first_index + 1)
#
#         if sec_ind != -1:
#             result = sec_ind
#
#     return result
#
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')


# def second_index(text, some_str):
#     first = text.find(some_str)
#     if first == -1:
#         return None
#
#     second = text.find(some_str, first + 1)
#     return second if second != -1 else None
#
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')


# def second_index(text, some_str):
#     index = -1
#     count = 0
#
#     while True:
#         index = text.find(some_str, index + 1)
#         if index == -1:
#             return None
#
#         count += 1
#         if count == 2:
#             return index
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')


# import re
#
#
# def second_index(text: str, some_str: str):
#     list_index = [
#         index.start()
#         for index in re.finditer(some_str, text)
#         ]
#
#     return list_index[1] if len(list_index) > 1 else None
#
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')


########## Generators ###########
# import sys
#
#
# my_range = range(100_000_000)
#
# print(my_range)
# print(type(my_range))
# print(sys.getsizeof(my_range))
# print(sys.getsizeof(list(my_range)))

# def add_one(number):
#     print("add_one", number)
#     return number + 1
#
#
# def my_generator():
#     for i in range(100_000_000):
#         yield i
#         add_one(i)
#
#
# my_gen = my_generator()
#
# print(my_gen)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


# def my_generator():
#     x = 1
#
#     while x > 0:
#         x = yield x
#         print(f"x = {x}")
#
#         if x is None:
#             x = 0
#
#
# my_gen = my_generator()
#
# print(my_gen)
# print(next(my_gen))
# my_gen.send(10)
# print(next(my_gen))

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# my_gen = my_generator()
#
# print(my_gen)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(list(my_gen))
# # print(list(my_gen))
# print(next(my_gen))

# list_comp = [i for i in range(200000)]
# list_comp2 = (i for i in range(200000))
#
# print(type(list_comp))
# print(type(list_comp2))
#
#
# print(sys.getsizeof(list_comp))
# print(sys.getsizeof(list_comp2))

########## Speed tests ###########
# import timeit, sys
#
# RANGE = 100_000_000
#
# def test_1():
#     my_list = []
#
#     for i in range(RANGE):
#         my_list.append(i ** 2)
#
#     return my_list
#
#
# def test_2():
#     return [i ** 2 for i in range(RANGE)]
#
#
# def test_3():
#     return (i ** 2 for i in range(RANGE))
#
#
# r = test_3()
# def test_4():
#     return next(r)
#
#
# def test_5():
#     return list(map(lambda x: x ** 2, range(RANGE)))


# print(timeit.timeit(test_1, number=1))
# print(timeit.timeit(test_2, number=1))
# print(timeit.timeit(test_3, number=1))
# print(timeit.timeit(test_4, number=RANGE))
# print(timeit.timeit(test_5, number=1))

# print(sys.getsizeof(test_1()))
# print(sys.getsizeof(test_2()))
# print(sys.getsizeof(test_3()))
# print(sys.getsizeof(test_4()))


################### Замикання ####################
# from typing import Callable
#
#
# type _Power = Callable[[int], int]
#
#
# def calculate_power(n: int) -> _Power:
#
#     def raise_to_power(number: int) -> int:
#         print(locals())
#
#         return number ** n
#
#     return raise_to_power
#
# my_func = calculate_power(2)
# my_func2 = calculate_power(3)
#
# print(my_func)
#
# num_1 = my_func(2)
# num_2 = my_func2(2)
#
# print(num_1)
# print(num_2)


################## Decorators ##################
# from typing import Callable, Iterable, Any
#
#
# type _Func = Callable[..., Any]
# type _Iterable = Iterable[int]
#
# my_functions = []
#
# def my_iter(iterable: _Iterable) -> _Iterable:
#     return iterable
#
#
# my_iter = my_iter({1, 2, "3"})
#
#
# def add_function(func: _Func) -> _Func:
#     """
#     Функція приймає будьяку функцію додає її до списку my_functions
#     та повертає її
#     """
#     my_functions.append(func)
#     return func
#
#
# @add_function  # Виклик функції-декоратора
# def my_mult(a: int, b: int) -> int:  # Декорована функція
#     return a + b
#
#
# @add_function
# def my_sub(a: int, b: int) -> int:
#     return a - b
#
#
# print(my_functions)
# print(my_mult(5, 2))
# print(my_sub(5, 2))


# def my_div(a: int, b: int) -> float:
#     return a / b
#
#
# my_div = add_function(my_div)
#
# print(my_div(6, 2))
#
# @add_function
# def my_div(a: int, b: int) -> float:
#     return a / b
#
#
# print(my_div(6, 2))
# print(my_functions)


# from typing import Callable
#
# type _Func = Callable[..., str]
#
# def to_str(func: _Func) -> _Func:
#
#     def wrapper(*args, **kwargs) -> str:
#         return str(func(*args, **kwargs))
#
#     return wrapper
#
#
# @to_str
# def my_sum(a: int, b: int) -> int:
#     return a + b
#
#
# result = my_sum(1, 2)
# print(my_sum, result, type(result))


# def my_decorator(func: Callable[..., int]) -> Callable[..., int]:
#     """My Decorator"""
#
#     print("before wrapper")
#
#     def wrapper(*args, **kwargs) -> int:
#         """Wrapper"""
#         print(f"name: {func.__name__}, args: {args}, kwargs: {kwargs}")
#         print("before function")
#         kwargs["number"] /= 2
#         my_function = func(*args, **kwargs) ** 2
#         print("after function")
#         return my_function
#
#     print("after wrapper")
#
#     return wrapper
#
#
# def my_decorator2(func: Callable[..., int]) -> Callable[..., int]:
#     """My Decorator"""
#
#     print("before wrapper2")
#
#     def wrapper(*args, **kwargs) -> int:
#         """Wrapper"""
#         print(f"name: {func.__name__}, args: {args}, kwargs: {kwargs}")
#         print("before function2")
#         kwargs["number"] *= 2
#         my_function = func(*args, **kwargs) ** 2
#         print("after function2")
#         return my_function
#
#     print("after wrapper2")
#
#     return wrapper
#
# @my_decorator2
# @my_decorator
# def my_func(number: int) -> int:
#     """My Function"""
#     return number
#
#
# print(my_func(number=10))
# print(my_func)

# print(my_func.__name__, my_func.__doc__)  # Імʼя та документація функції


# def my_decorator(func: Callable[..., int]) -> Callable[..., int]:
#     """My Decorator"""
#     def wrapper(*args, **kwargs) -> int:
#         """Wrapper"""
#         print(f"name: {func.__name__}, args: {args}, kwargs: {kwargs}")
#         return func(*args, **kwargs)
#
#     # Встановлюємо значення для функції wrapper, які були у декорованої функції
#     wrapper.__module__ = func.__module__
#     wrapper.__name__ = func.__name__
#     wrapper.__doc__ = func.__doc__
#
#     return wrapper
#
#
# @my_decorator
# def my_func(number: int) -> int:
#     """My Function"""
#     return number
#
# print(my_func.__name__, my_func.__doc__)  # Імʼя та документація функції

# import functools
#
#
# def my_decorator(func: Callable[..., int]) -> Callable[..., int]:
#     """My Decorator"""
#     def wrapper(*args, **kwargs) -> int:
#         """Wrapper"""
#         print(f"name: {func.__name__}, args: {args}, kwargs: {kwargs}")
#         return func(*args, **kwargs)
#
#     # Встановлюємо значення для функції wrapper, які були у декорованої функції
#     # за допомогою модуля functools
#     functools.update_wrapper(wrapper, func)
#
#     return wrapper
#
#
# @my_decorator
# def my_func(number: int) -> int:
#     """My Function"""
#     return number
#
# print(my_func.__name__, my_func.__doc__)  # Імʼя та документація функції


# import functools
#
#
# def my_decorator(func: Callable[..., int]) -> Callable[..., int]:
#     """My Decorator"""
#     # Встановлюємо значення для функції wrapper, які були у декорованої функції
#     # за допомогою декоратора з модуля functools
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs) -> int:
#         """Wrapper"""
#         print(f"name: {func.__name__}, args: {args}, kwargs: {kwargs}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @my_decorator
# def my_func(number: int) -> int:
#     """My Function"""
#     return number
#
# print(help(my_func))
# print(my_func.__name__, my_func.__doc__)  # Імʼя та документація функції
