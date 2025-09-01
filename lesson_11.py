################ 8.1 #######################
# def add_one(some_list: list[int]) -> list[int]:
#     some_list_to_num_plus_one = int(''.join(str(num) for num in some_list)) + 1
#     num_to_mod_list_int = [
#         int(item)
#         for item in str(some_list_to_num_plus_one)
#         ]
#
#     return num_to_mod_list_int
#
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")


# def add_one(some_list):
#     number = int("".join(map(str, some_list)))
#     number += 1
#     return [int(digit) for digit in str(number)]
#
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")

###################### 8.2 ###################

# import string
#
#
# def is_palindrome(text: str) -> bool:
#     mod_string = (
#         ''.join(
#             item
#             for item in text
#             if item not in string.punctuation
#         )
#         .lower()
#         .replace(' ', '')
#     )
#
#     reversed_string = mod_string[::-1]
#
#     return mod_string == reversed_string
#
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")


# import string
#
#
# def is_palindrome(text):
#     text = text.lower()
#
#     for ch in string.punctuation:
#         text = text.replace(ch, "")
#
#     text = text.replace(" ", "")
#     return text == text[::-1]
#
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")


# from string import punctuation
# from copy import deepcopy
#
#
# def is_palindrome(text: str) -> bool:
#     for i in punctuation:
#         text = text.replace(i, "")
#
#     text = text.lower().split()
#     text = "".join(text)
#     text_lst = list(text)
#
#     reversed_text = deepcopy(text_lst)
#     reversed_text = text_lst.copy()
#     reversed_text.reverse()
#
#     return text_lst == reversed_text
#
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
#
# print("ОК")


# import string
#
# def is_palindrome(text):
#     clean_text = text.translate(str.maketrans('', '', string.punctuation + " ")).lower()
#     # clean_text = clean_text.replace(' ', '').lower()
#     return clean_text == clean_text[::-1]
#
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

################### 8.3 ############################
# def find_unique_value(some_list: list) -> int | None:
#     """
#     This function finds the first unique value in the given list.
#
#     Args:
#         some_list: A list to find the first unique value in.
#
#     Returns:
#         int: The first unique value in the given list.
#         None: The list is empty.
#     """
#
#     unique_num_list = [
#         num
#         for num in some_list
#         if some_list.count(num) == 1
#     ]
#
#     return unique_num_list[0] if unique_num_list else None
#
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# assert find_unique_value([3, 4, 5, 6]) == 3, 'Test4'
# assert find_unique_value([3, 3, 3]) is None, 'Test5'
# print("ОК")

#
# def find_unique_value(some_list):
#     for ch in some_list:
#         if some_list.count(ch) == 1:
#             return ch
#
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")


# def sum_num(lst):
#     total = 0 # Одна змінна => O(1)
#     for num in lst:
#         total += num
#     return total
#
# print(sum_num([1, 2, 3, 4, 5]))


# def copy_list(lst):
#     return lst.copy() # створювати повну копію => O(n)
#
# nums = [1, 2, 3, 4, 5]
# new_nums = copy_list(nums)
# print(new_nums)

# def adj_matrix(n):
#     matrix = [[0] * n for _ in range(n)] # Матриця n * n => O(n2)
#     return matrix
#
# size = 5
# matrix = adj_matrix(size)
# for row in matrix:
#     print(row)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             print(arr[j], arr[j + 1], end=" _ ")
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             print(arr)
#
#         print("----" * 4)
#
# # Приклад використання
# my_list = [64, 34, 25, 12, 22, 11, 90, 38]
# bubble_sort(my_list)
# print("Відсортований масив:", my_list)

# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid  # Повертає індекс знайденого елемента
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return -1  # Повертає -1, якщо елемент не знайдено
#
# # Приклад використання
# my_list = [11, 12, 22, 25, 34, 64, 90]
# result = binary_search(my_list, 22)
# print("Індекс шуканого елемента:", result)


################## Files #####################

# filename = "test.txt"
# file = open(filename, "w")  # r, w, a

# file.write("Hello\n")
# file.write("Hello\n")
# file.write("Hello\n")
# file.write("Hello")
# file.write("Hello")

# strings = ["Hello1\n","Hello1", "\n","Hello1\n","Hello1\n",]

# file.writelines(strings)
#
# file.close()

# with open(filename, "w+") as file:
#     file.writelines(strings)
#     lines = file.readlines()
#     for line in lines:
#         print(line)


# with open(filename +"8", "r") as file:
    # lines = file.readlines()
    # file.seek(4)
    # lines = file.read()
    # for line in lines:
    #     print(line, end="")

    # print(lines)


# with open(filename, "a") as file:
#     file.write("Hello\n")
#     file.write("Hello\n")
#     file.write("Hello\n")
#     file.write("Hello")
#     file.write("Hello")


################# OOP #################

# class Car:
#     color = "RED"
#     make = "Mazda"
#
#     def status(self, broken: bool):
#
#         return "OK" if not broken else "FAILED"
#
#     def get_make(self):
#         print(self.status(True))
#         return self.make
#
#
# car = Car()
# print(car.color)
# print(car.make)
# print(car.status(True))
# print(car.status(False))
# print(car.get_make())
#
# print()
#
# car_2 = Car()
# car_2.color = "BLUE"
# car_2.body = "Sedan"
#
# print(car_2.color)
# print(car_2.make)
# print(car_2.body)
# print(car_2.status())
