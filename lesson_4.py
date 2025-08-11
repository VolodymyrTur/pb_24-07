# from copy import deepcopy
# my_list = [1, 2, 3, 4, 5, 4, 0]
# my_list2 = ["apple", "banana", "orange", "onion"]
# my_list2.sort()
# print(my_list2)
# my_copy = my_list.copy()
# my_copy = deepcopy(my_list)

# my_string = "hello"
# my_list2 = [1, 2, 3, 4, 5]
# print(my_list[::2])
# print(my_list)
# my_list = my_list.append(6) # None
# my_list.extend([[7, 8, 9]])
# print(id(my_list))
# my_list.sort(reverse=True)
# print(id(my_list))
# sorted_list = sorted(my_list, reverse=True)
# my_list.remove(4)
# my_list.reverse()
# print(my_list[::-1])

# my_list[-1].insert(0, 2)
# my_list.insert(7, "hello")
# my_list.insert(7, "hello1")
# my_list.insert(7, "hello2")
# my_list.insert(7, "hello3")
# my_list.insert(7, "hello4")
# ind = my_list.pop(2)
# del my_list[2]
# print(my_list2 + [[7, 8, 9]])
# print(my_list)
# print(list(my_string).count("l"))

# print(id(sorted_list))
# print(my_copy)
# print(ind)

# some_string = "blue1"

# if some_string == "red":

# match some_string:
#     case "red":
#         print("some_string is red")
#     case "blue":
#         print("some_string is blue")
#     case _:
#         print("some_string is not red or blue")

# if some_string == "red" or "blue":
#     print("+++++++++++++++++++++")
# else:
#     print("##################")

# if len(my_list) > 1:
#     print("my_list is not empty")
#     # do something
# else:
#     print("my_list is empty")

# print(min(my_list))
# print(max(my_list))
# print(min(my_list2))
# print(max(my_list2))

# print(all(my_list)) # Повертає True якщо всі значення True

# cond = [
#     1<2,
#     True,
#     10<4,
#     2
# ]
#
# if all(cond):
#     print(True)
# else:
#     print(False)

# if 1 and 2 and 3 and 4 and 0:
#     print(True)
# else:
#     print(False)

# print(any(my_list)) # Повертає True якщо хочаб одне значення True
#
# if any(cond):
#     print(True)
# else:
#     print(False)
#
#
# if 1 or 2 or 3 or 4 or 0:
#     print(True)
# else:
#     print(False)


############# LOOPS ##############

# counter = 0

# while True:
#     print("Hello", counter)
#     counter += 1
#
#     cond = False
#     if counter == 10:
#         break
#     elif counter == 5:
#         continue
# else:
#     print("End")

# for item in my_list:
# for item in range(2, 10, 2):
#     print(item)
# else:
#     print("End")

# for ind, item in enumerate(my_list):
#     print(ind, item)

# for item in enumerate(my_list):
#     print(item)

# print(*my_list, sep="\n", end="\nEND")
# import random
#
# print(random.randint(1, 10))
# print(random.random())
