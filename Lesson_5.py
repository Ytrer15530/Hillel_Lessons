# Lesson 5

# list
# numbers = []
# numbers_1 = list()

# numbers = [1, 3, 25, 7, 2, 7]

# print(numbers)
# print(numbers[0])
#
# numbers[1] = 11111
# print(numbers)
# print(len(numbers))
# print(numbers[-1])

#######
# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
# print()
#
# for numbers in numbers:
#     print(numbers, end=" ")
#
# print()
######

#####
# values = ["one", 12, 12.4, True]
# print(values)
#
# nums = [1, 3] * 5
# print(nums)
#######

# users = ["Vasya", "Petya"]
# user_1, user_2 = users
# print(user_1)
# print(user_2)
# print(users)

##########

# import random

# print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))   # append добавляет элемент в конец списка
#
# print(numbers)
#
# numbers.append(2222)
# print(numbers)
#
# numbers.insert(1, 33333)   # insert вставляет значение на индекс (всё остальное двигается)
# print(numbers)
#
# numbers.extend([2, 3, 4])   # extend добавляет в конец значения
# print(numbers)
#
# numbers.remove(2222)    # remove убирает значение
# print(numbers)

# numbers.clear()   очищает список
# index(item) возвращает индекс
# print(numbers.pop())  # удаляет и возвращает либо по индексу, либо последнее число
# print(numbers.pop(0))
#
# print(numbers.count(3))    # count считает количество

############
# v1
# numbers.sort()    # sort сортирует и изменяет оригинал
# print(numbers)

# v2
# numbers_sorted = sorted(numbers)     # sorted сортирует и делает копию оригинал не меняется
# print(numbers_sorted)
# print(numbers)


# people = ["Tom", "bob", "alice", "Sam", "Bill"]

# people.sort(key=str.lower)
# print(people)

# people_sorted = sorted(people, key=str.lower)
# print(people_sorted)
# print(people)

################

# numbers = ["Vasya", 33, ["dance", "walk"]]
# print(numbers)
# print(numbers[2][0])


# v1
# matrix = [
#     [2, 4, 1, 6, 76],
#     [22, 41, 21, 62],
#     [41, 54, 73, 44],
#     [27, 76, 98, 97]
# ]
#
# # print(matrix[0][1])
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

# v2
# import random
#
# matrix = []
#
# print(matrix)
# for i in range(10):
#     matrix.append([])
#     for j in range(10):
#         matrix[i].append(random.randint(10, 99))
#
# print(matrix)

#################
# GAME

import random

words = ["Cat", "Apple", "Dog", "Letter", "Helicopter"]

secret_word = words[random.randint(0, len(words) - 1)]

user_word = ["_"] * len(secret_word)

attempts_counter = 0

while True:
    print("".join(user_word))

    letter = input("Enter letter: ").strip().lower()
    attempts_counter += 1
    