####################### 9.1 ########################
# def popular_words(text, words):
#     text_words = text.lower().split()
#     return {word: text_words.count(word) for word in words}
#
# assert popular_words(
#     '''When I was One I had just begun When I was Two I was nearly new ''',
#     ['i', 'was', 'three', 'near']
# ) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
#
# print("OK")


# def popular_words(text: str, words: list) -> dict:
#     res = {word: 0 for word in words}
#     res = dict.fromkeys(words, 0)
#     print(res)
#     for word in text.lower().split():
#         if word in res:
#             res[word] += 1
#
#     return res
#
#
# assert popular_words(
#     '''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']
#     ) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
#
# print('OK')


# def popular_words (text, words):
#     text_l = text.lower().split()
#     result = (text_l.count(word) for word in words)
#
#     return dict(zip(words, result))
#
# assert popular_words(
#     '''When I was One I had just begun When I was Two I was nearly new ''',
#     ['i', 'was', 'three', 'near']
#     ) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
#
# print('OK')


# def popular_words(text: str, words: list) -> dict:
#     count_lst = []
#
#     for i in words:
#         i += " "
#         count_lst.append(text.lower().count(i))
#
#     dct = dict(zip(words, count_lst))
#
#     return dct
#
#
# assert popular_words(
#     '''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']
#     ) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
#
# print('OK')


######################## 9.2 #######################
# def difference(*args):
#     if not args:
#         return 0
#
#     diff = max(args) - min(args)
#     return round(diff, 2)
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
#
# print('OK')

# def difference(*args: int | float) -> int | float:
#     diff_max_min_num = max(args) - min(args) if args else 0
#
#     return round(diff_max_min_num, 2) if diff_max_min_num % 1 else diff_max_min_num
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')


# def difference(*args) -> int:
#     if args:
#         max_num = max(args)
#         min_num = min(args)
#
#         result = round(max_num - min_num, 2)
#     else:
#         result = 0
#
#     return result
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'

# print('OK')


# def difference(*args):
#     return round(max(args) - min(args), 2) if args else 0
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
#
# print('OK')


# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hello(self):
#         print(f"Hello, {self.name}!")
#
#
# p = Person("Vova", 20)
# p2 = Person("Vasay", 20)
# print(p.age)

# p2 = Person()
# p2.age = 25
# p2.gender = "female"
# print(p2.age)
# print(p2.gender)
# print(p.gender)

# p.say_hello()
# p2.say_hello()
# print(p.name)


# Encapsulation Abstraction Inheritance Polymorphism


# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#
# person = Person("Vova", 20)
# print(person.get_age())
# # person.name = "Vasay"
# print(person._name)

# from abc import ABC, abstractmethod

# class Person(ABC):
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hello(self):
#         pass
#
#     def get_age(self):
#         raise NotImplementedError
#
#     def get_name(self):
#         pass
#
#
#
# class Man(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.gender = "male"
#
#
#     def say_hello(self):
#         print(f"Hello, I'm {self.name}!")
#
#
# class Woman(Person):
#     def __init__(self, name, age):
#         print(self.name, self.age)
#         super().__init__(name, age)
#         self.gender = "female"
#
#     def say_hello(self):
#         print(f"Hello, I'm {self.name}!")
#
#
# man = Man(name="Alex", age=32)
# woman = Woman(name="Anna", age=25)
# man.say_hello()
# woman.say_hello()


# class Car:
#     def __init__(self, brand, model, color):
#         self.brand = brand
#         self.model = model
#         self.color = color
#
#     def drive(self):
#         print("Car is drivig")
#
#
#
# class Boat:
#     def __init__(self, brand, model, color):
#         self.brand = brand
#         self.model = model
#         self.color = color
#
#     def drive(self):
#         print("Boat is sailing")



# car = Car("BMW", "5 Series", "Black")
# boat = Boat("Yamaha", "5 Series", "Blue")
#
# for vehicle in [car, boat]:
#     vehicle.drive()


# class Car:
#     def __init__(self, brand, model, color):
#         print("Init method")
#         self.brand = brand
#         self.model = model
#         self.color = color
#
#     def __new__(cls, *args, **kwargs):
#         print("New method")
#         self = super().__new__(cls)
#         return self

    # @staticmethod
    # def drive():
    #     print("Car is driving")


