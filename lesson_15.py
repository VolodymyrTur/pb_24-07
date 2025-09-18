##################### 13.1 ####################
# class Human:
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"Name: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}"
#
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return f"{super().__str__()}, Record Book: {self.record_book}"
#
#
# class Group:
#
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         self.group.add(student)
#
#     def delete_student(self, last_name):
#         self.group.discard(self.find_student(last_name))
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = '\n'.join(map(str, self.group))
#         return f'Group Number: {self.number}\n{all_students}'

##################### 13.2 ####################
# class Counter:
#
#     def __init__(self, current=1, min_value=0, max_value=10):
#         self.current = current
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def set_current(self, start):
#         self.current = start
#
#     def set_max(self, max_max):
#         self.max_value = max_max
#
#     def set_min(self, min_min):
#         self.min_value = min_min
#
#     def step_up(self):
#         if self.current == self.max_value:
#             raise ValueError('Max value exceeded')
#         self.current += 1
#
#     def step_down(self):
#         if self.current == self.min_value:
#             raise ValueError('Min value exceeded')
#         self.current -= 1
#
#     def get_current(self):
#         return self.current


#################### 14.1 #######################
# class LimitGroupError(Exception):
#
#     def __init__(self, message="У групі не може бути більше 10 студентів!"):
#         self.message = message
#         super().__init__(self.message)
#
#
# class Human:
#
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"Name: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}"
#
#
# class Student(Human):
#
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return f"{super().__str__()}, Record Book: {self.record_book}"
#
#
# class Group:
#
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         if len(self.group) >= 10:
#             raise LimitGroupError(f"Unable to add {student.first_name} {student.last_name} to Group: {self.number}."
#                                   f" There are already {len(self.group)} students in this group.")
#             # raise LimitGroupError
#         self.group.add(student)
#
#     def delete_student(self, last_name):
#         self.group.discard(self.find_student(last_name))
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = '\n'.join(map(str, self.group))
#         return f'Group Number: {self.number}\n{all_students}'



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
#     def __str__(self):
#         return f"Cat(name={self.name}, age={self.age}, color={self.color})"
#
#     def __getattribute__(self, item):
#         print(f"__getattribute__({item})")
#         try:
#             return object.__getattribute__(self, item)
#         except AttributeError:
#             if item == "type":
#                 return "Stray Cat"
#             print(item)
#             return None
#
#
# cat = Cat("Vasyl", 2, "Black")
# # print(cat.name)
# print(cat.type)


# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f"Cat(name={self.name}, age={self.age}, color={self.color})"
#
#     def __getattribute__(self, item):
#         print(f"__getattribute__({item})")
#         return object.__getattribute__(self, item)
#
#     def __getattr__(self, item):
#         print(f"__getattr__({item})")
#         if item == "type":
#             return "Stray Cat"
#         return None
#
#
# cat = Cat("Vasyl", 2, "Black")
# print(cat.name)
# print(cat.type)
# print(cat.bread)

# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f"Cat(name={self.name}, age={self.age})"
#
#     def __getattribute__(self, item):
#         return object.__getattribute__(self, item)

    # def __setattr__(self, key, value):
    #     print(f"__setattr__({key, value})")
    #     if key == "name":
    #         self.__dict__[key] = value + "!!"
    #     else:
    #         self.__dict__[key] = value


# cat = Cat("Vasyl", 2, "Black")
# print(cat.__dict__)
# cat.bread = "Siamese"

# print(cat.__dict__)


# import math
#
#
# setattr(math, "my_value", 12345)
# print(math.my_value)

# my_list = ["name", "age", "color"]
# my_dict = {
#     "name": "Murchik",
#     "age": 20,
#     "color": "white",
# }

# for key in my_list:
#     print(getattr(cat, key))

# print(cat)
# for key, value in my_dict.items():
#     setattr(cat, key, value)
#
# print(cat)


# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f"Cat(name={self.name}, age={self.age}, color={self.color})"
#
#     def __getattribute__(self, item):
#         return object.__getattribute__(self, item)
#
#     def __getattr__(self, item):
#         print(f"__getattr__({item})")
#         if item == "type":
#             return "Stray Cat"
#         return None
#
#     def __setattr__(self, key, value):
#         print(f"__setattr__({key, value})")
#         self.__dict__[key] = value
#
#     def __delattr__(self, item):
#         print(f"__delattr__({item})")
#         del self.__dict__[item]
#

# cat = Cat("Vasyl", 2, "Black")
# cat.bread = "Siamese"
# print(cat.type)
# print(cat.__dict__)
# del cat.bread
# print(cat.__dict__)
#
# delattr(cat, "name")








# property

# class Cat:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.age = age
#         self.color = color
#
#     def get_name(self):
#         print("get_name")
#         return self.__name
#
#     def set_name(self, value):
#         print("set_name")
#         self.__name = value
#
#     def del_name(self):
#         print("del_name")
#         del self.__name
#
#     name = property(get_name, set_name, del_name, "Name of the cat")
#
#     def __str__(self):
#         return f"Cat(name={self.__name}, age={self.age}, color={self.color})"
#
#
# cat = Cat("Vasyl", 2, "Black")
# print(cat.name)
# cat.name = "Murchik"
# print(cat.name)


