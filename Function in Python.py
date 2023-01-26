 # -------------------------------------------Exercises 1----------------------------------
# Write a Python function to sum all the numbers  in a list
# def summa(List_if_numbers):
#     summa=0
#     for numbers in List_of_numbers:
#         summa+=numbers
#     return summa
#
# simpl_list=[1,2,5,6]
# print(summa(simpl_list))
# ------------------------------------------Exercises 2-------------------------------
# Write a Python function to check whether a number is in given  range:
# a,b,c =2,(3,5)
# def numers_range(a,b,c):
#     if a in range(b,c):
#         return True
#     else:
#         return False
#
# numers_range(a,b,c)
# print("numbers_range")
# ----------------------------------------exercises 3--------------------------------------------------
# write a python function  that accepts a string and calculate the number of upper case letters and lower case letters

# name = "The quick Brown Fox"
#
#
# def string_count(name):
#     upper_count = 0
#     lower_count = 0
#     for i in name:
#         if i.isupper():
#             upper_count += 1
#         elif i.islower():
#             lower_count += 1
#     return (upper_count, lower_count)
#
#
# string_count(name)
# print(string_count(name))
# ---------------------------------------- exercises 4--------------------------------------------
# write a python function that takes a list and return a new list with unique elements of the frist list
# def unique_elements(List):
#     List1 = []
#     for i in List:
#         if i not in List1:
#             List1.append(i)
#     return List1
#
#
# List = [1, 2, 5, 5, 6, 2]
# print(unique_elements(List))

#  --------------------------------------exercises 5---------------------------------------------
# Write a Python program to print the even numbers from a given list
# def even_list(mylist):
#     for number in mylist:
#         if number%2==0:
#             print('YES')
#         else:
#             print("no")
#
# even_list([1,2,5,6,8])
# -----------------------------------exercises 6--------------------------------------
# Write a function that will calculate and return the perimeter of a rectangle. Get side lengths from console.
# lenght = int(input("please enter the lenght number:\t"))
# width = int(input("please enter the width number:\t"))
#
#
# def perimetr_of_Rectangle(lenght, width):
#     return 2 * (lenght + width)
#
#
# perimetr = perimetr_of_Rectangle(lenght, width)
# print(lenght,"and",width,"=", perimetr)
# ----------------------------------------------------- exercises 7----------------------------
# Write a function that calculates and returns the perimeter of a square. Take the length from console
# width = int(input("enetr the number width:\t"))
# lenght =width
#
# def primeter_of_square(width):
#     return 4 * (width)
#
# primeter = primeter_of_square(width)
# print('width', "=", width,"primeter", "=", primeter)
# -------------------------------------------------------exercises 8 ------------------------------------------
# Write a function that will calculate and return the area of the rectangle. Get the lengths from the console.
# lenght = float(input("enter the lenght number:\t"))
# width = float(input("enter the width number:\t"))
#
#
# def area_of_rectangle(lenght, width):
#     return lenght * width
#
#
# area = area_of_rectangle(lenght, width)
# print("lenght", "=", lenght, "width", "=", width, "area", "=", area)
# # --------------------------------------------------exercises 9--------------------------------------------------
# Write a function that calculates and returns the area of a square. Take the length  from the console.
# lenght = int(input("enter the lenght number:\t"))
# width=lenght
#
# def area_of_square(lenght):
#     return lenght**2
#
# area = area_of_square(lenght)
# print("lenght", "=", lenght,  "area", "=", area)