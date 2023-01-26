# -----------------------------------exercises 1------------------------------------------------------------------------
# write a program to print the following number pattern  using a loop
# rows = int(input("input number of rows :\t"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")
# --------------------------------------exercise 2----------------------------------------------------------------------
# Display numbers from a list using loop
# write a program to display only those numbers from a list that satisfy the folowing conditions
# numbers =[12,75,120,150,180,525,50]
# the numbers must be divisible by five
# for i in numbers:
#     if i>150:
#         continue
#     if i>500:
#         break
#     if i%5==0:
#         print(i)
# -------------------------------------exercises 3----------------------------------------------------------------------
# --------------------------version 1--------------------------
# i = 6546
# count = 0
# while i != 0:
#     i //= 10
#     count += 1
# print("number of digits :" + str(count))
# ----------------------------- version 2-------------------------------------------------------------------------------
# i ="5645"
# print(len(i))
# ---------------------exerecises 5-------------------------------------------------------------------------------------
# # write a program to print the following number pattern  using a loop
# rows = int(input("input number of rows :\t"))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#
#     print("")
#
# rows = int(input("input number of rows :\t"))
# for i in range(0, rows + 1):
#     for j in range(rows - i, 0, -1):
#         print(j, end=" ")
#     print("")
# --------------------------------exercises 6---------------------------------------------------------------------------
# creat new dict from another
# write a program to find the lenght of a given dictonary values
# --------------------------------exercises 6.1-------------------------------------------------------------------------
# dict = {1: "red", 2: "green", 3: "black", 4: "white", 5: "black"}
# dict1={}
# for val in dict.values():
#     dict1[val]=len(val)
# print(dict1)
# # -------------------------------exercises 6.2------------------------------------------------------------------------
# dict={"1":"Austin Little","2":"Natasha Howard","3":"Alfred Mullins","4":"Jamie Rowe"}
# dict1={}
# for val in dict.values():
#     dict1[val]=len(val)
# print(dict1)
# --------------------------------------exercises 7---------------------------------------------------------------------
# sentence = input("input the sentece:\t")
# list_of_word = sentence.lower().split()
# print(list_of_word.count(""))
# print(list_of_word)
# word_dict = {}
# for word in list_of_word:
#     if word in word_dict:
#         word_dict[word] += 1
#     else:
#         word_dict[word] = 1
# print(word_dict)
# W = input("input the word count:\t")
# if W in word_dict:
#     print(word_dict[W])
# else:
#     print("your word dosnt exist")

# ------------------------------------------------- exercises 9---------------------------------------------------------
# list_of_numbers = [2, -7, 5, -14, -35, 55, -11, -66, -44]
# pos_count, neg_count = 0, 0
# for val in list_of_numbers:
#     if val >= 0:
#         pos_count += 1
#     else:
#         neg_count += 1
# print("Pos = ", pos_count)
# print("Neg = ", neg_count)
# __________-----------------------------------------exercises 10-------------------------------------------------------
# Program to swap any two elements in the list
# List_of_numbers = [5, 6, 12, 8]
# Enter indexes to be swapped
# num = int(input("enter the  position1 elements:\t"))
# num1 = int(input("enter the postions2 elements:\t"))
# Swapping given elements
# List_of_numbers[num], List_of_numbers[num1] = List_of_numbers[num1], List_of_numbers[num]
# Printing list
# print(List_of_numbers)