# class Cat:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.age = age
#         self.color = color
#
#     name = property(doc="Name of the cat")
#
#     @name.getter
#     def get_name(self):
#         print("get_name")
#         return self.__name
#
#     @name.setter
#     def set_name(self, value):
#         print("set_name")
#         self.__name = value
#
#     @name.deleter
#     def del_name(self):
#         print("del_name")
#         del self.__name
#
#
#     def __str__(self):
#         return f"Cat(name={self.__name}, age={self.age}, color={self.color})"
#
#
# cat = Cat("Vasyl", 2, "Black")
# print(cat.name)
# cat.name = "Murchik"
# print(cat.name)

# class Cat:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.age = age
#         self.color = color
#
#     @property
#     def name(self):
#         return self.__name
#
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#
#     def __str__(self):
#         return f"Cat(name={self.__name}, age={self.age}, color={self.color})"
#
#
# cat = Cat("Vasyl", 2, "Black")
# print(cat.name)
# cat.name = "Murchik"
# print(cat.name)

# from functools import cached_property
#
# class Human:
#     def __init__(self, first_name, last_name, age, gender, height, weight):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#
#     def show_info(self):
#         full_name = f"Full name is {self.full_name}\n"
#         gender_age = f"Gender is {self.gender}\nAge is {self.age}\n"
#         height_weight = f"Height is {self.height} cm\nWeight is {self.weight} kg\n"
#         return full_name + gender_age + height_weight
#
#     # @property  # cached_property
#     @cached_property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     @property
#     def short_full_name(self):
#         return f"{self.last_name} {self.first_name[0]}."
#
# human = Human("Jon", "Dou", 20, "Male", 170, 60)
#
# # print(human.full_name)
# # print(human.show_info())
# print(human.short_full_name)
# print(human.last_name)


# Descriptors



# class MyDescriptor:
#     def __init__(self, value):
#         self.value = value
#
#     def __get__(self, instance_self, instance_class):
#         print(self)
#         print(instance_self)
#         print(instance_class)
#         return self.value * instance_self.p
#
#
# class Box:
#     volume = MyDescriptor(2)
#
#     def __init__(self, width, height, depth):
#         self.p = width * height * depth
#
#
# box = Box(1, 2, 3)
# # print(box.volume)
# box.volume = 4
# print(box.volume)

# class MyDescriptor:
#     def __init__(self, value):
#         self.value = value
#
#     def __get__(self, instance_self, instance_class):
#         return self.value * instance_self.p
#
#     def __set__(self, instance_self, value):
#         raise AttributeError("Can't set value")
#
#
# class Box:
#     volume = MyDescriptor(2)
#
#     def __init__(self, width, height, depth):
#         self.p = width * height * depth
#
# box = Box(1, 2, 3)
# print(box.volume)
# box.volume = 4
# print(box.volume)
#
# class ProtectedField:
#     def __init__(self, field):
#         self.field = field
#
#     def __get__(self, instance_self, instance_class):
#         field = f"_{instance_class.__name__}{self.field}"
#         return getattr(instance_self, field)
#
#
# class Cat:
#     name = ProtectedField("__name")
#     age = ProtectedField("__age")
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#
# cat = Cat("Vasyl", 2)
# # print(cat.__name)  # Буде помилка
# # print(cat._Cat__name)  # Доступ до захищеного поля
# # # Доступ за допомогою дескриптора
# print(cat.name)
# print(cat.age)
#
# cat.name = "Tom"
# print(cat.name)

# class ProtectedField:
#     def __init__(self, field):
#         self.field = field
#
#     def __get__(self, instance_self, instance_class):
#         field = f"_{instance_class.__name__}{self.field}"
#         return getattr(instance_self, field)
#
#     def __set__(self, instance_self, value):
#         # instance_class не передається як у методі __get__
#         instance_class = instance_self.__class__
#         field = f"_{instance_class.__name__}{self.field}"
#         setattr(instance_self, field, value)
#
#
# class Cat:
#     name = ProtectedField("__name")
#     age = ProtectedField("__age")
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
# cat = Cat("Vasyl", 2)
# print(cat.name)

# class ProtectedField:
#     def __init__(self, field):
#         self.field = field
#
#     def __get__(self, instance_self, instance_class):
#         field = f"_{instance_class.__name__}{self.field}"
#         return getattr(instance_self, field)
#
#     def __set__(self, instance_self, value):
#         # instance_class не передається як у методі __get__
#         instance_class = instance_self.__class__
#         field = f"_{instance_class.__name__}{self.field}"
#         setattr(instance_self, field, value)
#
#     def __delete__(self, instance_self):
#         instance_class = instance_self.__class__
#         field = f"_{instance_class.__name__}{self.field}"
#         delattr(instance_self, field)
#
#     # def __delete__(self, instance_self):
#     #     raise AttributeError("Can't be deleted")
#
#
# class Cat:
#     name = ProtectedField("__name")
#     age = ProtectedField("__age")
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
# cat = Cat("Vasyl", 2)
# print(cat.name)
# del cat.name

