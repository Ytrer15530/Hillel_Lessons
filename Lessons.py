# Lesson 3

# num = float(input("Enter the number: "))
# print(num)
# print(int(num))
#
#
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     result = num1 / num2
#
#     print(f"Result: {result}")
# except ZeroDivisionError as error:
#     print(f"ZeroDivisionError occurred: {error}")
# except ValueError as error:
#     print("Enter only integer numbers please!")
#     print(f"ValueError: {error}")
# except  Exception as error:
#     print(f"Exception occurred: {error}")
# finally:
#     print("End of calculation")


# try:
#     name = input("Enter your name: ")
#
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise Exception("Please enter a valid name!")
# except Exception as e:
#     print(f"Error: {e}")

# try:
#     print("1. Start game\n2. Settings\n3. Saved games\n4. Exit")
#     user_select = int(input("Enter menu number: "))
#
# #   v1 #################
#     if user_select == 1:
#         print("Game started")
#     elif user_select == 2:
#         print("Settings opened")
#     elif user_select == 3:
#         print("Saved games")
#     elif user_select == 4:
#         print("Exit")
#     else:
#         print("Incorrect menu item!")
#
# #   v2 ##########################
#     match user_select:
#         case 1:
#             print("Game started")
#         case 2:
#             print("Settings opened")
#         case 3:
#             print("Saved games")
#         case 4:
#             print("Exit")
#         case _:
#             print("Incorrect")
# except Exception as e:
#     print(f"Error: {e}")

#################

# v1 ########################
# i = 0
#
# while i < 10:
#     print(i, end=" ")
#     i += 3

# v2 ##########################
# i = 12
#
# while True:
#     print(i)
#     i += 10

# v3 #######################
# i = 0
#
# while True:
#     i += 1
#     if i == 5:
#         print("Continue")
#         continue
#
#     if i >= 10:
#         print("break...")
#         break
#
# print(i)
# i += 1

########################
# Lesson 4

# for i in range(5):
#     #print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(2, 5):
#     #print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(1, 5, 2):
#     #print("Hello")
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(start, end + 1):
#     print(i, end=" ")
#
# print()
#
# for i in range(end, start - 1, -1):
#     print(i, end=" ")
##########

