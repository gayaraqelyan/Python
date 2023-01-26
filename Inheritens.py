# 1.Create a Python class Person with attributes:name and age of the type string
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#  2.Create Display() method that displays the name and age of an object created via the Person class
#
#
#     def display(self):
#         print(f"Person name:\t{self.name}\nPerson age:\t{self.age}")
#
# 3.Create the chils class Student which inherits from the Person class and which also has a section attribute
#
#
# class Student(Person):
#
#     def __init__(self, name, age, section):
#         Person.__init__(self, name, age)
#         self.section = section


#  4. Create a method displayStudent() that displays the name ,age and section of an object created  via the Student class


    # def displayStudent(self):
    #     print(f"Student name:\t{self.name}\nStudent age:\t{ self.age}\nStudent section:\t{ self.section}")

#
# dis = Person("Gayane", 30)
# dis.display()
# child = Student("Ani", 30, "Developer")
# child.displayStudent()

# -----------------------------------------------------Exercises 2---------------------------------------------
# Write a Rectangle class in Python language ,allowing you to build a rectangle with lenght and widht attributes
# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     # Create a Perimeter method to calculate the perimeter of the rectangle
#

    # def perimeter(self):
    #     return 2 * (self.width + self.length)
# #
#     # Create a Area method to calculate the perimeter of the rectangle
#

#     def area(self):
#         return self.width * self.length
# #
# Create a method display() that display the lenght,width,perimeter and area of an object created using an instantiation on rectangle class
#
    # def display(self):
    #     print("Parimeter of rectangle:\t", self.perimeter())
    #     print("Area of rectangle:\t", self.area())

#
# # Create a Parallelepipede child class inheriting from the Rectangle class and width a height attribute and Another Volume()
#
#


# class parallelepipede(Rectangle):
#     def __init__(self, width, length, height):
#         Rectangle.__init__(self,width, length)
#         self.height = height
#
#
#     def Volume(self):
#         return self.area() * self.height
#
#
# Number1 = int(input("Enter the width:\t"))
# Number2 = int(input("Enter the length:\t"))
# Number3 = int(input("Enter the height:\t"))
#
# object= Rectangle(Number1, Number2)
# object.display()
# parallelepipede = parallelepipede(Number1, Number2, Number3)
# print(f"Volume of pararallepipede:\t{parallelepipede.Volume()}")