# class PositiveValue:
#     def __init__(self):
#         self.value = None
#
#     def __get__(self, instance_self, instance_class):
#         return self.value
#
#     def __set__(self, instance_self, value):
#         if value < 0:
#             raise ValueError("Value must be positive")
#         self.value = value
#
# class Box:
#     weight = PositiveValue()
#     height = PositiveValue()
#     length = PositiveValue()
#
#     def __init__(self, weight, height, length):
#         self.weight = weight
#         self.height = height
#         self.length = length

# box = Box(1, 2, -3)
# box = Box(1, 2, 3)
# box.weight = -1


# Ітератори

# class Sequence:
#     def __init__(self, number):
#         self.number = number
#
#     def __getitem__(self, index):
#         if index < self.number:
#             return index ** 2
#
#         raise IndexError("Index out of range")
#
#     def __len__(self):
#         return self.number
#
#
# seq = Sequence(10)
# for item in range(len(seq)):
#     print(seq[item])











# # Отримання елементу за індексом
# print(seq[6])
# # Відтворення елементів у вигляді списку
# print(list(seq))
# # Алє зрізи не працюють
# print(seq[6:10])


# a = [1, 2, 3, 4, 5]
# b = a[1:4]
# print(b)

# _slice = slice(1, 4)
# print(_slice)
# print(_slice.start)
# print(_slice.stop)
# print(_slice.step)
# print(a[_slice])

# print(a[slice(1, None)])
# print(a[1:])
# print(a[slice(None, 4)])
# print(a[:4])
# print(a[slice(None, None, 2)])
# print(a[::2])

# class Sequence:
#     def __init__(self, number):
#         self.number = number
#
#     def __getitem__(self, index):
#         # перевірка що index є обʼєктом зрізу
#         if isinstance(index, slice):
#             # перевірка коректності значень
#             if index.start and index.start < 0:
#                 raise IndexError
#             elif index.stop and index.stop > self.number:
#                 raise IndexError
#
#             result = []
#             # встановлення коректних значень
#             start = 0 if index.start is None else index.start
#             stop = self.number if index.stop is None else index.stop
#             reverse = False
#
#             # якщо значення кроку відʼємне, значить буде перевернуто послідовність
#             if index.step and index.step < 0:
#                 reverse = True
#                 step = index.step * (-1)
#
#             else:
#                 step = 1 if index.step is None else index.step
#
#             # формування послідовності
#             for i in range(start, stop, step):
#                 result.append(i ** 2)
#
#             # перевертаємо послідовність, якщо треба
#             return list(reversed(result)) if reverse else result
#
#         if isinstance(index, int):
#             if index < self.number:
#                 return index ** 2
#             else:
#                 raise IndexError
#
#         raise TypeError
#
#     def __len__(self):
#         return self.number


# iter()
# next()

# a = "Hello"
#
# b = a.__iter__()
# # print(type(b))
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())

# class Goods:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __repr__(self):
#         return f"Goods(name='{self.name}', price={self.price})"
#
#     def __str__(self):
#         return f"{self.name} - {self.price}"


# class Basket:
#     def __init__(self, user):
#         self.user = user
#         self.goods = list()
#
#     def add_goods(self, good):
#         self.goods.append(good)
#
#     def __str__(self):
#         result = f"User: {self.user}\n"
#         for goods in self.goods:
#             result += f"{goods}\n"
#         return result
#
#
# basket = Basket("Vova's basket")
#
# apple = Goods("Apple", 10)
# banana = Goods("Banana", 5)
#
# basket.add_goods(apple)
# basket.add_goods(banana)
#
# print(basket)
# for goods in basket:
#     print(goods)

# class BasketIterator:
#     def __init__(self, goods):
#         self.goods = goods
#         self.index = 0
#
#     def __next__(self):
#         if self.index < len(self.goods):
#             result = self.goods[self.index]
#             self.index += 1
#             return result
#         raise StopIteration
#
#     def __iter__(self):
#         return self
#
#
# class Basket:
#     def __init__(self, user):
#         self.user = user
#         self.goods = list()
#
#     def add_goods(self, good):
#         self.goods.append(good)
#
#     def __str__(self):
#         result = f"User: {self.user}\n"
#         for goods in self.goods:
#             result += f"{goods}\n"
#         return result
#
#     def __iter__(self):
#         return iter(self.goods)
#
#
# basket = Basket("Vova's basket")
#
# apple = Goods("Apple", 10)
# banana = Goods("Banana", 5)
#
# basket.add_goods(apple)
# basket.add_goods(banana)

# print(basket)
# for goods in basket:
#     print(goods)

# iter_basket = iter(basket)
# print(next(iter_basket))
# print(next(iter_basket))
# print(next(iter_basket))

# mango = Goods("Mango", 15)
# basket.add_goods(mango)
#
#
# while True:
#     try:
#         print(next(iter_basket))
#     except StopIteration:
#         print("End of basket")
#         break
#
# print()
# for i in basket:
#     print(i)
# else:
#     print("End of basket")