# --------------------------------------------Exercises 1---------------------------------------------------------------
# Write a program to print multiplication table of a given numbers
# num = int(input("Please,enter the number:\t"))
#
# print("Multiplication")
#
# for i in range(1, 11):
#     print(num, "*", i, "=", i * num)
#
# print("Addition")
#
# for i in range(1, 11):
#
#     print(num, "+", i, "=", i + num)
#
# print("Subtraction")
#
# for i in range(1, 11):
#     print(num, "-", i, "=", i - num)
#
# print("Divsion")
#
# for i in range(1, 11):
#     print(num, "", i, "=", i / num)

# -----------------------------------------------------------Exercises 2------------------------------------------------
# Find the factorial of a given number:
# number = int(input("Please,enter the number:\t"))
# factorial = 1
# if number >= 1:
#     for num in range(1, number + 1):
#         factorial *= num
#     print("Factorial of the given number is:\t", factorial)

# num = int(input("Please ,enter the number:\t"))
# for i in range(1,11):
#     print(num ,"*",i,"=",i*num)

# num =int(input("Enter the number:\t"))
# fac=1
# for n in range(1,num+1):
#     if num>=1:
#         fac*=n
# print(fac)

# -------------------------------------------------------------------Exercises 3----------------------------------------
# Print the sum of all two-digit numbers that, when divided by 4, leave a remainder of 1.
# sum=0
# for i in range(10,100):
#     if i%4==1:
#         sum+=i
#         print(i)
# print(sum)

# ---------------------------------------------------------------------Exercises 4--------------------------------------
# Temperature assessment
# t = int(input("Please,enter the number:\t"))
# if t<=18:
#     print("It's cold")
# elif 18<t<24:
#     print("It's nice")
# elif t>=24:
#     print("It's hot")
# else:
#     print("dont print")

# --------------------------------------------------------------------Exercises 5---------------------------------------
# Change for a while
# for i in range(40):
#     if i % 4 == 0:
#         print("Number:\t", i)
#
# print("Change for a while")
#
# i=0
# while i<40:
#     i += 1
#     if i%4==0:
#         print("Number:\t",i)

# ----------------------------------------------------------------Exercises 6---------------------------------------------
# Change while a for
# i = 7
# sum = 0
# while i < 30:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(sum)
#
# print("Change while a for")
# sum=0
# for i in range(7,30):
#     if i%2==0:
#         sum+=i
# print(sum)
#

# ------------------------------------------------------Exercises 7-----------------------------------------------------
# Print all numbers between 100 and 600
# for i in range(100, 600):
#     if i % 3 == 0 and i % 11 == 0:
#         print("divisible by 3 and 11:\t", i)
#     elif i % 7 != 0:
#         print("not divisible by 7:\t", i)

#     else:
#         print("is not divisible by 3,7 and 11:\t", i)
# --------------------------------------------------------Exercises 8---------------------------------------------------
# Count and print the number of digits in the user-entered range divisible by 7
# a = int(input("Please,enter the number:\t"))
# b = int(input("Please,enter the number:\t"))
# for i in range(a, b):
#     if i % 7 == 0:
#         print("Divisible by 7:\t",i)
#     else:
#         print("Is not divisible by 7:\t",i)