# car = Car("BMW", "5 Series", "Black")

# Car.drive()

# class User:
#     @staticmethod
#     def validate_email(email):
#         if "@" not in email:
#             raise ValueError("Invalid email")
#
#         print("Email is valid")


# User.validate_email("tur@mail")
# User.validate_email("some_email")

# import datetime
#
#
# class Person:
#     def __init__(self, name, age, birth_year):
#         self.birth_year = birth_year
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_age(cls, name, age):
#         current_year = datetime.datetime.now().year
#         birth_year = current_year - age
#         return cls(name, age, birth_year)
#
#
# person = Person.from_age("Alex", 32)
# print(person.name)
# print(person.age)
# print(person.birth_year)


# class Phone:
#     def __init__(self, brand, price, model):
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def __str__(self):
#         return f"Phone {self.brand} {self.model} {self.price}"
#
#     def __repr__(self):
#         return f"Phone({self.brand=}, {self.price=}, {self.model=})"
#
#
# # Створення екземплярів класу Phone
# phone1 = Phone("Apple", 10000, "iPhone 12")
# # print(phone1)
# phone2 = Phone("Samsung", 8000, "Galaxy S21")
# phone3 = Phone("Huawei", 5000, "P30 Pro")
# phone4 = Phone("Xiaomi", 7000, "Mi 12")
# phone5 = Phone("OPPO", 9000, "A5s")
#
# class Laptop:
#     def __init__(self, brand, price, model):
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def __str__(self):
#         return f"Laptop {self.brand} {self.model} {self.price}"
#
#
# class Warehouse:
#     def __init__(self, address):
#         self.address = address
#         self.storage = {}
#
#     def add_to_storage(self, item, value):
#         """Додає товар на склад"""
#         self.storage[item] = value
#
#     def remove_from_storage(self, item):
#         """Видаляє товар зі складу"""
#         return self.storage.pop(item, None)
#
#     def get_item_value(self, item):
#         """Повертає кількість товару на складі"""
#         return self.storage.get(item)
#
#     def get_total_value(self):
#         """Повертає загальну вартість товарів на складі"""
#         total_value = 0
#         for item, value in self.storage.items():
#             total_value += item.price * value
#
#         return total_value
#
#     def __str__(self):
#         """Повертає інформацію про наявність товарів на складі"""
#         tmp = ""
#         for item, value in self.storage.items():
#             tmp += f"{item}: {value} pcs.\n"
#
#         return f"Warehouse at {self.address} contains\n{tmp}"
#
#
# wh = Warehouse("Dnipro")
# # print(wh.get_total_value())  # Порожній склад
#
# # Додаємо товари на склад
# wh.add_to_storage(phone1, 11)
# wh.add_to_storage(phone2, 27)
# # print(wh.get_total_value())
# # print(wh.get_item_value(phone1))
# wh.add_to_storage(phone3, 34)
# wh.add_to_storage(phone4, 41)
# wh.add_to_storage(phone5, 50)
# # print(wh.get_total_value())
#
# laptop1 = Laptop("Apple", 80000, "MacBook Pro")
# laptop2 = Laptop("Razer", 60000, "Blade 2025")
#
# wh.add_to_storage(laptop1, 9)
# print(hash(laptop2))
# print(laptop2.__hash__())
# wh.add_to_storage(laptop2, 12)
# print(wh)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hello(self):
#         print(self)
#         return f"Hello, {self.name}!"
#
#     def get_age(self):
#         raise NotImplementedError
#
#     def get_name(self):
#         pass
#
#
# class Man(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.gender = "male"
#
#
#     def say_hello(self):
#         hello = super().say_hello()
#         print(hello)
#         return hello + "!!!!!!!!!"

#
# man = Man("Alex", 32)
# print(man.say_hello())



# Проблема "ромба"
# class Shape:
#     def draw(self):
#         print("class shape")
#
# class Circle(Shape):
#     def draw(self):
#         print("class circle")
#
# class Square(Shape):
#     def draw(self):
#         print("class square")
#
# class Cylinder(Circle, Square):
#     pass
#
# obj = Cylinder()
# obj.draw() # Resolves using the MRO
# print(Cylinder.mro())  # Displays the MRO


# class Shape:
#     def greet(self):
#         print("class shape called")
#
#
# class Circle(Shape):
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
